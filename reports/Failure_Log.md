# 失败与限制记录 / Failure log

1. CELLxGENE 下载在 683,242,469 bytes 处提前结束；使用经核实的 HTTP 206 Range 补齐 21,764,726 bytes，最终达到 705,007,195 bytes 且 HDF5 和 SHA256 校验通过。不得把初始残缺文件作为输入。详细请求和校验见 `data/download_manifest.json`。
2. 初次 cell ULM 默认 `empty=True` 使部分全零 target 在单个 chunk 被删除，导致 ZNF148 不再满足 min targets。已修为 `empty=False`，重新完成全流程；固定背景和独立 t-statistic 的测试通过。未发布失败批次的 cell 图。
3. 第一次 target-subsampling 统计触发 pandas 3 的 label-indexing `KeyError: 1`；改为显式 NumPy 参数输入，重跑 20 iterations 完成。不影响已经完成的主要统计。
4. 原始 Williams Table S1 直接下载遇到 publisher/补充材料访问限制；已取得论文主文、GEO titles 和 CELLxGENE 作者 metadata。PD 代码后缀保守合并，仍明确标记 `verified=False`，不臆造患者信息。
5. 图件初稿出现 Unicode 箭头字体异常、组合图图例裁切和密集候选标签；改用 ASCII 标题、短图例和有限避让标签后重新导出，并对每张图视觉检查。
6. 约 100 个 independent samples、充分 ARACNe bootstrap、cisTarget motif databases、ATAC、模型环境/权重和重型 GRN 内存尚不具备；这些方法仅来源核查，未声称实测。

原始大文件、下载缓存与本机环境没有推送；现有 Research OS/单细胞/空间数据库未修改。环境安装仅在本次工作目录进行。
