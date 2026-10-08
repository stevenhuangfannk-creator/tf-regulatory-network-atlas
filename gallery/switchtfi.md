# switchtfi Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## switchtfi-01 · Transition-specific GRN

- 科学用途 / Purpose：识别两种真实细胞状态之间的调控候选
- 所需数据 / Input：预推断 GRN；真实 state labels；transition edge scores
- 生成方式 / Generation：软件输出后定制状态网络
- 代码入口 / Entry：[官方文档或源码](https://github.com/bionetslab/SwitchTFI)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：边筛选依赖明确的状态定义和原始 GRN
- 场景 / Scenario：具有合理分化/状态转换问题的 scRNA
- 局限与误用 / Limits：Healthy/Disease 不自动构成分化轨迹
- 状态 / Status：`planned`

## switchtfi-02 · Differentiation TF ranking

- 科学用途 / Purpose：根据 transition network 排序候选 TF
- 所需数据 / Input：真实 ranked TFs；网络拓扑；评分
- 生成方式 / Generation：官方 example notebook 或定制 rank 图
- 代码入口 / Entry：[官方文档或源码](https://github.com/bionetslab/SwitchTFI)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：排名说明所定义的分化转换中候选重要性
- 场景 / Scenario：完成状态过滤与排序流程
- 局限与误用 / Limits：与表达差异或 ULM/VIPER 活性排名的定义不同
- 状态 / Status：`planned`

## switchtfi-03 · State-specific target expression

- 科学用途 / Purpose：解释候选 TF 与 target 的状态关系
- 所需数据 / Input：真实表达；TF-target scores；state metadata
- 生成方式 / Generation：官方 example 与定制配对分布图
- 代码入口 / Entry：[官方文档或源码](https://github.com/bionetslab/SwitchTFI)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：状态内关联与转换评分分别显示
- 场景 / Scenario：候选 regulator 的机制审计
- 局限与误用 / Limits：表达状态关联不是 lineage tracing 或因果验证
- 状态 / Status：`planned`
