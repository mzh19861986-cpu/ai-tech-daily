# ✨ 每日 AI Prompt 技巧 - 2026-10-06

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章的核心建议是：**学会把 AI 当作自主的研究/开发代理，而不是逐步骤的助手**——给它一个高层次目标（如“为我的模型设计更高效的推理硬件”），让它自己规划、迭代和验证，你只负责设定目标与评估结果。

对应的 Prompt 技巧可以写成：**“目标委托式提示”**——只描述你要达成的最终目标和约束条件，不指定具体步骤，让模型自行分解任务、探索方案并自我验证。**

📎 来源：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## 2. 💡 技巧 2

**这篇文章没有提供具体内容，因此无法从中提炼 Prompt 技巧或 AI 使用建议。如果你能补充文章正文或讨论内容，我可以帮你总结成一条可直接使用的 Prompt 最佳实践。**

📎 来源：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## 3. 💡 技巧 3

**这篇文章没有明显的 Prompt 内容，主要讨论自托管邮件服务器方案。

其中关于更好使用 AI 的建议是：**在向 AI 提问时，应提供完整的上下文和具体需求，避免信息被截断或不完整**——因为原文内容在关键处中断，AI 无法给出准确判断，这也提醒我们：**输入给 AI 的信息越完整、越具体，得到的回答就越有价值**。**

📎 来源：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## 4. 💡 技巧 4

****技巧提炼：**  
让 AI 先根据执行反馈自动“诊断”问题原因，再显式提取并复用可迁移的解决技能，而不是只让它重试或直接改代码。

**为什么有效：**  
执行反馈只能告诉模型哪里失败了，不一定能让它理解失败原因；先做归因诊断、再总结成可复用技能，可以让后续改进更稳定，也更接近“真正提升算法”而不是碰运气修 bug。**

📎 来源：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## 5. 💡 技巧 5

****技巧：用代理模型的 log-probabilities 给黑箱 LLM Agent 做"自信度审计"**

既然前沿模型 API 隐藏 token 概率、自述置信度几乎等同于瞎猜、重复采样也无效，那就**训练/调用一个可访问输出概率的替代（surrogate）模型，从其 log-probabilities 中提炼出"代理置信度"信号**，用它在 Agent 真正执行工具调用、查询或代码前拦截那些"悄悄出错"的动作。

**实践要点：** 当无法直接获取目标模型的不确定性信息**

📎 来源：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*