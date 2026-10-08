# LINGER / 方法卡片

定位：**multiomics; GRN inference; TF activity; perturbation**。来源核查日期：2026-10-08。

atlas-scale外部bulk训练信息与lifelong neural network、motif先验联合multiome，产生TF–RE、RE–TG、TF–TG网络并支持下游TF activity。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/Durenlab/LINGER)；[官方文档](https://github.com/Durenlab/LINGER/blob/main/docs/User_guide.md)。
- 论文：Inferring gene regulatory networks from single-cell multiome data using atlas-scale external data.，Nature biotechnology，indexed year 2025，首次发表日期 2024-04-12。[DOI](https://doi.org/10.1038/s41587-024-02182-7)。
- GitHub latest release: `v1.0.0`; published `2024-02-09T10:09:22Z`; repository pushed `2026-07-11T14:41:24Z`.
- 许可证：**README claims MIT; standard license text not found**。核查级别：`readme_claim_unresolved`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** scRNA counts+ATAC accessibility counts、peaks、参考genome、motif、匹配外部bulk/pretrained参数；纯RNA TF activity依赖已有LINGER网络。

**输出：** population/cell type GRN、cis/trans regulatory strength、TF activity、可选perturbation prediction。

## 分析流程 / Analysis logic

获取数据/权重并记录版本 →multiome预处理 →逐gene NN拟合/transfer →Shapley/embedding-derived links →cell-type GRN →activity/driver score。

**适用边界：** 平均absolute Shapley strength不自动提供激活/抑制符号。跨组织和纯RNA转移需要验证。README论文年份2024与issue pubYear2025并存，DOI固定。

## 隔离环境与命令 / Environment and recipes

隔离Python + bedtools（官方要求）；Linux/WSL2优先。README推荐LingerGRN==1.110，GitHubtag v1.0.0不是该PyPI版本。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m pip install LingerGRN==1.110
conda install -c bioconda bedtools
```

```text
python -c "import linger; print(linger.__file__)"
# Version-matched real-data workflow: docs/PBMC.md; do not substitute a generic RNA-only call.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：逐gene NN和Shapley较重；CPU并行/可选GPU需按官方benchmark匹配；外部模型权重大小、下载可用性和许可证未运行核查，不提供虚构GB/分钟。

## 图件与验收 / Figures and acceptance

TF–RE–TG网络、cell-type network heatmap、driver-score排名、activity map与真实扰动曲线。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。

## 外部模型/网络资源 / External assets

官方[PBMC教程](https://github.com/Durenlab/LINGER/blob/main/docs/PBMC.md)要求先获取外部bulk general GRN/parameters data_bulk.tar.gz，链接[Google Drive页面](https://drive.google.com/file/d/1jwRgRHPJrKABOk7wImKONTtUupV7yJ9b/view?usp=sharing)。本次核对了该URL出现在官方教程，但未验证Google Drive下载端点、archive完整性、大小或具体权重授权；因此不能标为已可运行。下载完成后应生成本地checksum，选择与genome/build匹配的资源，并保留原始模型版本。见[外部资源证据](../docs/methods_assets.json)。
