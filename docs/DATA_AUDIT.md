# 数据来源与独立重复审计 / Data and replication audit

审计日期：2026-10-08。主分析选择公开 CELLxGENE 牙周 meta-atlas 中 **Williams / GSE164241 同一研究的健康与牙周炎样本**，避免把不同研究的健康与种植体周炎直接作为疾病效应比较。原始研究、meta-atlas 和本项目分析是不同层级；这里记录的是数据完整性与可用性，不证明细胞标签或调控机制的生物学真值。

机器可读清单：[source_audit.json](../data/source_audit.json) · [source_audit.csv](../data/source_audit.csv) · [下载与校验](../data/download_manifest.json) · [GEO 当前元数据](../data/geo_current_metadata.json)。

## 公开候选 / Public candidates

| 来源 | 可用表达与规模 | 分组与注释 | 本次状态与限制 |
|---|---|---|---|
| [GSE266897](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE266897) | 4 个人牙龈 MEX 整数计数文件；36,601 features；共 8,698 released barcodes；矩阵 gzip 共 50,884,934 bytes | 新提交的 4 个样本均为 **诱导性牙龈炎**；不是健康–牙周炎完整研究队列。GEO 所列文件中未发现细胞类型注释 | 当前样本元数据及所有矩阵头通过 HTTP 206 核实；未完整下载或逐值验证 GEO MEX |
| [GSE310110](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE310110) | 3 个 PI MEX 文件；36,601 features；共 15,059 released barcodes；矩阵 gzip 共 140,292,297 bytes | 3 个新样本均为 **种植体周炎**，没有该 accession 内健康对照；供体独立性不能由 GSM 数量单独证明 | 当前样本元数据及所有矩阵头核实；未完整下载。GEO 声明 Cell Ranger 3.1.0，实际文件头分别为 6.1.2、7.2.0、8.0.1，保留这个处理版本差异 |
| [CELLxGENE periodontal meta-atlas](https://cellxgene.cziscience.com/collections/71f4bccf-53d4-4c12-9e80-e73bfb89e398) | 105,918 cells × 35,369 genes；34 个文库标签；705,007,195-byte H5AD；raw/X 为计数，X 为标准化表达 | 原作者/CELLxGENE 细胞注释、UMAP、Study、GSE、Sample ID、assay、disease 可用；健康、牙龈炎、牙周炎齐全 | **已完整下载并审计**；来自 4 个研究的派生对象，不能按 34 个标签直接声称 34 位独立供体 |

GSE266897 对应论文 DOI [10.1038/s41467-024-49037-y](https://doi.org/10.1038/s41467-024-49037-y)；GSE310110 对应 [10.1038/s41467-026-72452-2](https://doi.org/10.1038/s41467-026-72452-2)。CELLxGENE 对应前一篇论文，成员来源为 GSE152042、GSE161267、GSE164241 和 GSE266897。Williams 原始研究为 [10.1016/j.cell.2021.05.013](https://doi.org/10.1016/j.cell.2021.05.013)。

GEO 矩阵的直接 HTTPS 下载地址、压缩字节数、Matrix Market 头及范围探测 hash 均保存在 [candidate_matrix_probes.json](../data/candidate_matrix_probes.json)。这些前缀探测只证明端点可达及文件头声明整数类型，不能替代完整 gzip CRC、SHA 或逐值检查。表中 released barcodes 不是作者最终 QC 后细胞数。

## 主对象完整性 / Object integrity

实际输入是 `data/raw/periodontal_atlas.h5ad`，使用版本固定的 [下载地址](https://datasets.cellxgene.cziscience.com/171607d7-dcc2-4993-9deb-bbc62cf13273.h5ad)。SHA256：

```text
7dc13de46fd2702dbfaf8d69bec933b79b05196ebce7d516e59cea471aa83c4e
```

下载首次提前结束在 683,242,469 bytes。大小和 HDF5 stored_eof 检查发现截断后，用经过 Content-Range 检查的 206 响应补齐最后 21,764,726 bytes，再计算完整 SHA256。当前文件大小与发布值一致，HDF5 可正常只读打开。

[对象审计](../data/cellxgene_object_inspection.json) 对 **raw/X 的全部 138,928,204 个非零值**分块验证：均为非负整数，最大值 58,299；float32 是存储类型，不代表非整数计数。X 的同数量非零值为非负、非整数标准化值。原始 counts 与标准化表达分开使用。

var 的 `_index` 为 Ensembl gene IDs，`feature_name` 为人类基因符号，`feature_reference=NCBITaxon:9606`。源处理记录为 GRCh38/hg38；不能据此声称已经核实所有原始研究使用相同的 GTF release。TF 网络按基因符号匹配时，必须先记录重名 symbol 的处理，并在计数层合并后再标准化。

全部 `is_primary_data=True` 指的是 meta-atlas 在 CELLxGENE 中的首选表示，不是与原 GEO 成员独立的新实验。禁止把成员数据与该 meta-atlas 相加作为新增样本。

## 主比较与供体映射 / Main contrast and donor mapping

选择 `Study=Williams` 且 `GSE=164241`：86,138 cells，其中 normal 54,352、periodontitis 31,786；13 个健康文库、8 个牙周炎文库。21 个选中文库的 GEO 样本标题与分组都在本次实时核实。

[donor_map.csv](../data/donor_map.csv) 保留 CELLxGENE 原 `donor_id` 为 `sample_id`，另存 original_gsm、sample_title、author_sample_id、assay 和 biological_donor。重复编码作如下保守合并：

| 原始活检文库标题 | 分析使用的供体编码 | 核实程度 |
|---|---|---|
| PD161、PD161b | PD161 | GEO 标题已核实；跨活检患者身份仍待原始 Table S1 确认 |
| PD164、PD164b、PD164c | PD164 | GEO 标题已核实；跨活检患者身份仍待原始 Table S1 确认 |
| 其他 GM/PD 编码 | 原编码；GM184a 对应 meta-atlas GM184 | 无选中队列内重复编码；保留来源映射 |

因此采用 **13 个健康供体编码与 5 个保守牙周炎供体编码**，不声称已经完全核实 18 位独立患者。原论文正文确认 8 份疾病活检，但没有在可获取正文中给出重复活检的患者关联。Table S1 XLSX 的 PMC 路径返回 HTML/404，Europe PMC 原文接口返回 500；NCBI BioC 正文已取得。这些访问失败不表示补充表不存在。重复 PD 编码的 5 行 `verified=False`；其他行 `verified=True` 仅表示来源标签映射已核实，不是独立患者身份的全面认证。

计数汇总：[donor_replication_audit.json](../data/donor_replication_audit.json) · [donor_celltype_counts.csv](../data/donor_celltype_counts.csv)。每个健康/疾病供体编码的 fibroblast 分别至少 220/268 cells；artery+capillary+venule 血管内皮合并后至少 560/381 cells，适合作为首批 TF 活性分析。macrophage、neutrophil 的健康供体细胞量较少，需按预设阈值报告实际保留的供体数，不能只报告全组织供体数。

## 批次与统计边界 / Batch and statistical limits

| 分组 | 10x 3′ v2 供体编码 | 10x 3′ v3 供体编码 |
|---|---:|---:|
| normal | 10 | 3 |
| periodontitis | 1 | 4 |

这是 reagent assay 注释，与 GEO 的 Cell Ranger 软件版本是不同字段。主分析采用 donor × cell type pseudobulk，合并同一保守供体编码的计数；疾病比较必须考虑 assay。建议报告 assay-adjusted 模型与 v3-only 敏感性分析。后者最多只有 3 healthy / 4 disease 编码，统计能力有限。调整 assay 不能消除所有未记录的临床和处理混杂。

作者联合 UMAP 用于显示 meta-atlas 细胞位置，不能证明批次消除或疾病效应已经得到独立验证。原作者细胞类型注释保留，不冒称本项目完成独立重注释。TF 活性是基于表达与调控先验的计算推断；不能与 TF 本身表达、实际蛋白活性或因果作用等同。

## 已有本地资产 / Existing local assets

已有 oral-scrna-atlas 索引的 Lin2026 主对象与 curated-v2 overlay 经只读完整 SHA 核对，原文件没有移动或修改。它含 92,112 cells × 21,934 genes：GSE164241 健康局部视图 53,464 cells / 13 donor IDs；Zenodo 19697597 PI 视图 38,648 cells / 8 libraries / 7 donors，其中 IGT6 与 IGT8 同为 D6。counts 抽样为非负整数，X 为标准化表达，注释仍为复现项目的 provisional curated labels。

该局部健康视图不包含 GSE164241 牙周炎队列，且健康与 PI 来源研究和条件完全混杂。因此此次主分析使用重新取得的 CELLxGENE 同研究比较。已有资产仅作为可复用入口审计，未用它推断健康–PI 疾病效应。原位路径与完整检查证据仅保存在忽略的本地 evidence 中；可通过 `LIN2026_PROJECT` 配置原复现根目录。

## 资源与方法适配 / Resources and eligibility

H5AD 约 672 MiB；仅 raw CSR 的 data+indices 就约 1.1 GB，加上 X 和其他对象会超过当前约 1 GB 空闲内存。整个 dense float32 表达矩阵约 14 GiB。此次应使用 h5py 只读元数据、按 CSR 行分块读取以及 donor pseudobulk；不把完整对象转成 dense 矩阵。

RNA、注释和计数支持 CollecTRI/DoRothEA 活性分析及使用有出处网络的 VIPER。同一研究只有 18 个保守供体编码，不能以 86,138 个细胞冒充约 100 个独立样本完成 ARACNe 正式网络重建。pySCENIC motif ranking 数据库仍需单独匹配基因组和 ID；多组学网络需要匹配的 ATAC/enhancer 数据，该 H5AD 未提供。模块、motif 和扰动图件只有实际计算完成后才能标记为完成。

大矩阵和未使用的全文/平台记录保存在 `data/raw/`、`data/cache/`，不进入 Git。CELLxGENE API 未提供明确 dataset-license 字段，本仓库仅保存来源、代码、小型审计表和真实派生结果；引用原始论文并遵守 CELLxGENE 与各原始来源的数据条款。
