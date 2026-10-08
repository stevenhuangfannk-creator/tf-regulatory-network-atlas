# CollecTRI / 方法卡片

定位：**TF activity prior**。来源核查日期：2026-10-08。

来自多个知识资源的有符号 TF–target regulon 集合；它是先验网络资源，需与 ULM/VIPER 等算法配合。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/saezlab/CollecTRI)；[官方文档](https://github.com/saezlab/CollecTRI)。
- 论文：Expanding the coverage of regulons from high-confidence prior knowledge for accurate estimation of transcription factor activities.，Nucleic acids research，indexed year 2023，首次发表日期 2023-11-01。[DOI](https://doi.org/10.1093/nar/gkad841)。
- GitHub latest release: `biorxiv`; published `2023-04-12T09:05:38Z`; repository pushed `2026-08-24T16:12:21Z`.
- 许可证：**Repository GPL-3.0; constituent data resource licenses vary**。核查级别：`verified_code_text_data_mixed`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 物种参数；后续活动推断使用统一 symbol 的表达矩阵。注意 TF complexes 的保留/拆分设置。

**输出：** source、target、weight 的先验边表；不是由本队列重新推断的调控边。

## 分析流程 / Analysis logic

下载网络 → 保存原始响应与 checksum → 记录版本/访问日期/complex策略 → 筛出实际表达靶基因 → 每 TF 记录 total/observed targets → 用 decoupler 推断活性。

**适用边界：** 网络先验来源、signed权重与推断活性应分开记录。resource license 不可仅从代码 GPL 推断；OmniPath 各原始资源条款仍适用。

## 隔离环境与命令 / Environment and recipes

与选定 decoupler 版本的隔离 Python 环境共用；CollecTRI不是独立 GRN inference 可执行软件。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m pip install decoupler==2.2.0
```

```text
import decoupler as dc
net = dc.op.collectri(organism="human")
net.to_csv("collectri_download.tsv", sep="\t", index=False)
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：网络下载和表格处理一般低于 de novo GRN 推断；服务器可用性、基因覆盖及资源许可需记录。

## 图件与验收 / Figures and acceptance

网络覆盖/靶基因数 QC；活性 heatmap、网络图均依赖后续实际分析。

该方法/资源已用于本项目真实数据流程；实际科学图和执行证据见Gallery与reports。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。

## 本项目实际执行 / Project execution

真实网络先验用于ULM/Python VIPER；网络来源和覆盖保留在结果表。边是curated prior，不是本牙周数据de novo推断。实际流程见[run manifest](../reports/run_manifest.json)。
