# granie Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## granie-01 · Enhancer-mediated GRN

- 科学用途 / Purpose：展示 TF–peak–gene 关联链
- 所需数据 / Input：GRaNIE connections；TF motif；peak/gene correlations
- 生成方式 / Generation：原生 GRN 可视化或输出后定制网络
- 代码入口 / Entry：[官方文档或源码](https://grp-zaugg.embl-community.io/GRaNIE/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：边是相关和 motif 候选证据的组合
- 场景 / Scenario：足够独立样本的 RNA+ATAC 联合队列
- 局限与误用 / Limits：细胞数量不补足独立样本；相关不等于调控
- 状态 / Status：`planned`

## granie-02 · Connection/correlation diagnostics

- 科学用途 / Purpose：审计 TF–peak/peak–gene 关联筛选
- 所需数据 / Input：真实 correlation distributions；background；FDR
- 生成方式 / Generation：官方 connection QC 绘图
- 代码入口 / Entry：[官方文档或源码](https://grp-zaugg.embl-community.io/GRaNIE/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：背景分布与 FDR 反映候选筛选
- 场景 / Scenario：GRaNIE 网络构建前后质量检查
- 局限与误用 / Limits：相关方向与背景假设应完整记录
- 状态 / Status：`planned`

## granie-03 · GRN communities and GRaNPA performance

- 科学用途 / Purpose：解释网络模块并评估预测质量
- 所需数据 / Input：真实 community；独立 perturbation/reference；GRaNPA outputs
- 生成方式 / Generation：官方拓扑图；GRaNPA 实际评估后性能图
- 代码入口 / Entry：[官方文档或源码](https://grp-zaugg.embl-community.io/GRaNIE/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：性能仅针对使用的验证任务
- 场景 / Scenario：存在匹配外部数据时
- 局限与误用 / Limits：未运行 GRaNPA 不能将社区图称验证
- 状态 / Status：`planned`
