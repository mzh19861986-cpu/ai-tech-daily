# ✨ 每日 AI Prompt 技巧 - 2026-10-06

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章没有包含任何关于 AI 使用或 Prompt 工程的内容，它只是报道了 JetBrains 首次出现净财务亏损的新闻。

因此，无法从中提炼 Prompt 技巧或 AI 使用建议。如果你希望我基于这篇文章生成一个总结类的 Prompt（例如把新闻要点提取成结构化摘要），我可以帮你写一个，但严格来说那属于“为新闻写作设计 Prompt”，而不是文章本身提供的内容。**

📎 来源：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## 2. 💡 技巧 2

**这篇文章没有提供具体内容，因此无法提炼 Prompt 技巧或 AI 使用建议。如果你能补充文章正文或讨论内容，我可以帮你总结出可直接使用的 Prompt 工程实践。**

📎 来源：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## 3. 💡 技巧 3

**这篇文章本身没有涉及 Prompt 技巧，讨论的是自建邮件服务器（self-hosted email），因此没有可直接提炼的 Prompt 最佳实践。**

📎 来源：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## 4. 💡 技巧 4

****提炼的 Prompt 技巧：**

让 AI 先"诊断"再"解决"——即要求模型明确说出问题背后的**根本原因**及对应的**具体改进方向**，而不只是给出一个能跑通的结果。

**实践建议：** 在使用 AI 生成代码或方案时，不要只问"给我一个能工作的版本"，而要追问："这个结果为什么不够好？根本原因是什么？应该应用哪项具体技能/方法来改进？"这种"自动诊断 + 技能发现"的两步式提示，能把 AI 从"执行反馈"推进**

📎 来源：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## 5. 💡 技巧 5

****技巧：用“代理信心”替代模型自报信心。** 当你无法获取 LLM 的 token 概率时，不要依赖模型嘴上说的“我有把握/我不确定”，而是用一个可访问 log-probabilities 的替代模型（surrogate）对同一输出打分，把它的对数概率当作该行为的风险信号来触发审查。**

📎 来源：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*