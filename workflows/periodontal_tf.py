"""Real-data TF activity workflow; stream CSR counts and aggregate biological donors."""
import os
for key in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMBA_NUM_THREADS"]:
    os.environ.setdefault(key, "2")
import importlib.metadata as metadata
import json
import time
from pathlib import Path
import decoupler as dc
import h5py
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import sparse, stats
from statsmodels.stats.multitest import multipletests
from threadpoolctl import threadpool_limits

ROOT = Path(__file__).resolve().parents[1]

def read_column(node):
    if isinstance(node, h5py.Group):
        categories = read_column(node["categories"])
        codes = node["codes"][:]
        return np.array([categories[i] if i >= 0 else "" for i in codes])
    return node.asstr()[:] if h5py.check_string_dtype(node.dtype) else node[:]

def csr_rows(group, start, stop):
    pointers = group["indptr"][start:stop + 1]
    a, b = int(pointers[0]), int(pointers[-1])
    return sparse.csr_matrix((group["data"][a:b], group["indices"][a:b], pointers - a), shape=(stop - start, int(group.attrs["shape"][1])))

def score(data, net, method, cfg):
    kwargs = {"pleiotropy": cfg["viper_pleiotropy"]} if method == "viper" else {}
    # Keep the fixed background universe across chunks, including zero features.
    scores, _ = getattr(dc.mt, method)(data, net, tmin=cfg["min_targets"], empty=False, verbose=False, **kwargs)
    return scores

def differential(activity, sample_meta, cfg):
    rows = []
    rng = np.random.default_rng(cfg["seed"])
    for cell_type, group in sample_meta.groupby("cell_type", sort=True):
        healthy = group.index[group.condition == "Healthy"]
        disease = group.index[group.condition == "Periodontitis"]
        if min(len(healthy), len(disease)) < cfg["min_donors_per_condition"]:
            continue
        is_disease = (group.condition == "Periodontitis").astype(float).to_numpy()
        is_v3 = group.assay.str.contains("v3").astype(float).to_numpy()
        design = np.column_stack([np.ones(len(group)), is_disease, is_v3])
        if np.linalg.matrix_rank(design) != 3:
            raise ValueError(f"Disease and assay cannot be separated in {cell_type}")
        for tf in activity.columns:
            h, d = activity.loc[healthy, tf].to_numpy(), activity.loc[disease, tf].to_numpy()
            values = activity.loc[group.index, tf].to_numpy()
            model = sm.OLS(values, design).fit(cov_type="HC3", use_t=True)
            effect, pvalue = float(model.params[1]), float(model.pvalues[1])
            low, high = model.conf_int(alpha=0.05)[1]
            boot = rng.choice(d, (cfg["bootstrap_iterations"], len(d)), replace=True).mean(1) - rng.choice(h, (cfg["bootstrap_iterations"], len(h)), replace=True).mean(1)
            boot_low, boot_high = np.quantile(boot, [0.025, 0.975])
            loo = []
            for i in range(len(group)):
                x, y = np.delete(design, i, axis=0), np.delete(values, i)
                if np.linalg.matrix_rank(x) == 3:
                    loo.append(sm.OLS(y, x).fit().params[1])
            v3_h = values[(is_disease == 0) & (is_v3 == 1)]
            v3_d = values[(is_disease == 1) & (is_v3 == 1)]
            v3_effect = float(v3_d.mean() - v3_h.mean()) if len(v3_h) and len(v3_d) else np.nan
            v3_pvalue = float(stats.ttest_ind(v3_d, v3_h, equal_var=False).pvalue) if min(len(v3_h), len(v3_d)) >= 3 else np.nan
            rows.append({"cell_type": cell_type, "tf": tf, "effect": effect, "unadjusted_effect": float(d.mean() - h.mean()), "ci_low": float(low), "ci_high": float(high), "pvalue": pvalue, "n_healthy": len(h), "n_disease": len(d), "n_v3_healthy": len(v3_h), "n_v3_disease": len(v3_d), "v3_effect": v3_effect, "v3_pvalue": v3_pvalue, "loo_sign_fraction": float(np.mean(np.sign(loo) == np.sign(effect))), "n_loo_estimable": len(loo), "bootstrap_low": float(boot_low), "bootstrap_high": float(boot_high)})
    result = pd.DataFrame(rows)
    if len(result):
        result["fdr"] = result.groupby("cell_type")["pvalue"].transform(lambda x: multipletests(x.fillna(1), method="fdr_bh")[1])
    return result

def main():
    started = time.monotonic()
    cfg = json.loads((ROOT / "config/analysis.json").read_text())
    tables, local = ROOT / "results/tables", ROOT / "data/local"
    tables.mkdir(parents=True, exist_ok=True)
    local.mkdir(parents=True, exist_ok=True)
    mapping = pd.read_csv(ROOT / "data/donor_map.csv").set_index("sample_id")
    with h5py.File(ROOT / "data/raw/periodontal_atlas.h5ad", "r") as f:
        obs = pd.DataFrame({k: read_column(f["obs"][v]) for k, v in {"cell_id": "_index", "sample_id": "donor_id", "author_cell_type": "cell_type", "source_study": "Study", "disease": "disease", "assay": "assay"}.items()})
        obs["donor"] = obs.sample_id.map(mapping.biological_donor)
        obs["condition"] = obs.disease.map({"normal": "Healthy", "periodontitis": "Periodontitis"})
        classes = cfg["cell_type_map"]
        obs["cell_type"] = obs.author_cell_type.map(classes)
        mask = obs.sample_id.str.startswith(cfg["sample_prefix"]) & obs.disease.isin(cfg["conditions"]) & obs.cell_type.isin(cfg["cell_types"])
        selected = obs.loc[mask].copy()
        if selected.donor.isna().any():
            raise ValueError("Unmapped biological donor: stop before inference")
        selected["sample"] = selected.donor + "|" + selected.cell_type
        samples = selected.groupby("sample").agg(donor=("donor", "first"), condition=("condition", "first"), cell_type=("cell_type", "first"), assay=("assay", "first"), n_cells=("cell_id", "size"))
        if selected.groupby("sample").assay.nunique().max() != 1:
            raise ValueError("Mixed-assay donor requires explicit assay proportions")
        # A biological donor must have one disease condition in this unpaired design.
        if selected.groupby("donor").condition.nunique().max() != 1:
            raise ValueError("Mixed condition donor requires paired design")
        samples.to_csv(tables / "sample_cell_counts_before_filter.csv")
        samples = samples[samples.n_cells >= cfg["min_cells_per_donor_celltype"]]
        selected = selected[selected["sample"].isin(samples.index)]
        samples.to_csv(tables / "pseudobulk_metadata.csv")
        genes_original = read_column(f["raw/var/feature_name"])
        if set(read_column(f["raw/var/feature_reference"])) != {"NCBITaxon:9606"}:
            raise ValueError("This workflow requires human gene symbols; do not mix species")
        genes, inverse = np.unique(genes_original, return_inverse=True)
        valid_gene = np.array([bool(g) and g != "unknown" for g in genes])
        # Sum duplicate gene symbols instead of choosing an arbitrary duplicate.
        collapse = sparse.csr_matrix((np.ones(len(inverse)), (np.arange(len(inverse)), inverse)), shape=(len(inverse), len(genes)))
        matrix = np.zeros((len(samples), len(genes)), dtype=np.float64)
        sample_lookup = {s: i for i, s in enumerate(samples.index)}
        group = f["raw/X"]
        if group.attrs["encoding-type"] != "csr_matrix":
            raise ValueError("Expected raw.X CSR counts")
        for start in range(0, len(obs), cfg["chunk_size"]):
            stop = min(start + cfg["chunk_size"], len(obs))
            chosen = selected.index[(selected.index >= start) & (selected.index < stop)]
            if not len(chosen):
                continue
            block = csr_rows(group, start, stop)[chosen - start]
            if (block.data < 0).any() or not np.allclose(block.data, np.round(block.data), rtol=0, atol=1e-6):
                raise ValueError("Raw data are not nonnegative integer counts")
            collapsed = block @ collapse
            for s, indexes in selected.loc[chosen].groupby("sample").groups.items():
                positions = np.flatnonzero(np.isin(chosen, indexes))
                matrix[sample_lookup[s]] += np.asarray(collapsed[positions].sum(0)).ravel()
        library_sizes = matrix.sum(1)
        if (library_sizes <= 0).any():
            raise ValueError("Zero count pseudobulk")
        expressed = valid_gene & (matrix.sum(0) >= 10) & ((matrix > 0).sum(0) >= 3)
        expression = pd.DataFrame(np.log2(matrix[:, expressed] / library_sizes[:, None] * 1e6 + 1), index=samples.index, columns=genes[expressed])
        expression.to_csv(local / "pseudobulk_logcpm.csv.gz", compression="gzip")
        np.savez_compressed(local / "pseudobulk_counts.npz", counts=matrix[:, expressed], genes=genes[expressed], samples=samples.index.to_numpy(dtype=str))
        centered = expression.copy()
        for cell_type, indexes in samples.groupby("cell_type").groups.items():
            centered.loc[indexes] -= expression.loc[indexes].mean(0)
        centered.to_csv(local / "pseudobulk_centered.csv.gz", compression="gzip")
        net = pd.read_csv(ROOT / "data/cache/collectri.csv").drop_duplicates(["source", "target"])
        net = net.dropna(subset=["source", "target", "weight"])
        coverage = net.groupby("source").agg(n_targets_total=("target", "nunique"))
        present = net[net.target.isin(expression.columns)]
        coverage["n_targets_present"] = present.groupby("source").target.nunique()
        coverage = coverage.fillna(0).astype(int)
        coverage["coverage"] = coverage.n_targets_present / coverage.n_targets_total
        coverage.rename_axis("tf").to_csv(tables / "regulon_coverage.csv")
        present = present[present.source.isin(coverage.index[coverage.n_targets_present >= cfg["min_targets"]])]
        activities, differences = {}, []
        for method in ["ulm", "viper"]:
            print("Scoring donor pseudobulk", method, expression.shape, flush=True)
            activities[method] = score(centered, present, method, cfg)
            activities[method].to_csv(tables / f"{method}_activity_matrix.csv")
            result = differential(activities[method], samples, cfg)
            result["method"] = method
            differences.append(result)
        diff = pd.concat(differences, ignore_index=True)
        diff.to_csv(tables / "differential_activity.csv", index=False)
        long_activity = []
        for method, activity in activities.items():
            frame = activity.rename_axis("sample").reset_index().melt("sample", var_name="tf", value_name="score").merge(samples.reset_index(), on="sample")
            frame["method"] = method
            long_activity.append(frame)
        pd.concat(long_activity).to_csv(tables / "pseudobulk_activity.csv", index=False)
        diff[["cell_type", "tf", "method", "loo_sign_fraction", "n_loo_estimable", "bootstrap_low", "bootstrap_high", "v3_effect", "v3_pvalue", "n_v3_healthy", "n_v3_disease"]].to_csv(tables / "stability.csv", index=False)
        concordance = differences[0].merge(differences[1], on=["cell_type", "tf"], suffixes=("_ulm", "_viper"))
        concordance = concordance.rename(columns={"effect_ulm": "ulm_effect", "effect_viper": "viper_effect"})
        for method in ["ulm", "viper"]:
            concordance[f"{method}_rank"] = concordance.groupby("cell_type")[f"pvalue_{method}"].rank(method="min")
        concordance.to_csv(tables / "method_concordance.csv", index=False)
        ulm_diff = diff[diff.method == "ulm"].sort_values(["fdr", "pvalue"])
        chosen_tfs = ulm_diff[ulm_diff.tf.isin(expression.columns)].drop_duplicates("tf").head(cfg["figure_tfs"]).tf.tolist()
        print("Selected result-ranked TFs", chosen_tfs, flush=True)
        (tables / "selected_tfs.json").write_text(json.dumps(chosen_tfs, indent=2))
        focused = present[present.source.isin(chosen_tfs)].copy()
        focused["evidence_type"] = "curated_prior"
        # Sparse prior figure: strongest absolute observed target contrast, no causal edge claim.
        focus_type = ulm_diff.iloc[0].cell_type
        meta = samples[samples.cell_type == focus_type]
        target_change = expression.loc[meta.index[meta.condition == "Periodontitis"]].mean(0) - expression.loc[meta.index[meta.condition == "Healthy"]].mean(0)
        focused["target_logcpm_change"] = focused.target.map(target_change)
        focused["abs_change"] = focused.target_logcpm_change.abs()
        focused = focused.sort_values(["source", "abs_change"], ascending=[True, False]).groupby("source").head(6).drop(columns="abs_change")
        focused["contrast_cell_type"] = focus_type
        focused.to_csv(tables / "selected_network_edges.csv", index=False)
        # Cell scores use observed log1p CP10K, not donor-centered disease signatures.
        cell_net = present[present.source.isin(chosen_tfs)]
        gene_columns = np.flatnonzero(expressed)
        cell_outputs = []
        for start in range(0, len(obs), cfg["chunk_size"]):
            stop = min(start + cfg["chunk_size"], len(obs))
            chosen = selected.index[(selected.index >= start) & (selected.index < stop)]
            if not len(chosen):
                continue
            block = (csr_rows(group, start, stop)[chosen - start] @ collapse).tocsr()
            totals = np.asarray(block.sum(1)).ravel()
            if (totals <= 0).any():
                raise ValueError("Zero count cell: requires explicit exclusion")
            normalized = block.multiply(1e4 / totals[:, None]).tocsr()
            normalized.data = np.log1p(normalized.data)
            value = pd.DataFrame(normalized[:, gene_columns].toarray().astype(np.float32), index=selected.loc[chosen, "cell_id"], columns=genes[expressed])
            cell_scores = score(value, cell_net, "ulm", cfg)
            output = selected.loc[chosen, ["cell_id", "sample_id", "donor", "condition", "cell_type", "author_cell_type"]].copy()
            coordinates = f["obsm/X_umap"][chosen.to_numpy()]
            output["umap_1"], output["umap_2"] = coordinates[:, 0], coordinates[:, 1]
            for tf in chosen_tfs:
                output[tf + "_activity"] = cell_scores[tf].to_numpy()
                output[tf + "_expression"] = value[tf].to_numpy() if tf in value else np.nan
            cell_outputs.append(output)
        cells = pd.concat(cell_outputs, ignore_index=True)
        cells.to_csv(tables / "cells.csv.gz", index=False, compression="gzip")
        summaries = []
        for (cell_type, condition), subset in cells.groupby(["cell_type", "condition"]):
            for tf in chosen_tfs:
                summaries.append({"cell_type": cell_type, "condition": condition, "tf": tf, "mean_activity": subset[tf + "_activity"].mean(), "mean_expression": subset[tf + "_expression"].mean(), "n_cells": len(subset)})
        pd.DataFrame(summaries).to_csv(tables / "celltype_activity.csv", index=False)
    report = {"seed": cfg["seed"], "input_cells": len(obs), "retained_cells": len(selected), "pseudobulk_samples": len(samples), "biological_donors": selected.donor.nunique(), "genes_original": len(genes_original), "genes_unique": len(genes), "genes_analyzed": expression.shape[1], "regulators_tested": len(activities["ulm"].columns), "selected_tfs": chosen_tfs, "normalization": cfg, "seconds": time.monotonic() - started, "packages": {p: metadata.version(p) for p in ["decoupler", "numpy", "scipy", "pandas", "h5py", "anndata", "numba", "statsmodels"]}, "versions": "dc.mt.viper is Python reimplementation; not Bioconductor viper or ARACNe reconstruction", "embedding": "Author CELLxGENE X_umap reused; no new trajectory inferred"}
    (ROOT / "reports/run_manifest.json").parent.mkdir(parents=True, exist_ok=True)
    (ROOT / "reports/run_manifest.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2), flush=True)

if __name__ == "__main__":
    with threadpool_limits(limits=2):
        main()
