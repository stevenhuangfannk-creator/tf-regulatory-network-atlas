# CellOracle / 方法卡片

定位：**GRN inference; perturbation**。来源核查日期：2026-10-08。

结合base GRN先验与单细胞RNA建模context-specific网络，模拟TF扰动及状态位移/向量场。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/morris-lab/CellOracle)；[官方文档](https://morris-lab.github.io/CellOracle.documentation/)。
- 论文：Dissecting cell identity via network inference and in silico gene perturbation.，Nature，indexed year 2023，首次发表日期 2023-02-08。[DOI](https://doi.org/10.1038/s41586-022-05688-9)。
- GitHub latest release: `v0.10.12`; published `2022-10-25T21:19:11Z`; repository pushed `2026-04-30T03:24:49Z`.
- 许可证：**Modified Apache-2.0; NON-COMMERCIAL ACADEMIC ONLY**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** count层AnnData、细胞类型/cluster、低维状态图、物种/build匹配base GRN（ATAC+motif或有出处预建先验）。

**输出：** cluster-specific Links/GRN、模拟表达变化、transition probability、perturbation vector field。

## 分析流程 / Analysis logic

选择并审计base GRN → RNA预处理/cluster →GRN拟合与filter →真实TF扰动输入 →simulation →transition/vector field及对照。

**适用边界：** 模型外推不等于真实敲除；先验和状态图限制可识别的变化。没有ATAC时必须标明使用预构建base GRN；单次静态数据不能证明细胞命运或谱系。

## 隔离环境与命令 / Environment and recipes

隔离Python环境；使用官方installation/changelog匹配版本。当前release很旧，原生Windows兼容尚未测；优先Linux/WSL2。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m pip install celloracle==0.10.12
```

```text
python -c "import celloracle; print(celloracle.__version__)"
# GRN fitting and simulation must follow the version-matched official notebooks.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU与基因/细胞数相关；base-GRN数据库另计；memory/runtime未测。

## 图件与验收 / Figures and acceptance

GRN网络、扰动quiver/vector field、simulation scores、TF ranking；Fig10只有真实模拟完成后可生成。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
