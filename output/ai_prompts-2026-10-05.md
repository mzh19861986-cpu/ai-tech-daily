# ✨ 每日 AI Prompt 技巧 - 2026-10-05

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章没有提供足够的实质内容来提炼 Prompt 技巧。它只有一个指向 Lobste.rs 讨论帖的链接（"Claude Says"），没有正文、评论或任何关于 AI 使用的建议。

如果你能提供该讨论帖的完整内容或核心观点，我可以帮你提炼出可用的 Prompt 技巧或最佳实践。**

📎 来源：[Claude Says](https://ohhfishal.net/Posts/claude)

## 2. 💡 技巧 2

**这篇文章没有涉及 Prompt 工程或 AI 使用技巧，内容是一篇关于 flow matching 约束采样的学术论文摘要。

如果你需要，我可以根据这篇论文的主题（生成模型在约束下采样），帮你写一个用于向 AI 解释或讨论该论文的 Prompt 模板。**

📎 来源：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## 3. 💡 技巧 3

**从这篇论文中可提炼的 AI 使用最佳实践：

**为高频、类型固定的小决策（如选模型、选工具、判断相关性/注入）使用"单次前向传播 + 类别概率"的系统1式小模型，而非每次都调用完整 LLM；但对每个这类快速模型做配对且自审计的评估，以验证其在真实 harness 中的可靠性。**

一句话即：让快模型处理快决策以省成本/延迟，同时用严格评估（配对比较 + 自审计）换取可验证的证据。**

📎 来源：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## 4. 💡 技巧 4

**这篇文章本身并不是在讲 Prompt 技巧，但它展示了一个非常实用、可直接复用的技巧：**用“两阶段分类流水线”而不是让模型一步到位地做复杂判断**。

**技巧：先用 LLM 做粗筛/打标签，再对筛选出的内容做精细分类。**

比如这个研究里处理近万份年报时，没有直接让模型一次性回答“这家公司如何披露 AI 风险与应对”，而是拆成两步——先（可能是关键词或模型）筛出与 AI 相关的段落/报告，再用 LLM 对这些内容做**

📎 来源：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## 5. 💡 技巧 5

****技巧：让 AI 先“比较”再“行动”**

在需要多步工具调用的长任务中，不要只让 AI 直接执行，而是让它先对候选的下一步动作进行对比评估（如比较不同选择的价值/预期效果），再决定执行哪一个。这样可以提供比只看最终结果更精准的逐步反馈，改善长链条任务的决策质量。**

📎 来源：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*