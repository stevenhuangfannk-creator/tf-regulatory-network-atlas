# hdWGCNA / 方法卡片

定位：**co-expression**。来源核查日期：2026-10-08。

在单细胞/空间高维数据中构建context-specific共表达模块，分析eigengene、kME、hub和preservation。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/smorabit/hdWGCNA)；[官方文档](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html)。
- 论文：hdWGCNA identifies co-expression networks in high-dimensional transcriptomics data.，Cell reports methods，indexed year 2023，首次发表日期 2023-06-12。[DOI](https://doi.org/10.1016/j.crmeth.2023.100498)。
- GitHub latest release: `v0.4.12`; published `2026-06-16T09:03:39Z`; repository pushed `2026-06-16T09:03:39Z`.
- 许可证：**GNU GPLv3 in DESCRIPTION; LICENSE file is copyright stub**。核查级别：`verified_description_license_stub`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** Seurat对象、规范化表达、donor/sample和cell_type；metacell按sample×cell_type内构建。可评估donor-level pseudobulk路线。

**输出：** module assignment、TOM、module eigengene/hME、kME hub表、module–trait association/preservation结果。

## 分析流程 / Analysis logic

SetupForWGCNA → MetacellsByGroups/NormalizeMetacells → SetDatExpr → TestSoftPowers → ConstructNetwork → ModuleEigengenes → ModuleConnectivity → GetHubGenes →trait/preservation与regulon交叉关联。

**适用边界：** 基础模块是无向共表达，不能直接标为TF–target GRN。metacell不是独立donor。trait关联要用生物重复评估；不要把Harmony后的hME与疾病信号去除问题忽略。最新软件另有TF network功能，需额外motif/GRN证据。

## 隔离环境与命令 / Environment and recipes

独立R/Seurat/WGCNA环境；官方建议conda R4.4环境。Windows编译依赖可能需要Rtools；复杂依赖可用WSL2。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
Rscript -e "remotes::install_github('smorabit/hdWGCNA', ref='v0.4.12')"
```

```text
library(hdWGCNA)
set.seed(1)
# Each construction step requires the real Seurat object and audited metadata.
# See the linked tutorial; inspect PlotSoftPowers before selecting the soft power.
packageVersion("hdWGCNA")
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU；TOM/adjacency以基因²增长，应先限制适用基因并评估block参数；未运行所以无模块、hub或trait结果。

## 图件与验收 / Figures and acceptance

已核对原生函数：PlotSoftPowers、PlotDendrogram、PlotKMEs、ModuleFeaturePlot、ModuleRadarPlot、ModuleCorrelogram、DimPlotMetacells。module–trait和preservation参考官方专门教程。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
