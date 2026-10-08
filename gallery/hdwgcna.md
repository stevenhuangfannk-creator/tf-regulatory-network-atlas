# hdwgcna Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## hdwgcna-01 · Soft-power diagnostic

- 科学用途 / Purpose：选择网络软阈值
- 所需数据 / Input：不同 power 的 scale-free fit/mean connectivity
- 生成方式 / Generation：hdWGCNA 官方 tutorial 原生诊断图
- 代码入口 / Entry：[官方文档或源码](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：拟合与连通度之间的折中
- 场景 / Scenario：满足 metacell/样本条件的 WGCNA 构建
- 局限与误用 / Limits：拟合高不等于生物网络真实
- 状态 / Status：`planned`

## hdwgcna-02 · Gene dendrogram and module colors

- 科学用途 / Purpose：展示基因共表达模块
- 所需数据 / Input：TOM/dissimilarity；dynamic tree cut module assignment
- 生成方式 / Generation：PlotDendrogram 原生绘图
- 代码入口 / Entry：[官方文档或源码](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：颜色表示无向共表达模块
- 场景 / Scenario：实际完成 network/module construction
- 局限与误用 / Limits：模块不是有向 GRN；不得标为 TF regulon
- 状态 / Status：`planned`

## hdwgcna-03 · Module eigengene embedding

- 科学用途 / Purpose：展示模块在细胞状态中的表达
- 所需数据 / Input：真实 ME/hME；embedding；batch correction definition
- 生成方式 / Generation：原生 ME embedding 或定制 FeaturePlot
- 代码入口 / Entry：[官方文档或源码](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：ME 是模块表达的主成分概括
- 场景 / Scenario：cell-type-specific module 描述
- 局限与误用 / Limits：ME 与 hME 处理不同；sign 任意不能直接解释激活
- 状态 / Status：`planned`

## hdwgcna-04 · Module–trait association

- 科学用途 / Purpose：检查模块与 donor 疾病状态的联系
- 所需数据 / Input：donor ME summary；trait；model；CI/q
- 生成方式 / Generation：原生/定制关联热图；正式统计按 donor
- 代码入口 / Entry：[官方文档或源码](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：相关方向表示模块表达和表型共变
- 场景 / Scenario：生物学重复充分的模块表型分析
- 局限与误用 / Limits：metacell 不是独立 donor；疾病批次混杂需排查
- 状态 / Status：`planned`

## hdwgcna-05 · Hub gene connectivity

- 科学用途 / Purpose：根据 kME 排序模块 hub
- 所需数据 / Input：kME；module membership；基因表达
- 生成方式 / Generation：原生 hub/connectivity 图或定制 network
- 代码入口 / Entry：[官方文档或源码](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：hub 指模块内高连接/高 kME 候选
- 场景 / Scenario：同组织模块候选筛选
- 局限与误用 / Limits：hub gene 不自动是 master regulator
- 状态 / Status：`planned`

## hdwgcna-06 · Module preservation and regulon overlap

- 科学用途 / Purpose：检查模块可迁移性和 TF prior 关联
- 所需数据 / Input：independent dataset preservation stats；gene universe；overlap/q
- 生成方式 / Generation：原生 preservation diagnostics 与定制 overlap 矩阵
- 代码入口 / Entry：[官方文档或源码](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：preservation 支持结构稳定；overlap 提出 regulator 候选
- 场景 / Scenario：真实独立数据验证/与 TF 活性整合
- 局限与误用 / Limits：模块重叠与 regulon 有向性不能互相替代
- 状态 / Status：`planned`
