# KEGNI / 方法卡片

定位：**GRN inference; knowledge graph**。来源核查日期：2026-10-08。

2025 Genome Biology的knowledge-graph-enhanced方法，从scRNA与cell-type prior知识图谱推断GRN。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/Lipxiao/KEGNI)；[官方文档](https://github.com/Lipxiao/KEGNI)。
- 论文：KEGNI: knowledge graph enhanced framework for gene regulatory network inference.，Genome biology，indexed year 2025，首次发表日期 2025-09-22。[DOI](https://doi.org/10.1186/s13059-025-03780-7)。
- GitHub latest release: `none observed`; published `unknown`; repository pushed `2026-05-30T08:27:40Z`.
- 许可证：**MIT**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** scRNA、cell-type-specific知识图谱、候选TF/genes；benchmark ground-truth需独立保留。

**输出：** cell-type-specific regulatory edge scores/network与benchmark指标。

## 分析流程 / Analysis logic

下载/审计知识图谱和input →适配cell type →锁定repository commit/env →官方训练/inference shell →独立prior-heldout评估。

**适用边界：** 对口腔细胞的KG可用性与迁移能力尚未实测；prior重叠可能造成benchmark泄漏，不能把高分先验学习等同新增实验机制。

## 隔离环境与命令 / Environment and recipes

隔离Linux/WSL2环境；依据源码依赖和官方shell配置，不自动安装未经完整锁定的依赖。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
git clone https://github.com/Lipxiao/KEGNI.git
# Review repository dependencies and pin a commit; no installation was verified here.
```

```text
bash run_mESC.sh
# Official mouse ESC example; the periodontal input adapter is pending.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：knowledge graph和model训练可能需要GPU；显存、权重/数据下载大小和runtime未实测，不编造需求。

## 图件与验收 / Figures and acceptance

knowledge-guided网络、precision-recall/AUPRC比较、GO/program关联；不生成虚假牙周示例。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
