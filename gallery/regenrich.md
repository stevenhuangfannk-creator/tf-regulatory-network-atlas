# regenrich Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## regenrich-01 · Differential-regulator ranking

- 科学用途 / Purpose：结合表达变化和网络目标富集筛查 regulator
- 所需数据 / Input：RegEnrich input；DE signatures；inferred network；scores
- 生成方式 / Generation：原生 regulator score/enrichment plots；核对安装版帮助
- 代码入口 / Entry：[官方文档或源码](https://bioconductor.org/packages/RegEnrich/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：排名是算法综合评分
- 场景 / Scenario：有适当重复和完整表达输入的比较
- 局限与误用 / Limits：regulator rank 不等于 TF activity 或 msVIPER NES
- 状态 / Status：`planned`

## regenrich-02 · Regulator–target subnetwork

- 科学用途 / Purpose：解释候选 regulator 的目标程序
- 所需数据 / Input：actual RegEnrich network；selected regulators；scores
- 生成方式 / Generation：网络输出后定制图
- 代码入口 / Entry：[官方文档或源码](https://bioconductor.org/packages/RegEnrich/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：边来自选定 inference model
- 场景 / Scenario：完整 RegEnrich workflow
- 局限与误用 / Limits：无符号边不能画为激活/抑制
- 状态 / Status：`planned`

## regenrich-03 · Enrichment robustness

- 科学用途 / Purpose：检查候选排名对网络/签名选择敏感性
- 所需数据 / Input：真实不同网络/参数重跑；ranks；common universe
- 生成方式 / Generation：定制配对排名/稳定性图
- 代码入口 / Entry：[官方文档或源码](https://bioconductor.org/packages/RegEnrich/)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：一致性说明特定设定下的算法稳健性
- 场景 / Scenario：至少两个真实设置/方法
- 局限与误用 / Limits：不可通过人工 rank 模拟方法一致性
- 状态 / Status：`planned`
