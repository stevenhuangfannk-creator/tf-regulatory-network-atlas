# nichenet Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## nichenet-01 · Ligand activity ranking

- 科学用途 / Purpose：估计哪些 sender ligands 可解释 receiver 差异基因
- 所需数据 / Input：sender expressed ligands；receiver geneset/background；prior
- 生成方式 / Generation：官方 ligand activity outputs 后排名图
- 代码入口 / Entry：[官方文档或源码](https://github.com/saeyslab/nichenetr)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：activity 是 target program 解释力
- 场景 / Scenario：明确 sender/receiver 与条件对比
- 局限与误用 / Limits：不是配体蛋白分泌量；不等于受体占用
- 状态 / Status：`planned`

## nichenet-02 · Ligand–target heatmap

- 科学用途 / Purpose：展示配体与候选 receiver targets 的先验得分
- 所需数据 / Input：actual predicted ligand-target regulatory potential
- 生成方式 / Generation：官方 ligand-target heatmap
- 代码入口 / Entry：[官方文档或源码](https://github.com/saeyslab/nichenetr)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：颜色是 prior-derived regulatory potential
- 场景 / Scenario：NicheNet 完整执行后的机制候选
- 局限与误用 / Limits：不代表已观测 TF–target/配体因果
- 状态 / Status：`planned`

## nichenet-03 · Ligand–receptor interaction matrix

- 科学用途 / Purpose：结合 sender/receiver 表达筛查信号联系
- 所需数据 / Input：expressed LR pairs；cell labels；prior
- 生成方式 / Generation：官方/定制 LR dotplot
- 代码入口 / Entry：[官方文档或源码](https://github.com/saeyslab/nichenetr)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：表达筛选支持通信可行性
- 场景 / Scenario：明确细胞来源与组织 context
- 局限与误用 / Limits：共表达不足以证明空间接触或通信
- 状态 / Status：`planned`

## nichenet-04 · Ligand–signaling–TF–target graph

- 科学用途 / Purpose：追踪候选 upstream regulatory route
- 所需数据 / Input：NicheNet signaling/GR prior；selected ligands/TF/targets
- 生成方式 / Generation：官方路径可视化或定制有证据分层图
- 代码入口 / Entry：[官方文档或源码](https://github.com/saeyslab/nichenetr)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：每段连边均保留 prior 来源和方向
- 场景 / Scenario：关键 ligand 机制解释
- 局限与误用 / Limits：最短路径不证明实际活跃信号链
- 状态 / Status：`planned`
