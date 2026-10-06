# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 4 条

## 技巧 1

**The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?**

✨ 这篇论文想知道：能不能用大语言模型批量分析企业年报，从中提取出公司如何披露自己应对AI风险的真实信号。研究团队对9,821份年报跑了一套可复现的两阶段分类流程，试图把「AI风险披露」变成可量化、可比较的数据。

值得关注的是，它把AI治理研究从理论讨论拉到了实证层面——如果年报披露真能反映企业的AI应对态度，那监管者、投资者和研究者就多了一个低成本、大规模的观察窗口，而不必依赖企业自愿的问卷调查或零散的案例研究。

📎 [阅读原文](https://arxiv.org/abs/2610.02281)

## 技巧 2

**We Open Sourced Our Web Crawler. Here's How to Run a Node.**

✨ cl0q 把自己的网页爬虫开源了——你可以直接看代码、跑一个节点，参与共建开放网络的索引。它目前已经爬了 3850 万个域名，算是一个真正独立的搜索引擎，有自己的爬虫和索引，而不是套壳别人的结果。值得关注的点在于：主流搜索引擎从不告诉你它爬了什么、怎么排序、拿数据干了什么，而 cl0q 试图把这件事摊开来做。

📎 [阅读原文](https://dev.to/cl0qsearch/we-open-sourced-our-web-crawler-heres-how-to-run-a-node-145)

## 技巧 3

**How to extract every image from a web page: srcset, lazy loading and tracking pixels (Python & JS)**

✨ 这篇文章讲的是如何从现代网页中提取**真正的图片**——因为光抓 `<img src>` 会漏掉大量内容，你拿到的可能全是缩略图、占位符和网站图标，而主图根本不在那。

值得关注的点在于：现代网页把真实图片藏在 `srcset`（多分辨率候选）、懒加载（图片地址延迟注入）和追踪像素（伪装成图片的监控代码）里，普通爬虫看不见。作者给出了 Python 和 JS 的可用代码，并附上了自己踩过的坑。如果你做过图片抓取却总抓不全，这篇能直接省掉你排查半天的功夫。

📎 [阅读原文](https://dev.to/sstempresarial/how-to-extract-every-image-from-a-web-page-srcset-lazy-loading-and-tracking-pixels-python-js-2ikk)

## 技巧 4

**How to Write Your First Agent Skill**

✨ Anthropic 在 Claude Code 里推出了 **Agent Skills**——本质是把你的"家规"（提交信息格式、代码审查清单、会议记录模板）从剪贴板搬进一个 Agent 会自动加载的文件里，从此不用每次开新会话就重新粘贴一遍。它解决的不是模型记忆问题，而是**指令存放位置**的问题：与其靠每次开场白式的叮嘱（到第十条消息就被遗忘），不如让规则成为持久化、可复用的技能模块。

📎 [阅读原文](https://dev.to/alapha888/how-to-write-your-first-agent-skill-ab6)

---
*每天一个小技巧，一年就是 365 个进步~*