# linger Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## linger-01 · TF–CRE–gene network

- 科学用途 / Purpose：展示模型推断的多层调控网络
- 所需数据 / Input：actual TF–RE、RE–TG weights；genome；prior/model versions
- 生成方式 / Generation：LINGER 实际输出后定制三层图
- 代码入口 / Entry：[官方文档或源码](https://github.com/Durenlab/LINGER)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：区分预训练 prior 与当前样本模型权重
- 场景 / Scenario：满足模型所需 paired/unpaired 输入的方案
- 局限与误用 / Limits：预训练可迁移性和 reference 影响结果；非实测绑定
- 状态 / Status：`planned`

## linger-02 · Cell-type regulatory activity

- 科学用途 / Purpose：比较模型输出的 TF 调控活性
- 所需数据 / Input：真实 TF activity；cell labels；model config
- 生成方式 / Generation：输出后定制热图/embedding
- 代码入口 / Entry：[官方文档或源码](https://github.com/Durenlab/LINGER)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：分数解释遵循对应模型版本定义
- 场景 / Scenario：完成 LINGER workflow 的 cell-type programs
- 局限与误用 / Limits：不能将其他工具 TF 分数标为 LINGER
- 状态 / Status：`planned`

## linger-03 · Generalization/perturbation benchmark

- 科学用途 / Purpose：审计预测网络的泛化
- 所需数据 / Input：公开 benchmark；holdout split；actual predictions；metrics
- 生成方式 / Generation：重现官方 benchmark 后 performance curve
- 代码入口 / Entry：[官方文档或源码](https://github.com/Durenlab/LINGER)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：泛化只对未泄漏的 holdout 有意义
- 场景 / Scenario：具备参考网络或扰动数据的评估
- 局限与误用 / Limits：共享训练 prior 的 benchmark 可能有信息泄漏
- 状态 / Status：`planned`
