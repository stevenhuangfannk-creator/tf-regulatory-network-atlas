# 科学图形参考 / Figure reference index

以下为核实过出处的原始论文和官方教程，用作图形语法、布局和证据表达的参考。本项目的图件由本次真实结果重新绘制；未复制这些论文的原图、数值、网络或细胞轨迹。论文 DOI 与官方入口是索引，具体面板可通过原文检索；不把未逐面板提取的内容标为“已复现”。

| 方法与出处 / Source | 可学习的图形与证据层次 / What to inspect | 对本项目的适配 / Adaptation |
|---|---|---|
| Aibar et al., SCENIC, Nature Methods (2017), [10.1038/nmeth.4463](https://doi.org/10.1038/nmeth.4463) | Regulon activity、motif 证据与细胞类型结构的对应 | 同一细胞坐标展示活动；无 motif 数据时只展示已执行的 activity score |
| Van de Sande et al., SCENIC protocol, Nature Protocols (2020), [10.1038/s41596-020-0336-2](https://doi.org/10.1038/s41596-020-0336-2) | GRN → motif pruning → AUCell 的输入/输出流程 | 流程图明确区分 coexpression、motif 和 activity 三种证据；未执行步骤保持待实现 |
| Bravo González-Blas et al., SCENIC+, Nature Methods (2023), [10.1038/s41592-023-01938-4](https://doi.org/10.1038/s41592-023-01938-4) | TF–enhancer–gene 三层网络、gene/region activity | 网络按边证据分层；本次 RNA-only 案例不仿制 enhancer 面板 |
| Kamimoto et al., CellOracle, Nature (2023), [10.1038/s41586-022-05688-9](https://doi.org/10.1038/s41586-022-05688-9) | 扰动模型与预测向量场的分离 | 只在实际模型模拟成功后加入 perturbation gallery 示例 |
| Alvarez et al., VIPER, Nature Genetics (2016), [10.1038/ng.3593](https://doi.org/10.1038/ng.3593) | 蛋白调控活性、regulon 富集与主调控因子证据 | 把活性分数与 TF 自身表达分开；单 TF 打分不称为已完成 msVIPER |
| Schubert et al., PROGENy, Nature Communications (2018), [10.1038/s41467-017-02391-6](https://doi.org/10.1038/s41467-017-02391-6) | 通路表达足迹与直接通路成员表达的区分 | 通路图单独命名；不能用 PROGENy 活性替代 TF 活性 |
| LINGER, Nature Biotechnology (2024), [10.1038/s41587-024-02182-7](https://doi.org/10.1038/s41587-024-02182-7) | 多组学 prior、预测网络与验证指标的层级 | 模型 prior 和样本推断边分开记录；不具备权重/多组学输入时保持待实现 |
| scPRINT, Nature Communications (2025), [10.1038/s41467-025-58699-1](https://doi.org/10.1038/s41467-025-58699-1) | 模型表征、表达重建和 GRN 评估的独立面板 | 模型 attention 作为候选边证据；不将 attention 称为直接结合 |
| Morabito et al., hdWGCNA, Cell Reports Methods (2023), [10.1016/j.crmeth.2023.100498](https://doi.org/10.1016/j.crmeth.2023.100498) | Module eigengene、kME 和共表达拓扑 | 真实执行后才展示模块；当前不以普通相关图替代 hdWGCNA |

## 官方可运行图例 / Official plotting examples

| 教程 / Tutorial | 已核实的入口 / Verified entry | 注意事项 / Boundary |
|---|---|---|
| [hdWGCNA basic tutorial](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html) | `PlotSoftPowers`、`PlotDendrogram`、`PlotKMEs`、`ModuleFeaturePlot`、`ModuleRadarPlot`、`ModuleCorrelogram`；`DimPlotMetacells` 是 wrapper | `Sample` 与 `cell_type` 应参与 metacell 分组；metacells 不视为独立供体 |
| [pySCENIC documentation](https://pyscenic.readthedocs.io/) | `grn`、`ctx`、`aucell` 输出；结果矩阵可供定制图 | 必须记录 motif ranking 数据库、motif 注释与基因组版本 |
| [Bioconductor VIPER](https://bioconductor.org/packages/release/bioc/html/viper.html) | `viper` 活性矩阵；msVIPER 的富集可视化按安装版帮助运行 | 本项目实际使用原始 Bioconductor VIPER 1.36.0；当前未执行 msVIPER |
| [decoupler documentation](https://decoupler.readthedocs.io/) | ULM、VIPER 等方法的 score 与统计输出；本项目 R 图为 custom plotting | 先验来源一致性不是算法独立验证；按实际 API 版本记录参数 |

## 采用的图形原则 / Design rules used here

统一 Arial 字体、白底、克制的蓝/玫红连续色与带线型的有符号 prior 边；色彩不单独承担正负边含义。网络只保留结果驱动的候选 TF 和实际 prior targets，以清晰二部结构呈现。UMAP 使用原作者坐标、保留全部输入细胞并只栅格化密集点，文字仍为矢量。疾病效应用供体层面的模型系数与区间呈现；描述性细胞图不显示伪造的统计显著性。

英文标题、英文图注、中文解释以及输入表路径详见 [real_figures.md](real_figures.md)。当前输出采用期刊风格设计，正式投稿前仍需按目标期刊当时的文件规格核对。
