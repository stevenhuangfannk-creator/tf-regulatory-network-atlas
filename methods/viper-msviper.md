# VIPER / 方法卡片

定位：**TF activity**。来源核查日期：2026-10-08。

VIPER 根据有出处的 regulon 推断样本/细胞的调控蛋白活性；msVIPER 根据组间表达 signature、null model 和 regulon 寻找 master regulators。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://git.bioconductor.org/packages/viper)；[官方文档](https://bioconductor.org/packages/viper/)。
- 论文：Functional characterization of somatic mutations in cancer using network-based inference of protein activity.，Nature genetics，indexed year 2016，首次发表日期 2016-06-20。[DOI](https://doi.org/10.1038/ng.3593)。
- GitHub latest release: `none observed`; published `unknown`; repository pushed `unknown`. Bioconductor当前网页版本 `1.46.0`；仓库push日期未从该来源取得。
- 许可证：**Columbia software evaluation; non-commercial academic/educational restrictions**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 基因 × 样本表达或基因差异 signature；R regulon list，每个 TF 的 tfmode（signed mode of regulation）和 likelihood；msVIPER 需要合适 signature/null model。

**输出：** 蛋白/TF 活性矩阵、NES、主调控因子及富集结果；不等于 TF RNA 表达。

## 分析流程 / Analysis logic

验证网络组织/物种/ID 和靶基因覆盖 → 构造 regulon → VIPER 活性 → donor × cell type 汇总或 pseudobulk → 组间统计 → msVIPER signature 与 null-model 检验 → 同数据比较。

**适用边界：** 预构建网络用于推断不能声称已完成 ARACNe de novo 网络。msVIPER 的显著性依赖 null model；细胞级分数分布不能充当供体级疾病显著性。不要把 decoupler 的相似富集算法替代品称为运行了 Bioconductor VIPER。

## 隔离环境与命令 / Environment and recipes

独立 R/Bioconductor 环境。当前网页显示 BioC 3.23、R 4.6；若使用旧 R，选匹配的 BioC release并记录 sessionInfo。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
Rscript -e "if (!requireNamespace('BiocManager', quietly=TRUE)) install.packages('BiocManager'); BiocManager::install('viper')"
```

```text
Rscript -e "library(viper); print(packageVersion('viper')); browseVignettes('viper')"
# Analysis entry points in the package: viper(), msviper(), aracne2regulon().
# The expression, network and null-model objects must be supplied and audited first.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU；矩阵和 regulon 覆盖决定内存；ARACNe 重建资源另计。没有本机安装/数据实测。

## 图件与验收 / Figures and acceptance

活性 heatmap/feature map、master regulator enrichment、NES 排名；由真实 VIPER/msVIPER 输出构建。

原始Bioconductor VIPER已经实际运行；msVIPER尚未运行。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。

## 本项目实际执行 / Project execution

Bioconductor viper 1.36.0原始实现已运行；source-audit网页的当前1.46.0是另一版本快照。输入为真实46个donor×cell_type pseudobulk、21690个genes和CollecTRI有符号先验；minsize=10、likelihood=1、pleiotropy=TRUE，method="none"表示传入已经准备的signature，不由VIPER再次转换。输出516个regulators，保存在results/tables/bioc_viper_activity_matrix.csv，并进行donor-level OLS/HC3。实现比较入口为[validate_viper.py](../workflows/validate_viper.py)和[viper validation](../reports/viper_validation.json)。

ULM与原始VIPER在同一数据和同一先验上的疾病效应Spearman为约0.935（Endothelial）、0.941（Fibroblast）、0.935（Macrophage）。这只说明算法间一致性，不是独立生物学证据。msVIPER/master-regulator enrichment、ARACNe de novo网络均未运行。
