# MultiHop-RAG：面向多跳查询的 RAG 基准

> 来源：literature/papers/markdown/multihop-rag-2401.15391.md
> 说明：这是中文精读笔记，不是全文翻译。

## 一句话定位

MultiHop-RAG 专门评测 RAG 在多文档证据检索和跨证据推理上的短板，证明单跳相似度检索和直接拼接上下文不足以支撑复杂查询。

## 研究问题

论文指出许多真实 RAG 查询需要从多个文档取证并进行推理、比较或时间排序，而现有 RAG 基准多关注单个证据即可回答的问题。研究问题包括：检索器能否一次取回全部必要证据；LLM 在拿到检索证据后能否跨证据推理；系统在知识库没有答案时能否返回 insufficient information。

## 评测对象与任务设置

任务分为四类：Inference query 需要从多个证据合成关系或实体；Comparison query 比较多个来源中的属性或陈述；Temporal query 判断跨文档事件的时间顺序；Null query 的答案不能从知识库推出，应该拒答。实验分检索和生成两部分：检索侧比较多种 embedding 与 reranker；生成侧比较 GPT-4、GPT-3.5、Claude-2.1、Google PaLM、Llama-2-70B、Mixtral-8x7B 等模型在 retrieved chunks 和 ground-truth chunks 两种输入下的回答准确率。

## 指标与评测方法

检索指标包括 MAP@K、MRR@K、Hit@K，关注 top-K 中是否覆盖 ground-truth evidence。生成指标是答案准确率，比较模型输出与标准答案。论文还区分 retrieved chunk 设置和 ground-truth chunk 设置：前者评估端到端 RAG，后者剥离检索误差，评估 LLM 的多跳推理上限。Null query 用模型是否能识别无法回答来衡量拒答鲁棒性。

## 数据集/标注/实验设计

知识库来自 2023-09-26 到 2023-12-26 的英文新闻，覆盖技术、娱乐、体育、科学、商业、健康等类别，共 609 篇文章，平均约 2,046 tokens。流程包括：抽取事实/观点句作为 evidence；用 GPT-4 将 evidence 改写成 claim；抽取 bridge-entity 或 bridge-topic 把不同证据连接起来；再用 GPT-4 生成多跳问题和答案；最后人工抽样检查，并用 GPT-4 按“是否用到全部证据、是否仅凭证据可答、答案格式、问题类型一致性”等规则质检。数据集共 2,556 个查询，其中推理 816、比较 856、时间 583、空查询 301；约 42% 需要 2 条证据，30% 需要 3 条，15% 需要 4 条。

## 主要发现

多跳检索仍然困难。使用 voyage-02 加 bge-reranker-large 的最好配置，Hits@10 也只有 0.7467，Hits@4 降到 0.6625；这对真实系统很关键，因为上下文窗口通常只能容纳少量 chunk。生成侧同样不理想：用实际检索 chunk 时 GPT-4 准确率约 0.56；即使直接给 ground-truth evidence，GPT-4 也只有 0.89，PaLM 0.74，GPT-3.5 0.57，Llama-2-70B 和 Mixtral-8x7B 分别约 0.32/0.36。Mixtral 在比较和时间类问题上明显弱，常误处理否定或时间顺序。

## 局限与风险

数据生成高度依赖 GPT-4，虽然有质检但仍可能带入模板化问题、桥接偏差或答案过短的偏好。知识库只用英文新闻，且时间窗口较短。生成准确率的判定对开放式、多表述答案不够细。Null query 只是知识库不可推出，并不等同于现实世界不可回答，模型可能凭内部知识作答，导致评测目标需要严格限定为“根据给定证据”。

## 对本仓库 ragbench 的启发

ragbench 需要单独报告 evidence coverage，而不是只看最终答案。多跳任务应记录每题需要几条证据，并测 top-K 是否完整覆盖全部 evidence；只命中一条不能算检索成功。生成评测要拆成 retrieved-context 与 oracle-context 两档，以区分检索失败和推理失败。Null query 可以作为多跳拒答测试：问题形式复杂、看起来可答，但知识库缺少必要桥接证据。

## 对“公理化 LLM wiki”论文的可借用点

bridge-entity/bridge-topic 很适合 wiki 场景：把不同页面中的事实命题通过共享实体、主题、时间或属性连接起来，再生成可验证的复合断言。公理化 LLM wiki 可以将一个条目结论拆成多个 evidence-backed atoms，并要求每个 atom 的来源、桥接关系和组合规则可追踪。Null query 也能用于避免 wiki 在缺证时补写“合理但无来源”的段落。

## 可落地的测试项

- 证据覆盖率：每个问题标注 `required_evidence_ids`，计算 HitAll@K、PartialHit@K、MRR-first-evidence。
- oracle vs retrieved 双轨测试：同一问题分别喂 ground-truth evidence 和检索 top-K，分离检索瓶颈与推理瓶颈。
- 多跳类型集：推理、比较、时间、空查询四类分别报告准确率和拒答率。
- 证据数量梯度：2/3/4 条证据分桶，检查上下文长度和证据数增加时性能衰减。
- 否定与时间陷阱：构造包含 “not/except/before/after” 的比较和时间查询，检查模型是否反转关系。
