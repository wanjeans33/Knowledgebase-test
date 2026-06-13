# LLM 时代的 RAG 评测综合综述

> 来源：literature/papers/markdown/rag-evaluation-comprehensive-survey-2504.14891.md
> 说明：这是中文精读笔记，不是全文翻译。

## 一句话定位

这篇较新的 survey 将 RAG 评测扩展为内部评测与外部评测：内部评测覆盖检索、生成、chunking、embedding、reranking 等组件，外部评测覆盖安全、效率、成本、公平性和可解释性等部署维度。

## 研究问题

论文试图回答：在 LLM 已成为 RAG 核心组件和评测工具之后，如何系统组织 RAG 的评测对象、指标、benchmark 和实践趋势。它不仅复述传统 IR/NLG 指标，也把 LLM-based evaluation、RAG-specific benchmark、安全攻击、隐私、成本收益和多语言覆盖纳入同一视角。

## 评测对象与任务设置

内部评测把 RAG 系统拆成可评测组件：预处理与 chunking、embedding、检索召回、排序/reranking、上下文融合、生成、引用或解释。检索目标包括 relevance、correctness、comprehensiveness；生成目标包括 faithfulness、correctness、relevance。论文比 2405 survey 更强调上游组件：chunking 可用关键词覆盖、tokens-to-answer、下游检索/生成效果评估；embedding 可借助 MTEB/MMTEB 等外部 benchmark，但最终仍需在 RAG 任务上验证。

外部评测关注系统是否能在真实环境中可用。安全评测包括噪声、冲突上下文、检索语料投毒、提示劫持、隐私泄露和公平性；效率评测包括检索时间、生成时间、资源消耗、token cost、索引维护成本，以及成本-效果折中。

## 指标与评测方法

IR 指标被分为非排序和排序两类。非排序指标包括 Hit@K、Recall@K、Precision@K、F1 和 coverage；排序指标包括 MRR、nDCG、MAP。nDCG 适合有 graded relevance 的任务，MRR 适合首个正确文档最重要的任务，Recall@K 适合 RAG 中“证据是否进入上下文窗口”的场景。

NLG 指标包括 EM、F1、ROUGE、BLEU、METEOR、BERTScore、语义相似度、人评和 LLM-as-a-judge。LLM 裁判可评 context relevance、answer relevance、faithfulness、completeness、hallucination 等，但论文强调它并非免费可靠：模型版本、prompt、温度、rubric 和安全性都会影响结果。

安全与鲁棒指标包括 factual accuracy、faithfulness、attack success rate、precision/recall/F1 for poisoned retrieval、resilience、conflict handling、privacy leakage、membership inference success、公平性差异等。效率指标包括单查询延迟、检索/生成分阶段耗时、索引大小、GPU/CPU 资源、token 成本和 performance per cost。

## 数据集/标注/实验设计

论文汇总了大量 RAG benchmark：RAGAS/WikiEval、FreshQA、ARES、RGB、MultiHop-RAG、CRUD-RAG、MedRAG、FeB4RAG、RAGBench、ReEval、DomainRAG、TelecomRAGEval、LegalBench-RAG、RAGEval、CoURAGE、RAGUnfairness、CoFE-RAG、OCRHindersRAG、OmniEval、CRAG、RAGPlayground、MTRAG、CDQA、U-NIAH、SCARF 等。

数据趋势大致是三类：早期复用 NQ、HotpotQA、FEVER 等静态 QA/KILT 数据；中期使用新闻、网页或领域语料构造更贴近现实的时效任务；近期增加法律、医疗、金融、电信、扫描文档 OCR、多轮对话、长上下文 needle-in-haystack、反事实和安全攻击数据。论文特别提醒，只包含 gold answer 而没有 gold evidence 的数据很难做组件级评测。

## 主要发现

统计分析显示，当前 RAG 研究仍主要评 retrieval 和 generation，安全和效率评测明显不足。传统指标仍占主导，因为便宜、稳定、易复现；LLM-based 评测增长很快，尤其在 2024 下半年和 2025 上半年，但一致性和成本仍是阻碍。

论文的重要判断是：许多新组件仍被端到端 QA 分数粗略评估，缺少功能分解。例如 chunking、embedding、reranking、context compression 可能都影响最终答案，但如果只看答案 EM/F1，很难知道是哪一步贡献或破坏了效果。

## 局限与风险

综合综述覆盖面很广，但由于纳入很多新 benchmark，部分比较停留在表格层面，缺少统一实验。LLM 裁判的黑箱性、时间漂移、prompt 注入和评分不稳定会污染评测结论。安全、隐私、公平性评测目前尚未形成统一标准。多语言覆盖有限，许多 benchmark 仍集中于英语和中文。

## 对本仓库 ragbench 的启发

ragbench 可以按“内部组件 + 外部属性”组织评测套件。内部组件至少包括 chunking 质量、embedding/retrieval 召回、reranking 排序、context relevance、answer faithfulness 和 answer correctness。外部属性至少包括 latency、token cost、索引大小、噪声鲁棒性、冲突处理、拒答、引用质量和安全攻击。

评测输出应支持按组件聚合：同一问题要能看到 top-k evidence、每个 evidence 的相关性、最终 answer 使用了哪些 evidence、哪些声明无法被 evidence 支持。这样才能服务调参，而不是只给一个端到端分数。

## 对“公理化 LLM wiki”论文的可借用点

这篇 survey 对“公理化 LLM wiki”最有用的是“功能分解评测”。可以把 wiki 条目生成拆成：检索覆盖公理、证据相关公理、声明蕴含公理、引用充分公理、冲突证据处理公理、更新知识优先公理、成本约束公理。

外部评测也可转化为 wiki 场景的约束：不得让语料投毒改变无关条目；不得泄露私有检索内容；引用必须可解释；当检索证据互相冲突时，条目应显式呈现不确定性或选择可信来源。

## 可落地的测试项

- Chunking 内在测试：gold evidence 是否完整落在一个或少数 chunk 中，记录 full-keyword coverage 与 tokens-to-answer。
- Embedding/检索测试：对每个问题计算 Recall@k、nDCG@10、MRR，并按领域、长度、问题类型分组。
- Reranking 测试：比较 rerank 前后 gold evidence 排名变化，以及无关高分文档比例。
- Context relevance：让裁判模型或人工判断 top-k 文档是否真正回答 query。
- Faithfulness：答案声明逐条对齐 evidence，统计 unsupported claim rate。
- 安全测试：构造语料投毒、检索劫持、冲突上下文、隐私诱导问题。
- 效率测试：分阶段记录 retrieval latency、rerank latency、generation latency、token cost、index size。
- 多语言测试：至少保留中英双语同构样本，避免只优化英文 benchmark。
