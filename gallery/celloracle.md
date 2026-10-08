# celloracle Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## celloracle-01 · Cell-type GRN network

- 科学用途 / Purpose：展示状态条件下拟合的 TF–target 权重
- 所需数据 / Input：base GRN；cell type links；filtered regression coefficients
- 生成方式 / Generation：CellOracle link 输出后原生/定制网络
- 代码入口 / Entry：[官方文档或源码](https://morris-lab.github.io/CellOracle.documentation/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：系数符号属于模型估计的局部影响
- 场景 / Scenario：base GRN 条件满足的单细胞建模
- 局限与误用 / Limits：RNA-only prior 与匹配 ATAC 证据应分别标明
- 状态 / Status：`planned`

## celloracle-02 · TF perturbation vector field

- 科学用途 / Purpose：展示真实完成的 in silico TF perturbation 预测
- 所需数据 / Input：实际 simulation displacement；embedding；grid field
- 生成方式 / Generation：官方 simulation/vector-field 绘图
- 代码入口 / Entry：[官方文档或源码](https://morris-lab.github.io/CellOracle.documentation/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：箭头表示预测状态变化方向和相对幅度
- 场景 / Scenario：完成 GRN、simulation、projection 的模型
- 局限与误用 / Limits：预测不是实验 knockout；UMAP field 不是细胞轨迹实测
- 状态 / Status：`planned`

## celloracle-03 · Perturbation score landscape

- 科学用途 / Purpose：量化预测扰动与状态梯度的对齐
- 所需数据 / Input：perturbation scores；reference differentiation gradient
- 生成方式 / Generation：原生 perturbation score 图
- 代码入口 / Entry：[官方文档或源码](https://morris-lab.github.io/CellOracle.documentation/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：分数表达与指定参考梯度一致程度
- 场景 / Scenario：梯度定义可信的状态转换问题
- 局限与误用 / Limits：横断面炎症数据未必存在可靠 differentiation gradient
- 状态 / Status：`planned`

## celloracle-04 · Network cartography/hub ranking

- 科学用途 / Purpose：筛查拓扑位置特殊的 regulator
- 所需数据 / Input：真实 filtered links；degree/betweenness；parameters
- 生成方式 / Generation：官方 network analysis 后定制 ranking
- 代码入口 / Entry：[官方文档或源码](https://morris-lab.github.io/CellOracle.documentation/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：高中心性反映当前阈值的图拓扑
- 场景 / Scenario：GRN 已跑通后的候选优先级
- 局限与误用 / Limits：中心性容易受边阈值影响；不证明 essential regulator
- 状态 / Status：`planned`
