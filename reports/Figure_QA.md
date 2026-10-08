# 图件验收 / Figure QA

日期：2026-10-08。已输出 13 套图件，均有 PDF、SVG 和 600 dpi PNG；全部由 R 原生图形设备生成。组合图宽约 183 mm、高 247 mm，8 个面板；其他图的尺寸与 subset/source hash 见 `results/figures/figure_provenance.json`。

## 自动与字体检查 / Automated and typography checks

R source preflight：17 PASS、3 WARN、0 FAIL；warnings 分别为简单 delimiter 检查需 R `parse()` 补充、PNG 而非 TIFF、宽度从 JSON 读取而非代码字面量。已完成 parse、600 dpi PNG 与实际 PDF 宽度测量，详见 [source preflight](../gallery/source_preflight.json)。

技能要求的 PDF `Tf` operator 审计已对 13 PDFs 运行。Cairo 使用归一化 `Tf=1` 并在文字矩阵放大，该简化脚本不处理文字矩阵，因而产生原始 1pt 警告。随后使用 PyMuPDF **非绘图文件检查**量出实际 transformed text spans：所有 PDF 最小实际字号均 ≥6.5 pt，Fig01 ≥7.68 pt；没有小于 5 pt 的 glyph spans。原始警告、实际测量和说明保留于 [effective-font audit](../gallery/pdf_effective_font_audit.json)。未使用 Python 绘制、替换或重新渲染 R 图。

PDF 文本可提取，SVG 保留 text 元素，密集 UMAP 点由 R 原生 rasterization 生成，不影响坐标文字可编辑性。没有下载/复制第三方原图；workflow 是原创示意，其余数值来自真实表。图件没有临床/实验照片、图像增强或拼接。

## 逐图和面板 / Rendered inspection

| 图件/面板 | 科学问题与数据 | 区间/统计单位 | 视觉与结论检查 |
|---|---|---|---|
| Fig01 | 实际分析顺序及待扩展边界 | 示意，无观测值/误差条 | ASCII donor x cell type；字体与箭头清晰 |
| Fig02 | 真实作者 UMAP、GTF3A/ZNF148 transcript 与 activity | 全部 38,971 细胞，描述性，无推断误差条 | 同坐标不抽样，表达/活性不同 scale，未制造轨迹 |
| Fig03 | 候选 ULM 供体异质性 | donor×cell type raw score 按 factor z 标准化 | H/PD、donor、cell type 可读；不把 z 值叫效果大小 |
| Fig04 | CollecTRI signed prior target | donor 未调整表达差仅作颜色背景 | 激活蓝实线、抑制橙虚线；ASCII 标题；非 de novo GRN |
| Fig05 | ULM disease association | assay-adjusted coefficient；HC3 95% CI；donors | reference zero、q 星号和不确定区间清晰，不混同 cell p 值 |
| Fig09 | 细胞类型活性轮廓 | mean cell ULM，描述性 | 点大小记录 cells，标准化色标明示；不是 AUCell RSS |
| Fig12 | 同先验算法 nominal P-value rank | Spearman descriptive 516 regulators/type | candidate shape legend 替代拥挤标签；P rank 与 effect rank 区分 |
| Fig13 | PROGENy donor pathway scores | donor-level scores 按 pathway z | 14 pathways、Healthy/PD donor columns；不是 TF 活性 |
| Fig13b | PROGENy disease association | assay-adjusted donor model/HC3 CI/BH | 原始 effect/CI 与实际表一致，q 仅探索性 |
| Fig14 | 原始 Bioconductor VIPER donor scores | 与 ULM 相同 inputs/prior | matched rows/donors、within-factor z；不是 ARACNe |
| Fig15 | TF prior targets 与 Hallmark overlap | 400 hypergeometric tests，统一 BH | 点大小 actual overlaps、色标 -log10q；非新模块/causal path |
| Fig16 | 同一供体 transcript/activity 对照 | 原始配对观测，描述性 | 不同量纲标出，不画暗示因果的拟合线 |
| Composite a/b | cell context 与 GTF3A footprint | all analyzed cells；descriptive | 同真实坐标，legend/axis 清晰 |
| Composite c/d | disease effect 与 donor variation | HC3 95% CI；13H/5PD group | 横坐标、donor 标签、不确定区间无冲突；small-n 在 caption |
| Composite e/f | prior structure 与算法一致性 | signed prior / nominal P ranks | 10 target 子集 logged，shape labels 不遮挡点，legend 不裁切 |
| Composite g/h | pathway score 与 gene-set overlap | HC3 donor CI / prior hypergeometric | 2 类证据清楚区分；未冒充 TF–module network |

初稿 Unicode 箭头标题、边图图例裁切、过密 label 和长模型副标题已改正并重新导出。所有 13 PNG 逐图检查，综合图再次整页检查。作者 UMAP、heatmap、network 和候选点图/森林图的 selected rows 与 code/provenance 对照；没有为了排版篡改数值。

## 适用边界 / Limits

本 QA 确认来源、图形、字体和数值追溯，不认证患者独立性、assay causal identification、蛋白测量或期刊正式录用图件要求。供体不平衡、后验 candidate/target selection、来源 prior 和共享算法输入局限见 [Validation Report](Validation_Report.md)。重跑如果资源、参数或图件源代码变动，需要重新检验并更新本 QA。
