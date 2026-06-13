# 生成式搜索引擎的可验证性评测

> 来源：literature/papers/markdown/generative-search-verifiability-2304.09848.md
> 说明：这是中文精读笔记，不是全文翻译。

## 一句话定位

这篇论文提出 citation recall、citation precision 和 citation F1，用人工评测审计生成式搜索回答是否“每个外部世界断言都有来源支持，且每个引用真的支持对应断言”。

## 研究问题

生成式搜索会给用户一个流畅答案和行内引用，但引用可能只是可信外观。论文问两个问题：生成答案中的可验证断言是否都被引用充分支持；提供的引用是否真的支持它们所挂靠的句子。它把 verifiability 与 factuality 区分开：可验证性不保证事实绝对为真，但要求用户能从给定来源核查每条断言。

## 评测对象与任务设置

论文审计 Bing Chat、NeevaAI、perplexity.ai、YouChat 四个商业生成式搜索引擎。查询共 1,450 个，覆盖 12 个分布：AllSouls 开放论述题、davinci-debate、ELI5 KILT/Live、WikiHow 关键词，以及 Natural Questions 的多种答案形态。系统输出为带行内引用的单轮回答；未带行内引用的 ChatGPT/Bard 当时不纳入，因为可验证性天然很低或不可比。

## 指标与评测方法

citation recall 衡量可验证断言中有多少被其关联引用集合完整支持。citation precision 衡量生成引用中有多少支持其关联断言；若多个引用合起来完整支持一句话，部分支持的引用可计入 precision。citation F1 是 recall 与 precision 的调和平均。标注流程三步：先评 fluency/perceived utility；再过滤不需要引用的句子；最后判断每个引用对对应句子的支持关系，包括 full support、partial support、no support，并在多引用时判断引用集合是否联合支持。

## 数据集/标注/实验设计

标注由 34 名 MTurk 标注者完成，先通过资格测试和个性化反馈。每个带引用 query-response pair 约 4 分钟完成，抽样 250 对做三人复标，一致性超过 82% pairwise agreement 和 91.0 F1。查询设计刻意包含短答案、长答案、列表、表格、开放论述和实时 Reddit ELI5，以测试检索证据是否容易直接抽取。NeevaAI 有约 22.7% abstention，其他系统几乎都回答。

## 主要发现

回答通常看起来流畅有用，平均 fluency 约 4.48、perceived utility 约 4.50，但引用质量明显不足。总体只有 51.5% 生成断言被引用完整支持，只有 74.5% 引用支持其关联断言。系统间差异很大：perplexity.ai recall 最高约 68.7，NeevaAI 67.6，Bing Chat 58.7，YouChat 11.1；precision 则 Bing Chat 最高约 89.5，perplexity.ai 72.7，NeevaAI 72.0，YouChat 63.6。开放论述类查询 citation recall 特别低，因为网页往往没有可直接抽取的答案。论文还发现 citation precision 与 perceived utility 负相关，原因可能是高 precision 系统更常贴近或复制来源文本，但这些来源片段未必真正回答用户问题。

## 局限与风险

人工标注成本高，每个样本主评一次，虽然有复标估计一致性但无法完全消除主观差异。评测对象是 2023 年早期商业系统，结果不代表当前产品。citation recall 以句子为单位，句内多断言可能仍有粒度不足。可验证性不是事实性：一个断言被来源支持，不代表来源本身可靠或真实。

## 对本仓库 ragbench 的启发

ragbench 的 citation 评测要同时测“少引”和“乱引”：生成了事实却没引用是 recall 问题，引用挂错或不支持是 precision 问题。不能只检查答案后面是否有 citation id，也不能只看引用文档是否包含相关关键词。需要建立 statement-level 对齐：把回答拆成可验证断言，映射到一个或多个 evidence chunk，并判断联合支持、部分支持、无支持和矛盾。

## 对“公理化 LLM wiki”论文的可借用点

公理化 wiki 可以把每个 wiki 句子或事实 atom 视作 verification-worthy statement，要求有来源集合完整支持。citation recall 对应“条目中有多少事实命题有证据”，citation precision 对应“挂到命题上的来源是否真的支持该命题”。多引用联合支持的设计很适合 wiki：一个复杂断言可以由多个页面分别支持不同子属性，但需要明确哪些来源支持哪些 atom。

## 可落地的测试项

- statement-level citation recall：抽取回答中的外部世界断言，判断每条是否至少被一组引用完整支持。
- citation precision：逐个 citation 检查其是否 full/partial/no support 对应断言，避免“引用堆砌”。
- 联合证据支持：允许多个 chunk 合起来支持一个断言，但要求记录每个 chunk 支持的子断言。
- 引用错挂测试：提供含答案的文档 A 和相似无关文档 B，检查模型是否把 citation 挂到 A 而不是 B。
- 可用性-可验证性权衡：同时报告回答有用性、citation recall、citation precision，防止系统通过复制来源片段提高 precision 却降低回答质量。
