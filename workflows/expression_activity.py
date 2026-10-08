"""Compare regulator transcripts with downstream footprint scores at donor level."""
import json
from pathlib import Path
import pandas as pd
from scipy.stats import spearmanr
from statsmodels.stats.multitest import multipletests
from periodontal_tf import differential

ROOT = Path(__file__).resolve().parents[1]

def main():
    cfg = json.loads((ROOT / "config/analysis.json").read_text())
    tables = ROOT / "results/tables"
    meta = pd.read_csv(tables / "pseudobulk_metadata.csv", index_col=0)
    expression = pd.read_csv(ROOT / "data/local/pseudobulk_logcpm.csv.gz", index_col=0)
    activity = pd.read_csv(tables / "ulm_activity_matrix.csv", index_col=0)
    common = sorted(set(expression.columns) & set(activity.columns))
    expression_diff = differential(expression[common], meta, cfg)
    expression_diff.to_csv(tables / "regulator_expression_differential.csv", index=False)
    activity_diff = pd.read_csv(tables / "differential_activity.csv")
    comparison = activity_diff[activity_diff.method == "ulm"].merge(expression_diff, on=["cell_type", "tf"], suffixes=("_activity", "_expression"))
    rows = []
    selected = json.loads((tables / "selected_tfs.json").read_text())
    for cell_type, group in meta.groupby("cell_type"):
        for tf in common:
            result = spearmanr(expression.loc[group.index, tf], activity.loc[group.index, tf])
            rows.append({"cell_type": cell_type, "tf": tf, "donor_spearman": result.statistic, "donor_correlation_pvalue": result.pvalue, "n_donors": len(group)})
    comparison = comparison.merge(pd.DataFrame(rows), on=["cell_type", "tf"])
    comparison["donor_correlation_fdr"] = comparison.groupby("cell_type")["donor_correlation_pvalue"].transform(lambda x: multipletests(x.fillna(1), method="fdr_bh")[1])
    comparison.to_csv(tables / "expression_activity_comparison.csv", index=False)
    scatter = []
    for sample, row in meta.iterrows():
        for tf in selected:
            scatter.append({"sample": sample, "donor": row.donor, "condition": row.condition, "cell_type": row.cell_type, "tf": tf, "expression_logcpm": expression.loc[sample, tf], "activity": activity.loc[sample, tf]})
    pd.DataFrame(scatter).to_csv(tables / "donor_expression_activity.csv", index=False)
    print("Transcript/activity comparison:", len(common), "regulators,", len(scatter), "selected donor observations")

if __name__ == "__main__":
    main()
