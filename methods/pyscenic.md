# pySCENIC / 方法卡片

定位：**GRN inference; TF activity**。来源核查日期：2026-10-08。

GRNBoost2/GENIE3共表达候选 → cisTarget motif剪枝 → regulon → AUCell细胞内靶基因rank富集。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/aertslab/pySCENIC)；[官方文档](https://pyscenic.readthedocs.io/)。
- 论文：A scalable SCENIC workflow for single-cell gene regulatory network analysis.，Nature protocols，indexed year 2020，首次发表日期 2020-06-19。[DOI](https://doi.org/10.1038/s41596-020-0336-2)。
- GitHub latest release: `0.12.1`; published `2022-11-21T13:20:37Z`; repository pushed `2025-06-26T09:57:37Z`.
- 许可证：**GPL-3.0**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 单细胞表达loom/适配矩阵、候选TF列表、物种和genome build匹配的motif ranking Feather v2数据库、motif annotations。

**输出：** adjacencies.tsv、motif enrichment/regulons、细胞 × regulon AUCell矩阵；RSS需基于有细胞注释的AUCell矩阵另算。

## 分析流程 / Analysis logic

GRNBoost2或GENIE3 →共表达modules →motif enrichment剪枝 →regulon构建 →AUCell →RSS、regulon聚类与TF–target图。保留motif数据库版本及checksum。

**适用边界：** AUCell不是VIPER/ULM的同一统计尺度。motif富集不等于ChIP证明；基于TF motif提供的方向仍是候选。不要把GRNBoost2纯共表达边与motif支持regulon边混称。

## 隔离环境与命令 / Environment and recipes

独立Python3.10环境为起始方案；官方0.12.1较旧，须检查NumPy/Dask/ctxcore兼容。Linux/WSL2优先；Feather v2、ctxcore>=0.2是官方要求。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m pip install pyscenic==0.12.1
```

```text
pyscenic grn expression.loom tfs.txt -o adjacencies.tsv --num_workers 4 --seed 1
pyscenic ctx adjacencies.tsv rankings.feather --annotations_fname motifs.tbl --expression_mtx_fname expression.loom --output regulons.csv --num_workers 4
pyscenic aucell expression.loom regulons.csv --output aucell.loom --num_workers 4 --seed 1
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU并行；motif排名数据库通常是大型外部依赖，禁止直接推GitHub；需记录磁盘/内存测量，卡片不承诺固定耗时。

## 图件与验收 / Figures and acceptance

AUCell feature map/heatmap、RSS、regulon clustering、motif enrichment、TF–target图；RSS/source计算入口应使用版本匹配tutorial。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
