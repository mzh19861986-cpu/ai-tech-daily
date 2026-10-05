# ✨ 每日 AI Prompt 技巧 - 2026-10-05

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章没有提供足够的正文内容，只有一个指向 Lobste.rs 讨论帖的链接。因此无法从中提炼出具体的 Prompt 技巧或 AI 使用建议。如果你能提供该讨论帖的具体内容，我可以帮你总结。**

📎 来源：[Claude Says](https://ohhfishal.net/Posts/claude)

## 2. 💡 技巧 2

**这篇文章没有可直接提取的 Prompt 技巧，因为它是一篇关于 flow matching 约束采样（constrained sampling）的学术论文，与 Prompt 工程无关。

如果硬要从"更好使用 AI"的角度总结：当预训练生成模型需要满足外部约束（如观测数据、物理规律）时，与其强行改写生成过程导致样本偏离原分布，不如采用"最小轨迹干预"的思路——只做必要的最小修正，以在满足约束的同时尽量保留模型原有能力。这一原则也可类比到 AI 使用中：对模型输出做最小必要的约束调整，比大**

📎 来源：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## 3. 💡 技巧 3

**从这项研究中可提炼的 Prompt 技巧：**让 AI 执行具体的"系统1"单次判断任务（如"这段文字是否相关""是否包含注入"）时，要求它直接输出类别概率或单一结论，而不要附加解释或推理步骤。**

这样能让轻量模型以单次前向传播完成决策，大幅降低成本和延迟，同时把复杂推理留给更强的模型处理。**

📎 来源：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## 4. 💡 技巧 4

****Prompt 技巧：**  
把“分析对象 + 输出标签体系 + 两阶段流程”明确写进 Prompt，并先让模型做粗分类、再做细分类，可显著提高大规模文本分类的一致性与可复现性。

**最佳实践：**  
在企业披露/长文档分析中，不要指望一次 Prompt 完成所有判断；应设计可复现的“两阶段分类流水线”（先粗筛、后细判），并把标签定义和步骤写死在提示词里。**

📎 来源：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## 5. 💡 技巧 5

****技巧：长流程工具调用任务中，让 AI 在每一步“先比较再行动”。**

具体做法：在 Agent 的每个决策步骤，不只让模型直接选下一个工具，而是要求它先对候选动作做**相对价值估计**（比较几个可选动作的预期收益），再据此选择——这样能提供比只看最终结果更精准的步级信号，缓解长链路中信用分配困难的问题。**

📎 来源：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*