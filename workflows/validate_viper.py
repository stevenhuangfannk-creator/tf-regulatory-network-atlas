"""Compare original Bioconductor VIPER with ULM and the Python reimplementation."""
import json
from pathlib import Path
import pandas as pd
from scipy.stats import spearmanr
from periodontal_tf import differential

ROOT = Path(__file__).resolve().parents[1]

def main():
    cfg = json.loads((ROOT / "config/analysis.json").read_text())
    tables = ROOT / "results/tables"
    meta = pd.read_csv(tables / "pseudobulk_metadata.csv", index_col=0)
    original = pd.read_csv(tables / "bioc_viper_activity_matrix.csv", index_col=0)
    original = original.loc[meta.index]
    differences = differential(original, meta, cfg)
    differences["method"] = "bioc_viper"
    differences.to_csv(tables / "bioc_viper_differential.csv", index=False)
    primary = pd.read_csv(tables / "differential_activity.csv")
    concordance = primary[primary.method == "ulm"].merge(differences, on=["cell_type", "tf"], suffixes=("_ulm", "_viper"))
    concordance = concordance.rename(columns={"effect_ulm": "ulm_effect", "effect_viper": "viper_effect"})
    for method in ["ulm", "viper"]:
        concordance[method + "_rank"] = concordance.groupby("cell_type")["pvalue_" + method].rank(method="min")
    py_effect = primary[primary.method == "viper"][["cell_type", "tf", "effect", "pvalue"]].rename(columns={"effect": "dc_viper_effect", "pvalue": "dc_viper_pvalue"})
    concordance = concordance.merge(py_effect, on=["cell_type", "tf"])
    concordance["viper_implementation"] = "Bioconductor viper"
    concordance.to_csv(tables / "method_concordance.csv", index=False)
    long = original.rename_axis("sample").reset_index().melt("sample", var_name="tf", value_name="score").merge(meta.reset_index(), on="sample")
    long["method"] = "bioc_viper"
    long.to_csv(tables / "bioc_viper_pseudobulk_activity.csv", index=False)
    python_viper = pd.read_csv(tables / "viper_activity_matrix.csv", index_col=0)
    common = sorted(set(original.columns) & set(python_viper.columns))
    rows = []
    for sample in meta.index:
        rows.append({"sample": sample, "spearman_r": spearmanr(original.loc[sample, common], python_viper.loc[sample, common]).statistic, "n_regulators": len(common)})
    pd.DataFrame(rows).to_csv(tables / "viper_implementation_comparison.csv", index=False)
    summary = []
    for cell_type, frame in concordance.groupby("cell_type"):
        summary.append({"cell_type": cell_type, "n_regulators": len(frame), "effect_spearman": spearmanr(frame.ulm_effect, frame.viper_effect).statistic, "rank_spearman": spearmanr(frame.ulm_rank, frame.viper_rank).statistic, "same_sign_fraction": ((frame.ulm_effect > 0) == (frame.viper_effect > 0)).mean(), "note": "Same data and shared prior: agreement is not independent validation"})
    (ROOT / "reports/viper_validation.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
