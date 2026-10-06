# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: AI is now capable of developing its own inference hardware？

**A:** AI现在能自己设计推理芯片了——不是辅助优化，而是从架构探索到版图生成全流程自主完成。这意味着硬件迭代的瓶颈正从人类工程师的带宽，转移到算力和算法的自我进化速度上。当AI开始为自己造芯片，算力增长的飞轮可能比我们预想的转得更快。

📎 更多阅读：[AI is now capable of developing its own inference hardware](https://github.com/FeSens/openTPU)

## Q2: JetBrains reported a net financial loss first time in its tracked history？

**A:** JetBrains 首次出现净亏损，打破了公司自成立以来持续盈利的纪录。这家以 IntelliJ IDEA、Kotlin 和 Fleet 闻名的开发工具厂商，此番转亏主要受 AI 研发投入加大和订阅增长放缓的双重挤压。值得关注的是，连长期稳健的「开发者工具印钞机」都开始承压，说明 AI 正在重写整个 IDE 赛道的成本结构和竞争规则。

📎 更多阅读：[JetBrains reported a net financial loss first time in its tracked history](https://www.helgilibrary.com/companies/jetbrains)

## Q3: Email Self Hosters - what are you using?？

**A:** 有人讨论自建邮件服务器用什么方案，楼主目前在用 maddy 管理多个域名的邮箱和 catch-all，整体能用但体验不够顺滑——最大的痛点是 iOS 原生邮件客户端连接慢到让人抓狂。

值得关注的是这个问题并非个例：自建邮件服务器的难点往往不在收发本身，而在客户端兼容性、IMAP 连接性能这些"最后一公里"体验上。如果你也在折腾自建邮箱，maddy 是个轻量选择，但要接受它和主流客户端磨合时的粗糙感。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## Q4: Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery？

**A:** 这篇论文提出了 ADSD 框架，让 AI 智能体能自己诊断数值求解器"跑得不好"的根本原因，并自动发现可复用的改进技巧。关键在于它跳出了"能跑就行"的代码生成逻辑，把执行反馈从"报错/没报错"升级为"哪里弱、怎么修"——这对那些需要精度和性能的数值计算场景（比如科学仿真、工程求解）是个实质性突破。

📎 更多阅读：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

## Q5: Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities？

**A:** 这篇论文提出了一个叫「Proxy Confidence」的审计方法，用一个小型开源代理模型（surrogate）的 token 对数概率，来间接判断黑盒 LLM agent 即将执行的动作是否可能出错。值得关注的地方在于，它瞄准了一个真实痛点：GPT-4、Claude 这类前沿 API 不返回 token 概率，agent 自己说的置信度在关键错误上几乎等于瞎猜，而重复采样也没用（因为前沿模型太确定性了），所以这个「曲线救国」的思路算是填了个实用空白。

📎 更多阅读：[Proxy Confidence: Auditing Black-Box LLM Agents with a Surrogate's Log-Probabilities](https://arxiv.org/abs/2610.03894)

---
*有问题想问？欢迎在 GitHub 提 Issue~*