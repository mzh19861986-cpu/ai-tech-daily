# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: JetBrains reported a net financial loss first time in its tracked history？

**A:** JetBrains 去年出现了有记录以来的首次净亏损，这家以 IntelliJ IDEA、Kotlin 和全家桶 IDE 闻名的公司，一直是自筹资金、不靠风投独立运营的「开发者工具标杆」。亏损本身不算惊人，但信号意义很强：连最稳的订阅制工具厂商都开始被 AI 编程助手（Cursor、Copilot 等）的冲击波扫到，值得关注它后续会不会调整产品线或定价策略。

📎 更多阅读：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## Q2: AI is now capable of developing its own inference hardware？

**A:** AI 现在能自己设计推理芯片了——不是辅助优化，而是从架构层面自主完成设计。这意味着硬件迭代不再完全依赖人类工程师的灵感，AI 可以针对特定模型反向定制专用芯片，把推理成本压到传统方案的零头。值得关注的是，一旦这条路跑通，模型和硬件会形成闭环加速，后来者追赶的窗口期可能比想象中更短。

📎 更多阅读：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## Q3: Ask a model if code is malicious and it reaches for its morals？

**A:** 研究发现，当你直接问大语言模型“这段代码是恶意的吗”，模型往往会调用它内置的道德判断而非纯粹的代码分析能力来回答。这意味着模型的安全对齐机制可能干扰其技术判断，让安全检测结果带上主观道德色彩，而非基于代码行为的客观评估。对于依赖AI做代码审计或恶意软件检测的团队来说，这提醒我们：模型的“道德感”未必等于准确率。

📎 更多阅读：[Ask a model if code is malicious and it reaches for its morals](https://www.manifold.security/blog/do-models-consider-morality-malware)

## Q4: Email Self Hosters - what are you using?？

**A:** 有人问自建邮件服务器该用什么方案，提问者目前用的是 **maddy**——一个轻量级的开源邮件服务器，能同时托管多个域名、支持 catch-all 收信。值得关注的点在于：maddy 配置相对简单、资源占用低，但遇到的实际痛点是 **iOS 原生邮件客户端连接极慢**，这也是不少自建玩家共同的槽点。如果你也在折腾自建邮箱，这类真实使用反馈比官方文档更有参考价值。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## Q5: Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery？

**A:** AI智能体能写出科学计算代码，但遇到数值求解器性能不佳时，传统的执行反馈只能告诉它“慢了”，却说不清“为什么慢、怎么改”。ADSD框架让智能体自己诊断问题根源并发现可复用的改进技能，相当于把“会写代码”升级成“会优化算法”。这意味着AI在科学计算领域从工具人向真正的问题解决者迈进了一步。

📎 更多阅读：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

---
*有问题想问？欢迎在 GitHub 提 Issue~*