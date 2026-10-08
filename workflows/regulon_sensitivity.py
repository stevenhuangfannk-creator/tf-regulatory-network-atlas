"""Target subsampling sensitivity on real donor pseudobulk, not biological validation."""
import json
from pathlib import Path
import decoupler as dc
import numpy as np
import pandas as pd
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]

def main():
    cfg = json.loads((ROOT / "config/analysis.json").read_text())
    tables = ROOT / "results/tables"
    selected = json.loads((tables / "selected_tfs.json").read_text())
    expression = pd.read_csv(ROOT / "data/local/pseudobulk_centered.csv.gz", index_col=0)
    meta = pd.read_csv(tables / "pseudobulk_metadata.csv", index_col=0)
    net = pd.read_csv(ROOT / "data/cache/collectri.csv")
    net = net[net.source.isin(selected) & net.target.isin(expression.columns)].drop_duplicates(["source", "target"])
    rng = np.random.default_rng(cfg["seed"])
    rows = []
    for iteration in range(20):
        keep = []
        retained = {}
        for tf, group in net.groupby("source"):
            n_keep = max(cfg["min_targets"], int(0.8 * len(group)))
            keep.append(group.iloc[rng.choice(len(group), n_keep, replace=False)])
            retained[tf] = (len(group), n_keep)
        scores, _ = dc.mt.ulm(expression, pd.concat(keep), tmin=cfg["min_targets"], empty=False)
        for cell_type, group in meta.groupby("cell_type"):
            design = np.column_stack([np.ones(len(group)), (group.condition == "Periodontitis").to_numpy(dtype=float), group.assay.str.contains("v3").to_numpy(dtype=float)])
            for tf in selected:
                coefficient = sm.OLS(scores.loc[group.index, tf].to_numpy(), design).fit().params[1]
                total, retained_n = retained[tf]
                rows.append({"iteration": iteration, "cell_type": cell_type, "tf": tf, "effect": coefficient, "n_targets": total, "n_retained": retained_n, "actual_target_fraction": retained_n / total})
    result = pd.DataFrame(rows)
    result.to_csv(tables / "regulon_target_subsampling.csv", index=False)
    reference = pd.read_csv(tables / "differential_activity.csv")
    reference = reference[reference.method == "ulm"][["cell_type", "tf", "effect"]].rename(columns={"effect": "reference_effect"})
    result = result.merge(reference, on=["cell_type", "tf"])
    summary = result.groupby(["cell_type", "tf"]).apply(lambda x: pd.Series({"iterations": len(x), "requested_target_fraction": 0.8, "actual_target_fraction": x.actual_target_fraction.iloc[0], "n_targets": x.n_targets.iloc[0], "n_retained": x.n_retained.iloc[0], "same_sign_fraction": np.mean(np.sign(x.effect) == np.sign(x.reference_effect)), "effect_min": x.effect.min(), "effect_max": x.effect.max()}), include_groups=False).reset_index()
    summary.to_csv(tables / "regulon_target_stability.csv", index=False)
    print(summary.to_string(index=False))

if __name__ == "__main__":
    main()
