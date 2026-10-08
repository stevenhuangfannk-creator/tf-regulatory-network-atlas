# Pando / 方法卡片

定位：**multiomics; GRN inference**。来源核查日期：2026-10-08。

利用TF表达与motif-associated accessibility建模target expression，形成TF–regulatory region–gene模型及modules。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/quadbio/Pando)；[官方文档](https://quadbio.github.io/Pando/)。
- 论文：Inferring and perturbing cell fate regulomes in human brain organoids.，Nature，indexed year 2023，首次发表日期 2022-10-05。[DOI](https://doi.org/10.1038/s41586-022-05279-8)。
- GitHub latest release: `none observed`; published `unknown`; repository pushed `2026-04-10T15:04:33Z`.
- 许可证：**MIT**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** RNA+ATAC Seurat对象、候选regions、PFM/motif数据库、BSgenome参考版本。

**输出：** 模型coefficients、TF/gene/regulatory modules、region关联。

## 分析流程 / Analysis logic

FindVariableFeatures →initiate_grn →find_motifs →infer_grn →coef →find_modules/NetworkModules；按donor设计评估泛化。

**适用边界：** 不能用纯RNA替代ATAC；regression coefficient是条件建模证据，不能把所有coefficients当作已实验证实的direct binding。

## 隔离环境与命令 / Environment and recipes

隔离R+Seurat+Signac/BSgenome依赖环境；引用genome build必须与peaks匹配。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
Rscript -e "remotes::install_github('quadbio/Pando')"
```

```text
library(Pando)
# Official README analysis entry points:
# grn_object <- initiate_grn(seurat_object)
# grn_object <- find_motifs(grn_object, pfm=motifs, genome=BSgenome.Hsapiens.UCSC.hg38)
# grn_object <- infer_grn(grn_object)
# coef(grn_object)
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU回归/motif scanning；成本取决于regions和candidate interactions，未实测。

## 图件与验收 / Figures and acceptance

TF/gene module、coefficient heatmap、regulome网络/embedding，读者可学习原论文多层网络布局。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
