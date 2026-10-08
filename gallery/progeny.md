# progeny Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## progeny-01 · Pathway activity heatmap

- 科学用途 / Purpose：估计信号通路表达足迹
- 所需数据 / Input：PROGENy weights；输入表达；实际 pathway scores
- 生成方式 / Generation：PROGENy/decoupler 评分后定制热图
- 代码入口 / Entry：[R 入口](../scripts/plot_atlas.R)；源结果、筛选和版本见 [provenance](../results/figures/figure_provenance.json)
- 示例 / Example：![Pathway activity heatmap](../results/figures/Fig13_progeny_donor_pathways.png)；[图注与真实结果说明](real_figures.md)
- 解读 / Interpretation：颜色表示通路推断活性，不是 TF activity
- 场景 / Scenario：RNA-only 炎症信号描述或 donor 比较
- 局限与误用 / Limits：不能作为激酶活性/磷酸化的直接测量
- 状态 / Status：`implemented`

## progeny-02 · Differential pathway activity

- 科学用途 / Purpose：展示 donor-level 通路变化
- 所需数据 / Input：真实 donor pathway scores；CI；p/q
- 生成方式 / Generation：同 donor-level 统计后定制森林图
- 代码入口 / Entry：[R 入口](../scripts/plot_atlas.R)；源结果、筛选和版本见 [provenance](../results/figures/figure_provenance.json)
- 示例 / Example：![Differential pathway activity](../results/figures/Fig13b_progeny_disease_effects.png)；[图注与真实结果说明](real_figures.md)
- 解读 / Interpretation：推断通路响应与疾病状态相关
- 场景 / Scenario：有供体重复的疾病对比
- 局限与误用 / Limits：通路之间依赖；需要多重检验处理
- 状态 / Status：`implemented`

## progeny-03 · Pathway–TF association

- 科学用途 / Purpose：提出 TF 与信号足迹的关联候选
- 所需数据 / Input：匹配 donor pathway/TF scores；相关/先验来源
- 生成方式 / Generation：真实关联边的三层图或矩阵
- 代码入口 / Entry：[官方文档或源码](https://saezlab.github.io/progeny/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：关联提示共同程序，先验路径单独标注
- 场景 / Scenario：候选机制整合
- 局限与误用 / Limits：相关方向不能确定上游驱动；PROGENy 不自动推断有向通路
- 状态 / Status：`planned`
