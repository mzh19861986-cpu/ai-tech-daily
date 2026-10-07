# 📊 每周技术精选周报 - 2026-10-07

> 由 AI Agent 自动汇总整理 | 共 5 条精选

## 🎯 本周概览

- 精选内容：5 条
- 数据来源：Hacker News / Lobsters / ArXiv / GitHub Trending
- 生成时间：2026-10-07

## 📝 精选内容

## 📌 综合

### 1. [Janet on x32: 32-bit Pointers, 64-bit Speed, 25% Less RAM](https://alexalejandre.com/programming/lisp/janet-for-the-x32-abi/)
*lobsters*
Janet 语言现在跑在 x32 ABI 上：指针还是 32 位，但能用到 64 位 CPU 的寄存器和指令，结果是内存占用比标准 64 位构建少了约 25%，速度却没打折扣。对嵌入式或内存敏感场景来说，这是用更少 RAM 换几乎不损失性能的实用选择。

### 2. [That Time I Worked With a Laptop Thief (2025)](https://blog.pipetogrep.org/2025/07/27/that-time-i-worked-with-a-laptop-thief/)
*lobsters*
这篇文章讲的是作者在2025年的一段奇特经历：他曾与一名偷笔记本电脑的人共事，揭露了IT行业中一个不太光彩的现实——有些公司或个人会通过灰色渠道获取设备，而技术人员往往在不知情的情况下参与其中。

### 3. [Brut, the Brutal Router for Unix Tools](https://brut.sh)
*lobsters*
Brut 是一个 Unix 风格的请求路由器，让你用 shell 命令而非脚本代码来定义 HTTP 路由——每条路由本质上就是一个可执行程序，请求进来就触发对应进程。值得关注是因为它把 Unix 的「小工具组合」哲学搬到了 Web 服务层：不用起 Node/Python 框架，几行 shell 就能拼出一个正经的 HTTP 服务，特别适合内部工具和轻量 API。

## 🤖 AI / 大模型

### 1. [A sustainable web career, for when all this blows over](https://dbushell.com/2026/10/07/sustainable-web-career/)
*lobsters*
这篇来自 Lobste.rs 的讨论聚焦一个越来越多人关心的问题：Web 开发这份职业怎么做得长久、做得不烧尽自己。核心观点大概率是——别把全部赌注押在某一波技术浪潮上，而要积累可迁移的底层能力和可持续的工作节奏，等技术泡沫破了你还站得住。对当下被 AI 和框架迭代搞得焦虑的开发者来说，值得一读。

### 2. [Email Self Hosters - what are you using?](https://lobste.rs/s/rwloew/email_self_hosters_what_are_you_using)
*lobsters*
有人在社区问“自建邮件服务器你们都用什么”，楼主自己用的是 maddy——一个支持多域名、能配 catch-all 的全能型邮件服务端。他吐槽 iOS 原生邮件客户端连它特别慢，暗示这个问题可能是 maddy 的兼容性坑。如果你也在自托管邮箱，这条帖子值得蹲一下评论区，看看大家都在用什么方案绕开这类客户端兼容问题。


---
*本周报由 AI 自动汇总生成，精选自公开技术社区。*