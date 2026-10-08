"""Build source-grounded Chinese report from the committed real result tables."""
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def md_table(frame):
    # Avoid an optional tabulate dependency.
    lines = ["| " + " | ".join(frame.columns) + " |", "| " + " | ".join(["---"] * len(frame.columns)) + " |"]
    lines.extend("| " + " | ".join(str(x) for x in row) + " |" for row in frame.itertuples(index=False, name=None))
    return "\n".join(lines)

def main():
    t = ROOT / "results/tables"
    manifest = json.loads((ROOT / "reports/run_manifest.json").read_text())
    diff = pd.read_csv(t / "differential_activity.csv")
    bioc = pd.read_csv(t / "bioc_viper_differential.csv")
    concordance = pd.read_csv(t / "method_concordance.csv")
    coverage = pd.read_csv(t / "regulon_coverage.csv")
    stability = pd.read_csv(t / "regulon_target_stability.csv")
    expression = pd.read_csv(t / "expression_activity_comparison.csv")
    original = json.loads((ROOT / "methods/viper/R_runtime.json").read_text())
    pathway = pd.read_csv(t / "progeny_differential.csv")
    candidates = diff[diff.method == "ulm"].sort_values(["fdr", "pvalue"]).head(12)
    candidates = candidates.merge(bioc[["cell_type", "tf", "effect", "fdr"]], on=["cell_type", "tf"], suffixes=("", "_bioc"))
    display = candidates[["cell_type", "tf", "effect", "fdr", "effect_bioc", "fdr_bioc", "loo_sign_fraction", "v3_effect"]].copy()
    for col in display.columns[2:]:
        display[col] = display[col].map(lambda x: f"{x:.3g}")
    display.columns = ["细胞", "调控因子", "ULM系数", "ULM q", "VIPER系数", "VIPER q", "留一同号比例", "v3差值"]
    counts = diff[diff.method == "ulm"].groupby("cell_type").first()[["n_healthy", "n_disease", "n_v3_healthy", "n_v3_disease"]].reset_index()
    summary = []
    for method, frame in [("ULM", diff[diff.method == "ulm"]), ("Python VIPER", diff[diff.method == "viper"]), ("Bioconductor VIPER", bioc)]:
        for cell_type, subset in frame.groupby("cell_type"):
            summary.append({"方法": method, "细胞": cell_type, "检验调控因子": len(subset), "q<0.05": (subset.fdr < .05).sum()})
    expression_rows = expression[expression.tf.isin(manifest["selected_tfs"]) & (expression.cell_type == "Fibroblast")][["tf", "effect_expression", "fdr_expression", "donor_spearman"]].copy()
    for col in expression_rows.columns[1:]:
        expression_rows[col] = expression_rows[col].map(lambda x: f"{x:.3g}")
    pathway_top = pathway.sort_values("fdr").head(8)[["cell_type", "pathway", "effect", "fdr"]].copy()
    for col in ["effect", "fdr"]:
        pathway_top[col] = pathway_top[col].map(lambda x: f"{x:.3g}")
    report = f"""# Validation Report / 计算验证与结论边界

版本：v0.1；日期：2026-10-08（Asia/Shanghai）。本报告由 `scripts/build_report.py` 读取真实结果表生成。

## 已完成 / Executed

下载并 SHA256 校验 CELLxGENE 人牙周 meta-atlas（105,918 cells，35,369 features）；实际分析限定同一 Williams/GSE164241 研究，使用 raw.X 非负整数计数、作者细胞注释、作者 UMAP。保留成纤维细胞、巨噬细胞、血管内皮细胞，共 **{manifest['retained_cells']:,} cells、{manifest['pseudobulk_samples']} donor×cell-type pseudobulk、{manifest['genes_analyzed']:,} expressed genes、{manifest['regulators_tested']} prior regulators**。13 个健康编码及 5 个保守疾病编码是推断单位。

完整运行 CollecTRI + decoupler {manifest['packages']['decoupler']} ULM；Python `dc.mt.viper`；原始 Bioconductor viper {original['version']}；PROGENy + ULM（14 pathways）。TF activity、蛋白活性推断与实际蛋白量分开；PROGENy 是扰动实验训练的 pathway footprint，不能叫 TF 活性。CollecTRI 包含 TF 复合体和辅助调控因子，并非所有 source 都是具有独立 DNA-binding motif 的 TF。

## 重复与模型 / Replication and model

{md_table(counts)}

PD161/PD161b 及 PD164/PD164b/PD164c 按 GEO 标题患者代码保守合并，避免将同人活检视为独立患者；Table S1 完整患者联系未取得，所以患者映射仍有不确定性。不得把原 8 个 PD 文库称为 8 个独立患者。

每个 donor×cell type 至少 50 cells；巨噬细胞因此丢失 7 个健康、1 个疾病供体组，不能把这种筛选当成随机缺失。健康 10 个 v2、3 个 v3；疾病 1 个 v2、4 个 v3。主模型为 `activity ~ disease + assay`，采用 HC3 robust SE、t-based 95% CI，BH 按 cell type×method 分别校正。OLS 是未配对比较，细胞不是统计重复。分组样本量小，协变量没有涵盖所有临床/部位因素。

疾病 v2 只有一个患者，模型可估计但对该点和 assay 分层非常敏感。独立设计检查中，PD134 对疾病系数的线性权重约 34.65%（成纤维/内皮）和 52.63%（巨噬）；不能由显著 P 值忽略这个局限。v3-only 检查在成纤维/内皮有 3 H vs 4 PD；巨噬仅 1 H vs 3 PD，不进行正式 v3 子集检验。v3 差值仅提供方向和效应敏感性，不视为独立验证。粗粒度细胞群也可能存在状态/亚群组成变化：Endothelial 合并 artery/capillary/venule，不能证明细胞内在调控变化，作者原始亚型另列保留。原始数据处理是稀疏分块汇总，无随机细胞抽样；重复 symbol 的 9 features 求和。ULM 保留固定 21,690 gene background（`empty=False`），避免分块改变 score。

## 真实候选 / Observed candidates

{md_table(display)}

这是多重检验后按 ULM q/p 排序的候选；不是预设 NF-kB/STAT 家族命中，也不是因果主调控因子证明。GTF3A、ZNF148、TFE3、JUND 等为可继续验证候选；CREBBP 是转录共激活因子，NFKBIB 是 NF-kB 抑制蛋白，不能给它们强加与 sequence-specific TF 相同的解释。ETV3 在成纤维的推断方向为下降；GLI2 是内皮候选，不能从一类细胞外推另一类。

{md_table(pd.DataFrame(summary))}

显著条目较多，与疾病、技术方案和细胞状态可能同时有关；这些 q 值只在本次模型及假设下有效。高相关 TF regulon、共同靶基因、多重比较按分层校正、small-n 与未验证患者链接都降低机制结论可信度，不能据数量推断很多独立因果轴。

## 表达与活性 / Expression versus activity

{md_table(expression_rows)}

`effect_expression` 为 assay-adjusted log2(CPM+1) 系数，activity 为不同单位的下游 footprint score；不可直接比较两列数值大小。`donor_spearman` 为同一细胞类型内供体层面的描述性相关，疾病本身可能造成相关；不是 protein abundance 或 target regulation 的测量。细胞 UMAP 图使用 log1p CP10K + ULM，仅展示状态，正式推断来自 donor pseudobulk。

## 方法一致性与稳定性 / Concordance and stability

ULM 与原始 R VIPER 在共同的 516 regulon、相同中心化供体矩阵和 CollecTRI 上比较；效应 Spearman 约 0.94，排名 Spearman 约 0.85–0.87。见 [精确统计](viper_validation.json) 与 [实现比较](../results/tables/viper_implementation_comparison.csv)。Python 和 R VIPER 是不同实现，不能称逐位相同。共享先验和同一数据使一致性不能视为独立生物学验证。

对供体进行 1,000 次条件内 bootstrap（**未调整**均值差的百分位区间，单独记录，不替代主模型 HC3 CI）；删除每个供体重新拟合 assay-adjusted effect，并报告 estimable 次数及同号比例。8 个图示候选还完成 20 次靶基因随机保留敏感性分析：名义保留 80%，minimum 10 限制下实际比例按表记录，例如 ETV3 为 10/11=90.9%。成纤维 GLI2 同号率为 {float(stability[(stability.cell_type=='Fibroblast') & (stability.tf=='GLI2')].same_sign_fraction.iloc[0]):.2f}，不能把所有候选都称为稳定。详见 [供体检查](../results/tables/stability.csv)、[靶基因检查](../results/tables/regulon_target_stability.csv)。

## 功能背景 / Pathway context

{md_table(pathway_top)}

PROGENy 不等于通路组分表达，也不证明临床通路激活。Hallmark 的 50 gene sets 与图示 8 regulon 做 400 次 hypergeometric overlap，BH 一次校正；背景为实际 21,690 expressed genes。关联代表已知靶基因集合重叠，不能叫 disease GRN、共表达模块、TF→pathway 因果边。完整网络资源只保存 ignored cache；GitHub 发布派生 overlap 表与来源。

## 调控边与图件 / Edge evidence and figures

网络边全部来自固定版本 CollecTRI regulons（Zenodo 8192729），保留 source、target、weight、resources、PMIDs、sign_decision；权重 +1/-1 是先验激活/抑制关系，不是本数据重建的 MI、相关系数或效应大小。选取每个图示 regulator 最大绝对实际 target logCPM 差的 6 edges，并注明 contrast cell type；这是用于图示的后验筛选，不能据此验证候选。实体颜色展示 donor 平均表达差，箭头显示 prior sign，两者不应混同。

所有数值图对应 [结果表](../results/tables/) 与 [R 源代码](../scripts/plot_atlas.R)，导出 PDF/SVG/600 dpi PNG；作者 UMAP 只复用真实坐标，未计算轨迹。工作流 Fig01 是方法示意，不是生物数据。各图英文 caption、中文解释及来源见 [Figure Gallery](../gallery/README.md)；组合图不是投稿已验收文件。

## 未运行与阻塞 / Not executed

ARACNe-AP de novo、正式 msVIPER MRA、pySCENIC motif pruning/AUCell/RSS、hdWGCNA、CellOracle、SCENIC+、Pando、GRaNIE、LINGER、scPRINT、Inferelator、RegEnrich、NicheNet 未运行。18 个患者编码不满足本任务约 100 个独立表达样本的 ARACNe 首选条件；本次没有额外完成 bulk 网络。Java/Linux、多重 bootstrap、物种/基因组匹配 cisTarget database、ATAC/enhancer 输入、checkpoint 和足够内存均需分别准备。没有虚构模块、hub gene、motif 或计算扰动，Fig06/10/11 等维持待实现。运行环境磁盘足够但机器总 RAM 16 GB、开始约 1.1 GB 空闲；此轮采用 CSR streaming，不能宣称重型 GRN 已可承载。

## 自检与未来验证 / Checks and next validation

关键数据、统计和分块实现测试见 [test_status](test_status.json)；输入校验见 [input_manifest](../data/input_manifest.json)；独立审查和可视化 QA 分别见 [independent audit](independent_audit.md)、[figure QA](Figure_QA.md)。失败记录见 [Failure_Log](Failure_Log.md)。

下一步先确认 Table S1 生物供体关联，再在独立口腔同研究供体队列重复 candidate ranking；检查在 v3 或匹配 assay 数据中保持方向；使用 ChIP/CUT&Tag、TF perturbation、靶蛋白/通路读出和功能实验验证特异性。公开数据发现与算法一致性只能构成计算支持，不能证明蛋白活性、调控方向或组织修复因果机制。
"""
    (ROOT / "reports/Validation_Report.md").write_text(report, encoding="utf-8")
    print("Validation_Report written from real tables")

if __name__ == "__main__":
    main()
