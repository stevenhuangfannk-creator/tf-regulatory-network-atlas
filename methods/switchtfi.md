# SwitchTFI / 方法卡片

定位：**regulator ranking; differentiation**。来源核查日期：2026-10-08。

2025 Genome Biology方法，从既有GRN和单细胞状态转换数据识别分化相关TF。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/bionetslab/SwitchTFI)；[官方文档](https://github.com/bionetslab/SwitchTFI)。
- 论文：SwitchTFI: identifying transcription factors driving cell differentiation.，Genome biology，indexed year 2025，首次发表日期 2025-12-02。[DOI](https://doi.org/10.1186/s13059-025-03876-0)。
- GitHub latest release: `v0.1.0`; published `2025-09-23T07:34:24Z`; repository pushed `2025-12-03T16:53:19Z`.
- 许可证：**GPL-3.0**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** scRNA AnnData、预推断GRN、明确的两状态/transition细胞注释；需本任务验证state定义。

**输出：** transition-specific GRN/edge scores、ranked differentiation TFs。

## 分析流程 / Analysis logic

先审计base GRN →定义source/target states →edge/state统计 →transition网络过滤 →TF ranking与独立perturbation证据比较。

**适用边界：** 不是没有state信息的通用de novo GRN；疾病分组不自动等于分化转换。不能把静态UMAP路径当成真实谱系。

## 隔离环境与命令 / Environment and recipes

隔离conda环境；官方支持仓库switchtfi.yml或Bioconda。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
conda install -c conda-forge -c bioconda switchtfi
```

```text
# In a version-pinned clone with the official example data:
python example.py -d ery
# This is an upstream example recipe, not a run performed for this project.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU和GRN规模相关；本队列state条件未满足，未测。

## 图件与验收 / Figures and acceptance

state-specific表达/edge score、transition GRN、TF ranking与benchmark。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
