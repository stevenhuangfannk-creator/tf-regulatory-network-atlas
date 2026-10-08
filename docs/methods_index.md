# 方法索引 / Method atlas

本注册表涵盖21种方法/资源。资源、算法和软件实现分别命名：CollecTRI/DoRothEA是TF regulon先验，PROGENy是pathway footprint，OmniPath是知识资源，hdWGCNA基础网络是co-expression；NicheNet排序配体，不能与TF activity混同。

审计日期：2026-10-08。**`source_audited`不等于运行完成**。这次源码/论文审计没有安装或运行工具。仓库实际数据分析状态统一由 [Validation Report](../reports/Validation_Report.md) 与运行记录维护，避免方法卡的文献核查状态冒充执行状态。

| 方法/资源 | 定位 | 已观测版本/发布 | 核查许可证 | 方法卡 |
|---|---|---|---|---|
| ARACNe-AP | GRN inference | 无GitHub release记录 | Columbia software evaluation; non-commercial academic/educational restrictions | [卡片](../methods/aracne-ap.md) |
| VIPER | TF activity | 1.46.0 | Columbia software evaluation; non-commercial academic/educational restrictions | [卡片](../methods/viper-msviper.md) |
| CollecTRI | TF activity prior | biorxiv | Repository GPL-3.0; constituent data resource licenses vary | [卡片](../methods/collectri.md) |
| decoupler | TF activity; pathway activity | v2.2.0 | BSD-3-Clause | [卡片](../methods/decoupler.md) |
| DoRothEA | TF activity prior | v1.0.0 | GPL-3.0 code; constituent regulon data restrictions vary | [卡片](../methods/dorothea.md) |
| PROGENy | pathway activity | 无GitHub release记录 | Apache-2.0 | [卡片](../methods/progeny.md) |
| pySCENIC | GRN inference; TF activity | 0.12.1 | GPL-3.0 | [卡片](../methods/pyscenic.md) |
| hdWGCNA | co-expression | v0.4.12 | GNU GPLv3 in DESCRIPTION; LICENSE file is copyright stub | [卡片](../methods/hdwgcna.md) |
| CellOracle | GRN inference; perturbation | v0.10.12 | Modified Apache-2.0; NON-COMMERCIAL ACADEMIC ONLY | [卡片](../methods/celloracle.md) |
| SCENIC+ | multiomics; GRN inference; perturbation | v1.0a2 | Academic Non-commercial Software License Agreement | [卡片](../methods/scenicplus.md) |
| Pando | multiomics; GRN inference | 无GitHub release记录 | MIT | [卡片](../methods/pando.md) |
| GRaNIE | multiomics; GRN inference | 1.16.0 | Artistic-2.0 | [卡片](../methods/granie.md) |
| LINGER | multiomics; GRN inference; TF activity; perturbation | v1.0.0 | README claims MIT; standard license text not found | [卡片](../methods/linger.md) |
| scPRINT | GRN inference; foundation model | 2.3.8 | CONFLICT: GPL-3.0 LICENSE vs MIT pyproject metadata | [卡片](../methods/scprint.md) |
| Inferelator | GRN inference; TF activity | v0.6.4 | BSD-2-Clause | [卡片](../methods/inferelator.md) |
| RegEnrich | GRN inference; regulator ranking; co-expression | 1.22.1 | GPL (>=2) | [卡片](../methods/regenrich.md) |
| NicheNet | upstream signaling | v2.2.0 | GPL-3 in DESCRIPTION; license file not found in inspected paths | [卡片](../methods/nichenet.md) |
| OmniPath | upstream signaling prior | v1.0.10 | MIT client; resource data licenses vary | [卡片](../methods/omnipath.md) |
| RENGE | GRN inference; perturbation | v0.0.3 | MIT | [卡片](../methods/renge.md) |
| SwitchTFI | regulator ranking; differentiation | v0.1.0 | GPL-3.0 | [卡片](../methods/switchtfi.md) |
| KEGNI | GRN inference; knowledge graph | 无GitHub release记录 | MIT | [卡片](../methods/kegni.md) |

## 当前优先顺序 / Practical order

先在真实RNA数据上运行CollecTRI + decoupler并按donor检验；有充分独立样本和合适先验才考虑VIPER/msVIPER或ARACNe重建。pySCENIC需要正确motif数据库；hdWGCNA需要适合相关网络的样本结构和足够细胞，不用metacells伪造重复。SCENIC+、Pando、GRaNIE、LINGER需要相应chromatin/multiome输入；RENGE需要time-series CRISPR，不能对RNA横断面硬跑。CellOracle和scPRINT以模型、先验、环境和独立验证作为扩展前提。

近期补充筛选采用滚动2023-10-08至2026-10-08：RENGE（2023-12）、SwitchTFI（2025）、KEGNI（2025），均有peer-reviewed paper和论文链接公开实现；只完成来源审计，未将上游benchmark作为本牙周案例验证。

## 可机器读取证据 / Machine-readable evidence

- [方法表 CSV](methods_registry.csv)：类别、输入/输出、paper DOI、许可证核查级别、精确release/push日期和执行语义。
- [方法表 JSON](methods_registry.json)：适于后续自动检索和状态更新。
- [来源证据 JSON](methods_source_evidence.json)：HTTP状态、官方URL、原始字段及license文本短摘/hash。
- [论文元数据](literature_registry.json) 与 [检索日志](literature_search_log.md)。

GitHub`/releases/latest`返回404表示未观察到GitHub release，不能推断没有版本、没有维护或不可运行。`pushed_at`不是最后代码commit时间。本注册表未宣称所有源码能够在Windows安装；多组学/旧Python依赖采用隔离Linux/WSL2环境。

## 需要保留的元数据差异 / Audited discrepancies

- Python仓库`saezlab/decoupler-py`现指向`scverse/decoupler`；`saezlab/decoupler`会指向R `decoupleR`，不能混淆API和许可证。
- hdWGCNA正确论文DOI为`10.1016/j.crmeth.2023.100498`；`10.1016/j.xgen.2023.100263`是另一篇Cell Genomics论文。hdWGCNA当前DESCRIPTION写GNU GPLv3，LICENSE只留copyright stub，所以记录该差异。
- scPRINT原始方法已有Nature Communications 2025 paper；scPRINT-2另有后续模型。scPRINT 2.3.8的LICENSE是GPL-3.0，pyproject却写MIT：许可证字段冲突保持未解决。
- LINGER README称MIT，但检查的标准license路径未发现许可证全文：仅README claim，不能当作已核实完整授权。
- LINGER DOI带2024、early online 2024，与indexed issue year 2025不同；NicheNet/PROGENy亦有online与issue年份区别，表中保留首次发表日期而不从DOI后缀猜年份。
- CollecTRI/DoRothEA/OmniPath的代码许可证不自动覆盖全部来源网络条款。

## 本项目执行状态 / Project execution

CollecTRI已用于真实牙周数据，decoupler 2.1.2完成ULM和Python dc.mt.viper；PROGENy完成14条通路的ULM活性与供体对照。最新release标签和实际执行版本分开记录。详见[run manifest](../reports/run_manifest.json)、[pathway manifest](../reports/pathway_manifest.json)和[Validation Report](../reports/Validation_Report.md)。原始Bioconductor VIPER 1.36.0也已在同一真实pseudobulk/先验运行并比较；msVIPER、ARACNe、DoRothEA及其它高级方法未运行。

## 扩展与覆盖 / Extension and coverage

后续进入条件及独立bulk备选见[Extension roadmap](EXTENSION_ROADMAP.md)；命令与原始来源核对见[Command audit](methods_commands_audit.md)。[Gallery coverage](methods_gallery_coverage.json)核对21种方法/资源全部具有图形输出契约，共78项；新增RENGE、SwitchTFI、KEGNI各3项均保持planned。
