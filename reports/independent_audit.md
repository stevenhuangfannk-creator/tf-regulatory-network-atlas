# 独立计算与统计审计 / Independent computational and statistical audit

日期：2026-10-08。审计依据是实际代码、保存的表达/活性表、供体映射、图件脚本与 Validation Report；未仅根据流程说明判断。审计采用 nature-statistics 的统计单位、模型与图注核对原则。这里的“通过”表示数据与计算合同一致，不认证患者身份、机制或临床推广能力。

## 总体判断 / Overall assessment

**未发现阻止当前探索性案例交付的 P0 计算错误。** 主流程按供体编码 × 细胞类型汇总原始整数计数，正式疾病模型在每个细胞类型内拟合，不把 38,971 个细胞或 46 个跨类型 pseudobulk 当作 46 位独立患者。作者联合 UMAP、CollecTRI prior edges、PROGENy footprints 与 Hallmark prior overlap 都已分别标明证据层级，没有冒称 de novo ARACNe、hdWGCNA 模块、motif 或计算扰动。

模型的可估计性与数值正确性已核对；供体身份和 assay 不平衡仍限制疾病解释。FDR 数量不是独立机制数量，算法一致性不等于独立验证。

## 实际复核 / Verified calculations

| 检查 | 结果 | 证据 |
|---|---|---|
| 输入完整性 | 实际 H5AD / CollecTRI 完整 SHA 与固定 input manifest 一致 | [测试状态](test_status.json) |
| 细胞与统计单位 | 38,971 unique cells 映射到 46 个合格 donor × cell type；每个至少 50 cells；PD161/PD164 后缀未增加独立重复 | [数据合同测试](../tests/test_data_contracts.py)、[供体映射](../data/donor_map.csv) |
| 原始表达 | CSR 流式读取、counts 层合并 9 个重名 symbol；pseudobulk log2(CPM+1) 与单细胞 log1p(CP10K) 分开；中心化在 cell type 内进行 | [工作流](../workflows/periodontal_tf.py)、[数值测试](../tests/test_workflow.py) |
| ULM 分块 | `empty=False` 保留固定 gene background；明确的数值测试与独立 Pearson-regression t 统计量一致 | [数值测试](../tests/test_workflow.py) |
| 主模型 | 8 个图示候选 × 3 个 cell type，共 24 个模型独立重算，系数/CI 最大绝对误差 1.33e-15，P 值误差不超过 8.46e-17 | [逐模型复核](independent_coefficient_checks.csv) |
| 调控先验 | 输入没有重复 source-target 或 zero-weight edges；已保留有出处的正负 prior signs；图中没有转化为该队列重建边 | [网络边表](../results/tables/selected_network_edges.csv) |
| R / Python VIPER | 运行的是不同实现；R 使用相同表达与 signed prior、uniform target likelihood；比较脚本明确使用原始 Bioconductor 结果 | [原始 R 入口](../methods/viper/run_viper.R)、[比较代码](../workflows/validate_viper.py) |

## 重要限制与问题状态 / Findings and status

### P1：供体身份仍是保守映射 / Conservative donor identity — 已披露，仍待源材料确认

GEO 明确给出 PD161/PD161b 和 PD164/PD164b/PD164c 活检标题。把它们合并比按 GSM 数量计独立重复更保守，但 Table S1 的完整患者联系尚未取得。当前结果应始终写为 **13 healthy / 5 conservative disease donor codes**，不能升级为经过完整临床核实的 18 位患者，也不能用 8 个疾病文库作独立重复。这个未解决事项已在 DATA_AUDIT、donor_map 的 `verified=False` 及 Validation Report 中披露。

### P1：v2 疾病单点影响及 small-n / Singleton disease stratum and small samples — 已量化，属于设计限制

独立检查设计矩阵 `intercept + disease + assay_v3`，三个细胞类型均 full rank，未出现完全共线性。

| cell type | H / PD | residual df | max leverage | 单个 v2 PD134 对疾病系数的线性权重 |
|---|---:|---:|---:|---:|
| Endothelial | 13 / 5 | 15 | 0.40594（PD134） | 0.34653 |
| Fibroblast | 13 / 5 | 15 | 0.40594（PD134） | 0.34653 |
| Macrophage | 6 / 4 | 7 | 0.60526（GM283） | 0.52632 |

详见 [model_diagnostics.csv](model_diagnostics.csv)。这些权重来自固定设计下疾病系数对每个观测 score 的线性权重；它们不是某位患者解释的生物学方差比例。主模型对 assay 分层信息依赖很强，HC3 的有限样本修正不会补充不存在的临床重复。v3-only 成纤维/内皮仅 3 H / 4 PD；巨噬仅 1 H / 3 PD，代码正确留空正式 v3 P 值。

留一同号比例说明所列删除扰动中方向没有改变，不能证明系数幅度不受该点影响或解除临床混杂。bootstrap、LOO、v3 sensitivity 与 target subsampling 都是同一数据的计算稳健性检查。当前 ULM q<0.05 条目为内皮 44/516、成纤维 128/516、巨噬 0/516；这不能转述成发现了同样数量的独立致病轴。

### P1：bootstrap 与主 CI 是不同 estimand / Bootstrap versus model CI — 已在报告明确区分

`differential()` 的 `effect` 和 `ci_low/ci_high` 来自 assay-adjusted OLS；`bootstrap_low/high` 是条件内供体重新抽样的 **未调整均值差**区间。它们可以同时报告，但不能作为同一主效应的两套 CI 混用。当前森林图使用主模型 HC3 CI，Validation Report 已明确未调整 bootstrap 不替代它；本项计算无需重写。

### P1：支持性资源需要固定校验 / Supporting-resource reproducibility — 已修正并复核

主要 H5AD / CollecTRI 下载具有 fixed URL 与 expected SHA，支持核心分析复现。PROGENy 和 Hallmark cache 都被正确忽略；最初脚本只记录获取后的 SHA，没有在后续 clean-clone 重取后强制对照既有 pathway manifest。资源在线更新可能使支持图与首次结果不一致。

现有 [pathway_context.py](../workflows/pathway_context.py) 在使用两种资源前核对提交的 [pathway manifest](pathway_manifest.json) SHA；变化时明确失败，经过版本审查后才可更新期望值。最终本地 PROGENy/Hallmark cache 的 SHA 与 manifest 逐项一致，代码修正已复核。该问题不改变已保存结果的真实性；clean-clone 下载后仍需通过相同校验。

### P2：regulon 子抽样实际比例 / Actual target fraction — 结果元数据已修正并复核

代码使用 `max(min_targets, floor(0.8 × n_targets))`。例如 ETV3 有 11 个匹配 targets，实际保留 10/11=90.9%，不是 80%；恰好 10 个 targets 时会保留 100%，不存在 target removal。不能用固定 `target_fraction=0.8` 暗示每个 regulon 都经历同等扰动。

最终 [regulon_sensitivity.py](../workflows/regulon_sensitivity.py) 与 [summary table](../results/tables/regulon_target_stability.csv) 已保留 `requested_target_fraction=0.8`、`n_targets`、`n_retained` 和 `actual_target_fraction`；最低靶基因数由 [analysis config](../config/analysis.json) 固定为 10。实际结果为 480 个 iteration rows、24 个 summary rows，ETV3 的保留比例为 10/11。最终 Validation Report 也已把 80% 称为名义值；不应以子抽样同号率表述独立生物学稳定性。

### P2：matched coverage 与检测覆盖不同 / Matched versus detected targets — 已量化，无当前图示候选阻塞

当前 `regulon_coverage.csv` 的 present 是“target 在统一分析矩阵列中”，不是每个细胞类型都检测到该 target。逐细胞类型复核显示：有 4 个内皮、1 个成纤维、41 个巨噬 regulon 的至少一次非零检测 targets 少于 10；因此 matched-target 阈值不保证该细胞类型的 detection depth。详见 [celltype_target_detection.csv](celltype_target_detection.csv)。

这批低检测覆盖条目没有 ULM q<0.05；8 个当前图示候选在每个细胞类型都至少检测到 11 个 targets。当前主要候选没有因此失效，但后续迁移到稀疏细胞数据时应报告 cell-type detection coverage，避免把全局匹配覆盖写成细胞特异测量覆盖。

### P2：图注与字段精度 / Caption and metadata precision — 排名定义与字符问题已修正

Fig12 的 rank 实际按每个细胞类型的 nominal P 值排序；最终 [R plotting script](../scripts/plot_atlas.R) 与 [figure provenance](../results/figures/figure_provenance.json) 均明确写为 **nominal disease-association P-value ranks**，避免被理解为 signed effect-size rank。网络 target 颜色是未调整 donor 平均 logCPM 差，箭头是 prior sign；二者不能合成 assay-adjusted 调控证据。expression-activity 对照表已增加每个 cell type 内的 `donor_correlation_fdr` BH 校正；这些相关仍是同一供体数据的描述性关系，不是独立实验。v3 P 值为探索性敏感性检查，没有升级为新一套 BH 校正结论。

审计中发现的 Unicode replacement characters 已修复；最终仓库 Markdown 的 U+FFFD 扫描为 0，本报告全部本地链接均可解析。该文字问题不改变数值结果。

## 可接受的结论措辞 / Acceptable interpretation

“同研究人牙周样本的供体编码汇总表达，在 assay-adjusted 模型下呈现若干候选调控 footprint 差异。成纤维细胞的 GTF3A、ZNF148、TFE3、JUND 等和内皮 GLI2 可作为后续验证对象；CREBBP 与 NFKBIB 分别为共激活因子与抑制蛋白，应保留其不同定位。结果受到 small-n、assay 不平衡、患者关联未完全核实以及 shared prior 的限制。蛋白活性、直接靶基因调控和炎症因果作用均需要独立实验。”

## 审计边界 / Audit boundary

本轮不新增全套模型搜索，不为了降低 P 值更换分析方案，不重构根工作流。已完成的数值检查不是功效分析、形式化因果识别或投稿统计认证。后续优先确认患者关联、在独立且 assay 匹配的队列复核，再进行 CUT&Tag/ChIP、TF perturbation 与功能验证。当前未运行的高级方法仍保持未运行。

本地六项测试使用已下载的真实输入，全部通过；Git 中不包含的大型输入缺失时，CI 中两项 integration tests 明确 skip，其余数值/表格合同仍执行。最终审计未发现剩余的探索性交付阻塞项；以上固有推断限制仍有效。
