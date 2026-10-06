# ❓ 每日 AI 问答 - 2026-10-06

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: OpenTPU – An open-source AI accelerator, developed by AI？

**A:** OpenTPU 是一个完全开源的 AI 加速器项目，由 AI 自主设计开发——从架构到 RTL 代码全部开放，你可以直接拿来流片或做研究。值得关注的点在于：它探索了「AI 设计硬件」这条路是否可行，如果跑通，芯片迭代速度可能从年缩短到周，对硬件创业和学术圈都是低成本试错的新选项。

📎 更多阅读：[OpenTPU – An open-source AI accelerator, developed by AI](https://github.com/FeSens/openTPU)

## Q2: The smartest Claude Code feature is not for its users？

**A:** Anthropic给Claude Code加了个新功能，但它的目标用户其实不是写代码的人——而是让Claude自己用。简单说，这是在让AI学会用工具给自己搭梯子，而不是等人来喂提示词。值得关注的地方在于：当AI开始为自己优化工作流，工具的设计逻辑就从「方便人操作」转向了「方便AI自主执行」，这可能是agent进化的一条分水岭。

📎 更多阅读：[The smartest Claude Code feature is not for its users](https://www.zohaib.cc/blog/smartest-claude-code-feature)

## Q3: Email Self Hosters - what are you using?？

**A:** 最近有人在讨论自建邮件服务器用什么方案，楼主自己用的是 maddy，跑多个域名的邮箱和 catch-all 收信。目前遇到的小毛病一半是自己配置问题、一半不明来源，最头疼的是 iOS 原生邮件客户端连接慢得让人抓狂。

说白了就是：如果你也想摆脱大厂邮箱、自己托管邮件，maddy 是个轻量选择，但移动端体验可能会劝退——这类自建方案的通病，值不值得折腾得看你有多在意数据主权。

📎 更多阅读：[Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)

## Q4: A sustainable web career, for when all this blows over？

**A:** 科技行业裁员潮和AI冲击之下，有人开始讨论“可持续的Web职业”这条路该怎么走——核心思路是降低对单一雇主的依赖，靠个人品牌、独立产品和社区积累来构建更抗风险的职业模式。值得关注是因为它聊的不是“怎么卷赢”，而是“怎么不被淘汰出局”，对当下焦虑的技术人来说是个务实的方向参考。

📎 更多阅读：[A sustainable web career, for when all this blows over](https://dbushell.com/2026/10/07/sustainable-web-career/)

## Q5: Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery？

**A:** 这篇论文提出了一个叫 ADSD（自动诊断与技能发现）的框架，专门解决一个尴尬现状：AI 能写科学计算代码，但写出来的数值求解器性能差，它能告诉你「跑得不好」，却说不清「为什么差」和「怎么改」。ADSD 的价值在于把「执行反馈」升级成了「可归因的诊断 + 可复用的技能积累」，让 AI 从「会写代码」往「会改进算法」迈了一步。

如果你关注 AI for Science 或自动化科研，这篇值得留意——它触到的是当前 agent 能力的一个真实天花板：能执行，但不真懂优化。

📎 更多阅读：[Training Numerical Intelligence via Auto-Diagnosis and Skill Discovery](https://arxiv.org/abs/2610.03872)

---
*有问题想问？欢迎在 GitHub 提 Issue~*