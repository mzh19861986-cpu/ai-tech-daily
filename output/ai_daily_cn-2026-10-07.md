# 技术日报（中文版）- 2026-10-07

> 由 AI Agent 自动生成并翻译 | 共 5 条

## 📌 综合

### 1. [Janet在x32平台：32位指针，64位速度，内存占用减少25%](https://alexalejandre.com/programming/lisp/janet-for-the-x32-abi/)
*lobsters*
The Janet programming language now supports the x32 ABI, achieving 64-bit speed with 32-bit pointers while also reducing memory usage by 25%. For scenarios that run many small objects and are constrained by memory bandwidth (such as embedded systems or high-density services), this is a quite practical optimization—saving a quarter of memory without sacrificing performance.

### 2. [那年我和一个偷笔记本电脑的小偷共事 (2025)](https://blog.pipetogrep.org/2025/07/27/that-time-i-worked-with-a-laptop-thief/)
*lobsters*
这其实是一篇个人回忆文章，作者讲述了自己曾和一名偷笔记本电脑的人共事、后来才发现的经历。值得一读之处在于，它提醒我们：技术团队里坐在你旁边的同事，背景可能完全不是你以为的那样——对做背景审查和团队信任建设的人尤其有参考价值。

### 3. [Brut，Unix工具的残酷路由器](https://brut.sh)
*lobsters*
Brut 是一个面向 Unix 工具的“暴力”路由器——它能把任意命令行工具包装成 HTTP 接口，省去为每个小工具单独写 Web 服务的麻烦。值得关注是因为它延续了 Unix“小工具组合”的哲学，让 curl、jq 这类命令行程序直接变成可远程调用的 API，特别适合快速搭建内部工具或原型。

## 🤖 AI / 大模型

### 1. [一份可持续的网络职业生涯，待这一切风波平息之后](https://dbushell.com/2026/10/07/sustainable-web-career/)
*lobsters*
这条讨论来自 Lobste.rs 社区，主题是「如何打造一份可持续的 Web 开发生涯」。它值得关注的点在于：当 AI 冲击、行业裁员和框架内卷让很多人焦虑时，这篇文章/讨论串试图给出一个更长期主义的视角——不是追热点，而是想清楚什么样的技能组合和职业选择能穿越周期。

### 2. [自建邮件服务器的朋友们，你们都在用什么？](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)
*lobsters*
For self-hosted mail servers, the more actively discussed options in the community right now are maddy, Mailcow, Mail-in-a-Box, and docker-mailserver. The original poster used maddy, which is lightweight, a single binary, and simple to configure, but complained that the native iOS Mail client connects slowly. This is usually an issue with IMAP IDLE not being enabled or with the TLS handshake/certificate chain, so troubleshooting in that direction is more practical than switching software.

The core trade-off when choosing a self-hosted mail solution is this: all-in-one distributions (Mailcow comes with a full web panel and anti-spam) are worry-free but resource-hungry, while single-binary solutions (maddy, docker-mailserver) are lightweight but require you to handle SPF/DKIM/DMARC and IP reputation yourself. Another unavoidable reality is that if the sending IP has no warm-up and no PTR record, the probability of landing in spam is far higher than the problem of receiving mail.

---
*本报告由 AI Agent 自动抓取公开信息并翻译生成，仅供参考。*