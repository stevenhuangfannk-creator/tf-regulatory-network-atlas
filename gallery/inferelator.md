# inferelator Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## inferelator-01 · Weighted GRN and confidence network

- 科学用途 / Purpose：展示回归/先验整合后的候选调控边
- 所需数据 / Input：actual model edges；weights；confidence；prior
- 生成方式 / Generation：Inferelator 输出后定制 signed/weighted graph
- 代码入口 / Entry：[官方文档或源码](https://inferelator.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：系数与 confidence 的含义按模型定义
- 场景 / Scenario：足够样本的表达/先验输入
- 局限与误用 / Limits：权重不是实验效应；prior 与推断来源应区分
- 状态 / Status：`planned`

## inferelator-02 · Bootstrap confidence and task sharing

- 科学用途 / Purpose：评估网络重采样及多任务共识
- 所需数据 / Input：bootstrap edges；task-specific networks；confidence
- 生成方式 / Generation：定制 stability/overlap 图
- 代码入口 / Entry：[官方文档或源码](https://inferelator.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：共享支持反映定义的任务与采样
- 场景 / Scenario：真实多任务/重采样分析
- 局限与误用 / Limits：同数据重复抽样不算外部验证
- 状态 / Status：`planned`

## inferelator-03 · Precision–recall evaluation

- 科学用途 / Purpose：审计可识别参考关系的能力
- 所需数据 / Input：reference gold standard；held-out edges；predictions
- 生成方式 / Generation：官方 evaluation outputs 后 PR curve
- 代码入口 / Entry：[官方文档或源码](https://inferelator.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：覆盖与 precision–recall 需共同解读
- 场景 / Scenario：有参考且排除 prior leakage 的评估
- 局限与误用 / Limits：不完整参考将未知边当负例会偏置
- 状态 / Status：`planned`
