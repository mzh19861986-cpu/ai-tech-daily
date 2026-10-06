# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: Sharing AI Progress in Mathematics？

**A:** OpenAI 分享了 AI 在数学领域的进展，重点展示模型在形式化证明和数学推理上的能力突破。这值得关注，因为数学是检验 AI 深度推理的硬标准——能做好数学，意味着 AI 在逻辑严谨性上迈了一大步，而不只是会聊天。

📎 更多阅读：[Sharing AI Progress in Mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/)

## Q2: EmbeddingGemma 2: An open, lightweight multimodal embedding model？

**A:** 谷歌开源了 EmbeddingGemma 2，一个约 3 亿参数的多模态嵌入模型，能把文本和图像映射到同一向量空间，直接在自己的设备上跑。值得关注的是它把多模态检索的门槛压到了消费级硬件，开发者做本地搜索、RAG 或跨模态匹配时不必再依赖云端 API。

📎 更多阅读：[EmbeddingGemma 2: An open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)

## Q3: OpenTPU – An open-source AI accelerator, developed by AI？

**A:** OpenTPU 是一个完全开源的 AI 加速器项目，由 AI 自动生成设计代码，目标是在 FPGA 上实现可复现、可修改的 TPU 类硬件。它值得关注的地方在于：把 AI 芯片设计流程本身交给 AI 来做，同时全部开源，让个人开发者也能研究和定制专用推理加速器，而不只是停留在论文层面。

📎 更多阅读：[OpenTPU – An open-source AI accelerator, developed by AI](https://github.com/FeSens/openTPU)

## Q4: Claude Code’s suggested message feature: I think the real customer is the model？

**A:** Claude Code 新增了一个「建议消息」功能，会在你输入时主动提示下一句可以说什么——表面上是帮你写 prompt，实际上是在用你的反馈数据训练模型更懂怎么跟人协作。值得关注的点在于：这标志着 AI 编程工具从「被动响应」转向「主动引导」，产品设计的真正目标用户可能不是人，而是模型本身。

📎 更多阅读：[Claude Code’s suggested message feature: I think the real customer is the model](https://www.zohaib.cc/blog/smartest-claude-code-feature)

## Q5: Email Self Hosters - what are you using?？

**A:** 一、总结
有人在技术社区发帖讨论自建邮件服务器的方案，楼主目前用的是 maddy 这个开源邮件服务，管理多个域名下的邮箱和 catch-all 收信，但遇到了 iOS 原生邮件客户端连接极慢的恼人问题。

二、为什么值得关注
自建邮件服务器一直是"技术自由"和"运维噩梦"之间的拉扯。maddy 这类轻量方案降低了门槛，但邮件协议本身的复杂性意味着客户端兼容性、连接速度这类坑很难完全绕开。如果你也在考虑摆脱 Gmail/Outlook 自建邮箱，这条讨论里的实战经验——尤其是踩过的坑——会比官方文档更有参考价值。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

---
*有问题想问？欢迎在 GitHub 提 Issue~*