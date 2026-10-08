# ARACNe-AP / 方法卡片

定位：**GRN inference**。来源核查日期：2026-10-08。

利用互信息、DPI 与 bootstrap 构建候选 TF–target 网络，是 VIPER regulon 的一种来源。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/califano-lab/ARACNe-AP)；[官方文档](https://github.com/califano-lab/ARACNe-AP)。
- 论文：ARACNe-AP: gene network reverse engineering through adaptive partitioning inference of mutual information.，Bioinformatics (Oxford, England)，indexed year 2016，首次发表日期 2016-04-23。[DOI](https://doi.org/10.1093/bioinformatics/btw216)。
- GitHub latest release: `none observed`; published `unknown`; repository pushed `2023-03-06T16:48:35Z`.
- 许可证：**Columbia software evaluation; non-commercial academic/educational restrictions**。核查级别：`verified_license_text`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** 基因 × 样本的 tab-separated 标准化表达矩阵；每行一个 TF symbol 的列表；统一物种、基因 ID 和表达处理。

**输出：** network.txt：regulator、target、mutual information、整合检验 p value；各 bootstrap 网络和阈值文件。

## 分析流程 / Analysis logic

先计算 MI 阈值 → 使用不同固定种子做充分 bootstrap（正式初始方案至少 100 次，并检查稳定性）→ DPI 移除部分间接依赖 → consolidate → 保留边的 MI、p 值、bootstrap 来源 → 另行构造带 mode-of-regulation 和 likelihood 的 VIPER regulon。

**适用边界：** 本项目以约 100 个合适表达样本作为进入 de novo 网络评估的初始门槛，而非算法保证或独立性定理。小供体队列中的大量细胞不能替代独立生物重复。MI 没有激活/抑制符号；TF 列表提供候选来源方向，并不证明因果。

## 隔离环境与命令 / Environment and recipes

独立 Java/Ant 环境；官方要求 JDK > 1.8 和 Ant。Java 本身可在 Windows 使用；正式大规模并行可用 Linux/WSL2。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
git clone https://github.com/califano-lab/ARACNe-AP.git
cd ARACNe-AP
ant main
```

```text
java -Xmx5G -jar dist/aracne.jar -e expression.tsv -o aracne_out --tfs tfs.txt --pvalue 1E-8 --seed 1 --calculateThreshold
# Bash / Linux: bootstrap seeds 1..100
for i in {1..100}; do java -Xmx5G -jar dist/aracne.jar -e expression.tsv -o aracne_out --tfs tfs.txt --pvalue 1E-8 --seed "$i"; done
java -Xmx5G -jar dist/aracne.jar -o aracne_out --consolidate
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：CPU；官方例子 Java heap 5 GB 是示例，不是通用需求。成本随样本、基因数、TF 数与 bootstrap 次数增长；运行前在小子集测峰值内存和耗时。

## 图件与验收 / Figures and acceptance

MI/稳定性诊断、bootstrap edge frequency、稀疏 TF–target 网络；这些需要从边表自定义绘制。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。
