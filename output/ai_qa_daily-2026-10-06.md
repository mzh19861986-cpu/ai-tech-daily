# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: AI is now capable of developing its own inference hardware？

**A:** AI 现在能自己设计推理芯片了——不是辅助优化，而是从架构到电路层面自主完成设计。这意味着硬件迭代的瓶颈可能从「人不够聪明」变成「算力够不够跑设计循环」，芯片行业的节奏会被彻底改写。

📎 更多阅读：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## Q2: JetBrains reported a net financial loss first time in its tracked history？

**A:** JetBrains 首次出现净亏损，打破了公司有记录以来的持续盈利纪录。亏损主因是 AI 编程工具（如 Cursor、GitHub Copilot）的冲击，以及其自研 AI 助手推进缓慢，导致核心 IDE 订阅增长承压。对开发者来说，这意味着 JetBrains 可能被迫加速 AI 功能整合或调整定价策略，未来一两年是观察其能否守住专业 IDE 阵地的关键窗口。

📎 更多阅读：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## Q3: Email Self Hosters - what are you using?？

**A:** 折腾自建邮件服务器的人都懂，这玩意儿比自建网站难伺候十倍。这位老兄用的是 maddy，一个轻量级的 Go 语言邮件服务器，能管多域名和 catch-all 邮箱，但最大的痛点是 iOS 原生邮件客户端连接慢得让人抓狂。如果你也在考虑自建邮件，maddy 值得一试，但做好跟客户端兼容性斗争的准备。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## Q4: Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery？

**A:** 训练AI写代码已经不够了——这项研究让AI学会「诊断自己写的数值求解器哪里出错，然后自己补上缺失的技能」。核心思路是：光靠运行报错只能发现性能差，但看不出根因；ADSD框架把「诊断问题」和「发现所需技能」拆成两步，让AI能自主定位算法缺陷并针对性提升。价值在于：科学计算类代码的自动优化长期依赖人类专家调参，这套方法朝着「AI自己debug自己的算法」迈了一步，对自动化科研工具链有实际意义。

📎 更多阅读：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## Q5: Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities？

**A:** 这篇论文提出了一种「代理置信度」方法，用一个可访问log-prob的替代模型（surrogate）来审计黑盒LLM代理的每一步行动——当替代模型对黑盒模型输出的关键决策（工具调用、代码执行等）给出低置信度时，就标记为可能出错的风险点。

值得关注的原因在于：前沿API不暴露token概率，模型自报的置信度在关键错误上几乎等于瞎猜，反复采样又因为模型输出高度重复而没用——这等于给「已经执行完才发现错了」这个安全痛点提供了一个不依赖模型内部访问的检测思路。

📎 更多阅读：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

---
*有问题想问？欢迎在 GitHub 提 Issue~*