# GRaNIE / 方法卡片

定位：**multiomics; GRN inference**。来源核查日期：2026-10-08。

跨匹配样本整合RNA与ATAC/H3K27ac的共变，推断enhancer-mediated GRN；GRaNPA用于预测性能评估。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://git.embl.de/grp-zaugg/GRaNIE)；[官方文档](https://bioconductor.org/packages/GRaNIE/)。
- 论文：GRaNIE and GRaNPA: inference and evaluation of enhancer-mediated gene regulatory networks.，Molecular systems biology，indexed year 2023，首次发表日期 2023-04-19。[DOI](https://doi.org/10.15252/msb.202311627)。
- GitHub latest release: `none observed`; published `unknown`; repository pushed `unknown`. Bioconductor当前网页版本 `1.16.0`；仓库push日期未从该来源取得。
- 许可证：**Artistic-2.0**。核查级别：`verified_bioconductor_metadata`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 配对样本RNA-seq表达、ATAC/H3K27ac peaks/counts、motif和genome注释；样本可为不同个体。

**输出：** TF–enhancer、enhancer–gene、TF–gene eGRN；GRaNPA模型性能是单独流程。

## 分析流程 / Analysis logic

匹配sample/IDs →peak/motif整合 →TF–enhancer和enhancer–gene links →filter eGRN →GRaNPA/外部验证。

**适用边界：** 不是把同一患者的细胞数量当作跨个体协方差样本量的方法；纯RNA无输入条件。performance evaluation应避免训练/测试同样本泄漏。

## 隔离环境与命令 / Environment and recipes

隔离R/Bioconductor；官方源码在EMBL GitLab而非猜测的GitHub项目。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
Rscript -e "BiocManager::install('GRaNIE')"
```

```text
Rscript -e "library(GRaNIE); print(packageVersion('GRaNIE')); browseVignettes('GRaNIE')"
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU相关性/多重检验；成本取决于samples、peaks、genes，未测。

## 图件与验收 / Figures and acceptance

eGRN边和网络、motif/peak QC、TF–enhancer–gene层图；GRaNPA预测表现另记录。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
