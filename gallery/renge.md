# renge Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## renge-01 · Time-series CRISPR regulatory network

- 科学用途 / Purpose：用时序扰动模型筛查 direct/indirect 候选关系
- 所需数据 / Input：真实 time-series scCRISPR；A coefficients；A_qval
- 生成方式 / Generation：RENGE 实际模型矩阵后定制有符号网络
- 代码入口 / Entry：[官方文档或源码](https://github.com/masastat/RENGE)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：A[i,j] 是 gene j 到 gene i 的模型系数；边宽与符号分别编码
- 场景 / Scenario：满足 KO 和采样时间设计的分析
- 局限与误用 / Limits：RNA 横断面疾病分组不能替代时序扰动输入
- 状态 / Status：`planned`

## renge-02 · Knockout expression prediction

- 科学用途 / Purpose：评估模型对未观察时点/扰动的预测
- 所需数据 / Input：真实 KO expression predictions；独立观测；train/test split
- 生成方式 / Generation：模型预测与观测的配对时间图
- 代码入口 / Entry：[官方文档或源码](https://github.com/masastat/RENGE)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：误差反映指定测试任务的泛化
- 场景 / Scenario：有真实 held-out CRISPR 数据的验证
- 局限与误用 / Limits：训练 KO 拟合不是独立验证；不能绘制假预测轨迹
- 状态 / Status：`planned`

## renge-03 · Signed coefficient and q-value matrix

- 科学用途 / Purpose：审计网络方向、效应与候选边筛选
- 所需数据 / Input：A、A_qval；阈值；参考网络
- 生成方式 / Generation：真实输出矩阵后 heatmap/ranking
- 代码入口 / Entry：[官方文档或源码](https://github.com/masastat/RENGE)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：符号遵循模型方向定义；q 值属于模型边筛选
- 场景 / Scenario：真实 RENGE 输出后的网络解释
- 局限与误用 / Limits：模型 q 值不是临床疾病差异 q 值
- 状态 / Status：`planned`
