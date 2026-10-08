# RegEnrich / 方法卡片

定位：**GRN inference; regulator ranking; co-expression**。来源核查日期：2026-10-08。

整合differential expression、COEN/GRN构建、target enrichment和regulator ranking。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://git.bioconductor.org/packages/RegEnrich)；[官方文档](https://bioconductor.org/packages/RegEnrich/)。
- 论文：RegEnrich gene regulator enrichment analysis reveals a key role of the ETS transcription factor family in interferon signaling.，Communications biology，indexed year 2022，首次发表日期 2022-01-11。[DOI](https://doi.org/10.1038/s42003-021-02991-5)。
- GitHub latest release: `none observed`; published `unknown`; repository pushed `unknown`. Bioconductor当前网页版本 `1.22.1`；仓库push日期未从该来源取得。
- 许可证：**GPL (>=2)**。核查级别：`verified_bioconductor_metadata`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 基因 × 样本表达、实验设计/组别、候选regulators；bulk/pseudobulk设计优先。

**输出：** 差异表、COEN或GRN、enrichment/regulator score与ranking。

## 分析流程 / Analysis logic

设计与表达QC → differential expression →选择COEN/GRN模式 → FET/GSEA enrichment → regulator score/rank及参数敏感性。

**适用边界：** COEN模式不能标为有向GRN；regulator enrichment不等于TF蛋白活性测量；正式DE设计必须使用biological replicates。

## 隔离环境与命令 / Environment and recipes

独立R/Bioconductor；Bioc页面当前1.22.1（3.23）。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
Rscript -e "BiocManager::install('RegEnrich')"
```

```text
Rscript -e "library(RegEnrich); print(packageVersion('RegEnrich')); browseVignettes('RegEnrich')"
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：COEN矩阵/GRN推断可能随基因数²增长；论文有资源benchmark，但不能移植为本机性能承诺。

## 图件与验收 / Figures and acceptance

regulator ranking、target enrichment、网络/共表达与多数据集ranking一致性。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
