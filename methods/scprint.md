# scPRINT / 方法卡片

定位：**GRN inference; foundation model**。来源核查日期：2026-10-08。

原始scPRINT在超过50M细胞上预训练，通过transformer推断context-specific gene networks；另含denoising/embedding。

## 状态与证据 / Status and evidence

- 本卡：`source_audited`；本注册表审计未安装或运行该方法。项目实际执行见 [Validation Report](../reports/Validation_Report.md)。
- [官方源码](https://github.com/cantinilab/scPRINT)；[官方文档](https://github.com/cantinilab/scPRINT)。
- 论文：scPRINT: pre-training on 50 million cells allows robust gene network predictions.，Nature communications，indexed year 2025，首次发表日期 2025-04-16。[DOI](https://doi.org/10.1038/s41467-025-58699-1)。
- GitHub latest release: `2.3.8`; published `2026-02-20T09:16:30Z`; repository pushed `2026-08-11T10:12:46Z`.
- 许可证：**CONFLICT: GPL-3.0 LICENSE vs MIT pyproject metadata**。核查级别：`license_metadata_conflict`。本仓库不重新分发工具源码、受限数据库或模型权重。

`pushed_at`只表示仓库最近push，release日期只表示release；二者都不是运行成功、持续支持或科学性能保证。许可证和依赖以固定commit/实际安装版本为准。

## 输入与输出 / Inputs and outputs

**输入：** count-based单细胞AnnData、gene/protein/Ensembl映射、原始模型checkpoint与元数据；当前软件不等同于scPRINT-2。

**输出：** attention-derived gene networks、embeddings、denoised expression、labels（须分别记录所运行任务）。

## 分析流程 / Analysis logic

锁定原始model/software/checkpoint →下载权重并审计hash/model terms →species/gene映射 →GRN inference/attention heads选择 →与独立ChIP/perturbation benchmark评估。

**适用边界：** attention不是直接调控证明，也不能自动当作signedTF causal边。训练数据库与测试集可能重叠；零样本泛化要说明训练域。源码license与pyproject元数据冲突。

## 隔离环境与命令 / Environment and recipes

当前pyproject要求Python>=3.10,<3.13，torch==2.2.0，NumPy>=1.24,<2.0；可选triton2.2。须独立环境，兼容CUDA时才启用flash。

以下是文档核查后的安装/调用配方，状态为 **`documented_not_tested`**；不是本次运行日志。`--help`/import检查只能核对安装，不能代表完整科学流程。

```text
python -m pip install scprint==2.3.8
# Use a separate Python 3.11 environment, matching torch/CUDA to the device.
```

```text
hf download jkobject/scPRINT medium-v1.5.ckpt --revision 8e1ad1a1bc40c1fc2f4f1700fe27923eea9a2bed --local-dir models/scprint
scprint gninfer --adata my_human_anndata.h5ad --ckpt_path models/scprint/medium-v1.5.ckpt --species "NCBITaxon:9606" --cell_type "cell_type_name_from-cell_type-obs_col" --output_filename grn.h5ad
# scPRINT-2 is a separate repository/model, not a silent substitute.
```

参数与seed：正式运行必须锁定version/commit、输入checksum、全部参数、随机种子（初始建议1）及库自身随机状态。未运行方法没有冒造的参数优化或性能测量。

资源：GPU推断通常更适合；CPU模式可用性依赖具体任务。checkpoint大小、VRAM、runtime未实测；注意all-cell PCA/UMAP的RAM成本。

## 图件与验收 / Figures and acceptance

context-specific network、AUPRC/EPR benchmark、gene/program embedding和disease–cell-type多面板；模型benchmark不能冒充本案例验证。

该方法的示例科学图状态为**待实际运行**。可学习原文/官方教程图形结构；不得把原论文图或随机示例冒充本牙周案例结果。长期图形索引见 [Figure Gallery](../gallery/README.md)。

执行验收至少检查：物种/ID/build一致性、实际target覆盖、边类型与来源、donor独立性、参数/抽样稳定性、数值到输入表可追溯、结果和解释边界。预测、相关性和计算扰动均不能单独证明生物学因果。

## 模型权重 / Checkpoint evidence

官方README链接的 [Hugging Face原始scPRINT模型](https://huggingface.co/jkobject/scPRINT) API已核对（HTTP200）；revision 8e1ad1a1bc40c1fc2f4f1700fe27923eea9a2bed。medium-v1.5.ckpt大小221,742,980 bytes，LFS SHA256 96ff7c5d9e1ad5076e818bde3c38f498c95cd354cc42029d90691b5ba2964ff8。模型卡标注apache-2.0，这与软件LICENSE/pyproject是不同对象，不能互相替代。

这里只核对远端元数据，没有下载权重、校验实际文件或运行模型。其他原始checkpoint大小/hash见[模型与外部资源证据](../docs/methods_assets.json)；GPU显存和运行时间未测量。
