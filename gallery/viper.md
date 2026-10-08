# viper Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## viper-01 · Protein activity heatmap

- 科学用途 / Purpose：比较样本或细胞状态的推断蛋白活性
- 所需数据 / Input：VIPER NES/activity matrix；样本注释；已知 regulon
- 生成方式 / Generation：viper 输出矩阵后定制热图
- 代码入口 / Entry：[R 入口](../scripts/plot_atlas.R)；源结果、筛选和版本见 [provenance](../results/figures/figure_provenance.json)
- 示例 / Example：![Protein activity heatmap](../results/figures/Fig14_original_viper_activity.png)；[图注与真实结果说明](real_figures.md)
- 解读 / Interpretation：NES 反映靶基因表达与 regulon 权重方向的一致性
- 场景 / Scenario：预构建 regulon 或符合条件的 ARACNe 网络
- 局限与误用 / Limits：TF 活性不是 TF 蛋白量；跨方法绝对 NES 不直接可比
- 状态 / Status：`implemented`

## viper-02 · Master-regulator enrichment plot

- 科学用途 / Purpose：展示候选主调控因子的目标在差异签名中的分布
- 所需数据 / Input：msVIPER 结果；完整排序签名；正负 regulon
- 生成方式 / Generation：msVIPER 对象的官方绘图方法；按当前帮助确认参数
- 代码入口 / Entry：[官方文档或源码](https://bioconductor.org/packages/release/bioc/html/viper.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：目标富集支持签名与调控因子网络的一致性
- 场景 / Scenario：具有合理差异表达签名与网络的 master-regulator analysis
- 局限与误用 / Limits：单 TF viper 打分不等于已完成 msVIPER/MRA；受网络来源影响
- 状态 / Status：`planned`

## viper-03 · Differential activity forest plot

- 科学用途 / Purpose：报告疾病组相对健康组的效应与区间
- 所需数据 / Input：donor-level activity；对比；CI；BH q
- 生成方式 / Generation：同一层级统计后定制森林图
- 代码入口 / Entry：[官方文档或源码](https://bioconductor.org/packages/release/bioc/html/viper.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：方向表示目标 regulon 推断活性差异；区间表示 donor 不确定性
- 场景 / Scenario：独立生物学重复充分的组间比较
- 局限与误用 / Limits：每个细胞不能作为独立样本；NES 差异不是因果
- 状态 / Status：`planned`

## viper-04 · TF expression–activity concordance

- 科学用途 / Purpose：识别表达量与活性不一致的 TF
- 所需数据 / Input：Matched donor TF expression and ULM activity; original VIPER activity in separate Fig14
- 生成方式 / Generation：R donor expression/activity scatter; the delivered scatter uses ULM, not VIPER
- 代码入口 / Entry：[官方文档或源码](https://bioconductor.org/packages/release/bioc/html/viper.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；ULM 对照真实示例见 Fig16，VIPER 同 TF 对照尚未绘制
- 解读 / Interpretation：离对角线的 TF 可能受转录后调控或网络覆盖影响
- 场景 / Scenario：同输入的 CollecTRI/VIPER 比较与机制候选筛查
- 局限与误用 / Limits：不同量纲不能直接相减；不一致不证明转录后机制
- 状态 / Status：`planned`

## viper-05 · Regulon/synergy network

- 科学用途 / Purpose：展示候选 regulator 的靶基因与组合关系
- 所需数据 / Input：原始 regulon；有来源的 sign/likelihood；正式 synergy 结果
- 生成方式 / Generation：定制有符号网络；synergy 只有真实运行后显示
- 代码入口 / Entry：[官方文档或源码](https://bioconductor.org/packages/release/bioc/html/viper.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：边符号来自 regulon；组合富集单独标明
- 场景 / Scenario：候选 master regulator 展示
- 局限与误用 / Limits：不得把共享目标误标为已验证 synergy
- 状态 / Status：`planned`
