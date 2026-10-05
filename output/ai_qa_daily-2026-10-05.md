# ❓ 每日 AI 问答 - 2026-10-05

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: Claude Says？

**A:** 这个链接指向 lobste.rs 上关于「Claude Says」的讨论帖，具体内容我无法直接读取（链接只给了评论区入口，没有正文）。如果你能把原文或截图发过来，我可以帮你提炼成两三句有信息量的总结。

📎 更多阅读：[Claude Says](https://ohhfishal.net/Posts/claude)

## Q2: MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching？

**A:** Flow matching 模型生成能力很强，但下游任务常要求样本满足观测值、物理定律等硬约束，现有约束采样器一加强约束就会把样本推离预训练分布，生成质量跟着掉。这篇 MintFlow 的做法是只对生成轨迹做「最小干预」，用最小的改动让样本满足约束，从而在约束达标和保持原始分布之间少做取舍。对做科学计算、逆问题或任何需要「带约束生成」的人来说，这是直接冲着痛点去的思路。

📎 更多阅读：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## Q3: Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses？

**A:** 这篇论文给「小模型替代大模型做 Agent 决策」这个热门思路泼了盆冷水。作者系统评估了 System-1 决策模型（单次前向传播输出类别概率）在 Agent 框架各类小决策上的表现，发现速度优势明显，但证据质量跟不上——配对实验和自我审计揭示了性能与可靠性之间的落差。值得关注是因为它直接质疑了「用小快模型省钱省延迟」的工程直觉，给正在搭 Agent 系统的人提了个醒：别只看 benchmark 分数，审计要跟上。

📎 更多阅读：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## Q4: The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?？

**A:** 这篇论文问了一个很实际的问题：企业年报里关于AI的披露，能不能被用来衡量社会面对AI冲击的韧性？作者用一套可复现的两阶段LLM分类流程，处理了9,821份年报，试图把散落在财报里的AI表态变成可量化、可比较的信号。

值得关注的点在于方法本身——它展示了一条规模化挖掘企业文本的路径，把原本无人细读的年报变成政策研究和社会韧性分析的原料。对做AI治理、ESG或公司信息披露研究的人来说，这可能是新数据源的起点。

📎 更多阅读：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## Q5: Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents？

**A:** 这篇论文给长周期工具调用智能体提出了一种“先比较再行动”的价值估计方法，解决的是LLM在多步工具调用中「最终奖励难以归因到具体步骤」的老问题。通过对候选动作做相对价值比较而非绝对打分，它能在不依赖密集人工标注的情况下实现更精准的步级信用分配——这对构建真正能稳定完成复杂多步任务的Agent是个关键拼图。

📎 更多阅读：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

---
*有问题想问？欢迎在 GitHub 提 Issue~*