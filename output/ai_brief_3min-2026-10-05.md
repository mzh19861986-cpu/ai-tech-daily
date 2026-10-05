# ⚡ 3 分钟 AI 快讯 - 2026-10-05

> 每天 3 条最重要的 AI 新闻，3 分钟看完

**1. Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s**

   有人把 125B 参数的 Qwen 3.8 Flash Next 塞进单张 RTX 4090，还跑出了 100 tokens/s 的生成速度。关键在于它不是靠 INT4 暴力量化换速度，而是用了一种混合精度 + 分层卸载的策略，把大部分权重留在显存、只把少量层扔给 CPU——这意味着消费级显卡跑百亿...

**2. In the wake of Tippett Studios’ closure, a digital archive appears online**

   蒂皮特工作室（Tippett Studios）倒闭后，一个数字档案网站上线，整理并公开了这家曾参与《星球大战》《侏罗纪公园》等影片的视效公司的大量幕后素材。值得关注的是，它让外界第一次能系统性地看到定格动画与CG过渡时期的技术遗产，对影迷和从业者都是难得的资料库。...

**3. A 40ms Go garbage collector pause caused by swap**

   Go 的一次 GC 停顿被拖到了 40ms，罪魁祸首不是 GC 本身，而是 swap——当内存被换出到磁盘，GC 需要触碰那些页时就被磁盘 I/O 卡住了。值得关注的是：这提醒我们，Go 低延迟的前提是内存别被换出去，生产环境跑延迟敏感服务时最好关掉 swap 或设 swappiness=0，否则再...

---
*3 分钟，掌握 AI 圈动态*