# ✨ 每日 AI Prompt 技巧 - 2026-10-06

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章没有提供具体的 Prompt 技巧或 AI 使用建议。它讲的是 JetBrains 首次出现净亏损的财经新闻，与 Prompt 工程无关。如果你有包含实际 Prompt 方法或 AI 使用建议的文章，我可以帮你提炼。**

📎 来源：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## 2. 💡 技巧 2

**这篇文章主要讨论 AI 自主设计推理硬件的进展，并没有涉及具体的 Prompt 技巧或 AI 使用建议，因此无法提炼出可直接使用的 Prompt 最佳实践。**

📎 来源：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## 3. 💡 技巧 3

**这篇文章的核心发现是：当你直接问 AI 模型“这段代码是恶意的吗”，模型会滑向道德判断而非技术分析，容易给出模糊或过度谨慎的答案。

**可用的 Prompt 技巧：**

> 不要直接问模型“这是不是恶意的/有害的”，而是让它做**具体的技术特征分析**。例如：“逐行分析这段代码的功能，指出它访问了哪些资源、执行了哪些网络/文件操作、是否存在常见的恶意模式（如混淆、提权、数据外传），不要做道德评判。”

**为什么有效：****

📎 来源：[Ask a model if code is malicious and it reaches for its morals](https://www.manifold.security/blog/do-models-consider-morality-malware)

## 4. 💡 技巧 4

**这篇文章主要是关于自托管邮件服务器的讨论，没有涉及 AI Prompt 技巧或 AI 使用建议。**

📎 来源：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## 5. 💡 技巧 5

**这篇文章没有提供可操作的 Prompt 技巧，但其核心思想可转化为一个最佳实践：**当 AI 生成的代码/方案表现不佳时，不要只让它"重试"，而应引导它先诊断失败的根本原因，再据此总结出可复用的技能或策略。** 即用"先诊断、后改进"的两步提示代替单纯的错误反馈循环——例如先问"这段代码为什么性能差、根因是什么"，再让它"基于该诊断提炼一条可复用的改进规则"。**

📎 来源：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*