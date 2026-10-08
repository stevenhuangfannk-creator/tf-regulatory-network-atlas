# TF Regulatory Network Atlas / 转录因子与上游调控网络图谱

基于真实人牙周单细胞数据，连接方法核查、TF 活性、供体统计、可追溯调控先验、科研图形与可复用代码。**本项目已运行分析并产出真实图件；高级方法按输入与资源要求逐步扩展。**

Reproducible, source-audited TF activity analysis of human periodontal inflammation, with donor-level models, original VIPER and a method-specific figure gallery.

![真实数据综合图](results/figures/Composite_periodontal_regulatory_landscape.png)

## 本轮结果 / Executed case

- 输入：CELLxGENE 作者发布的人牙周 meta-atlas，105,918 cells；选取 **Williams / GSE164241 同研究健康与牙周炎**，避免把多研究健康/疾病对比当成清洁疾病效应。固定 H5AD 下载地址和 SHA 见 [输入清单](data/input_manifest.json)，原论文 DOI **10.1016/j.cell.2021.05.013**；meta-atlas 关联 GEO **GSE266897**。
- 实际保留 **38,971 cells**，成纤维/巨噬/血管内皮三类；**46 donor×cell-type pseudobulk、21,690 expressed genes、516 prior regulators**。13 个健康供体编码和 5 个保守疾病编码；PD161/PD164 后缀活检联系仍待完整补充表确认。
- 完成 **CollecTRI + decoupler ULM、Python VIPER、原始 Bioconductor VIPER、PROGENy（14 pathways）**。疾病模型调整 10x assay，使用 donor-level OLS/HC3；另有 v3 子集、留一供体、1,000 次供体 bootstrap、20 次 target subsampling。共表达、motif、perturbation、ARACNe de novo 没有伪装成完成。
- 候选由实际结果排序。成纤维中 GTF3A、ZNF148、TFE3、JUND 推断活性升高，ETV3 下降；内皮 GLI2 为另一候选。CREBBP/NFKBIB 是辅助调控因子，不能统称 sequence-specific TF。ULM 与原始 VIPER 效应 Spearman 约 0.94，但共享先验不构成独立验证。

**先读 [Validation Report](reports/Validation_Report.md)**：这里的差异是小样本、assay 不平衡、保守供体映射下的探索性计算结果；没有实验因果证明。网络箭头来自有文献证据的 CollecTRI prior，不是牙周炎数据新推断的调控边。

## 入口 / Navigation

| 内容 | 入口 |
|---|---|
| 21 种方法/资源、许可证、维护与实测状态 | [Methods index](docs/methods_index.md) / [machine-readable registry](docs/methods_registry.csv) |
| 数据下载、供体、批次和 source audit | [Data audit](docs/DATA_AUDIT.md) / [donor map](data/donor_map.csv) |
| 按方法检索图形、用途、数据、解读与误用 | [Figure Gallery](gallery/README.md) / [figure contracts](gallery/catalog.csv) |
| 真实单图与综合多面板图 | [Figures](results/figures/) / [PDF composite](results/figures/Composite_periodontal_regulatory_landscape.pdf) |
| 真实数值与边来源 | [Result tables](results/tables/) |
| 每张图英文标题/图注及中文解释 | [Figure captions](gallery/real_figures.md) |
| Nature/Cell/Genome Biology 等图形语法参考 | [Figure references](docs/figure_references.md) |
| 完整运行、软件版本与环境限制 | [Environments](environments/README.md) / [run manifest](reports/run_manifest.json) |
| 新口腔数据适配与统计范围 | [Reuse guide](docs/REUSE_GUIDE.md) |
| 未运行方法的资源门槛 | [Extension roadmap](docs/EXTENSION_ROADMAP.md) |
| 科学独立审查与失败 | [Independent audit](reports/independent_audit.md) / [Failure log](reports/Failure_Log.md) |

## 快速开始 / Quick start

在仓库根目录，准备 Python 3.12 和 R 4.3.x，使用隔离环境；完整版本及平台限制见环境说明。

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r environments/requirements.lock.txt
$env:R_LIBS_USER = "$PWD/data/local/Rlibrary"
Rscript environments/install_R.R
.\.venv\Scripts\python.exe scripts/run_all.py --rscript "C:/Program Files/R/R-4.3.1/bin/Rscript.exe"
```

实际顺序：下载并校验 → raw counts 分块、symbol 合并、donor pseudobulk → ULM/Python VIPER → 原始 R VIPER → 同输入比较 → PROGENy/Hallmark 功能背景 → TF transcript/activity 对照 → target 稳定性 → 报告 → R 出图 → tests。

已有结果直接出图：`python scripts/run_all.py --figures-only --rscript <Rscript>`。测试：`python -m unittest discover -s tests -v`。输入网络与数据 hash 不匹配即停止，避免资源更新悄悄改变旧结果。PROGENy/Hallmark 接口仍可能变动，确切 cache 应本地保留。

## 架构与边界 / Layout and boundaries

`docs/` 核查与决策；`methods/` 方法卡和原始 VIPER 入口；`workflows/` 实际分析；`data/` 来源、供体、校验；`config/` 数值参数与 seed；`environments/` 依赖；`results/` 真实表和图；`gallery/` 图形契约；`reports/` 运行与验证；`tests/` 关键不变量；`scripts/` 自动化入口。

本轮不计算 hdWGCNA modules/hub/preservation、SCENIC motif/AUCell/RSS、增强子 GRN 或模拟 TF knockout，所以 Fig06/10/11 等待实现；Fig09 是 ULM cell-type 活性轮廓，不叫 RSS。未来 ARACNe 独立 bulk 候选核查了 TCGA-HNSC 520 个开放病例，但未下载或重建；肿瘤案例不作为牙周炎效应验证。

所有图由 R 生成，PDF/SVG 保留可编辑文字，PNG 600 dpi。工作流图是示意；其余数值图来自结果表。原始矩阵、数据库、模型权重、cache、环境与本机路径不进入 Git。项目代码采用 MIT；第三方工具/数据库保留各自许可，学术非商业或许可冲突条目详见注册表。

## 维护 / Maintenance

新增方法先查原始论文、官方代码与许可证；新增图形先登记科学用途、输入、证据类型、source table 与状态，实测后才添加 example。数据/网络更新建立新版本并保留旧 checksum。重要文档采用中文正文配英文术语；跨平台和重型方法未实测时明确标注。提交前运行 tests、文档链接检查和图件 QA，禁止把依赖安装、示意图或候选代码登记为完成分析。
