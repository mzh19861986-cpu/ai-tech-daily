# 💡 每日开发技巧 - 2026-10-05

> 每天学一个实用技巧，效率慢慢提上来 | 共 4 条

## 技巧 1

**In the wake of Tippett Studios’ closure, a digital archive appears online**

✨ 曾参与《星河战队》《侏罗纪公园3》等视效制作的 Tippett Studios 关停后，一个线上数字档案开始浮出水面，试图保存这家老牌特效工作室的技术遗产与幕后资料。这类民间自发归档值得关注，因为大量早期 CG 与定格动画的原始资产往往随工作室倒闭而永久消失，而它们恰恰是理解当代视效工业演进的一手材料。

📎 [阅读原文](https://filmstories.co.uk/news/tippett-studios-in-the-wake-of-its-closure-a-digital-archive-of-animated-materials-appears-online/)

## 技巧 2

**The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?**

✨ 这篇论文问了一个很实际的问题：上市公司的年报里，能不能挖出企业如何应对AI风险的信号？作者用LLM对9,821份年报做了两阶段分类，试图把年报变成衡量「社会韧性」的可规模化数据源。

值得关注的点在于方法论：它把传统上零散、定性、难以比较的企业AI披露，转成了可复现、可批量分析的量化信号。如果这套管线站得住，意味着监管者、研究者和投资者可以不再依赖企业自说自话的公关稿，而是从强制披露的年报里读出更一致的AI风险图景——这对评估整个社会对AI冲击的准备程度，是个低成本的新入口。

📎 [阅读原文](https://arxiv.org/abs/2610.02281)

## 技巧 3

**Who Changed My Site Property? The OutSystems Service Center Trick You Should Know**

✨ 在OutSystems的生产环境里，站点属性（Site Property）被改动往往比代码改动更难排查——代码有版本记录，但配置的变更常常查无实据。Service Center里其实藏着一个查看属性的修改历史入口，能告诉你谁改的、什么时候改的、改前是什么值。下次遇到"应用没动过但行为变了"的情况，先别翻代码，去这里看看配置的时间线。

📎 [阅读原文](https://dev.to/engkerollosadel/who-changed-my-site-property-the-outsystems-service-center-trick-you-should-know-5aep)

## 技巧 4

**Building and using MCP servers: 4 things I learned**

✨ MCP（模型上下文协议）是一个开放标准，让 AI 应用能通过统一的接口连接外部工具和数据，服务方只需封装一次，所有支持 MCP 的 AI 客户端都能调用。作者在实际用 Claude Code 接入 Upwork 官方 MCP 服务器、并给自己的开源工具 doceval 写了 MCP 服务器之后，总结了四条踩坑经验。值得关注是因为 MCP 正在成为 AI 工具集成的通用接口，理解它的实际运作方式能帮你少走弯路。

📎 [阅读原文](https://dev.to/dave8172/building-and-using-mcp-servers-4-things-i-learned-4agj)

---
*每天一个小技巧，一年就是 365 个进步~*