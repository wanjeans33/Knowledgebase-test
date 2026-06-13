# SAFE/LongFact：搜索增强的长文本事实性评测

> 来源：literature/papers/markdown/safe-long-form-factuality-2403.18802.md
> 说明：这是中文精读笔记，不是全文翻译。

## 一句话定位

SAFE 用 LLM agent 将长回答拆成自包含事实，并通过多轮搜索判断支持性；LongFact 则提供覆盖多主题的长文本事实性提示集。

## 研究问题

长文本事实性不能只和预设参考答案比，因为开放问题可能包含大量合理事实。论文提出两个问题：如何自动构造能诱发长回答的事实性 benchmark；如何在没有固定参考答案全集的情况下，对模型长回答中的每个事实进行可扩展查证，并把 precision 与“足够丰富”结合起来。

## 评测对象与任务设置

LongFact 包含 2280 个 prompts，覆盖 38 个主题，要求模型给出多段、细节丰富的回答。实验在 LongFact-Objects 的随机 250 个 prompts 上比较 13 个模型，生成长度上限 1024 tokens，温度为 0。SAFE 输入为 prompt-response pair，输出 supported、irrelevant、not-supported 三类事实数量。

## 指标与评测方法

SAFE pipeline 包括四步：将回答按句拆成 individual facts；把每个 fact 改写成自包含事实，替换代词和省略指代；判断该 fact 是否与回答用户问题相关；对相关 fact 进行多步搜索查证。查证时，LLM 根据待查事实和已有搜索结果生成搜索 query，每个 query 保留若干搜索结果；预设步数后，LLM 根据搜索证据判断 supported 或 not-supported。

聚合指标是 `F1@K`。precision 为 `S/(S+N)`，其中 `S` 是 supported facts，`N` 是 not-supported facts，irrelevant facts 不计入事实性 precision。recall 用 `min(S/K, 1)` 近似，K 表示用户期望的支持事实数量上限。`F1@K` 将 precision 与该 recall 合并；满分要求没有不支持事实，并且至少提供 K 个支持事实。

## 数据集/标注/实验设计

论文用 FActScore 人工标注数据检验 SAFE：496 个 prompt-response pairs，约 16000 个 individual facts。SAFE 与人工标签在 individual fact 层面一致率约 72%；在随机抽取的 100 个分歧样本中，以研究者结合完整互联网复核为准，SAFE 正确比例高于众包人工。成本上，SAFE 约 0.19 美元/响应，而众包人工约 4 美元/响应。

## 主要发现

SAFE 的关键价值是把“事实拆解”和“动态证据获取”结合起来，能处理预设参考答案没有覆盖的事实。较大模型整体长文本事实性更好，但长度、precision、recall 之间存在权衡：要求更多细节通常提高 supported facts 数量，也可能带来更多错误。只看 precision 会偏好短而保守的回答；`F1@K` 用 K 把“答得够多”纳入评测。

## 局限与风险

SAFE 依赖 LLM 的拆解、改写、相关性判断和推理能力，弱 judge 会把多个事实混成一个，或生成无关搜索 query。搜索引擎不是绝对真相来源，在专业领域、冷门事实、搜索结果冲突时会失败。`F1@K` 假设支持事实不重复，因此可能被重复正确事实刷 recall，需要去重或另设重复惩罚。

## 对本仓库 ragbench 的启发

对 RAG 场景，SAFE 的“动态 Google Search”可替换为“只查本次 corpus/chunks”。这样能测试系统是否在受限知识库内完成 grounding，而不是借助外部常识。`F1@K` 很适合防止 RAG 模型通过极短答案获得高精度：既要事实都被支持，也要覆盖足够多的支持事实。

## 对“公理化 LLM wiki”论文的可借用点

可借用 self-contained fact 改写：wiki 条目里的每个事实公理应能脱离上下文独立判断，避免“他”“该机构”“同年”等隐式指代。`F1@K` 可扩展为条目质量函数：事实无错是 precision，条目达到主题所需最小事实集是 recall。

## 可落地的测试项

- self-contained 改写测试：把含代词、省略、时间指代的句子改写成独立事实后再验证。
- relevant/irrelevant 分流：检查模型闲聊、拒答、跑题事实是否不进入 factuality precision。
- 多轮证据查询测试：同一事实允许多次检索，但每次 query 必须与待查事实相关。
- `F1@K` 长答案评分：同时报告 supported facts、not-supported facts、precision、recall@K、F1@K。
- 重复事实防刷：对重复或近重复 supported facts 去重后再算 recall。
- 受限语料 SAFE：把搜索接口替换为 ragbench 的检索器，判断事实是否被本地知识库支持。
