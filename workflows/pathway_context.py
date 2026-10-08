"""PROGENy pathway footprints and Hallmark overlap; neither is a de novo GRN."""
import hashlib
import json
from pathlib import Path
import decoupler as dc
import pandas as pd
import requests
from scipy.stats import hypergeom
from statsmodels.stats.multitest import multipletests
from periodontal_tf import differential

ROOT = Path(__file__).resolve().parents[1]

def main():
    cfg = json.loads((ROOT / "config/analysis.json").read_text())
    manifest_file = ROOT / "reports/pathway_manifest.json"
    expected = json.loads(manifest_file.read_text()) if manifest_file.exists() else {}
    tables, cache = ROOT / "results/tables", ROOT / "data/cache"
    expression = pd.read_csv(ROOT / "data/local/pseudobulk_centered.csv.gz", index_col=0)
    samples = pd.read_csv(tables / "pseudobulk_metadata.csv", index_col=0)
    pathway_file = cache / "progeny_top100.csv"
    if not pathway_file.exists():
        dc.op.progeny(organism="human", top=100, thr_padj=0.05, license="academic").to_csv(pathway_file, index=False)
    progeny_hash = hashlib.sha256(pathway_file.read_bytes()).hexdigest()
    if expected and progeny_hash != expected["progeny"]["sha256"]:
        raise ValueError("PROGENy snapshot changed: preserve old cache; do not replace existing analysis")
    network = pd.read_csv(pathway_file)
    activity, _ = dc.mt.ulm(expression, network, tmin=10, empty=False)
    activity.to_csv(tables / "progeny_activity_matrix.csv")
    effects = differential(activity, samples, cfg)
    effects = effects.rename(columns={"tf": "pathway"})
    effects["method"] = "PROGENy_ULM"
    effects.to_csv(tables / "progeny_differential.csv", index=False)
    url = "https://maayanlab.cloud/Enrichr/geneSetLibrary?mode=text&libraryName=MSigDB_Hallmark_2020"
    hallmark_file = cache / "hallmark_2020.gmt"
    if not hallmark_file.exists():
        response = requests.get(url, timeout=90)
        response.raise_for_status()
        hallmark_file.write_bytes(response.content)
    hallmark_hash = hashlib.sha256(hallmark_file.read_bytes()).hexdigest()
    if expected and hallmark_hash != expected["hallmark"]["sha256"]:
        raise ValueError("Hallmark snapshot changed: preserve old cache; do not replace existing analysis")
    pathways = {}
    universe = set(expression.columns)
    for line in hallmark_file.read_text().splitlines():
        values = line.rstrip().split("\t")
        pathways[values[0]] = set(values[2:]) & universe
    collectri = pd.read_csv(cache / "collectri.csv")
    selected = json.loads((tables / "selected_tfs.json").read_text())
    rows = []
    for tf in selected:
        targets = set(collectri.loc[collectri.source == tf, "target"]) & universe
        for pathway, members in pathways.items():
            overlap = targets & members
            rows.append({"tf": tf, "pathway": pathway, "overlap": len(overlap), "n_targets": len(targets), "n_members": len(members), "universe": len(universe), "pvalue": hypergeom.sf(len(overlap) - 1, len(universe), len(members), len(targets)), "genes": ";".join(sorted(overlap)), "evidence_type": "curated_prior_gene_set_overlap"})
    links = pd.DataFrame(rows)
    links["fdr"] = multipletests(links.pvalue, method="fdr_bh")[1]
    links.to_csv(tables / "tf_pathway_links.csv", index=False)
    manifest = {"progeny": {"top": 100, "threshold": 0.05, "n_edges": len(network), "n_pathways_scored": len(activity.columns), "sha256": hashlib.sha256(pathway_file.read_bytes()).hexdigest(), "retrieval": "decoupler.op.progeny(organism=human, license=academic)", "meaning": "Perturbation-derived weighted pathway footprint, distinct from TF activity"}, "hallmark": {"url": url, "n_sets": len(pathways), "sha256": hashlib.sha256(hallmark_file.read_bytes()).hexdigest(), "tests": len(links), "meaning": "Hypergeometric prior-target overlap only; not demonstrated TF pathway regulation"}}
    (ROOT / "reports/pathway_manifest.json").write_text(json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2), flush=True)

if __name__ == "__main__":
    main()
