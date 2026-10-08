# 环境与实际运行 / Environments and execution

已实测：Windows 11、Python 3.12.14、decoupler 2.1.2；R 4.3.1、Bioconductor VIPER 1.36.0。Python 与 R 各用独立本地环境，没有升级已有科研环境。WSL2 无 Linux 发行版，本轮没有验证 WSL/Linux；高级方法需要另建环境。

Python 精确完整依赖见 `requirements.lock.txt`，主要分析依赖见 `requirements.txt`。decoupler 的可视化依赖由 pip 安装，但项目绘图只用 R。UMAP 坐标来自作者数据，不需要重新运行 scanpy/UMAP。

```powershell
# 在仓库根目录；使用 Python 3.12
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r environments/requirements.lock.txt
$env:R_LIBS_USER = "$PWD/data/local/Rlibrary"
Rscript environments/install_R.R
.\.venv\Scripts\python.exe scripts/run_all.py --rscript "C:/Program Files/R/R-4.3.1/bin/Rscript.exe"
```

本轮本机 R 库实际位于任务工作目录 `work/Rlibrary`；运行前可通过 `R_LIBS` 指向该隔离库。新机器按上面命令安装到仓库 ignored `data/local/Rlibrary`。R 安装脚本会选择兼容 Bioconductor，但最新 CRAN 和跨平台 font/device 可能导致渲染差异；**安装脚本不是已验证的逐版本 restore lock**。精确已加载版本记录于 `methods/viper/R_runtime.json`、`methods/viper/sessionInfo.txt` 与 `results/figures/R_plot_sessionInfo.txt`。R 最新版本与论文数值复现需要重新检验。

```bash
# Linux/WSL2 等价入口，未在本轮 Linux 主机验证
python3.12 -m venv .venv
.venv/bin/python -m pip install -r environments/requirements.lock.txt
export R_LIBS_USER="$PWD/data/local/Rlibrary"
Rscript environments/install_R.R
.venv/bin/python scripts/run_all.py --rscript "$(command -v Rscript)"
```

数据 H5AD 固定版本约 705 MB、CollecTRI 约 4.35 MB，SHA256 写入 input manifest。PROGENy 和 Hallmark 通过官方接口/Enrichr 获取并检查已记录 hash；这些接口可能更新，若 hash 改变会停止而不悄悄替换结果。保留本地 cache 或联系版本来源后另立新分析版本。原始/模型数据不进入 Git。

主要 Python 流程本次约 71 seconds；原始 R VIPER 约 14 seconds（首次 numba 编译和下载另计）；绘图耗时依设备。总内存 16 GB，开始空闲约 1.1 GB，因此固定 256-cell sparse chunks 和 2 threads；没有测量可保证的峰值 RAM 或高负载计算预算。大型 pySCENIC/hdWGCNA/多组学模型不能由这个演示的速度推断成本。

仅重新出图：`python scripts/run_all.py --figures-only --rscript <Rscript>`。仅统计验证：`python -m unittest discover -s tests -v`。不要在不同方法之间随意混用环境或把 dependency installed 当作 method executed。

非绘图导出检查：`python -m pip install -r environments/requirements.qa.txt`，随后 `python scripts/audit_exports.py`。它读取有效 PDF 字体、PNG dpi 和 SVG text，不重绘 R 图；统计测试结果记录用 `python scripts/run_tests.py`。所有文件链接/编码与忽略边界用 `python scripts/check_repository.py`。人工逐面板检验仍必要，见 `gallery/QA.md`。
