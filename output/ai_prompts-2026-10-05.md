# ✨ 每日 AI Prompt 技巧 - 2026-10-05

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章没有涉及 Prompt 工程内容，以下是关于如何更好使用 AI 的建议总结：

**核心思路：让 AI 在生成过程中“轻干预”，而非“硬约束”。**

MintFlow 的启示是，当你要求 AI（如生成模型）满足某些硬性条件时，强行施加约束会让输出严重偏离其原本擅长的分布，导致质量下降。更好的做法是对生成轨迹做**最小化的定向干预**——只在关键节点微调方向，让输出自然落到满足约束的区域，而不是每一步都强行拉拽。类比到 Prompt 实践中：与其**

📎 来源：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## 2. 💡 技巧 2

**从这篇文章中提炼的 Prompt 技巧：

**让模型在一次前向传播（single forward pass）中输出类别概率来做快速决策，而不是每次都调用完整的 LLM**——对于"该调哪个模型、该用哪个工具、检索文本是否相关、输入是否含注入攻击"这类小而有类型化的判断，用轻量的 System-1 决策模型替代昂贵的 LLM 调用，可大幅节省成本与延迟。

一句话建议：**把高频、简单、可枚举的分类判断交给快速小模型（给出概率即可），只在需要深度推理时才调用大模型**

📎 来源：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## 3. 💡 技巧 3

**这篇内容主要是学术研究摘要，没有直接讲 Prompt 技巧，但它的方法本身可以提炼成一个可复用的 AI 使用实践：

**用 LLM 处理大规模文本时，采用“两阶段分类流水线”（two-stage classification pipeline）：先粗筛、再精分，而不是让模型一步到位完成复杂分类。**  

这样做的好处是：每一阶段任务更单一、判断标准更明确，能显著提高可复现性和分类准确率，尤其适合成千上万份文档的批量分析。**

📎 来源：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## 4. 💡 技巧 4

**这篇文章主要讲的是长程工具调用智能体的强化学习信用分配问题，并非典型的 Prompt 技巧内容。不过可以从其核心思想提炼一个可迁移的实践建议：

**让 AI 在长序列任务中"先比较、再行动"：在每一步决策前，让模型显式对比几个候选动作的相对价值（哪个更优、优多少），而不是只看最终结果。** 这能把稀疏的终局反馈转化为逐步的、有指向性的引导，显著提升长链条工具调用任务的可靠性。

换句话说：与其让模型一口气跑完整个流程再看成败**

📎 来源：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

## 5. 💡 技巧 5

****技巧提炼：** 让 AI Agent 将「推理/动作生成」与「完成判断」拆分为两个独立步骤或角色，而不是让同一个策略同时负责执行和决定任务何时结束。

**效果：** 这样可以防止 Agent 在未真正完成任务时“声称完成”并提前终止，减少错误在流程中的传播。**

📎 来源：[DeReAct: Decomposed Reasoning and Acting for Reliable AI Agents](https://arxiv.org/abs/2610.02351)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*