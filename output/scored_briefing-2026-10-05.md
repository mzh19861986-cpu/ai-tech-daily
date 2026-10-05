# 🏆 AI 热度排行榜 Top 10 - 2026-10-05

> 由 AI 自动打分排序 | 共 5 条入选

## 🥇 Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s  (⭐ 7.0/10)
🔗 [hackernews](https://github.com/Niko1221/Strata)

有人把阿里 Qwen 3.8 Flash Next（125B 参数）塞进了单张 RTX 4090，还能跑到 100 tokens/秒。关键是靠量化 + 优化的推理框架把 125B 这种「数据中心级」模型压进了消费级显存，意味着本地跑大模型的门槛又低了一截。

## 🥈 Replacement of petroleum based products with plant-based materials (2025)  (⭐ 5.0/10)
🔗 [hackernews](https://onlinelibrary.wiley.com/doi/10.1002/eng2.70108)

全球越来越多的企业开始用植物基材料替代传统石油基产品——从生物塑料包装到植物纤维纺织品，这背后是成本下降、环保法规收紧和消费者偏好转变三股力量的叠加。值得关注的是，这不再是小众实验：2025年多个品类的植物基替代品在性能和价格上已接近甚至持平石油基产品，意味着大规模商用替代的拐点可能正在到来。

## 🥉 We ported the original Doom to SQL  (⭐ 5.0/10)
🔗 [hackernews](https://cedardb.com/blog/sqldoom/)

有人把 1993 年的初代《毁灭战士》跑在了 SQL 数据库里——不是模拟，是让数据库引擎真的执行游戏逻辑、渲染画面并响应用户输入。这听着像行为艺术，但背后其实是个硬核证明：现代关系型数据库的计算能力已经强到能当通用图灵机用，顺带也让人重新审视「数据库到底该干什么」这条边界。

## 4. A 40ms Go garbage collector pause caused by swap  (⭐ 5.0/10)
🔗 [hackernews](https://frn.sh/go-gc/)

Go 的垃圾回收器理论上能做到亚毫秒级暂停，但有人踩到了一个 40ms 的坑——罪魁祸首是 swap。当系统内存紧张、部分 Go 进程的内存被换到磁盘上时，GC 需要扫描这些页面就会触发磁盘 I/O，暂停时间直接爆炸。这提醒我们：跑 Go 服务的机器上，swap 该关就关，别让 GC 被磁盘拖后腿。

## 5. In the wake of closure, a digital archive of animated materials appears online  (⭐ 4.0/10)
🔗 [hackernews](https://filmstories.co.uk/news/tippett-studios-in-the-wake-of-its-closure-a-digital-archive-of-animated-materials-appears-online/)

日本动画制作者协会（JAniCA）在官网关闭后，上线了一个动画素材数字档案馆，收录了大量原画、分镜和制作资料。值得关注的是，这些资料此前仅对业内人士开放，如今普通观众也能免费查阅，对研究日本动画工业和保存创作史料都有实际意义。

---
*热度分由 AI 模型评估，仅供参考。*