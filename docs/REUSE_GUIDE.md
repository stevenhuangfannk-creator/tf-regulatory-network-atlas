# 迁移到其他口腔数据 / Reuse with another cohort

优先从有完整 donor、condition、study、assay 元数据的同研究人单细胞数据开始。保留作者数据和来源 SHA；所有新结果写入新的分析版本/独立 checkout，避免覆盖已发表案例。

1. 准备标准 CELLxGENE 结构的 H5AD：`raw.X` 为 cells×genes CSR 非负整数 counts；`raw.var.feature_name` 为 human gene symbols；`obs` 包含 `donor_id`（原 sample/library ID）、`cell_type`、`disease`、`Study`、`assay`；`obsm.X_umap` 是真实坐标。其他 AnnData/Seurat 数据先在独立文件中做格式转换，不写原始对象；未提供 count 层时不能假定归一化矩阵为 raw counts。
2. 为每个文库人工审计 `data/donor_map.csv`；`sample_id` 必须与 H5AD donor_id 字段精确一致，`biological_donor` 才是独立患者编码。合并技术文库/同人活检，不臆造供体。涉及配对、多个疾病状态或同人时间点时，当前未配对统计模型会阻止混合条件供体；应先改为配对/混合模型并增加复现测试。
3. 修改 `config/analysis.json` 的 `sample_prefix`、`cell_type_map`、`cell_types`、阈值和 seed；`study` 作为记录字段。当前条件对应 `normal`/`periodontitis`，技术敏感性针对 10x v2/v3。不同分组或 assay 必须明确修改条件映射和统计设计，不能只改文件名冒称通用差异模型。
4. 在 `scripts/download_inputs.py` 登记新数据固定 URL 和 SHA；把新 H5AD 存入本项目 ignored `data/raw/periodontal_atlas.h5ad`。不要沿用旧 input_manifest 校验新文件；旧 manifest/报告保留在 Git，新增案例另建版本。
5. 先核查 species、gene identifiers、reference genome 与网络来源：本案例 CollecTRI 是 human symbol prior；鼠数据要显式翻译/更换 regulon，不能直接转大写当作 orthology；motif 数据库需要独立核对 genome/build。
6. 运行 `scripts/run_all.py`，检查 donor-celltype 数量、固定背景基因、target 覆盖、模型 rank、v3 子集、留一供体和靶基因敏感性。某 celltype 少于 3 independent donors/condition 或疾病与 assay 完全混杂时应停止正式差异推断，不退回 cell-level p 值。
7. 复核新结果排名与所有图例；文章图不能复制旧 TF、旧 q 值、旧 donor 数。网络边保留 prior vs MI inference vs coexpression vs motif/enhancer 等证据类型。算法一致性、trajectory、in silico perturbation 和生物因果证据分开。

当前迁移范围是 **标准化人 scRNA、同研究健康/牙周炎、非配对 donor 分析**；一般 ATAC/multiome、疾病名、全新 assay、多因素临床设计的适配尚未验证。高级方法扩展见 [Roadmap](EXTENSION_ROADMAP.md)，图件契约见 [Gallery](../gallery/README.md)。
