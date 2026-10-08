# omnipath Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## omnipath-01 · Signed upstream signaling network

- 科学用途 / Purpose：整合候选 receptor–signaling–TF 路径
- 所需数据 / Input：OmniPath query edges；direction/sign；sources；license filters
- 生成方式 / Generation：资源/API 输出后定制图
- 代码入口 / Entry：[官方文档或源码](https://omnipathdb.org/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：符号和方向表示数据库证据
- 场景 / Scenario：候选 TF 的 upstream prior context
- 局限与误用 / Limits：OmniPath 是知识资源，不自动推断该样本信号活动
- 状态 / Status：`planned`

## omnipath-02 · Evidence/source coverage matrix

- 科学用途 / Purpose：审计每条先验的支持来源与覆盖
- 所需数据 / Input：interaction records；source count；curation flags
- 生成方式 / Generation：定制 evidence heatmap
- 代码入口 / Entry：[官方文档或源码](https://omnipathdb.org/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：多来源支持应区分独立实验与数据库重复
- 场景 / Scenario：上游网络证据审计
- 局限与误用 / Limits：source count 不等于独立实验重复
- 状态 / Status：`planned`

## omnipath-03 · Context-filtered intercellular network

- 科学用途 / Purpose：按表达/细胞注释过滤先验通信
- 所需数据 / Input：intercellular annotations；LR prior；真实表达阈值
- 生成方式 / Generation：定制 LR/path diagram
- 代码入口 / Entry：[官方文档或源码](https://omnipathdb.org/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：只表示给定表达过滤后保留的候选
- 场景 / Scenario：RNA-only upstream hypothesis generation
- 局限与误用 / Limits：不能作为已完成 NicheNet/通讯因果分析
- 状态 / Status：`planned`
