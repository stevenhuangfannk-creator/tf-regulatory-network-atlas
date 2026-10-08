# SCENIC+ / 方法卡片

定位：**multiomics; GRN inference; perturbation**。来源核查日期：2026-10-08。

联合scRNA和scATAC构建TF–region–gene enhancer-driven GRN（eGRN）。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/aertslab/scenicplus)；[官方文档](https://scenicplus.readthedocs.io/)。
- 论文：SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks.，Nature methods，indexed year 2023，首次发表日期 2023-07-13。[DOI](https://doi.org/10.1038/s41592-023-01938-4)。
- GitHub latest release: `v1.0a2`; published `2025-01-13T07:15:18Z`; repository pushed `2026-01-16T13:46:10Z`.
- 许可证：**Academic Non-commercial Software License Agreement**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 配对multiome或可整合的scRNA/scATAC、region accessibility、peak坐标/参考genome、motif/ranking databases、细胞注释。

**输出：** eRegulons、TF–region和region–gene links、region/gene regulon活动；额外模拟需单独运行。

## 分析流程 / Analysis logic

cisTopic accessibility分析 →cisTarget motif →region–gene推断 →eRegulon组装/过滤 →activity/RSS →chromatin-supported网络及可选扰动。

**适用边界：** 仅RNA案例不具备生成enhancer网络的输入。peak–gene距离/共变不是因果；配对与unpaired数据需分开描述。

## 隔离环境与命令 / Environment and recipes

官方明确Linux环境，建议独立conda Python3.11；WSL2/Linux执行。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
conda create --name scenicplus python=3.11 -y
conda activate scenicplus
git clone https://github.com/aertslab/scenicplus
cd scenicplus
# Pin and record a tested release or commit before installation.
pip install .
```

```text
scenicplus --help
# Configure the official workflow with real RNA/ATAC and external database paths.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：多组学 +大型motif/ranking数据库；CPU并行和大内存，实际资源未测。不可默认在Windows主环境安装。

## 图件与验收 / Figures and acceptance

eRegulon activity、RSS、TF–enhancer–gene网络、genome tracks、dot matrix、可选扰动；Fig11需motif/chromatin证据。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
