# 实际交付状态 / Execution status

本轮原始输入到最终图件已完整重跑成功，入口为 `scripts/run_all.py`。不是只执行 toy example 或安装依赖；数值、图件和失败记录均保留。

| 方法 / Module | 输入 | 真实输出与验证 | 状态 |
|---|---|---|---|
| CollecTRI + decoupler ULM | 固定版本 human signed prior；46 donor×cell-type、21,690 genes | 516 regulator scores、assay-adjusted disease effect/HC3 CI/BH、cell scores、coverage、donor/target sensitivity | 已完成 |
| decoupler Python VIPER | 与 ULM 完全相同 gene universe/centered pseudobulk/prior | 46×516 NES-like scores、同模型统计；版本和原始 R 实现区分 | 已完成 |
| 原始 Bioconductor VIPER 1.36.0 | 同一 centered matrix、CollecTRI tfmode/sign 与 uniform likelihood | 46×516 scores、donor disease effects、ULM concordance、两实现比较 | 已完成；不等于 ARACNe/msVIPER |
| PROGENy + ULM | 14 pathway footprints、每条 nominal top100、padj<0.05 | 1,398 matched model edges、14 scores/统计、donor heatmap/forest | 已完成，pathway 与 TF 分开 |
| TF expression versus activity | 实际 donor logCPM、ULM score | 451 own-transcript regulator 对照、8图示候选的配对观测 | 已完成，描述性相关 |
| Hallmark prior-target context | 8 result-selected regulators、50 sets、21,690 gene background | 400 overlap tests/BH、shared targets | 已完成，非共表达/因果模块 |
| ARACNe-AP de novo、msVIPER MRA | 需要足够独立表达样本、Java/充分 bootstrap | 独立 TCGA-HNSC bulk 520 case 源目录已查，不曾下载/重建 | 未运行 |
| DoRothEA、pySCENIC、hdWGCNA | 独立 resource/motif databases/metacells 等 | 方法卡、命令核查、适用与资源边界 | 未运行 |
| CellOracle、SCENIC+、Pando、GRaNIE | 可用 base-GRN/state/multiome/ATAC 等 | 方法卡与待实现图形 | 未运行 |
| LINGER、scPRINT、Inferelator、RegEnrich、NicheNet、OmniPath、RENGE、SwitchTFI、KEGNI | 适合任务的先验、模型/多模态/扰动输入及环境 | 论文/源码/维护/许可证核查、资源门槛及图形契约 | 未运行 |

科学输入：CELLxGENE 作者 105,918-cell human periodontal meta-atlas；实际只选 Williams/GSE164241 的同研究 healthy/periodontitis。38,971 cells，13 healthy+5保守PD编码；巨噬筛选后6H+4PD。患者联系、assay imbalance、小样本和 broad-cell-type composition 限制详见 [Validation Report](Validation_Report.md)。

出图：13 套 PDF/SVG/600dpi PNG，其中 8 面板综合图；全部来自真实结果或明确 workflow schematic。21 种方法/资源的 78 图形契约，可检索已实现和待实现状态。见 [Gallery](../gallery/README.md)。

自检：完整 root workflow exit 0；7 tests 通过（本机无 raw-input skips）；独立关键系数复算误差≤1.4e-15；资源 SHA、target retention fraction、全图有效字体≥6.5pt、600dpi/可编辑 SVG、文档链接及 Git 忽略边界通过。Linux CI 只检查小型结果/数值测试，缺 raw 大输入的两项 integration checks 明确 skip，不称整套跨平台重跑。

可复现命令及平台限制：[Environments](../environments/README.md)；新口腔数据迁移：[Reuse guide](../docs/REUSE_GUIDE.md)。本地大输入和模型/cache 保留在 ignored 路径；现有科研项目完全只读。
