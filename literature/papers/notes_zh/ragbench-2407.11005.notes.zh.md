# RAGBench：带 TRACe 细粒度标签的 RAG 评测数据集

> 来源：literature/papers/markdown/ragbench-2407.11005.md
> 说明：这是中文精读笔记，不是全文翻译。

## 一句话定位

RAGBench 是一个约 100K 样本的真实 RAG 评测数据集，提出 TRACe 框架，用 span 级标签同时评估检索相关性、上下文利用率、回答忠实度和完整性。

## 研究问题

已有 RAG 评测往往只判断答案是否正确或是否幻觉，缺少能训练评估模型的统一格式和细粒度标签。RAGBench 关注的问题是：如何构建一个跨行业、跨任务、带可解释标签的数据集，用于训练和比较 RAG evaluator，而不仅是评测单个 RAG 系统。

## 评测对象与任务设置

每个样本包含问题、若干检索文档、模型回答和标注。数据来自 12 个组件数据集，覆盖 biomedical research、general knowledge、legal contracts、customer support、finance 五类领域。任务包括多文档问答、客户支持手册问答、金融表格与文本推理、法律合同长上下文、开放网页查询等。上下文长度从约 100 token 到 11K token，文档数通常为 1-10。

## 指标与评测方法

TRACe 包含四项指标。Relevance 衡量检索文档中对回答问题有用的内容占比，反映检索器是否带来噪声。Utilization 衡量检索上下文中被生成器实际使用的内容占比，可识别“检索到但没用上”。Completeness 衡量所有相关信息中有多少被回答利用，防止模型只用部分证据生成不完整回答。Adherence 衡量回答是否完全被上下文支持，对应 faithfulness、groundedness、attribution；既可做 response-level hallucination 标签，也可做 sentence/span 级支持判断。

形式上，Relevance 和 Utilization 通过相关/被利用 span 长度除以文档长度计算；Completeness 通过 relevant span 与 utilized span 的交集比例计算；Adherence 通常聚合为“回答是否所有句子都被支持”的布尔标签。

## 数据集/标注/实验设计

组件数据集包括 PubMedQA、CovidQA、HotpotQA、MSMarco、HAGRID、ExpertQA、CUAD、DelucionQA、EManual、TechQA、FinQA、TAT-QA。所有数据被标准化为 RAG 格式，总量约 100K，划分为 train/dev/test，且同一来源内 query 不跨 split 重叠。除已有 LLM 回答的数据外，论文用 GPT-3.5 和 Claude 3 Haiku 为样本生成回答；提示不强制模型严格贴合上下文，以形成更丰富的标签分布。

标签由 GPT-4 生成：标出相关上下文片段、被回答使用的片段，以及回答句子是否被上下文支持。Completeness 由 Relevance 与 Utilization 派生。标注后做一致性检查和最多三轮重标，处理 schema 错误和内部矛盾；部分支持的句子按 hallucination 处理。与 DelucionQA 人工标注对齐时，去除“Neither”差异后 Adherence example-level F1/Accuracy 约 0.96/0.93，span-level 约 0.97/0.95；Utilization 在 40 条人工细标样本上约 0.92/0.94；Relevance 约 0.76/0.78，说明 relevance 更难。

## 主要发现

微调 DeBERTa-v3-Large NLI 模型可在单次前向中预测多个 TRACe 指标，并与 GPT-3.5 judge、RAGAS、TruLens 比较。测试集中 DeBERTa 的 hallucination AUROC 多数在 0.64-0.86，Relevance 和 Utilization 的 RMSE 约 0.04-0.26，整体可与更大 LLM judge 和商业评测系统竞争。论文特别指出 Relevance 比 Utilization 更难，因为它不仅是语义相似，还要求判断哪些上下文信息对正确回答是必要的。

## 局限与风险

RAGBench 的“真值”主要由 GPT-4 标注生成，虽有人类对齐验证和后处理，但仍存在 judge 偏差。Relevance 人工对齐低于其他指标，说明“必要信息”边界主观且困难。部分数据由商业模型生成回答，分布可能受模型风格影响。数据以英文为主，领域虽广但仍不覆盖所有生产 RAG，如多轮、工具执行、实时网页和多模态。

## 对本仓库 ragbench 的启发

本仓库如果要做 ragbench，不应只保存最终正确/错误标签，而应保存 span 级证据标签：哪些上下文相关、哪些被回答实际使用、回答哪些句子被支持。这样才能训练轻量 evaluator，并把失败归因到 retriever、reranker、context packing 或 generator。

## 对“公理化 LLM wiki”论文的可借用点

TRACe 很适合作为 wiki 生成的公理化评测骨架：Relevance 对应证据是否必要，Utilization 对应条目是否实际使用证据，Completeness 对应是否覆盖所有关键事实，Adherence 对应每个 wiki 断言是否可由证据推出。Span 级标注还能支撑“每个断言绑定最小证据集”的论文论点。

## 可落地的测试项

- Span 级证据标注：为每条样本保存 relevant_spans、utilized_spans、supported_response_spans。
- 检索器噪声测试：计算 Relevance，低分说明 top-k 或切块策略带来冗余。
- 生成器利用率测试：计算 Utilization，检索命中但未使用时定位到 prompt 或上下文组织问题。
- 完整性测试：计算 Completeness，发现只回答部分证据的样本。
- 幻觉检测测试：Adherence 任一句不支持即标为 hallucinated，并输出不支持句子。
- 轻量 evaluator 训练集：用 span 标签训练 DeBERTa/小模型，多头预测 TRACe 指标。
- 指标一致性检查：如果回答声称 fully supported 但没有支持 span，自动重评或进入人工队列。
