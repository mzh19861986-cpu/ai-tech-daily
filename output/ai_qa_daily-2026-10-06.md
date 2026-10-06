# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: EmbeddingGemma 2: An open, lightweight multimodal embedding model？

**A:** Google 发布了 EmbeddingGemma 2，一个开源的多模态嵌入模型，主打轻量级部署，能把文本和图像映射到同一向量空间。值得关注的是它体量小、可本地跑，同时保持多模态检索能力——这意味着在设备端做图文混合搜索、RAG 应用的门槛又低了一截，不用再依赖大模型 API。

📎 更多阅读：[EmbeddingGemma 2: An open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)

## Q2: OpenTPU – An open-source AI accelerator, developed by AI？

**A:** OpenTPU 是一个完全开源的 AI 加速器项目，由 AI 自主设计完成——从架构到 RTL 代码均由 AI 生成，人类只做验证。这意味着芯片设计的门槛被大幅拉低：以往需要资深团队数月完成的工作，现在 AI 可以独立产出可用的硬件设计。

📎 更多阅读：[OpenTPU – An open-source AI accelerator, developed by AI](https://github.com/FeSens/openTPU)

## Q3: Claude Code’s suggested message feature: I think the real customer is the model？

**A:** Claude Code 新增了「建议消息」功能——在模型等待用户输入时，主动弹出几条它自己生成的候选回复。作者的观点很犀利：这个功能表面上是帮用户省打字，真正的受益者其实是模型本身，因为用户越来越倾向于直接点选模型预设好的方向，等于让模型间接引导了对话走向。值得关注的是，这标志着 AI 工具设计的一个微妙转向：优化对象从「人的体验」悄悄变成了「模型的信息输入质量」。

📎 更多阅读：[Claude Code’s suggested message feature: I think the real customer is the model](https://www.zohaib.cc/blog/smartest-claude-code-feature)

## Q4: Email Self Hosters - what are you using?？

**A:** 有人在讨论自建邮件服务器用什么方案，发帖人目前用 **maddy**（一个轻量级、单二进制文件的邮件服务）托管多个域名的邮箱和 catch-all 地址。核心痛点是 iOS 原生邮件客户端连他的服务器特别慢，这其实是自建邮件最典型的坑——移动端兼容性和连接体验往往比服务端功能本身更折磨人。如果你也在考虑自建邮箱，这篇讨论值得围观，能提前看到大家踩过的雷。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## Q5: A sustainable web career, for when all this blows over？

**A:** 这是一个关于如何构建可持续网络职业生涯的讨论帖。核心观点大概是：与其追逐每一个技术风口，不如培养那些能穿越周期的底层能力和职业策略，让自己在行业动荡时依然站得稳。

📎 更多阅读：[A sustainable web career, for when all this blows over](https://dbushell.com/2026/10/07/sustainable-web-career/)

---
*有问题想问？欢迎在 GitHub 提 Issue~*