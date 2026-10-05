# ✨ 每日 AI Prompt 技巧 - 2026-10-05

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章是关于流匹配（flow matching）的约束采样技术，不涉及 Prompt 工程或 AI 使用技巧，因此没有可提炼的 Prompt 技巧或建议。**

📎 来源：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## 2. 💡 技巧 2

**这条内容并非 Prompt 技巧文章，而是一篇关于 LLM 智能体框架中"System-1 决策模型"（快速单次前向传播的分类模型）的学术论文摘要。若从中提炼对使用 AI 的启发，可总结为：

**最佳实践：把"快思考"和"慢验证"分层——对智能体的高频小决策（选模型、选工具、判断相关性/注入风险）用轻量快速模型，但需配套成对评估与自我审计来核查其可靠性，避免只图速度而牺牲证据质量。**

📎 来源：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## 3. 💡 技巧 3

**这篇文章没有直接给出可复用的 Prompt 写作技巧，但提供了一个可借鉴的 AI 使用思路：**用「两阶段分类流水线」处理大规模文本**——先做可复现的初筛分类，再对结果做二次精炼，从而从近万份年报中稳定提取出企业 AI 披露信号。启示是：面对海量材料时，把任务拆成「先粗筛、后精分」的流水线式 Prompt/工作流，比一次性让模型完成全部判断更可靠、更可复现。**

📎 来源：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## 4. 💡 技巧 4

****技巧提炼：**

在构建长周期工具调用的 AI Agent 时，与其只让模型在每一步"评估当前状态的绝对价值"，不如让它**对比多个候选动作的相对价值**再做决策——因为绝对价值估计在长链路中噪声大、信用分配弱，而比较式评估能把决策问题转化为"选哪个更好"，显著降低估计难度并提升长周期任务表现。

**一句话实践：** 当 Agent 需要连续多步调用工具时，在 Prompt 中让模型对候选动作进行两两/多项对比排序再选择，而不是让它**

📎 来源：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

## 5. 💡 技巧 5

****技巧提炼：** 将 AI Agent 的"推理"与"行动"解耦——用一个 LLM 负责思考并分解出下一步动作，用另一个独立的 LLM（或规则模块）来授权该动作是否执行、以及判断任务是否真正完成。

**一句话说明：** 不要让同一个模型"既当运动员又当裁判"，把动作提议、动作授权、完成判定拆成独立角色，能有效防止错误传播和"谎报完成"，提升 Agent 的可靠性。**

📎 来源：[DeReAct: Decomposed Reasoning and Acting for Reliable AI Agents](https://arxiv.org/abs/2610.02351)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*