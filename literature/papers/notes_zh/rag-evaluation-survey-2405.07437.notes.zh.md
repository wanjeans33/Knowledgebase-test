# RAG 评测综述：Auepora 统一评测流程

> 来源：literature/papers/markdown/rag-evaluation-survey-2405.07437.md
> 说明：这是中文精读笔记，不是全文翻译。

## 一句话定位

这篇 survey 把 RAG 评测拆成“评什么、用什么数据评、用什么指标量化”三步，提出 Auepora 框架，用来统一比较 RAG 工具、benchmark 和研究论文中的检索、生成及系统级评测。

## 研究问题

论文关注的问题不是提出一个新 RAG 系统，而是回答：RAG 这种检索与生成耦合的系统应如何被评测。作者指出传统 QA 或 IR 指标只能覆盖局部：检索端需要判断文档是否相关、是否排对、是否足够覆盖；生成端需要判断回答是否相关、正确、忠实于证据；系统端还要看检索是否真的提升生成，以及延迟、噪声鲁棒性、拒答能力等实际要求。

## 评测对象与任务设置

评测对象被分成三个层次：检索组件、生成组件、RAG 整体系统。检索组件的可评测输出是相关文档或候选文档排序，核心关系包括“相关文档与查询”的 relevance，以及“相关文档与候选文档集合”的 accuracy/ranking。生成组件的可评测输出是响应文本或结构化内容，核心关系包括 response-query 的相关性、response-relevant documents 的 faithfulness、response-reference answer 的 correctness。

系统级评测强调组件间互动：一个检索器的 Recall@k 很高，不等于生成器会使用证据；一个生成器回答正确，也可能来自参数记忆而非检索上下文。因此论文主张区分组件评测与端到端评测，并补充检索增益、上下文利用、噪声和拒答等 RAG 特有维度。

## 指标与评测方法

检索指标分为非排序指标与排序指标。非排序指标包括 Accuracy、Precision、Recall@k；排序指标包括 MRR、MAP@k、Hit@k 等，用于衡量相关文档出现的位置。论文同时指出，传统 Recall/Precision 无法完全刻画 RAG 检索，因为 RAG 还关心文档是否会误导生成、是否多样、是否覆盖多跳证据。

生成指标包括 ROUGE、BLEU、BERTScore、F1、Exact Match、人评和 LLM-as-a-judge。论文把 LLM 裁判视为趋势，但提醒其需要明确评分准则、prompt、尺度和一致性校验。额外系统指标包括 latency、diversity、noise robustness、negative rejection、counterfactual robustness；对应可用单查询延迟、文档 embedding 余弦距离、misleading rate、mistake reappearance rate、rejection rate、error detection rate 等。

## 数据集/标注/实验设计

论文将 RAG benchmark 数据来源分为复用既有数据与构造新数据。既有资源包括 KILT 中的 NQ、HotpotQA、FEVER，以及 SuperGLUE 的 MultiRC、ReCoRD 等；优势是成熟，缺点是静态、可能已被模型训练覆盖，难以测试时效性。新构造数据包括 WikiEval、RGB、MultiHop-RAG、CRUD-RAG、CDQA、DomainRAG 等，常从新闻、网站、领域文档生成 QA 或多文档任务，用来测试更新知识、复杂查询和噪声上下文。

数据设计的关键是让样本直接对应评测目标：如果要测 faithfulness，就必须有证据文档或可核验事实；如果要测 multi-hop，就必须标出跨文档证据；如果要测拒答或反事实鲁棒性，就必须包含信息不足、误导证据或冲突证据。

## 主要发现

RAG 评测正在从单一 QA 正确率转向多目标评测：检索 relevance、生成 faithfulness、回答 correctness、噪声鲁棒性、延迟和用户偏好需要同时出现。现有工具和 benchmark 覆盖面不均衡：RAGAS、ARES 偏向上下文相关性和答案忠实性，RGB 强调信息整合、噪声和拒答，MultiHop-RAG 强调多跳检索质量，CRUD-RAG 扩展到 Create/Read/Update/Delete 场景，DomainRAG 强调领域、时效和多轮设置。

论文最有价值的发现是：端到端答案指标不足以解释失败来源。RAG 评测必须记录中间产物，包括 query、retrieved documents、reranked documents、prompt/context、answer，以及可选的人评或 LLM 裁判理由。

## 局限与风险

survey 本身偏分类与综述，没有统一复现实验。Auepora 的分类清晰，但很多指标仍来自不同 benchmark，定义不完全一致。LLM-as-a-judge 的稳定性、偏见、版本漂移和 prompt 敏感性是明显风险。自动生成 benchmark 虽能提升时效性，但也可能引入错误标签、浅层模式或生成器偏见。

## 对本仓库 ragbench 的启发

ragbench 应把评测日志设计成组件级可追踪结构：检索 query、top-k 文档、文档分数、证据覆盖、生成输入、最终答案和引用必须分开保存。指标上不应只报 answer correctness，还应至少报告 retrieval Recall@k/Hit@k、faithfulness、context relevance、answer relevance、latency、token cost 和噪声鲁棒性。

测试集应包含静态知识、近期更新知识、多跳问题、信息不足问题、冲突证据问题和结构化输出问题。这样才能分辨“检索不到”“检索到了但没用”“证据错误”“生成器幻觉”“应该拒答但回答了”等失败类型。

## 对“公理化 LLM wiki”论文的可借用点

可以借用 Auepora 的 EO-GT 关系来定义公理：回答必须可追溯到相关文档；引用文档必须与 query 有关；生成结论不得与证据冲突；当证据不足时应拒答或标注不确定。公理化 LLM wiki 还可以把 faithfulness、correctness、negative rejection 和 counterfactual robustness 转成可验证断言。

论文中的组件评测 vs 端到端评测也很适合该方向：wiki 系统不只评最终条目质量，还要评检索证据、引用覆盖、证据到声明的蕴含关系，以及更新事实是否覆盖旧事实。

## 可落地的测试项

- 检索 relevance：给定问题与 gold evidence，计算 Recall@5、Recall@10、MRR、MAP 或 Hit@k。
- 证据覆盖：多跳问题要求每个必要证据页或段落至少命中一次。
- 生成 faithfulness：逐条抽取回答声明，检查是否由检索上下文支持。
- 正确性：对短答案使用 EM/F1，对长答案使用人工或 LLM 裁判加明确 rubric。
- 噪声鲁棒性：在 top-k 中插入无关文档，比较答案正确性和引用变化。
- 反事实鲁棒性：插入错误但高相关文档，测试模型是否识别冲突并避免复述错误。
- 拒答能力：设置 evidence missing / false premise 样本，统计错误作答率与合理拒答率。
- 系统成本：记录检索耗时、生成耗时、总 latency、输入输出 token 和评测成本。
