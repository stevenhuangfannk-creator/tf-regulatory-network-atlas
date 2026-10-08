# Figure Gallery / 长期图件目录

本目录记录每种方法理论上或软件实际支持的主要图件。`catalog.csv` 是可检索的逐图契约；方法页解释用途、输入、生成方式、入口、示例、解读、场景和边界。软件支持不等于本仓库已执行。

实际输出见 [本次真实图件](real_figures.md)，布局参考见 [科学图形参考](references.md)。每张结果图的输入表、筛选规则和参数记录于 `results/figures/figure_provenance.json`。

| 方法 / Method | 主要定位 / Role | 目录 |
|---|---|---|
| aracne-ap | GRN inference (mutual information) | [aracne-ap](aracne-ap.md) |
| viper | TF/protein activity, master regulators | [viper](viper.md) |
| decoupler | Activity scoring framework | [decoupler](decoupler.md) |
| collectri | Signed TF prior resource | [collectri](collectri.md) |
| dorothea | Confidence-ranked TF prior resource | [dorothea](dorothea.md) |
| progeny | Pathway activity | [progeny](progeny.md) |
| pyscenic | Coexpression + motif + regulon activity | [pyscenic](pyscenic.md) |
| hdwgcna | Undirected coexpression modules | [hdwgcna](hdwgcna.md) |
| celloracle | GRN modeling + in silico perturbation | [celloracle](celloracle.md) |
| scenicplus | Enhancer-driven multiomics GRN | [scenicplus](scenicplus.md) |
| pando | Multiomics GRN regression | [pando](pando.md) |
| granie | Enhancer-mediated multiomics GRN | [granie](granie.md) |
| linger | Model-based multiomics GRN | [linger](linger.md) |
| scprint | Foundation model / GRN candidates | [scprint](scprint.md) |
| inferelator | Regression/multitask GRN | [inferelator](inferelator.md) |
| regenrich | Differential regulator enrichment | [regenrich](regenrich.md) |
| nichenet | Ligand-to-target upstream signaling | [nichenet](nichenet.md) |
| omnipath | Signed signaling knowledge resource | [omnipath](omnipath.md) |
| renge | Time-series CRISPR GRN / perturbation | [renge](renge.md) |
| switchtfi | Transition-specific GRN / regulator ranking | [switchtfi](switchtfi.md) |
| kegni | Knowledge-graph-enhanced GRN | [kegni](kegni.md) |

## 按图形类别检索 / Browse by category

| 类别 | 逐图 ID |
|---|---|
| activity | [viper-01](viper.md), [decoupler-02](decoupler.md), [collectri-02](collectri.md), [dorothea-02](dorothea.md), [pyscenic-03](pyscenic.md), [pyscenic-05](pyscenic.md), [linger-02](linger.md), [switchtfi-03](switchtfi.md) |
| association | [hdwgcna-04](hdwgcna.md) |
| coexpression | [hdwgcna-02](hdwgcna.md), [hdwgcna-03](hdwgcna.md), [hdwgcna-05](hdwgcna.md) |
| comparison | [viper-04](viper.md), [decoupler-04](decoupler.md), [dorothea-03](dorothea.md), [kegni-03](kegni.md) |
| differential | [viper-03](viper.md), [decoupler-03](decoupler.md), [progeny-02](progeny.md), [regenrich-01](regenrich.md), [switchtfi-02](switchtfi.md) |
| embedding | [decoupler-01](decoupler.md) |
| enrichment | [viper-02](viper.md) |
| genomic-tracks | [scenicplus-04](scenicplus.md), [pando-03](pando.md) |
| model | [scprint-01](scprint.md), [scprint-04](scprint.md) |
| motif | [pyscenic-02](pyscenic.md) |
| multiomics | [scenicplus-01](scenicplus.md), [scenicplus-02](scenicplus.md), [pando-01](pando.md), [pando-02](pando.md), [granie-01](granie.md), [linger-01](linger.md) |
| network | [aracne-ap-01](aracne-ap.md), [viper-05](viper.md), [collectri-01](collectri.md), [progeny-03](progeny.md), [pyscenic-01](pyscenic.md), [pyscenic-06](pyscenic.md), [celloracle-01](celloracle.md), [celloracle-04](celloracle.md), [scprint-02](scprint.md), [inferelator-01](inferelator.md), [regenrich-02](regenrich.md), [switchtfi-01](switchtfi.md), [kegni-01](kegni.md) |
| pathway | [progeny-01](progeny.md) |
| perturbation | [celloracle-02](celloracle.md), [celloracle-03](celloracle.md), [renge-01](renge.md), [renge-02](renge.md) |
| quality-control | [aracne-ap-03](aracne-ap.md), [decoupler-05](decoupler.md), [dorothea-01](dorothea.md), [hdwgcna-01](hdwgcna.md), [granie-02](granie.md), [omnipath-02](omnipath.md), [renge-03](renge.md) |
| robustness | [aracne-ap-02](aracne-ap.md), [aracne-ap-04](aracne-ap.md), [collectri-03](collectri.md), [inferelator-02](inferelator.md), [regenrich-03](regenrich.md) |
| specificity | [pyscenic-04](pyscenic.md), [scenicplus-03](scenicplus.md) |
| upstream-signaling | [nichenet-01](nichenet.md), [nichenet-02](nichenet.md), [nichenet-03](nichenet.md), [nichenet-04](nichenet.md), [omnipath-01](omnipath.md), [omnipath-03](omnipath.md) |
| validation | [hdwgcna-06](hdwgcna.md), [granie-03](granie.md), [linger-03](linger.md), [scprint-03](scprint.md), [inferelator-03](inferelator.md), [kegni-02](kegni.md) |

## 更新规范 / Adding an executed figure

仅在输入来自实际分析、绘图命令成功、图件人工检查通过后，将该行状态改为 `implemented` 并添加真实示例链接。需保留完整输入结果表、方法版本、先验来源、筛选参数和统计单位。若方法只输出表格，明确写“custom plot from verified output”，不要声称软件原生支持该图。

没有独立供体信息时，正式组间统计图保持待实现。没有真实 motif/ATAC 证据时，不绘制 enhancer 网络；没有已执行模拟时，不绘制 perturbation landscape。普通相关网络只标记为 descriptive coexpression。

当前目录包含 78 个输出契约，覆盖 21 种方法/资源，其中 9 个长期契约已有对应的真实示例；本次共交付 13 套独立/综合图件。完整图注、中文解释和输入表见 [real_figures.md](real_figures.md)。Gallery 范围与 [21 项方法索引](../docs/methods_index.md) 对齐。
