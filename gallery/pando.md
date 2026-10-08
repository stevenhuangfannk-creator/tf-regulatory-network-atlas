# pando Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## pando-01 · TF coefficient network

- 科学用途 / Purpose：展示表达与开放元件联合模型的候选调控
- 所需数据 / Input：model coefficients；motif TF；regions；target genes
- 生成方式 / Generation：Pando 模型结果后定制有符号网络
- 代码入口 / Entry：[官方文档或源码](https://github.com/quadbio/Pando)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：系数表示模型条件下 TF–target association
- 场景 / Scenario：multiome 及正确 motif/annotation
- 局限与误用 / Limits：共线性与稀疏性影响系数，非因果效应
- 状态 / Status：`planned`

## pando-02 · Regulatory module heatmap

- 科学用途 / Purpose：展示 target program 在细胞状态中的变化
- 所需数据 / Input：真实 regulatory modules；RNA/activity；metadata
- 生成方式 / Generation：官方 module 输出后定制热图
- 代码入口 / Entry：[官方文档或源码](https://github.com/quadbio/Pando)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：模块是模型关联的调控程序
- 场景 / Scenario：Pando 模型成功后的状态比较
- 局限与误用 / Limits：需区别与 WGCNA module 的定义
- 状态 / Status：`planned`

## pando-03 · TF–region–gene locus view

- 科学用途 / Purpose：审计具体 enhancer 候选链接
- 所需数据 / Input：regions/motifs/coefficients；genome；signal tracks
- 生成方式 / Generation：定制 locus/network 图
- 代码入口 / Entry：[官方文档或源码](https://github.com/quadbio/Pando)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：多层证据共同支持候选关系
- 场景 / Scenario：multiome 关键候选解释
- 局限与误用 / Limits：不自动证明 enhancer 必要性或 promoter 接触
- 状态 / Status：`planned`
