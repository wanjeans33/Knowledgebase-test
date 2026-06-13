# FActScore：长文本事实精度的原子事实评测

> 来源：literature/papers/markdown/factscore-2305.14251.md
> 说明：这是中文精读笔记，不是全文翻译。

## 一句话定位

FActScore 将长文本拆成 atomic facts，再计算其中有多少被可信知识源支持，是 long-form factuality 精细评测的基础方法。

## 研究问题

长文本生成往往混合了正确、错误、无关和主观内容，整段二分类无法反映事实质量。论文要回答：如何用细粒度、可复现、可扩展的方式评估模型长回答的 factual precision，尤其是人物传记这类包含大量可查事实的文本。

## 评测对象与任务设置

任务是让模型生成某个人物 biography，并以英文 Wikipedia 作为知识源。评测只统计模型实际作答的响应，拒答单独记录。一个响应先被拆成多个 atomic facts；atomic fact 被定义为只承载一个信息点的短句，例如“某人是演员”“某人出演某作品”应分开。

## 指标与评测方法

FActScore 是被知识源支持的 atomic facts 占比。形式上，对每个响应 `y` 的原子事实集合 `A_y`，逐个判断 `a` 是否被知识源 `C` 支持，然后取平均；模型级得分是在非拒答样本上再平均。论文强调这是 factual precision，不衡量覆盖率/recall，也不衡量写得是否全面。

自动估计器也分两步：先生成 atomic facts，再验证每个 atomic fact。验证方法包括 no-context LM、retrieve-then-LM、非参数概率 NP，以及 retrieve-then-LM + NP ensemble。retrieve-then-LM 会从知识源检索相关 passage，把 passage、atomic fact 和 True/False 判断提示交给 evaluator LM；ensemble 只有两个方法都判 supported 才算支持，以降低过度支持。

## 数据集/标注/实验设计

人工评测采样 183 个 Wikidata 人物，让 InstructGPT、ChatGPT、PerplexityAI 生成传记。标注流程包括：采样实体、收集生成、拆 atomic facts、按 Wikipedia 标注 Supported/Not-supported/Irrelevant。论文报告人工标注成本高，一个生成约 4 美元，因为每篇包含约数十个原子事实。随后用人工数据校准自动估计器，并扩展评测 13 个模型的 6500 个生成。

## 主要发现

商业模型远未达到人类事实精度：早期结果中 InstructGPT、ChatGPT、PerplexityAI 的 FActScore 分别约为 42.5%、58.3%、71.5%。实体越冷门，得分越低；生成越靠后的位置，错误率越高，说明短答案评测低估了长文本中的后段幻觉。检索增强和 citation 并不自动保证 factual precision，PerplexityAI 中 supported 与 unsupported 句子都可能带引用。

自动估计方面，检索显著优于 no-context；但单独 retrieve-then-LM 可能过度判断 supported，NP ensemble 能缓和该问题。不同估计器在系统级排序上高度相关，但个体 atomic fact 仍可能错判。

## 局限与风险

论文主要研究人物传记和 Wikipedia，结论迁移到法律、医学、近期事件、专有知识库时需要重新定义知识源和支持标准。FActScore 默认所有 atomic facts 等权，这会忽略事实重要性差异。它只测 precision，不惩罚“少说但全对”的回答，也不衡量回答是否满足用户需求。

## 对本仓库 ragbench 的启发

ragbench 可以把长答案拆成 atomic facts 后再做 grounding，而不是只做整句或整段判断。对于 RAG，知识源不应是全网或 Wikipedia，而应是本次检索上下文或指定文档集合；标签也应表述为“被给定上下文支持”，避免混淆全球真实和上下文可证。

## 对“公理化 LLM wiki”论文的可借用点

atomic fact 很适合作为 wiki 条目的最小公理单元：每个条目可表示为原子事实集合，每个事实附带来源、支持状态和依赖关系。论文可借用“事实精度是原子事实支持率”的定义，同时补上重要性权重和覆盖率，形成更完整的公理质量指标。

## 可落地的测试项

- atomic fact extraction：检查一句多事实输出是否被拆成多个独立断言。
- context-supported FActScore：对每个 atomic fact 检索或匹配证据 chunk，标注 Supported/Not-supported/Irrelevant。
- 冷门实体测试：按实体频率或文档稀疏度分桶，比较事实精度。
- 位置衰减测试：按答案前/中/后段统计 atomic fact 支持率。
- citation 不等于支持测试：构造带引用但引用不支持的事实，防止只看 citation 存在。
- 拒答与少答记录：单独统计 abstention、facts per response、supported facts per response，避免高 precision 掩盖低覆盖。
