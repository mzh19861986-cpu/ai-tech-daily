# ✨ 每日 AI Prompt 技巧 - 2026-10-06

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章没有涉及 Prompt 工程内容。它是一篇关于自建邮件服务器的讨论，作者分享了自己使用 maddy 管理多个域名邮箱的经验，并提到最大的困扰是 iOS 原生邮件客户端连接速度极慢。

如果你需要，我可以帮你把这类「用户求助帖」提炼成一个可复用的提问 Prompt 模板，例如在向 AI 咨询自建邮件方案时，附上使用场景、已用工具、遇到的具体问题等结构，这样更容易获得针对性建议。需要的话我可以直接写出来。**

📎 来源：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## 2. 💡 技巧 2

**这篇文章来自 Lobste.rs 的讨论，标题为《A sustainable web career, for when all this blows over》（当这一切平息后，一份可持续的 Web 职业）。由于提供的正文内容仅为指向讨论区的链接，没有实际的讨论文字，无法从中提炼具体的 Prompt 技巧或 AI 使用建议。**

📎 来源：[A sustainable web career, for when all this blows over](https://dbushell.com/2026/10/07/sustainable-web-career/)

## 3. 💡 技巧 3

****技巧提炼：** 让 AI 先诊断"为什么不行"，再让它总结"该怎么改"。

具体做法：当 AI 产出效果不佳时，不要只反馈"结果差"，而是要求它分两步输出——(1) 诊断导致失败的根本原因，(2) 从中提炼出一条可复用的通用技能/原则。这样能把一次性的执行反馈升级为可迁移的能力，避免反复修同一个坑。**

📎 来源：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## 4. 💡 技巧 4

****技巧提炼：**  
用“代理置信度”审计黑盒 LLM 智能体：让一个可访问对数概率的替代模型（surrogate）对同一输入生成工具调用/代码，比较其低概率 token 与主模型实际动作是否吻合，从而在动作执行前发现潜在错误，而非依赖主模型自报的置信度。  

**一句话最佳实践：**  
如果无法获取目标模型的 token 概率，就用一个开放/可读 log-prob 的替代模型“复现”同一任务；当替代模型在其输出上出现**

📎 来源：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

## 5. 💡 技巧 5

****技巧提炼：**  
在构建或评估使用工具的 AI Agent 时，除了测试工具调用能力，还要专门加入“拒绝有害请求”的安全测试用例，并明确要求模型在调用工具前先做安全判断。  

**一句话总结：**  
用工具增强 AI 能力的同时，别忘在 Prompt 或评测中加入“先判断是否应拒绝、再决定是否调用工具”的安全约束，否则模型可能因工具使用而降低对有害请求的拒绝率。**

📎 来源：[MLLMs Fail to Refuse when Using Tools Agentically](https://arxiv.org/abs/2610.03938)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*