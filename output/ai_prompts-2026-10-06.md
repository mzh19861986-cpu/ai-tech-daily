# ✨ 每日 AI Prompt 技巧 - 2026-10-06

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章目前没有提供具体内容，因此无法从中提炼 Prompt 技巧或 AI 使用建议。请你把文章正文或讨论内容贴出来，我就能帮你总结成可直接使用的 Prompt 最佳实践。**

📎 来源：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## 2. 💡 技巧 2

**这篇文章没有提供具体内容（只有标题），因此无法提炼 Prompt 技巧。不过，仅从标题看，它讲的是 JetBrains 首次出现净财务亏损，属于商业/财经新闻，并不涉及 AI 使用建议。

如果你把正文内容贴出来，我可以帮你从中提炼可直接使用的 AI Prompt 技巧或最佳实践。**

📎 来源：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## 3. 💡 技巧 3

**这篇文章主要讨论自建邮件服务器的工具选择，没有涉及 AI Prompt 技巧或 AI 使用建议，因此无法提炼相关内容。**

📎 来源：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## 4. 💡 技巧 4

**提炼出的 Prompt 技巧：

**让模型先诊断失败原因，再自主总结可复用的"技能"，而不是直接重写代码。**

即：当 AI 生成的方案（代码、求解器等）表现不佳时，不要只让它重试，而是分两步提示——① 先分析"为什么失败"（根因诊断），② 再把修复经验提炼成一条可复用的通用技能/规则，用于后续任务。

这一技巧的核心价值在于：单纯的执行反馈只能暴露"表现差"，却很少揭示"原因"和"改法"；通过显式**

📎 来源：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## 5. 💡 技巧 5

**# 提炼的 Prompt 技巧/最佳实践

**用"代理置信度"替代直接询问 AI 自评：** 当你无法获取黑盒模型的 token 概率时，不要依赖让模型口头表达"我有多确定"（这种自评几乎和瞎猜差不多），而是用一个你**能读取 log-probabilities 的开源替代模型（surrogate）**去复现同样的任务，用它输出的概率分布来审计原模型的行为。

**为什么这样做：** 前沿闭源 API 隐藏了 token 概率，且模型高度可重复、重**

📎 来源：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*