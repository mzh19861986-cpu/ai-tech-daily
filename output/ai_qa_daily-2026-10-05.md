# ❓ 每日 AI 问答 - 2026-10-05

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: Claude Says？

**A:** Anthropic 给 Claude 加了个「Claude Says」功能，本质上是一个更主动的交互提示机制，会在对话中引导用户发现模型的能力边界和使用方式。

目前公开信息很有限，只知道它在 lobste.rs 上引发了讨论。如果你在用 Claude，值得留意它是否已经开始在你的对话里出现——这可能是 Anthropic 在交互层面做差异化的一个信号。

📎 更多阅读：[Claude Says](https://ohhfishal.net/Posts/claude)

## Q2: MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching？

**A:** 做可控生成的研究者常遇到一个两难：想让 flow matching 模型的输出满足约束（比如物理规律或观测数据），但硬加约束又容易把样本推离预训练分布，生成质量掉得厉害。MintFlow 的思路很取巧——不重构整个采样轨迹，只做「最小干预」，在关键时刻微调路径，让样本既满足约束又不跑偏。如果你在做人像修复、科学仿真或任何「带约束的生成」任务，这个方法值得扫一眼，因为它解决的正是约束与保真度之间那个老大难。

📎 更多阅读：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## Q3: Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses？

**A:** 这篇论文关注的是 LLM Agent 框架里的「系统1决策模型」——也就是用一次前向传播直接输出类别概率，来判断该调哪个模型、用哪个工具、检索内容是否相关、输入是否含注入攻击，理论上比调用完整 LLM 省时省钱得多。作者做了一套配对且自审计的评测，想验证这类快速决策到底靠不靠谱——换句话说，它戳中了「省钱提速」和「证据是否充分」之间的矛盾，对正在搭 Agent 基础设施的人值得一读。

📎 更多阅读：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## Q4: The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?？

**A:** AI风险观测站（AI Risk Observatory）尝试用大语言模型批量分析9821份企业年报，从中提取公司如何披露自身对AI的应对，从而为"社会韧性"研究提供可用的数据信号。这项研究值得关注的地方在于：它把企业年报这种原本用于财务披露的文本，重新定义为观察AI社会影响的可规模化数据源，并给出了一套可复现的两阶段分类流程——如果这条路走得通，未来监管者和研究者就能用同样方法追踪企业在AI风险上的真实态度，而不只是听它们PR怎么说。

📎 更多阅读：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## Q5: Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents？

**A:** 这篇论文关注的是长周期工具调用智能体的一个核心痛点：当 LLM 需要连续调用几十个工具完成任务时，最终只看结果给奖励，很难判断中间哪一步做对了、哪一步走偏了。作者提出了一种「先比较、再行动」的相对价值估计方法，让智能体在每一步决策前先比较候选动作的相对价值，而不是等任务结束才回头归因。对做 Agent 系统的人来说，这意味着长链路任务的训练信号可以更精准，不必再依赖昂贵的人工逐步标注。

📎 更多阅读：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

---
*有问题想问？欢迎在 GitHub 提 Issue~*