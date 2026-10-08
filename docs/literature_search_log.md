# 来源检索与核查 / Source audit log

日期：2026-10-08（Asia/Shanghai）。类型：有明确工具范围的scoping source audit；不是穷尽性系统综述，也不声称正式PRISMA筛选。

问题：哪些TF/GRN/activity/co-expression/upstream/multiomics工具具备公开论文、官方实现和可明确记录的输入/边界？哪些可用于现有RNA案例，哪些缺少必要数据或执行环境？

纳入：用户指定的全部工具/资源；原始方法论文；官方仓库、官方/Bioconductor文档；近期补充要求2023-10-08至2026-10-08同行评议方法与公开实现。排除：同名无关论文、仅检索摘要的性能主张、纯宣传材料、将原论文benchmark视为本队列结果。搜索中重复preprint/journal版本按journal DOI合并；不同软件/后续模型保留区别。

| 来源 | 查询/请求 | 结果与证据处理 |
|---|---|---|
| GitHub REST | 指定仓库`GET /repos/{owner}/{repo}`和`/releases/latest` | 保存canonical full_name、archived、pushed_at、license classifier、release tag/date；404不等于弃用 |
| 官方raw README/LICENSE/DESCRIPTION/pyproject | 使用API返回default_branch；核查source text | 用DOI/canonical source修正错误仓库；license全文短摘/hash保存在evidence |
| Crossref | query.title: RegEnrich/Dictys/TRIPOD/RENGE/LINGER/scPRINT/Pando/CollecTRI | HTTP429，未把失败响应当成验证；改用PubMed-indexed Europe PMC原始元数据与publisher DOI |
| Europe PMC/PubMed MED | `DOI:<original DOI>`；`resultType=core&pageSize=1` | 提取原始title、DOI、PMID、journal、pubYear与firstPublicationDate |
| Europe PMC scoped discovery | `TITLE_ABS:"gene regulatory" AND FIRST_PDATE:[2023-10-08 TO 2026-10-08] AND (JOURNAL:"Nature methods" OR JOURNAL:"Nature communications" OR JOURNAL:"Genome biology")` | 30篇候选源记录；近期纳入SwitchTFI、KEGNI，按原文code-availability再核对仓库 |
| Europe PMC targeted discovery | `TITLE_ABS:RENGE` | 同名无关记录排除；纳入Communications Biology 2023-12正式论文 |
| Europe PMC全文XML | RegEnrich/GRaNIE/scPRINT/RENGE/SwitchTFI/KEGNI的PMCID | 核对论文原文、code links及部分figure captions，未复制图像 |
| Bioconductor release pages | viper、GRaNIE、RegEnrich | 当前package version、R/BioC依赖、源码URL与license；viper自定义LICENSE另读取 |

发现的错误DOI和许可冲突在[方法索引](methods_index.md)保留。GRaNIE独立文档域本次请求出现TLS连接错误，官方Bioconductor页与EMBL源码URL/论文仍可核实；CellOracle猜测的simulation子路径404，仅引用其已核对官方文档根入口。未把未成功路径写成已验证页面。

完整body保留在本任务的中间工作区；提交仓库的证据是compact metadata、明确引用、license短摘和SHA256，避免复制大量第三方网页/软件。来源页面是动态的，长期维护需重新运行API审计并记录新访问日期；当前release并不意味着已安装或实测。
