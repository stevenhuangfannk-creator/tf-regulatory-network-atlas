# scenicplus Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## scenicplus-01 · eRegulon activity landscape

- 科学用途 / Purpose：比较 enhancer-driven regulon 的活动
- 所需数据 / Input：TF/region/gene eRegulons；gene/region AUC；RNA+ATAC
- 生成方式 / Generation：官方 eRegulon activity 输出后定制 embedding/heatmap
- 代码入口 / Entry：[官方文档或源码](https://scenicplus.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：gene-与region-based 活性应分开显示
- 场景 / Scenario：匹配或明确整合的 multiome 数据
- 局限与误用 / Limits：RNA-only TF scores 不能冒称 eRegulon
- 状态 / Status：`planned`

## scenicplus-02 · TF–enhancer–gene tripartite network

- 科学用途 / Purpose：呈现三层调控证据
- 所需数据 / Input：TF-region motif；region-gene links；distance/importance；genome
- 生成方式 / Generation：SCENIC+ 输出后定制三层网络
- 代码入口 / Entry：[官方文档或源码](https://scenicplus.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：每种边分别表示 motif/模型/关联证据
- 场景 / Scenario：明确 enhancer coordinate 与参考版本的 multiomics
- 局限与误用 / Limits：模型连边不是直接 chromatin contact 或因果
- 状态 / Status：`planned`

## scenicplus-03 · eRegulon specificity

- 科学用途 / Purpose：识别细胞类型特异 enhancer programs
- 所需数据 / Input：gene/region AUC；cell types；RSS
- 生成方式 / Generation：官方 specificity 分析后定制点图
- 代码入口 / Entry：[官方文档或源码](https://scenicplus.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：specificity 与绝对活动强度分别解读
- 场景 / Scenario：真实 multiome 跨类型比较
- 局限与误用 / Limits：RSS 依赖类型组成；非正式显著性
- 状态 / Status：`planned`

## scenicplus-04 · Enhancer genomic tracks

- 科学用途 / Purpose：将候选 enhancer 与位点上下文对应
- 所需数据 / Input：真实 region coordinates；ATAC signal；genes；links
- 生成方式 / Generation：导出 tracks 后 genome browser/定制轨迹图
- 代码入口 / Entry：[官方文档或源码](https://scenicplus.readthedocs.io/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：开放区域和候选 target links 提供位点上下文
- 场景 / Scenario：关键候选 locus 展示
- 局限与误用 / Limits：必须统一 genome build；不能制造信号峰
- 状态 / Status：`planned`
