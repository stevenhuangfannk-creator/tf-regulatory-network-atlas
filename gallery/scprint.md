# scprint Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## scprint-01 · Denoised expression landscape

- 科学用途 / Purpose：展示模型的表达重建
- 所需数据 / Input：actual predictions；raw counts；metadata；weight version
- 生成方式 / Generation：官方 inference 后定制 observed–predicted 图
- 代码入口 / Entry：[官方文档或源码](https://github.com/cantinilab/scPRINT)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：重建输出与原观测分开表示
- 场景 / Scenario：权重与基因词表匹配的 scRNA 数据
- 局限与误用 / Limits：denoising 可能改变基因相关结构，非新增观测
- 状态 / Status：`planned`

## scprint-02 · Attention-derived GRN

- 科学用途 / Purpose：展示模型内部权重导出的候选网络
- 所需数据 / Input：official GRN export；attention aggregation；pruning rule
- 生成方式 / Generation：scPRINT 实际 GRN inference 输出后定制网络
- 代码入口 / Entry：[官方文档或源码](https://github.com/cantinilab/scPRINT)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：边来自模型规定的 attention/aggregation 过程
- 场景 / Scenario：模型运行成功并完成 GRN extraction
- 局限与误用 / Limits：attention 不自动等于 TF binding 或因果
- 状态 / Status：`planned`

## scprint-03 · GRN benchmark performance

- 科学用途 / Purpose：比较推断网络的参考重现能力
- 所需数据 / Input：真实 predictions；reference；splits；AUROC/AUPRC
- 生成方式 / Generation：official benchmark 后定制曲线
- 代码入口 / Entry：[官方文档或源码](https://github.com/cantinilab/scPRINT)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：precision/recall 按指定参考 universe 解读
- 场景 / Scenario：无泄漏的网络评估
- 局限与误用 / Limits：稀疏 reference 下 AUPRC 与覆盖必须一起报告
- 状态 / Status：`planned`

## scprint-04 · Cell embedding and model annotation

- 科学用途 / Purpose：检查模型表示与已知细胞注释对应
- 所需数据 / Input：真实 model embedding；labels；held-out annotation
- 生成方式 / Generation：原生输出后定制 embedding/confusion matrix
- 代码入口 / Entry：[官方文档或源码](https://github.com/cantinilab/scPRINT)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：表示结构或分类性能属于模型特定任务
- 场景 / Scenario：权重与数据匹配的表征审计
- 局限与误用 / Limits：不是 GRN 证据；新投影不是 lineage tracing
- 状态 / Status：`planned`
