# 图形参考目录 / Figure references

用途：学习布局、信息层级、颜色/形状语法和证据表达。下表是可核查论文或官方教程链接，不复制原图，不借用论文结果。项目Gallery的科学示例只有在本项目真实执行后才标记生成。

| 论文/教程 | 期刊、年份 | 参考入口 | 可以学习的图形结构 | 本项目适用与限制 |
|---|---|---|---|---|
| SCENIC | Nature Methods, 2017 | [原文](https://doi.org/10.1038/nmeth.4463) / [Fig1](https://www.nature.com/articles/nmeth.4463#Fig1) | workflow→regulon activity→细胞状态的证据顺序；结构/活性分开编码 | 学习Fig01/03/09；AUCell不能等同ULM尺度 |
| SCENIC+ | Nature Methods, 2023 | [原文](https://doi.org/10.1038/s41592-023-01938-4) / [Fig1](https://www.nature.com/articles/s41592-023-01938-4#Fig1) | TF–enhancer–gene三层框架、数据模态和network evidence | Fig11只有chromatin/motif输入与真实推断时制作 |
| CellOracle | Nature, 2023 | [原文](https://doi.org/10.1038/s41586-022-05688-9) / [Fig1](https://www.nature.com/articles/s41586-022-05688-9#Fig1) | GRN拟合与扰动预测分步；低维图上向量场和对应对照 | Fig10须真正完成模拟；不要将箭头当成谱系追踪 |
| Functional characterization of somatic mutations… (VIPER) | Nature Genetics, 2016 | [原文](https://doi.org/10.1038/ng.3593) | protein-activity signature与regulon富集/效应排名 | 区分TF表达、推断activity与master-regulator检验 |
| CollecTRI | Nucleic Acids Research, 2023 | [原文](https://doi.org/10.1093/nar/gkad841) / [官方figure scripts](https://github.com/saezlab/CollecTRI/blob/main/scripts/figures/figures_manuscript.R) | 先验覆盖→perturbation benchmark→TF候选排序，多方法比较 | 没有knockTF ground truth，不转用原文benchmark当本案例证据 |
| hdWGCNA | Cell Reports Methods, 2023 | [原文](https://doi.org/10.1016/j.crmeth.2023.100498) / [全文](https://europepmc.org/articles/PMC10326379) / [官方basic教程](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html) | 模块dendrogram、eigengene feature map、hub ranking及trait/preservation | Fig06/07必须有真实模块；基础网络无向 |
| LINGER | Nature Biotechnology, early online 2024 / indexed 2025 | [原文](https://doi.org/10.1038/s41587-024-02182-7) | 多组学输入、external prior与cis/trans层级；分模态benchmark | 需要RNA+ATAC和外部参数；strength不自动带sign |
| scPRINT | Nature Communications, 2025 | [原文](https://doi.org/10.1038/s41467-025-58699-1) / [全文](https://europepmc.org/articles/PMC12003772) | 原文Fig2/3分离generic prior与orthogonal cell-type ground truth；Fig5/6连接atlas与sparse disease network | 论文caption已读取；借鉴多面板结构，不能拷贝其边/分数 |
| PROGENy | Nature Communications, 2018 | [原文](https://doi.org/10.1038/s41467-017-02391-6) | footprint activity及perturbation-response表达 | pathway score单独命名，勿标为TF regulon |
| SwitchTFI | Genome Biology, 2025 | [原文](https://doi.org/10.1186/s13059-025-03876-0) / [官方example](https://github.com/bionetslab/SwitchTFI/blob/main/docs/example.ipynb) | state/transition-specific GRN过滤与TF ranking | 需要真实state定义；疾病组不自动是分化状态 |
| KEGNI | Genome Biology, 2025 | [原文](https://doi.org/10.1186/s13059-025-03780-7) / [实现](https://github.com/Lipxiao/KEGNI) | knowledge graph输入与GRN结果/benchmark的分层结构 | prior heldout和independent validation避免数据泄漏 |
| RENGE | Communications Biology, 2023-12 | [原文](https://doi.org/10.1038/s42003-023-05594-4) / [全文Fig5](https://europepmc.org/articles/PMC10754834#Fig5) | 原文Fig5颜色区分positive/negative，边宽编码coefficient，过滤阈值显式说明 | 仅在time-series CRISPR真实分析后应用；本RNA案例不生成 |

Nature论文的Fig1链接是publisher figure导航入口，论文DOI/题名/期刊已核对；当前publisher图像未复制。Europe PMC scPRINT/RENGE图注已读取，其它具体panel无需猜测。另见[文献元数据](literature_registry.json)与[来源日志](literature_search_log.md)。

统一设计原则：paired expression/activity保持同一坐标和对应色条；供体点与组效应/区间同时展示；网络仅筛选有数据依据的节点/边，保留positive/negative/MI/unknown类型；热图明确行缩放与列聚合；显著性来自正式donor-level结果，模型p值不得换名为疾病p值。Chord等复杂图只在关系数量可控且确有输入表时使用。
