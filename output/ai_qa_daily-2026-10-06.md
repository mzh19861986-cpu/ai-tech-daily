# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: JetBrains reported a net financial loss first time in its tracked history？

**A:** JetBrains 首次出现净亏损——这家做了 IntelliJ IDEA、PyCharm、WebStorm 等全家桶的捷克公司，一直是「卖工具也能活得很好」的样板。亏损本身不算大，但信号意义强：AI 编程助手正在重构开发者的付费习惯，单纯卖 IDE license 的模式可能到了天花板。

📎 更多阅读：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## Q2: AI is now capable of developing its own inference hardware？

**A:** AI现在能自己设计推理芯片了。这意味着硬件优化的迭代速度可能从「人类工程师按年算」变成「AI按天算」——模型和芯片协同进化的飞轮一旦转起来，算力成本的下降曲线会比我们过去习惯的陡得多。

📎 更多阅读：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## Q3: Email Self Hosters - what are you using?？

**A:** 社区在讨论自建邮件服务器的方案选择，楼主目前用 **maddy** 托管多个域名的邮箱和 catch-all 地址，但遇到 iOS 原生邮件客户端连接奇慢的问题，这是他最头疼的地方。

值得关注的点在于：自建邮件服务一直是「入门容易、用着糟心」的领域，maddy 以单文件、配置简洁著称，适合不想折腾 Postfix+Dovecot 那套老古董的人；但兼容性和客户端体验往往是这类轻量方案的软肋。如果你也在自建邮箱，这条讨论能帮你判断 maddy 的实际坑位，或找到更稳的替代方案。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## Q4: Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery？

**A:** 这篇论文提出了 ADSD 框架，让 AI 智能体不只是会写科学计算代码，还能自动诊断数值求解器性能不佳的根本原因，并从中提炼出可复用的优化技能。它的价值在于把「写代码」升级成了「改算法」——这对于让 AI 真正参与科学计算的核心创新，而不是只当个码农，是个关键一步。

📎 更多阅读：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## Q5: Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities？

**A:** 这篇论文提出了一种「代理置信度」审计方法：既然前沿 LLM API 不暴露 token 概率、模型自报的置信度又几乎等于瞎猜、重复采样也因模型输出高度重复而失效，那就用一个可访问 log-probabilities 的小型替代模型来充当「测谎仪」，间接判断黑盒大模型 agent 即将执行的动作是否可靠。

值得关注的点在于，它把「错误在动作执行后才暴露」这个部署痛点变成了一个可量化的预判问题——不碰黑盒本身，靠白盒替身就能提前拦截可疑的工具调用和代码。对正在把 agent 推上生产环境、又苦于没有可靠性护栏的团队来说，这算是一条挺实用的思路。

📎 更多阅读：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

---
*有问题想问？欢迎在 GitHub 提 Issue~*