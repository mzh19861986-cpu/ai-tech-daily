# ✨ 每日 AI Prompt 技巧 - 2026-10-06

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章没有提供具体内容，因此无法提炼 Prompt 技巧或 AI 使用建议。如果你能补充文章正文，我可以帮你总结其中可复用的提示词方法或最佳实践。**

📎 来源：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## 2. 💡 技巧 2

**这篇文章的核心建议是：**让 AI 自己设计/优化它自己的推理硬件，而不是直接手工做低层实现**。  
可提炼为一条 Prompt 技巧：**“先让模型自行提出硬件架构与优化目标，再给出约束条件让其迭代改进。”****

📎 来源：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## 3. 💡 技巧 3

**这篇文章的核心建议是：**用具体、可验证的问题替代开放式道德判断题，能显著提高 AI 回答的质量和可靠性。**

例如，不要问“这段代码是恶意的吗？”，而是问“这段代码是否包含文件删除、网络外连或权限提升等具体行为？”——把模糊的价值判断拆解为可客观回答的事实性问题，AI 会更少陷入笼统的道德表态，给出更有用的分析。**

📎 来源：[Ask a model if code is malicious and it reaches for its morals](https://www.manifold.security/blog/do-models-consider-morality-malware)

## 4. 💡 技巧 4

**这篇文章是关于自建邮件服务器的技术讨论，没有明显的 Prompt 工程内容。不过若要从中提炼关于如何更好使用 AI 的建议，可以总结为：

**在使用 AI 解决自建服务（如邮件服务器）问题时，应尽量提供完整的环境信息——包括你使用的具体软件（如 maddy）、遇到的具体症状（如 iOS 原生邮件客户端连接缓慢）以及你已经排查过的可能原因，这样 AI 才能给出精准而非泛泛的排错建议。****

📎 来源：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## 5. 💡 技巧 5

****技巧提炼**：在让 AI 改进数值算法（或任何代码）时，不要只给执行反馈（比如"跑得慢/报错了"），而要引导 AI 先做**自我诊断**——明确指出性能问题的**根本原因**，再让它**发现并调用对应的解决技能**来对症修复。

**一句话说明**：与其说"这段代码跑得不好，帮我优化"，不如说"先诊断这段数值求解代码性能差的根本原因是什么，再针对该原因提出并应用相应的解决技能"——把"执行反馈"升级为"**

📎 来源：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*