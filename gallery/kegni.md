# kegni Figure Gallery

状态 / Status：`implemented` 仅指本仓库已有真实运行和图件；`planned` 表示尚未完成该图。软件支持与本仓库执行分开记录。

## kegni-01 · Knowledge-graph-enhanced GRN

- 科学用途 / Purpose：整合 cell-type-specific prior 与 scRNA 推断候选边
- 所需数据 / Input：真实 scRNA；知识图谱；edge scores；model config
- 生成方式 / Generation：KEGNI 输出后定制 TF-target 图
- 代码入口 / Entry：[官方文档或源码](https://github.com/Lipxiao/KEGNI)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：prior 与模型预测来源必须分别编码
- 场景 / Scenario：数据和知识图谱词表匹配的网络推断
- 局限与误用 / Limits：共享先验不得被当作独立 ground truth
- 状态 / Status：`planned`

## kegni-02 · Held-out GRN benchmark

- 科学用途 / Purpose：评估参考边的预测能力
- 所需数据 / Input：真实 prediction；held-out prior/reference；AUROC/AUPRC
- 生成方式 / Generation：实际 benchmark 后 precision-recall 等曲线
- 代码入口 / Entry：[官方文档或源码](https://github.com/Lipxiao/KEGNI)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：结论受验证边 universe 与 train/test split 限制
- 场景 / Scenario：具备可独立留出的参考边
- 局限与误用 / Limits：防止 prior leakage；缺少训练排除记录时不称独立验证
- 状态 / Status：`planned`

## kegni-03 · Cell-type network comparison

- 科学用途 / Purpose：比较真实模型推断的细胞类型网络
- 所需数据 / Input：各 cell type edge scores；统一 genes/threshold
- 生成方式 / Generation：定制 overlap/edge-score matrix
- 代码入口 / Entry：[官方文档或源码](https://github.com/Lipxiao/KEGNI)；定制图在对应输出真实完成后加入
- 示例 / Example：待实现；未生成示例图片
- 解读 / Interpretation：差异反映模型与输入的共同作用
- 场景 / Scenario：同一数据且统一网络过滤的细胞类型比较
- 局限与误用 / Limits：不能把细胞类型 cell 数量差异当作生物学重复
- 状态 / Status：`planned`
