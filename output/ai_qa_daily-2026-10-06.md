# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: Erdosproblems.com Succumbs to the AI Onslaught？

**A:** 一位数学家把上千个未解数学猜想挂上网，用AI自动筛选哪些“有戏”——结果AI一口气标记出上百个可能可攻克的难题，直接把这个手动整理的清单资源站冲垮了。这事值得关注是因为，它第一次大规模展示了AI在纯数学前沿的“选题能力”：不是替人证明，而是替人找到最值得下手的靶子。

📎 更多阅读：[Erdosproblems.com Succumbs to the AI Onslaught](https://www.erdosproblems.com/forum/thread/blog:9)

## Q2: Email Self Hosters - what are you using?？

**A:** 这条帖子是自建邮件服务器的用户在讨论用什么方案，原帖主目前用 **maddy**（一个轻量开源的邮件服务器）给自己的多个域名搭邮箱和 catch-all 收件。他最大的痛点是在 iOS 原生邮件客户端上连接特别慢。

如果你也想摆脱 Gmail 这类大厂、自己托管邮件，这类真实用户的踩坑经验比官网文档更值得参考——尤其是移动端兼容性，往往是自建邮件最容易翻车的地方。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## Q3: A sustainable web career, for when all this blows over？

**A:** 这篇来自 Lobste.rs 的讨论帖聚焦一个被忽视的话题：如何把 Web 开发当作一份能长期做下去的职业，而不是靠熬夜和内卷撑着的短期冲刺。它值得关注，因为在这个裁员频繁、技术迭代极快的行业里，「可持续」本身就是稀缺能力——帖子从工作节奏、技能选择到心态管理给出了具体建议，适合每个想在这行干得久一点的人看看。

📎 更多阅读：[A sustainable web career, for when all this blows over](https://dbushell.com/2026/10/07/sustainable-web-career/)

## Q4: Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery？

**A:** 这个叫ADSD的框架想让AI智能体不只是"写出能跑的代码"，而是真正改进数值求解算法本身——关键在于它能自动诊断性能问题的根因，并发现可复用的解题技能，而不只是靠执行反馈知道"结果不好"。值得关注的是，它切中了当前AI写科学代码的一大短板：能跑通，但不懂为什么慢、怎么改好。

📎 更多阅读：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## Q5: Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities？

**A:** 这篇论文提出了一种用「代理模型」审计黑盒 LLM Agent 的方法：既然前沿 API 不暴露 token 概率，就用一个可访问 log-probabilities 的替代模型去估算原模型的置信度，从而在错误动作真正执行前把它拦下来。

值得关注的点在于，它正面回应了 Agent 落地最棘手的问题——模型自报的置信度在关键错误上几乎等于瞎猜，而重复采样对高度确定性的前沿模型毫无帮助。如果这套代理置信度真能在真实工具调用场景里稳定预警，那它可能成为 Agent 上生产环境的一道必要安全网，而不只是又一篇 benchmark 论文。

📎 更多阅读：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

---
*有问题想问？欢迎在 GitHub 提 Issue~*