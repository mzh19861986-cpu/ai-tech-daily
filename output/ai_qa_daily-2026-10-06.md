# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: AI is now capable of developing its own inference hardware？

**A:** AI现在能自己设计推理芯片了——不是写写RTL代码那种辅助，而是从架构探索到物理实现全流程自主完成。值得关注的是，这意味着AI开始参与优化自己运行的底层硬件，形成「AI设计AI芯片」的闭环，长期看可能让专用推理硬件的迭代速度甩开传统人力设计节奏。

📎 更多阅读：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## Q2: JetBrains reported a net financial loss first time in its tracked history？

**A:** JetBrains 首次出现净亏损，打破了其有记录以来的持续盈利纪录。这家以 IntelliJ IDEA、Kotlin 和 Fleet 闻名的开发工具厂商，此前一直被视为「不靠融资、靠订阅就能活得很滋润」的独立软件公司标杆。亏损本身值得关注，但更关键的是原因——是激进投入 AI 工具研发，还是订阅增长见顶，将决定这只是一次战略性亏损，还是整个开发者工具商业模式承压的信号。

📎 更多阅读：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## Q3: Email Self Hosters - what are you using?？

**A:** 有人问自建邮件服务器大家都在用什么方案，楼主目前用 maddy 管理多个域名的邮箱和 catch-all 转发，但遇到个很烦的问题——iOS 原生邮件客户端连接他的服务器要等很久。这类讨论值得关注，因为自建邮件服务器的难点从来不在「能不能搭」，而在于各家邮件客户端兼容性和反垃圾策略的坑。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## Q4: Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery？

**A:** 训练AI写代码和让AI真正改进算法是两回事——尤其在数值求解器领域，程序跑得慢或不准，执行反馈只能告诉你「有问题」，却说不出「为什么」和「怎么改」。这篇论文提出的 ADSD 框架，让AI智能体自己诊断数值求解器的性能瓶颈，并自动发现可复用的改进技能，相当于给AI装上了一套「自查+自学」的闭环系统。值得关注的点在于：它试图把AI从「代码生成器」升级为「算法优化者」，这对科学计算自动化是个关键跨越。

📎 更多阅读：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## Q5: Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities？

**A:** 给黑盒LLM代理做“体检”，不用拆开模型也能看出它哪步要出错——这篇论文的做法是：找一个能拿到token概率的替代小模型，让它跟着代理的每一步操作走，用替代模型的log-probabilities当“信心探针”来审计代理的可靠性。值得关注的是它戳中了一个真实痛点：前沿API不给概率、代理自称的置信度在关键错误上几乎等于瞎猜、而重复采样又因为模型输出太雷同而失效，替代模型路线等于绕开了这些封锁，给部署方一个可落地的监控抓手。

📎 更多阅读：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

---
*有问题想问？欢迎在 GitHub 提 Issue~*