# FACTS Leaderboard：多维事实性与 grounding 排行榜

> 来源：literature/papers/markdown/facts-grounding-2512.10791.md
> 说明：这是中文精读笔记，不是全文翻译。

## 一句话定位

FACTS Leaderboard 把事实性拆成 Multimodal、Parametric、Search、Grounding 四个子榜，并用公开/私有集与自动 judge 维护可持续 leaderboard。

## 研究问题

单一事实性 benchmark 容易只覆盖一种能力：有的模型善于读上下文，有的善于闭卷事实问答，有的善于搜索或多模态理解。论文的问题是如何建立一个更全面、能持续区分前沿模型的事实性套件，同时降低 leaderboard 过拟合。

## 评测对象与任务设置

FACTS suite 包含四个子任务。Multimodal 要求模型回答图像相关事实问题，并结合视觉 grounding 与世界知识。Parametric 是 closed-book factoid QA，评估模型参数中的稳定世界知识。Search 要求模型使用统一搜索 API 回答困难问题。Grounding v2 要求模型只依据给定长文档和用户请求生成长回答。

## 指标与评测方法

总分 FACTS Score 是四个子任务 accuracy 的平均，每个子任务又分别报告细项指标和置信区间。Multimodal 使用人工 rubric，将关键事实分 Essential 和 Non-Essential，由自动 judge 给 Coverage 与 No-Contradiction。Parametric 聚焦单一、原子、稳定事实，judge 判断答案是否正确。Search 用 gold response 和自动 rater 将回答判为 correct、incorrect 或未尝试，并报告 accuracy、attempted accuracy、hedging rate、平均搜索次数等。Grounding v2 用两个 judge LLM 判断完整回答是否 grounded；若任一信息性 claim 不被上下文支持，则为 not accurate。

Grounding v2 还有 eligibility 调整：只说空泛但不违背文档的短回答会被判 ineligible，并在最终 factuality score 中视为 inaccurate。这避免模型用“少说少错”刷 grounding 分。

## 数据集/标注/实验设计

排行榜采用公开集与私有集，公开便于外部参与，私有降低过拟合，评测由 Kaggle 执行。Search 数据约 1884 题，分 Hard Tail、Wiki Two-Hop、Wiki Multi-Doc、KG Hops，强调长尾、多跳、难以一次搜索命中的问题，并统一使用 Brave Search API。Grounding v2 复用 v1 prompts：长文档最长约 32k tokens，覆盖金融、技术、零售、医疗、法律等企业场景，任务包括 QA、总结、改写，并明确禁止外部知识。

## 主要发现

四个子榜测到的能力差异明显，单一榜单不能代表整体事实性。Search 中高分模型不一定搜索最多，说明工具使用质量比次数更重要。Grounding v2 的 judge 模型与 prompt 更新会显著影响可靠性，因此论文用人工 held-out 集比较 judge/prompt 组合，并选择宏平均 F1 更好的设置。总体榜单顶部模型平均准确率仍有明显提升空间。

## 局限与风险

自动 judge 本身有模型偏置和误判风险，尤其可能偏向自身模型输出；论文用双 judge 缓解但不能消除。FACTS 不覆盖所有事实性场景，如视频、快速变化信息、知识库工具调用。总分平均可能掩盖子能力差异，因此应用时应优先看子榜和错误类型。

## 对本仓库 ragbench 的启发

ragbench 不应只有一个总准确率；至少应拆为 closed-book baseline、retrieval/search、context grounding、回答完整性/eligibility。Grounding 的“全回答任一信息性 claim 不支持即失败”适合高风险 RAG；同时需要 eligibility 防止模型只输出空泛安全话术。公开/私有 split 也可用于防止 prompt 过拟合。

## 对“公理化 LLM wiki”论文的可借用点

可借用多维事实性框架：公理化 wiki 不只是“条目是否被文档支持”，还包括参数知识、检索知识、多模态证据、工具证据的来源差异。Grounding v2 的 eligibility 概念可转化为条目充分性公理：完全不出错但遗漏用户/主题要求的核心内容，不能算高质量 wiki 条目。

## 可落地的测试项

- Grounding strictness：长回答中任一信息性 claim 无上下文支持，则样例失败。
- Eligibility gate：回答过短、空泛、未满足用户指定格式或要点，即使无错误也判不合格。
- Context-only 测试：明确禁止外部知识，构造上下文与常识冲突样例，检查模型是否服从上下文。
- Search tool parity：所有被测模型使用同一检索/搜索接口，记录调用次数与最终正确率。
- 多跳检索题：答案必须综合两个以上文档，不能由单个 chunk 直接得到。
- 公私集分离：保留一批私有 ragbench 样例只用于最终回归，公开集用于开发调参。
