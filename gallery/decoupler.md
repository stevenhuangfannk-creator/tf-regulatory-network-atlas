# decoupler Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## decoupler-01 · TF activity embedding

- 科学用途 / Purpose：在相同细胞坐标比较 TF 表达与活性
- 所需数据 / Input：真实 UMAP；cell annotations；ULM/activity matrix；TF expression
- 生成方式 / Generation：活动矩阵对齐细胞 ID 后由 scripts/plot_atlas.R 定制
- 代码入口 / Entry：[R 入口](../scripts/plot_atlas.R)；源结果、筛选和版本见 [provenance](../results/figures/figure_provenance.json)
- 示例 / Example：![TF activity embedding](../results/figures/Fig02_tf_activity_umap.png)；[图注与真实结果说明](real_figures.md)
- 解读 / Interpretation：局部颜色反映对应 regulon 在表达矩阵中的推断活性
- 场景 / Scenario：有可靠注释的单细胞描述性展示
- 局限与误用 / Limits：投影距离与活性颜色不是谱系或因果关系
- 状态 / Status：`implemented`

## decoupler-02 · Donor activity heatmap

- 科学用途 / Purpose：比较供体×细胞类型的 TF 活性模式
- 所需数据 / Input：donor×cell type 活性；疾病标签；实际 donor n
- 生成方式 / Generation：scripts/plot_atlas.R；row-z 标准化只用于展示
- 代码入口 / Entry：[R 入口](../scripts/plot_atlas.R)；源结果、筛选和版本见 [provenance](../results/figures/figure_provenance.json)
- 示例 / Example：![Donor activity heatmap](../results/figures/Fig03_donor_activity_heatmap.png)；[图注与真实结果说明](real_figures.md)
- 解读 / Interpretation：各 TF 行内的相对差异；不能将颜色跨行当绝对量
- 场景 / Scenario：具有供体信息的真实数据
- 局限与误用 / Limits：均值会掩盖供体异质性；每组 donor 数应另报告
- 状态 / Status：`implemented`

## decoupler-03 · Differential activity ranking

- 科学用途 / Purpose：寻找炎症相关候选 TF 并报告不确定性
- 所需数据 / Input：donor effect；CI；p；q；测试与纳入规则
- 生成方式 / Generation：scripts/plot_atlas.R；效应与置信区间
- 代码入口 / Entry：[R 入口](../scripts/plot_atlas.R)；源结果、筛选和版本见 [provenance](../results/figures/figure_provenance.json)
- 示例 / Example：![Differential activity ranking](../results/figures/Fig05_differential_tf_activity.png)；[图注与真实结果说明](real_figures.md)
- 解读 / Interpretation：正/负效应对应疾病方向；显著性按 BH q
- 场景 / Scenario：独立重复充分且批次可解释的比较
- 局限与误用 / Limits：没有 donor/混杂组只能描述，不作正式差异检验
- 状态 / Status：`implemented`

## decoupler-04 · Method rank concordance

- 科学用途 / Purpose：比较相同表达输入的推断方法
- 所需数据 / Input：相同 TF universe 的 ULM/VIPER/其他真实运行分数
- 生成方式 / Generation：scripts/plot_atlas.R；配对排名与 Spearman
- 代码入口 / Entry：[R 入口](../scripts/plot_atlas.R)；源结果、筛选和版本见 [provenance](../results/figures/figure_provenance.json)
- 示例 / Example：![Method rank concordance](../results/figures/Fig12_method_concordance.png)；[图注与真实结果说明](real_figures.md)
- 解读 / Interpretation：高一致性支持算法层面稳定；共享先验不是独立验证
- 场景 / Scenario：统一输入、gene universe 和 target threshold
- 局限与误用 / Limits：不同资源与不同数据不能混称算法验证
- 状态 / Status：`implemented`

## decoupler-05 · Network coverage QC

- 科学用途 / Purpose：报告 regulon target 覆盖与实际可评分的 TF
- 所需数据 / Input：prior target counts；observed target counts；min_n threshold
- 生成方式 / Generation：定制 size–coverage 图与 exclusion 统计
- 代码入口 / Entry：[官方文档或源码](https://decoupler.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：有效 targets 应达到预设阈值
- 场景 / Scenario：每次迁移新数据前
- 局限与误用 / Limits：覆盖率不能代替 prior 证据质量
- 状态 / Status：`planned`
