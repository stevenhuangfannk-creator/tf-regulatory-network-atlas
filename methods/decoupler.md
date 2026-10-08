# decoupler / 方法卡片

定位：**TF activity; pathway activity**。来源核查日期：2026-10-08。

整合多种基于先验网络的活动/富集方法；CollecTRI/DoRothEA 推断 TF 活性，PROGENy 推断 pathway 活性。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/scverse/decoupler)；[官方文档](https://decoupler.scverse.org/)。
- 论文：decoupleR: ensemble of computational methods to infer biological activities from omics data.，Bioinformatics advances，indexed year 2022，首次发表日期 2022-03-08。[DOI](https://doi.org/10.1093/bioadv/vbac016)。
- GitHub latest release: `v2.2.0`; published `2026-07-11T00:57:05Z`; repository pushed `2026-10-05T18:49:08Z`.
- 许可证：**BSD-3-Clause**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 细胞/样本 × 基因矩阵或 AnnData；source、target、weight 网络；规范化处理、物种和ID必须显式指定。

**输出：** TF/pathway activity、方法适用的模型 p value；AnnData obsm 或返回矩阵，取决于版本/API。

## 分析流程 / Analysis logic

统一表达/网络 gene ID → 按 TF 覆盖过滤 → ULM 等适用方法 → 细胞注释整合 → donor × cell type 分析 → TF expression–activity 对照 → 同数据算法一致性。

**适用边界：** ULM 单条回归的模型 p value 不是疾病组间显著性。Python v2 API 为 dc.op / dc.mt，不能混用 v1 的 run_ulm/get_collectri 示例；实际本项目版本以环境锁和报告为准。

## 隔离环境与命令 / Environment and recipes

独立 Python 环境；canonical repo scverse/decoupler（saezlab/decoupler-py重定向）。saezlab/decoupler会指向R decoupleR。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m venv .venv-decoupler
# Activate this environment with the command appropriate to the shell.
python -m pip install decoupler==2.2.0
```

```text
import decoupler as dc
net = dc.op.collectri(organism="human")
# Run with the version-matched ULM API on the audited matrix/AnnData:
# dc.mt.ulm(data, net, tmin=5)
# Real project execution is documented in reports, not certified by this card.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU；大矩阵应使用稀疏/分块表示。成本取决于细胞数、基因数和 TF 数；本卡没有进行测量。

## 图件与验收 / Figures and acceptance

活动 feature map、group activity matrix、差异 rank dot/forest、TF expression–activity scatter、方法一致性；绘图API应与v2文档匹配。

该方法/资源已用于本项目真实数据流程；实际科学图和执行证据见Gallery与reports。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。

## 本项目实际执行 / Project execution

项目实际版本decoupler 2.1.2（上文最新release为独立来源快照）。实际运行ULM和dc.mt.viper Python实现，使用同一CollecTRI先验。38971个筛选细胞、46个donor×cell_type pseudobulk、18名生物供体；seed=20261008。统计按donor-level disease+assay OLS/HC3和v3-only sensitivity；具体输入/结果及环境见[run manifest](../reports/run_manifest.json)。这不是原始Bioconductor VIPER执行证明。
