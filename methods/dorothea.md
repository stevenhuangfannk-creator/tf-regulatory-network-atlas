# DoRothEA / 方法卡片

定位：**TF activity prior**。来源核查日期：2026-10-08。

有置信度分层的 TF–target regulon 资源，适合对已知先验的活性推断与网络敏感性分析。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/saezlab/dorothea)；[官方文档](https://saezlab.github.io/dorothea/)。
- 论文：Benchmark and integration of resources for the estimation of human transcription factor activities.，Genome research，indexed year 2019，首次发表日期 2019-07-24。[DOI](https://doi.org/10.1101/gr.240663.118)。
- GitHub latest release: `v1.0.0`; published `2020-05-08T08:44:14Z`; repository pushed `2024-02-24T12:21:16Z`.
- 许可证：**GPL-3.0 code; constituent regulon data restrictions vary**。核查级别：`verified_code_text_data_mixed`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 人/鼠 regulon、confidence选择、表达矩阵；保留 interaction direction、sign、来源。

**输出：** 带 confidence 与 signed weight 的网络；活动矩阵由下游算法产生。

## 分析流程 / Analysis logic

按预先设定置信度（如A/B）选择 → 网络覆盖检查 → ULM/VIPER类推断 → confidence层与CollecTRI敏感性比较。

**适用边界：** DoRothEA与CollecTRI共享部分来源，二者一致不是完全独立验证。代码GPL-3.0；部分网络来源对非学术/商业使用有限制。

## 隔离环境与命令 / Environment and recipes

R/Bioconductor或version-matched decoupler Python；不要为纯资源访问额外安装所有R工具。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
Rscript -e "BiocManager::install('dorothea')"
```

```text
Rscript -e "library(dorothea); print(packageVersion('dorothea')); browseVignettes('dorothea')"
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：先验表与activity矩阵；主要成本在下游算法，无本机测试。

## 图件与验收 / Figures and acceptance

置信度分层覆盖、活性 heatmap、TF 排名稳定性与资源一致性。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
