# PROGENy / 方法卡片

定位：**pathway activity**。来源核查日期：2026-10-08。

通过通路扰动响应基因 footprint 推断 pathway 活性，不能把 pathway score标为TF活性。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/saezlab/progeny)；[官方文档](https://saezlab.github.io/progeny/)。
- 论文：Perturbation-response genes reveal signaling footprints in cancer gene expression.，Nature communications，indexed year 2018，首次发表日期 2018-01-02。[DOI](https://doi.org/10.1038/s41467-017-02391-6)。
- GitHub latest release: `none observed`; published `unknown`; repository pushed `2023-01-30T10:01:10Z`.
- 许可证：**Apache-2.0**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 表达矩阵、物种及PROGENy footprint基因数/权重网络。

**输出：** 通路 × 样本/细胞活性矩阵；受上游信号影响的转录 footprint。

## 分析流程 / Analysis logic

选择species/top footprint数 → 检查覆盖 → decoupler或R推断 → donor-level汇总 → 与TF活动关联作为探索。

**适用边界：** 通路活性不是 TF regulon；RNA footprint并非直接磷酸化测量。不能将通路–TF相关性转为已证明上游调控边。

## 隔离环境与命令 / Environment and recipes

独立R环境或现有decoupler Python环境。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
Rscript -e "BiocManager::install('progeny')"
```

```text
Rscript -e "library(progeny); print(packageVersion('progeny')); browseVignettes('progeny')"
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU；表格/矩阵计算，无本机测试。

## 图件与验收 / Figures and acceptance

pathway活动heatmap/dot plot；TF–pathway关联网络需额外统计并标为association。

该方法/资源已用于本项目真实数据流程；实际科学图和执行证据见Gallery与reports。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。

## 本项目实际执行 / Project execution

真实PROGENy footprint使用top=100、threshold=0.05、academic资源条件，1398条prior footprint边、14个pathways，ULM输出和donor-level对照已保存。来源checksum见[pathway manifest](../reports/pathway_manifest.json)；prior-target pathway overlap另作探索，不能声称已证实TF→pathway调控。
