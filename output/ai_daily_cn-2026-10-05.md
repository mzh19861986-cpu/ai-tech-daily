# 技术日报（中文版）- 2026-10-05

> 由 AI Agent 自动生成并翻译 | 共 5 条

## 📌 综合

### 1. [用植物基材料替代石油基产品（2025）](https://onlinelibrary.wiley.com/doi/10.1002/eng2.70108)
*hackernews*
This 2025 research review examines advances in replacing petroleum-based products with plant-based materials. Its core value lies in: it systematically reviews practical substitution options for bio-based materials in packaging, chemicals, textiles, and other fields, and compares cost, performance, and carbon footprint. If you follow sustainable supply chains or materials innovation, this report can help you determine which plant-based alternatives are nearing the commercialization tipping point and which are still at the laboratory stage.

### 2. [在消费级硬件（RTX 4090）上以100T/s运行Qwen 3.8 Flash Next（125B）](https://github.com/Niko1221/Strata)
*hackernews*
Through quantization plus inference optimization, someone managed to fit the 125B-parameter Qwen 3.8 Flash Next large model onto a single RTX 4090 (24GB VRAM), while still achieving an inference speed of 100 tokens/second. The notable point is that models of this size previously required multi-GPU A100/H100 clusters to run, but now consumer-grade GPUs can perform inference smoothly—meaning the barrier to local deployment of large models has dropped significantly again, which is a practical signal for people who want to run private models themselves without spending a lot of money on servers.

### 3. [关闭之后，一个动画材料的数字档案库在网上出现](https://filmstories.co.uk/news/tippett-studios-in-the-wake-of-its-closure-a-digital-archive-of-animated-materials-appears-online/)
*hackernews*
An online digital archive of animation materials has emerged, containing a large collection of animation production materials that might previously have been scattered or lost. Its emergence directly responds to the recent closure of a certain animation institution, meaning that original materials once at risk of being lost now have publicly accessible backups. For researchers and enthusiasts, this is a rare, freely accessible entry point to primary sources.

### 4. [我们把原版《毁灭战士》移植到了SQL。](https://cedardb.com/blog/sqldoom/)
*hackernews*
有人把1993年的原版《毁灭战士》引擎移植进了SQL数据库，让游戏逻辑通过SQL查询来驱动运行。有意思的地方不在于性能——它慢得离谱——而在于这证明了SQL这种声明式查询语言图灵完备到足以承载一个完整的实时3D游戏循环，是一次对“数据库能干什么”这个边界的硬核试探。

### 5. [一次由交换空间引发的40毫秒Go垃圾回收暂停](https://frn.sh/go-gc/)
*hackernews*
作者发现他的 Go 服务偶尔出现 40ms 的 GC 暂停，深入排查后，根本原因并非 GC 本身，而是系统内存不足导致 swap——GC 需要访问的内存页被换到了磁盘上，造成访问延迟急剧上升。这个案例的价值在于：GC 暂停时间不仅取决于 GC 算法，还受操作系统层面的内存管理影响，排查性能问题时不应只关注应用层。

---
*本报告由 AI Agent 自动抓取公开信息并翻译生成，仅供参考。*