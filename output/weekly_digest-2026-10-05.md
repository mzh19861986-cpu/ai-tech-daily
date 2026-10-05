# 📊 每周技术精选周报 - 2026-10-05

> 由 AI Agent 自动汇总整理 | 共 5 条精选

## 🎯 本周概览

- 精选内容：5 条
- 数据来源：Hacker News / Lobsters / ArXiv / GitHub Trending
- 生成时间：2026-10-05

## 📝 精选内容

## 📌 综合

### 1. [Replacement of petroleum based products with plant-based materials (2025)](https://onlinelibrary.wiley.com/doi/10.1002/eng2.70108)
*hackernews*
植物基材料替代石油基产品的进程在2025年明显提速，从包装、纺织到化妆品原料都在出现可规模化落地的方案。值得关注的原因是：它不再只是环保概念，而是成本、性能和供应链三重压力下，企业主动选择的替代路径。

### 2. [Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s](https://github.com/Niko1221/Strata)
*hackernews*
有人在单张 RTX 4090（24GB 显存）上跑起了 125B 参数的 Qwen 3.8 Flash Next，速度达到 100 tokens/s，关键手段是极端的量化压缩加显存优化调度。这事值得关注的点在于：它进一步打破了「大模型必须上多卡 A100/H100 集群」的固有印象，让消费级显卡也能跑百亿级以上的旗舰模型。如果你手上有 4090，这套方案基本意味着可以本地跑一个接近云端体验的大模型。

### 3. [In the wake of closure, a digital archive of animated materials appears online](https://filmstories.co.uk/news/tippett-studios-in-the-wake-of-its-closure-a-digital-archive-of-animated-materials-appears-online/)
*hackernews*
日本动画公司GAINAX（《新世纪福音战士》制作方）2018年破产后，一批原属该公司的动画制作素材近日以数字档案形式在互联网上流出，涵盖分镜、原画、设定稿等原始资料。值得关注的是，这些本可能随公司清算永久消失的一线创作痕迹，如今以未经官方授权的方式重见天日——对研究者是珍贵史料，对版权方则是灰色地带，也再次提醒业界：日本动画的工业档案保存长期依赖民间自发，系统性缺失严重。

### 4. [We ported the original Doom to SQL](https://cedardb.com/blog/sqldoom/)
*hackernews*
有人把 1993 年的原版《Doom》移植进了 SQL 数据库——不是模拟器套壳，而是用 SQL 查询来驱动游戏逻辑和渲染，让数据库引擎直接跑起这款经典射击游戏。值得关注的是它把「SQL 到底能干什么」这个问题推到了荒诞又硬核的边界：原本用于增删改查的语言被拿来处理实时游戏循环，既是对数据库计算能力的极限测试，也是一次相当好玩的工程恶作剧。

### 5. [A 40ms Go garbage collector pause caused by swap](https://frn.sh/go-gc/)
*hackernews*
Go 的 GC 暂停被拉长到 40 毫秒，罪魁祸首竟是 swap——当进程内存被换出到磁盘，GC 需要重新触碰这些页时就会触发缺页中断，把本该微秒级的暂停拖慢了几个数量级。值得关注的是，这提醒我们在容器内存限制紧张、或宿主机内存吃紧的环境里，光调 GC 参数没用，得先关掉 swap 或给足内存。


---
*本周报由 AI 自动汇总生成，精选自公开技术社区。*