# OmniPath / 方法卡片

定位：**upstream signaling prior**。来源核查日期：2026-10-08。

整合intra/intercellular signaling和regulatory interactions的知识数据库及Python/R客户端；本身不是GRN推断算法。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/saezlab/omnipath)；[官方文档](https://omnipathdb.org/)。
- 论文：Integrated intra- and intercellular signaling knowledge for multicellular omics analysis.，Molecular systems biology，indexed year 2021，首次发表日期 2021-03-01。[DOI](https://doi.org/10.15252/msb.20209923)。
- GitHub latest release: `v1.0.10`; published `2025-10-08T11:10:44Z`; repository pushed `2026-02-19T12:35:05Z`.
- 许可证：**MIT client; resource data licenses vary**。核查级别：`verified_code_text_data_mixed`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** organism/resource/license筛选参数；可用于构建有来源的signed/directed先验。

**输出：** interaction/annotation/complex tables、source、direction/sign、references及资源可用字段。

## 分析流程 / Analysis logic

设定resource与用途 →API下载 →保存访问时间/hash →保留provenance →与表达/先验分析整合。

**适用边界：** client MIT不覆盖所有数据资源；方向与符号冲突/缺失要保留，不以相关性填补。资源网络不能称为本队列推断边。

## 隔离环境与命令 / Environment and recipes

独立Python client或R OmnipathR；本卡仅核对Python saezlab/omnipath。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m pip install omnipath==1.0.10
```

```text
python -c "import omnipath; print(omnipath.__version__)"
# Query the official API with explicit resource and license filters.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：HTTP下载/表格处理；可用性和资源条款需按访问日期固定，无本机推断。

## 图件与验收 / Figures and acceptance

有provenance的upstream pathway graph、source overlap/coverage；所有绘图需后处理。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
