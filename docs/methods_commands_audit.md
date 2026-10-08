# 命令与原始论文核对 / Command and paper audit

日期：2026-10-08。方法卡中的未执行配方标为documented_not_tested，不是运行日志；实际执行版本和结果另见reports。命令使用的占位输入必须由真实数据适配，import或help成功不是完整方法成功。

| 方法 | 已核对的命令/入口 | 直接证据 | 判定 |
|---|---|---|---|
| ARACNe-AP | ant main；Java阈值、bootstrap及consolidate参数；seed、pvalue、tfs | [官方README](https://github.com/califano-lab/ARACNe-AP) | 参数与例子一致；本任务未构建Java软件 |
| Python decoupler/CollecTRI | dc.op.collectri、dc.mt.ulm、dc.mt.viper | 官方CollecTRI README和本项目实际run manifest | 本项目使用2.1.2；来源快照latest2.2.0不得写成实际运行版本 |
| VIPER/msVIPER | 原始R viper调用，msviper入口单独记录 | [Bioconductor文档](https://bioconductor.org/packages/viper/)和实际viper validation | viper1.36.0完成；msVIPER未调用 |
| pySCENIC | grn/ctx/aucell；grn与aucell seed；num_workers；annotations_fname和expression_mtx_fname | [官方CLI源码](https://raw.githubusercontent.com/aertslab/pySCENIC/master/src/pyscenic/cli/pyscenic.py) | CLI源码HTTP200核对；依赖、输入loom和ranking库未运行验证 |
| SCENIC+ | 独立Python3.11环境、源码安装、scenicplus CLI | [官方README](https://github.com/aertslab/scenicplus) / [CLI源码](https://raw.githubusercontent.com/aertslab/scenicplus/main/src/scenicplus/cli/scenicplus.py) | 官方Linux要求保留；配方未运行 |
| Pando | initiate_grn/find_motifs/infer_grn/coef | [官方README](https://github.com/quadbio/Pando) | 官方真实对象quick-start；card仅列条件化调用 |
| hdWGCNA | MetacellsByGroups/SetDatExpr/TestSoftPowers/ConstructNetwork/ModuleEigengenes | [basic tutorial](https://smorabit.github.io/hdWGCNA/articles/basic_tutorial.html) | 函数与sample分组规则核对；本任务未构建模块 |
| LINGER | pip LingerGRN==1.110、bedtools、import linger及PBMC流程 | [README](https://github.com/Durenlab/LINGER) / [PBMC教程](https://github.com/Durenlab/LINGER/blob/main/docs/PBMC.md) | 软件PyPI版本与GitHubtag不可混同；外部资源未核实下载 |
| scPRINT | hf download固定revision；scprint gninfer的adata、ckpt_path、species、cell_type和output_filename | [官方README](https://github.com/cantinilab/scPRINT) | 参数来自README；HF原始模型远端元数据核对，未下载/运行 |
| RENGE | estimate_hyperparams_and_fit(X,E)、calc_qval、predict | [README](https://github.com/masastat/RENGE) | E/X与A[i,j]方向明确；缺少scCRISPR输入，本任务未运行 |
| SwitchTFI | python example.py -d ery；conda安装方案 | [README](https://github.com/bionetslab/SwitchTFI) | 上游仓库包含example data时才可执行；并非本牙周运行 |
| KEGNI | bash run_mESC.sh；run_pbmc_naiveCD4T.sh | [README](https://github.com/Lipxiao/KEGNI) | 上游例子名一致；口腔数据adapter与环境仍待实现 |
| DoRothEA/PROGENy/RegEnrich/GRaNIE/NicheNet/Inferelator/OmniPath/CellOracle | 相应包安装、import/packageVersion、官方vignette入口 | 各[方法卡](methods_index.md)对应的官方来源 | 保留为环境/文档检查入口；PROGENy现有真实运行另有manifest，其余未宣称完整执行 |

全部原始论文DOI和题名已经按DOI查询PubMed-indexed Europe PMC metadata，见[literature registry](literature_registry.json)与[source evidence](methods_source_evidence.json)。scPRINT采用正式2025论文，不使用scPRINT-2预印本替代；hdWGCNA正确DOI为10.1016/j.crmeth.2023.100498。CLI source哈希追加至evidence，只表明核对版本快照，不保证将来branch不变。
