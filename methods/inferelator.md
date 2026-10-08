# Inferelator / 方法卡片

定位：**GRN inference; TF activity**。来源核查日期：2026-10-08。

基于regularized regression与先验的GRN推断，包含单任务/多任务和bootstrap稳定性，软件package版本与论文Inferelator3.0名称不同。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/flatironinstitute/inferelator)；[官方文档](https://inferelator.readthedocs.io/)。
- 论文：High-performance single-cell gene regulatory network inference at scale: the Inferelator 3.0.，Bioinformatics (Oxford, England)，indexed year 2022，首次发表日期 2022-04-01。[DOI](https://doi.org/10.1093/bioinformatics/btac117)。
- GitHub latest release: `v0.6.4`; published `2026-06-09T15:45:28Z`; repository pushed `2026-06-09T15:45:28Z`.
- 许可证：**BSD-2-Clause**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 规范化表达、TF列表、prior network、可选gold standard、样本/任务元数据。

**输出：** TF–target coefficients/combined confidence、network和cross-validation/bootstrap结果。

## 分析流程 / Analysis logic

准备prior/expression/TF一致性 →设置workflow/regression和seed →bootstrap/模型选择 →confidence网络 →holdout/独立gold-standard评估。

**适用边界：** prior和gold standard必须分开；对同一先验评估易数据泄漏。RNA regression方向依赖建模假设，未证明binding/cause。

## 隔离环境与命令 / Environment and recipes

独立Python；官方推荐PyPI安装，joblib本地并行，Dask集群可选。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m pip install inferelator==0.6.4 joblib
```

```text
python -c "import inferelator; print(inferelator.__version__)"
# Follow the official workflow example with real prior, TF list and sample metadata.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU并行；成本受genes/tasks/bootstrap控制，未测。

## 图件与验收 / Figures and acceptance

precision-recall、coefficient/network confidence、task-specific网络和bootstrap稳定性，自定义图需真实输出。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
