# NicheNet / 方法卡片

定位：**upstream signaling**。来源核查日期：2026-10-08。

链接sender ligand–receiver target genes，联合ligand–receptor、signaling与TF target先验排序上游配体。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/saeyslab/nichenetr)；[官方文档](https://github.com/saeyslab/nichenetr)。
- 论文：NicheNet: modeling intercellular communication by linking ligands to target genes.，Nature methods，indexed year 2020，首次发表日期 2019-12-09。[DOI](https://doi.org/10.1038/s41592-019-0667-5)。
- GitHub latest release: `v2.2.0`; published `2024-09-05T14:26:21Z`; repository pushed `2026-09-25T08:37:54Z`.
- 许可证：**GPL-3 in DESCRIPTION; license file not found in inspected paths**。核查级别：`verified_description`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** sender/receiver表达、receiver gene set与background、ligand–target matrix及signaling/LR先验。

**输出：** ligand activity ranking、ligand–target权重、ligand–receptor与candidate signaling paths。

## 分析流程 / Analysis logic

定义receiver和contrast →target/background set →表达ligand/receptor过滤 →ligand activity →prior-weighted target/link可视化。

**适用边界：** ligand activity不是TF activity；表达通讯预测不是真实相互作用或上游因果证明。没有严格receiver对照不能制造疾病配体差异。

## 隔离环境与命令 / Environment and recipes

独立R；本卡核对R nichenetr，Python nichenetpy为另一个实现。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
Rscript -e "remotes::install_github('saeyslab/nichenetr', ref='v2.2.0')"
```

```text
Rscript -e "library(nichenetr); print(packageVersion('nichenetr')); browseVignettes('nichenetr')"
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU；先验RDS矩阵另下载并记录hash/版本；不能直接vendor大型模型。

## 图件与验收 / Figures and acceptance

ligand activity rank、ligand–target heatmap、LR dot/chord、prior signaling path graph。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
