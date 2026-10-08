# aracne-ap Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## aracne-ap-01 · Mutual-information TF–target graph

- 科学用途 / Purpose：筛选与 TF 表达依赖的候选靶基因
- 所需数据 / Input：bootstrap 汇总 network.txt；TF 列表；MI 分数
- 生成方式 / Generation：ARACNe-AP 输出边表后，定制 igraph/ggraph 图；非原生因果图
- 代码入口 / Entry：[官方文档或源码](https://github.com/califano-lab/ARACNe-AP)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：边表示经 DPI 筛选的互信息依赖；箭头仅表示候选 TF–target 角色
- 场景 / Scenario：样本量足够、组织/细胞状态较一致的表达队列
- 局限与误用 / Limits：MI 不给激活/抑制符号；DPI 和方向设置不等于因果证明
- 状态 / Status：`planned`

## aracne-ap-02 · Bootstrap edge stability

- 科学用途 / Purpose：衡量边的重采样稳定性
- 所需数据 / Input：每个 bootstrap 的边列表；共同候选边 universe
- 生成方式 / Generation：汇总边出现比例后绘制分布/排序图
- 代码入口 / Entry：[官方文档或源码](https://github.com/califano-lab/ARACNe-AP)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：高出现比例表示同一数据内对重采样较稳定
- 场景 / Scenario：正式配置充分 bootstrap 的 de novo 网络
- 局限与误用 / Limits：稳定性不是外部验证；少样本不能用大量 bootstrap 补足
- 状态 / Status：`planned`

## aracne-ap-03 · Regulon size and gene coverage

- 科学用途 / Purpose：检查实际用于活性推断的靶基因覆盖
- 所需数据 / Input：网络 TF–target；输入基因；每 TF target counts
- 生成方式 / Generation：条形图与覆盖率散点图
- 代码入口 / Entry：[官方文档或源码](https://github.com/califano-lab/ARACNe-AP)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：网络较大而覆盖低的 TF 可能存在输入不匹配
- 场景 / Scenario：转交 VIPER 前的网络 QC
- 局限与误用 / Limits：目标数多不等于质量高；应保留排除规则
- 状态 / Status：`planned`

## aracne-ap-04 · DPI/threshold sensitivity map

- 科学用途 / Purpose：检查网络对 DPI 与 MI 阈值的依赖
- 所需数据 / Input：同数据不同参数网络；边重叠与统计
- 生成方式 / Generation：定制参数热图与 overlap 曲线
- 代码入口 / Entry：[官方文档或源码](https://github.com/califano-lab/ARACNe-AP)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：一致候选边可支持对设置的稳健性
- 场景 / Scenario：同一数据和统一运行预算下敏感性评估
- 局限与误用 / Limits：不同参数重复不是独立生物学重复
- 状态 / Status：`planned`
