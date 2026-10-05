# ✨ 每日 AI Prompt 技巧 - 2026-10-05

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章讨论的是 Claude 的一个有趣现象或技巧，但没有提供具体的文章内容。基于标题和上下文，我无法提炼出明确的 Prompt 技巧。

**建议：** 如果你能提供文章的具体内容（讨论中关于 Claude 的实际对话或技巧），我可以帮你提炼出可用的 Prompt 最佳实践。

从现有信息看，唯一可总结的 AI 使用建议是：**在分享或讨论 AI 输出时，附上完整的上下文和对话内容，而不是只给一个标题链接**——这样他人才能真正理解、复用其中的 Prompt 技巧。**

📎 来源：[Claude Says](https://ohhfishal.net/Posts/claude)

## 2. 💡 技巧 2

**这篇文章没有直接讨论 Prompt 技巧，但提供了一个可迁移的 AI 使用原则：**在约束生成时，优先采用“最小干预”策略——只对轨迹中必要的部分进行微调，而非从头重塑或强力约束整个生成过程。** 对应到 Prompt 使用中，就是若已有满意的输出，应尽量用最少的补充指令或局部修正来满足新约束，避免重写整个提示词导致原始风格或信息丢失。**

📎 来源：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## 3. 💡 技巧 3

**这篇文章的核心建议可以提炼为一个 Prompt 实践：

**让"快思考"模型（小模型/单次前向）只负责可打分的类型化判断（如选工具、判相关性、判是否注入），并把概率输出作为筛选信号；关键决策再用"慢思考"的 LLM 复核。**

即：用低成本模型做高频小决策的初筛，保留概率校准与成对自审（paired self-audit）机制来校验其可靠性，而非直接信任其结论。**

📎 来源：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## 4. 💡 技巧 4

**这篇讨论的核心其实是一个**可复现的两阶段分类流水线**思路，而非直接讲 Prompt 写法。可以提炼为：

**技巧：面对大规模文本分类任务时，采用"两阶段提示"策略——第一阶段用 LLM 做粗筛/初分类，第二阶段再对初筛结果做精分类/校验，并在每一步固定提示词与流程以保证可复现性。**

这样既能降低单次提示的复杂度、提高准确率，也让整个分析过程可重复、可扩展（如该研究对 9,821 份年报的处理）。**

📎 来源：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## 5. 💡 技巧 5

****技巧：让 AI 在行动前先做"比较式价值评估"**

在规划多步工具调用时，不要只让 AI 评估"这一步好不好"，而是让它对多个候选动作进行**两两/相对比较**再择优执行——即在"行动之前"先估计各候选步骤的相对价值，从而在长流程中获得更精准的反馈信号。**

📎 来源：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*