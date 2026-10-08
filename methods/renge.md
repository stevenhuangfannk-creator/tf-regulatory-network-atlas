# RENGE / 方法卡片

定位：**GRN inference; perturbation**。来源核查日期：2026-10-08。

2023-12发表的time-series scCRISPR GRN方法，模型化KO效应传播以区分部分direct/indirect links。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/masastat/RENGE)；[官方文档](https://github.com/masastat/RENGE)。
- 论文：RENGE infers gene regulatory networks using time-series single-cell RNA-seq data with CRISPR perturbations.，Communications biology，indexed year 2023，首次发表日期 2023-12-28。[DOI](https://doi.org/10.1038/s42003-023-05594-4)。
- GitHub latest release: `v0.0.3`; published `2023-11-11T20:41:14Z`; repository pushed `2026-09-18T16:59:57Z`.
- 许可证：**MIT**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** E: cells×genes normalized/log表达；X: cells×(genes+1)，KO one-hot +sampling time。

**输出：** A: genes×genes；A[i,j]为gene j→gene i coefficient；A_qval同形状q值；可选KO expression predictions。

## 分析流程 / Analysis logic

核对guide/time/sample/KO对照 →拟合与hyperparameter估计 →calc_qval →sign/FDR网络 →时序预测与外部验证。

**适用边界：** 需要真实多时间点CRISPR perturbation数据；本牙周RNA横断面不能运行。causal interpretation依赖干预、时间和模型假设，不能泛化全部预测边为已验证因果。

## 隔离环境与命令 / Environment and recipes

独立Python，官方pip renge；版本按release/环境锁固定。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m pip install renge
```

```text
# Official README calls (after importing Renge and supplying X/E):
# reg = Renge()
# A = reg.estimate_hyperparams_and_fit(X, E)
# A_qval = reg.calc_qval()
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU模型/genes²矩阵；需要真实perturbation/timepoints，资源未测。

## 图件与验收 / Figures and acceptance

signed/FDR-filtered network、KO time-series预测、AUPRC benchmark；原论文Fig5明确颜色区分正负边。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
