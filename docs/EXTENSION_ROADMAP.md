# 扩展路线与进入条件 / Extension roadmap

当前实际完成CollecTRI–decoupler ULM、Python VIPER、原始Bioconductor VIPER和PROGENy。以下按科学输入和资源成熟度排序；未运行流程有明确进入条件、下一个操作和验收产物，不能被计入当前科学结果。

## 优先级与验收 / Priorities and acceptance

| 优先级 | 扩展 | 当前缺口 | 下一项具体操作 | 进入/完成标准 |
|---|---|---|---|---|
| P1 | 现有RNA案例的敏感性与独立复现 | 当前病/健康数量与assay不完全平衡，现有方法共享先验 | 用同一元数据审核另一个真实牙周/种植体周炎队列；固定TF/normalization后复现效应方向；按donor做重复与assay敏感性 | 保留每队列donor表与effect/CI，不以细胞数代替重复；外部支持与共享先验算法一致性分开报告 |
| P2 | pySCENIC | 缺少固定的species/build/ID匹配motif ranking和annotation数据库、兼容环境及正式预算 | 先核对数据参考基因组和gene symbol映射；选择Feather v2数据库并保存URL/hash；独立环境做固定seed子集安装/GRN/ctx/AUCell验证 | 三步输出完整、motif target coverage可追溯；RSS需真实注释；完成全数据及donor敏感性后才能比较疾病TF排名 |
| P2 | hdWGCNA | 尚未构建模块，没有模块/trait/hub结果；TOM成本需测量 | 按donor×cell_type设置metacells或明确pseudobulk路线；先在有足够cells/donors的Fibroblast类型测试soft-power和block资源 | 样本间不混合metacells；保留模块、eigengene、kME、TOM参数；用donor-level trait分析和module preservation评估稳定性 |
| P3 | ARACNe-AP standalone bulk | 当前46个donor×cell_type不是46个独立同类样本，更不是100个独立供体；缺少足够表达队列、Java/Ant环境和运行预算 | 使用下面已核对的GDC候选先做临床/组织/表达文件审计，再选择至少约100个独立合格case的同类bulk队列 | 阈值计算、充分bootstrap、DPI和consolidation真实完成；report标为独立HNSC bulk案例，不能跨疾病当作牙周效应 |
| P4 | DoRothEA资源敏感性 | 未运行DoRothEA | 在固定现有RNA矩阵上指定confidence A/B，保留覆盖/资源许可；与CollecTRI使用同一算法与gene universe | 标明先验来源重叠；不把一致性称为独立实验验证 |
| P4 | NicheNet/OmniPath upstream context | sender/receiver设计、receiver contrast和prior尚未按案例固定 | 先定义具体cell-type pair与donor-level receiver差异，下载并hash ligand-target/prior和来源 | ligand activity单独命名，实际通讯预测和TF activity分开；所有边标prior/inferred/unknown |
| P5 | CellOracle | 缺少适用base GRN、可信state问题及实际模型运行 | 选择物种/build和组织适配base GRN；评估是否具备可识别的状态转换；独立环境小规模拟合和对照扰动 | 真实simulation及projection成功才生成Fig10；报告模型外推，不称为敲除实验证明或谱系追踪 |
| P5 | SCENIC+/Pando/GRaNIE | 当前案例缺少RNA–ATAC配对或匹配chromatin输入 | 找到有供体、peak坐标和genome版本的真实multiome资源，逐样本匹配RNA/ATAC；先核对motif及peak–gene证据 | 有真实TF–region和region–gene输出才生成Fig11；保留paired/unpaired方案、背景和统计单位 |
| P6 | LINGER/scPRINT | LINGER外部bulk archive完整性和授权未核实；scPRINT原始checkpoint未下载，软件许可字段冲突，GPU/环境未测 | 先完成assets表的下载可用性、hash、授权与独立环境检查；优先运行现成checkpoint推断，不重做atlas预训练 | 记录model revision、checkpoint hash、训练域和评估heldout；不能以attention/Shapley自动制造signed因果边 |
| P6 | RENGE/SwitchTFI/KEGNI | 当前案例缺少RENGE时序CRISPR、SwitchTFI可信transition标签、KEGNI适配口腔细胞知识图谱 | 按各方法card的输入门槛获得真实数据/先验后，运行官方小例再适配实际队列 | 新Gallery条目在真实输入和图件检查前保持planned；prior leakage与模型任务差异必须报告 |

## ARACNe的独立bulk候选 / Audited bulk candidate

候选：**TCGA-HNSC原发肿瘤bulk RNA-seq**。这是口腔/头颈癌相关的独立网络重建演示候选，研究问题与牙周炎不同。采用[官方GDC门户](https://portal.gdc.cancer.gov/projects/TCGA-HNSC)和GDC files API，不使用搜索片段推断样本量。

2026-10-08实际查询条件：project=TCGA-HNSC、Gene Expression Quantification、workflow=STAR - Counts、access=open、sample_type=Primary Tumor。HTTP200返回**520个文件、520个唯一case ID、520个唯一原发肿瘤sample ID**；元数据中每case一个表达文件/样本。总文件大小2,200,875,562 bytes（约2.20GB十进制；只是API元数据，不是已下载数据）。文件/case/sample映射与完整query见[候选manifest](methods_aracne_bulk_candidate.json)。

**执行状态：未下载表达文件，未运行ARACNe。** Case ID用于TCGA研究参与者标识，仍须在实际准备过程中检查patient去重、组织部位、临床纳入、RNA质量、异常样本和batch/purity；不能把metadata可用数直接当作最终通过QC样本数。文件内STAR列/Ensembl版本、count或TPM字段也尚未读取。

具体准备顺序：

1. 固定manifest并读临床/sample信息，选择一致的primary-tumor研究范围；每患者最多一个样本，记录纳入/排除原因。
2. 下载开放表达文件到data/raw并校验GDC/本地checksum；选择同一个STAR表达字段，映射human Ensembl到统一TF symbol，明确重复gene ID合并方案。
3. 在日志中报告通过QC的独立case数；若不足约100，停止此de novo案例而使用有出处预构建regulon。这个门槛是本项目可行性起点，不是算法性能保证。
4. 依据真实批次/组织差异选择并记录表达变换/预处理。混杂、肿瘤purity和细胞比例可以主导MI，因此不能把bulk边直接当作髓系细胞内调控。
5. 构建ARACNe-AP，先试运行阈值和少量bootstrap以测量内存/耗时，然后配置充分bootstrap（初始100次并检查更多次数是否稳定）、固定seed、DPI及整合检验。
6. 报告真正的network.txt、MI/p值、bootstrap边支持和参数敏感性；MI没有激活/抑制符号。转入VIPER需要另行建立有说明的tfmode/likelihood并检查target覆盖。
7. 将此case放在单独workflow/report，与牙周数据分开解释；HNSC网络推断成功不是牙周疾病机制或外部验证。

## pySCENIC进入条件 / Motif and genome gates

至少确认human/mouse物种、真实参考build（例如确认为GRCh38/hg38后才选该build数据库）、gene-ID namespace和motif annotation版本。不能因表达symbol相同就假定build正确。官方0.12系列支持Feather v2，ctxcore版本须匹配；数据库必须由固定URL重建，禁止直接推送大型ranking缓存。

先完成GRNBoost2/GENIE3、ctx motif剪枝、AUCell三个实际步骤，再计算RSS和regulon clustering。源码CLI已核对grn/aucell存在seed参数，ctx的annotations与expression_mtx参数存在；本项目没有证明旧环境在当前Windows/Python可安装。用独立Linux/WSL2 Python环境锁定PySCENIC/NumPy/Dask依赖，完整软件组合按真正安装验证后写锁文件。

## hdWGCNA进入条件 / Cells, donors and memory

metacells只能在同一donor×cell_type内部聚合，降低稀疏性不会增加生物重复。当前稀有类型/患者的细胞支持需先检查；不得为了纳入所有类别压低min_cells。构建所需基因数应明确，不默认对所有35360个genes直接做dense TOM。

单个G×G float64矩阵最少约8G² bytes：5000 genes约200MB，10000约800MB，20000约3.2GB。该计算仅为一个矩阵的理论存储，实际TOM、adjacency、距离、R复制和多线程峰值会更高，**不是实测内存承诺**。先限制分析gene universe，评估block网络和磁盘输出，再通过峰值内存/实际耗时决定全量预算。

soft-power、module dendrogram、MEs/hMEs和kME/hub表均必须来自真实构建；trait association使用donor单位，harmonization要防止把疾病信号当作batch消除。基础共表达模块/中心性不是有向TF GRN；TF–module富集是候选关联，需要motif/调控先验等另层证据。没有真实模块时Fig06和模块版Fig07保持待实现。

## 多组学与模型资源 / Multiomics and model assets

SCENIC+/Pando需要peaks、genome/motifs和RNA/ATAC匹配；GRaNIE跨样本共变需要足够适配生物样本，不能以一个患者细胞数替代跨个体样本。Linux/WSL2独立环境优先，各方法不能共用一个强行堆满依赖的主环境。

scPRINT原始checkpoint的官方HF API已核对revision、size及LFS SHA256，medium-v1.5.ckpt约222MB文件大小只说明远端权重，不代表GPU显存需求。LINGER的data_bulk.tar.gz仅核对到官方教程链接，archive下载/大小/hash/授权仍待核实。详见[模型与数据库资源表](methods_assets.json)、[许可证和方法边界](methods_index.md)。先验证可下载/可授权/可加载，再决定实际计算；不为没有实测的模型编造VRAM、小时数或科学成功率。
