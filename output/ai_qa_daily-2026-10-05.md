# ❓ 每日 AI 问答 - 2026-10-05

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: Claude Says？

**A:** 这篇文章讨论的是 Claude 的一个有趣现象：当用户以特定方式提问时，Claude 会输出「Claude Says」这类固定格式的回应，引发社区对模型行为模式的讨论。值得关注的点在于，这暴露了 LLM 可能存在的隐藏提示词或训练数据中的模式痕迹，对理解模型实际行为与预期行为的偏差有参考价值。

📎 更多阅读：[Claude Says](https://ohhfishal.net/Posts/claude)

## Q2: MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching？

**A:** MintFlow 提出了一种「最小轨迹干预」方法，让 flow matching 模型生成样本时能满足观测约束或物理定律等硬性要求。它的巧妙之处在于：不像现有约束采样器那样用强力手段把样本硬拽到合规区域（代价是严重偏离预训练分布），而是只对生成轨迹做最小幅度的修正，在合规和保真之间取得更好的平衡。对于需要「既遵守规则、又保持生成质量」的扩散/流匹配应用来说，这是个值得留意的思路。

📎 更多阅读：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## Q3: Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses？

**A:** 这篇论文给"用小模型替代LLM做Agent决策"这个思路泼了盆冷水：作者设计了一套配对+自审计的评估方法，专门测试那些单次前向传播就能给出分类概率的"System-1"决策模型（比如判断该调哪个工具、检索内容是否相关、输入是否含注入攻击）。

结论是标题里的那句话——模型跑得快，但证据站不住：这些小模型在速度上确实有优势，可一旦用严格的配对评估去检验，它们在Agent真实决策场景里的可靠性远不如预期。对正在搭Agent harness、考虑用轻量分类器省钱省延迟的团队来说，这是个值得先读再动手的信号。

📎 更多阅读：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## Q4: The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?？

**A:** 这项研究用 LLM 批量分析了 9,821 份公司年报，搭建了一个「AI 风险观测站」，试图从企业公开披露中提取它们如何应对 AI 风险的信号。值得关注的是，它把年报这种枯燥的合规文件变成了衡量社会韧性（societal resilience）的数据源——如果这套方法可复现，监管者和研究者就能低成本地追踪企业对 AI 风险的真实反应，而不只是听它们在 ESG 报告里的漂亮话。

📎 更多阅读：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## Q5: Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents？

**A:** 这篇论文针对长周期工具调用智能体的信用分配难题，提出了一种「行动前先比较」的价值估计方法，让模型在执行每一步工具调用前就对候选动作做相对价值评估，而不是等最终结果出来才回溯打分。它的价值在于：长链路任务中最终奖励太稀疏、步级奖励又难获取，而对比式估计绕开了对绝对奖励的依赖，为智能体的中间决策提供了更可行的训练信号。

📎 更多阅读：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

---
*有问题想问？欢迎在 GitHub 提 Issue~*