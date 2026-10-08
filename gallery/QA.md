# 图件审查 / Figure QA

状态：13 套真实图件已生成并检查；每套包含 PDF、SVG、600 dpi PNG。绘图后端为 R 4.3.1，ggplot2、patchwork、svglite、Cairo PDF、ragg 和 ggrastr。每个科学数值来源于真实结果表，不生成模拟替代。图源、输入校验值、软件版本和显示筛选见 [provenance](../results/figures/figure_provenance.json)，科学图注见 [real_figures.md](real_figures.md)。

## 自动检查 / Automated checks

- R `parse()` 检查绘图与原始 VIPER 脚本通过。
- 科学图源 preflight：17 PASS、3 WARN、0 FAIL，见 [source_preflight.json](source_preflight.json)。3 个警告分别为 R 的简单 delimiter 检查需 `parse()` 补充、PNG 而非 TIFF、宽度由 JSON 读取而非脚本字面量；本项目已实际 parse、按用户要求生成 600 dpi PNG，并测得所有 PDF 宽度约 183 mm。
- 必需的 `audit_pdf_text.py` 已对全部 13 个 PDF 执行。Cairo 使用 `Tf = 1` 配合 scaled text matrix，该脚本只读 `Tf` 而产生低于 5 pt 的警告。没有把该原始检查标成通过；[pdf_effective_font_audit.json](pdf_effective_font_audit.json) 保存了原始结果与解释。
- 使用 PyMuPDF 非绘图文本提取读取 text matrix 后的有效字体尺寸，13 个 PDF 的可选文字均达到 5 pt 下限。最小有效字号为 6.5 pt；Fig01 最小约 7.682 pt。该检查没有重画、渲染或改变 R 图件。
- PDF 和 SVG 保存可编辑文字，UMAP 密集点由 R 以 600 dpi 栅格化；没有为了性能抽取细胞。综合图尺寸约 183 × 247 mm。

## 逐图视觉和科学检查 / Panel review

| 图或面板 / Panel | 独立科学问题 / Unique question | 概括与区间 / Summary and uncertainty | 重复单位 / Unit | 标签、碰撞与状态 / Review |
|---|---|---|---|---|
| Fig01 | 实际执行了哪些证据步骤 | 真实细胞数、先验和模型流程；无数值区间 | 流程示意 | 已检查框内文本、箭头和 ASCII donor x label；通过 |
| Fig02 | 自身表达和下游足迹如何分布 | 所有细胞原始显示分数；无区间，描述图 | Cell，非独立统计重复 | 同作者坐标、独立色条；通过 |
| Fig03 | 候选分数是否随供体共同变化 | Within-factor/celltype z；区间不适用，详见 Fig05 | Donor × cell type | 实际合格组合、空白不补零；通过 |
| Fig04 | 评分先验有哪些有符号 target | Curated signed prior；节点描述性 logCPM change | Prior edge / donor expression summary | 二部结构与两种线型；网络不是 de novo；通过 |
| Fig05 | disease 关联效应有多大 | Assay-adjusted coefficient、HC3 95% CI、BH q | Donor | 全部显示 effect 与 CI；供体不确定性与 assay 不平衡在图注明确；通过 |
| Fig09 | 细胞类型均值活动有何差别 | 均值和 within-factor z；描述图，无 RSS | Cell-type aggregate | 点大小为细胞数；无显著性；通过 |
| Fig12 | 两评分器的关联排序是否一致 | Nominal P-value rank、描述性 Spearman rho | Shared regulators，非生物学重复 | 3 个候选用形状/独立图例，无标签与点云碰撞；通过 |
| Fig13 | 信号通路足迹如何随供体变化 | Within-pathway/celltype z；描述图 | Donor × cell type | 标为 PROGENy pathway，非 TF；通过 |
| Fig13b | 通路是否与疾病状态关联 | Same assay-adjusted model、HC3 95% CI、BH q | Donor | 14 pathways 全部显示，模型限制同 Fig05；通过 |
| Fig14 | 原始 VIPER 的实际活动模式如何 | Original VIPER NES，within-factor/celltype z；描述图 | Donor × cell type | 与 ULM 相同候选与行序；未冒称 ARACNe/msVIPER；通过 |
| Fig15 | 先验 target 是否重叠 Hallmark | Hypergeometric overlap、BH q、真实 overlap 数 | Gene set / matched prior target | 全部 TF × 显示 gene set 对保留；非疾病通路激活；通过 |
| Fig16 | 供体中的自身表达与 target 足迹是否一致 | 真实 paired variables，无拟合或因果显著性 | Donor × cell type | Condition 用颜色与形状双编码；通过 |
| Composite a–b | 细胞背景和主要候选活动 | Same unsampled author embedding | Cell | 色条短于面板高度，文字未碰撞；通过 |
| Composite c–d | 模型效应与供体模式 | 8 fibroblast factors，HC3 CI + descriptive donor heatmap | Donor | 短字幕、8 行标签清晰；通过 |
| Composite e–f | 先验结构与算法排序 | 10 prior targets + all 516 shared regulator ranks | Prior / regulator | 筛选规则显式、候选形状图例完整；通过 |
| Composite g–h | 通路足迹与 target 功能重叠 | 5真实 pathway模型效应 + 3实际 Hallmark overlap | Donor / gene set | 推断通路和静态 prior 重叠分开命名；通过 |

## 显示子集与来源完整性 / Display subsets

分析先按研究来源、疾病标签、指定三种 cell types、基因过滤及 donor × celltype 最低 50 细胞筛选。本绘图脚本保留分析输出中的全部 38,971 个细胞，不改变数据原文件。单独 TF 热图显示每类 12 个结果排序因子，森林图显示每类 10 个；完整 516 个因子结果仍在输入表中。先验网络显示 3 个结果驱动的因子及按绝对 target 表达变化排序的最多 28 个 targets。

综合图为保持最终物理字号可读，显示 8 个成纤维细胞因子、10 个网络 targets、5 个 PROGENy 路径和 3 个 Hallmark sets；这些是同一真实数据的展示子集，不是新的统计筛选结论。单独图保留更完整的展示。完整选中列表和 before/after 行数写入 provenance。

未执行的 hdWGCNA 模块、enhancer/motif 图和扰动面板保持待实现。共调控因子不笼统视为序列特异 TF；数据库默认激活符号不当作实验证明；方法共享先验的一致性不称为独立验证。
