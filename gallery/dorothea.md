# dorothea Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## dorothea-01 · Confidence-stratified regulon coverage

- 科学用途 / Purpose：显示 A–E 证据级别与输入覆盖
- 所需数据 / Input：confidence labels；observed targets；物种
- 生成方式 / Generation：DoRothEA 资源后定制分层 QC
- 代码入口 / Entry：[官方文档或源码](https://saezlab.github.io/dorothea/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：高置信度较少与低置信度更多的权衡
- 场景 / Scenario：预构建 TF prior 选择
- 局限与误用 / Limits：证据级别不是该队列真阳性概率
- 状态 / Status：`planned`

## dorothea-02 · DoRothEA TF activity heatmap

- 科学用途 / Purpose：在替代 regulon 中估计 TF 活性
- 所需数据 / Input：实际 viper/decoupler activity；confidence filter
- 生成方式 / Generation：DoRothEA 提供资源，评分器输出后定制热图
- 代码入口 / Entry：[官方文档或源码](https://saezlab.github.io/dorothea/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：与 CollecTRI 共同 TF 的活动模式比较
- 场景 / Scenario：同输入先验敏感性评估
- 局限与误用 / Limits：不是新增 de novo GRN 推断
- 状态 / Status：`planned`

## dorothea-03 · Prior-source rank comparison

- 科学用途 / Purpose：量化 CollecTRI 与 DoRothEA 对候选的影响
- 所需数据 / Input：统一输入和评分器的两种资源结果；common TFs
- 生成方式 / Generation：定制配对排名/重叠热图
- 代码入口 / Entry：[官方文档或源码](https://saezlab.github.io/dorothea/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：差异可能来自 target set 与权重
- 场景 / Scenario：resource-level robustness
- 局限与误用 / Limits：资源共享文献；一致性不是外部验证
- 状态 / Status：`planned`
