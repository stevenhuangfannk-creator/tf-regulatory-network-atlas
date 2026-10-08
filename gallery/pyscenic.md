# pyscenic Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## pyscenic-01 · Coexpression adjacency network

- 科学用途 / Purpose：展示 GRNBoost2/GENIE3 原始候选关系
- 所需数据 / Input：adjacencies.tsv；importance；TF list
- 生成方式 / Generation：pySCENIC grn 输出后定制图
- 代码入口 / Entry：[官方文档或源码](https://pyscenic.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：importance 表示模型特征贡献
- 场景 / Scenario：SCENIC 的 motif pruning 前 QC
- 局限与误用 / Limits：importance 不是 MI、p 值或已验证结合；无符号
- 状态 / Status：`planned`

## pyscenic-02 · cisTarget motif enrichment

- 科学用途 / Purpose：检查候选模块的 motif 支持
- 所需数据 / Input：matching genome motif ranking DB；annotation；ctx enrichment
- 生成方式 / Generation：pySCENIC ctx 输出后定制 NES/AUC 与 motif 表
- 代码入口 / Entry：[官方文档或源码](https://pyscenic.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：富集支持 TF motif 与候选 targets 的关联
- 场景 / Scenario：基因 ID 与数据库一致的模块筛选
- 局限与误用 / Limits：motif 富集不等于 TF binding；注释可能通过同源 TF
- 状态 / Status：`planned`

## pyscenic-03 · AUCell activity embedding/heatmap

- 科学用途 / Purpose：展示 motif-pruned regulon 活性
- 所需数据 / Input：真实 regulons.csv；AUCell matrix；cell metadata
- 生成方式 / Generation：pySCENIC aucell 输出后定制 embedding/heatmap
- 代码入口 / Entry：[官方文档或源码](https://pyscenic.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：AUC 表示该 regulon targets 在细胞表达排名中的富集
- 场景 / Scenario：完整完成 grn→ctx→aucell 流程
- 局限与误用 / Limits：用 prior gene sets 的 AUCell 不能冒称完成 SCENIC
- 状态 / Status：`planned`

## pyscenic-04 · Regulon Specificity Score

- 科学用途 / Purpose：排序细胞类型特异 regulons
- 所需数据 / Input：nonnegative AUCell matrix；type labels；RSS outputs
- 生成方式 / Generation：官方 RSS 分析后定制点图/矩阵
- 代码入口 / Entry：[官方文档或源码](https://pyscenic.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：相对特异性度量，不代表绝对活动强度
- 场景 / Scenario：跨细胞类型候选 regulon 描述
- 局限与误用 / Limits：样本比例和标签影响 RSS；不是差异检验
- 状态 / Status：`planned`

## pyscenic-05 · Regulon clustering

- 科学用途 / Purpose：识别协同活性模式
- 所需数据 / Input：regulon activity；距离/聚类设定
- 生成方式 / Generation：定制聚类热图
- 代码入口 / Entry：[官方文档或源码](https://pyscenic.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：共同变化可能说明共享细胞状态
- 场景 / Scenario：同一数据的 regulon program discovery
- 局限与误用 / Limits：共活性不是 TF–TF 有向调控
- 状态 / Status：`planned`

## pyscenic-06 · Motif-supported TF–target network

- 科学用途 / Purpose：展示保留的 motif-pruned 网络
- 所需数据 / Input：ctx-pruned edge membership；来源与数据库版本
- 生成方式 / Generation：定制网络并区分共表达与 motif 支持
- 代码入口 / Entry：[官方文档或源码](https://pyscenic.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：与原始 adjacency 相比具有额外 motif 证据
- 场景 / Scenario：完整 SCENIC 候选解释
- 局限与误用 / Limits：motif 支持不提供疾病特异因果边
- 状态 / Status：`planned`
