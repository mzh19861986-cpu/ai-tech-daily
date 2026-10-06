# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 2 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ **是什么：** 这篇论文提出了一个叫 Ch 的自动驾驶决策框架，把中国哲学智慧（比如中庸、和谐这类思想）注入基于检索增强的大语言模型决策流程中，让自动驾驶系统在安全、效率之外，还能兼顾社会规范和伦理判断。

**为什么值得关注：** 现有自动驾驶决策要么纯做数值优化，要么直接用 LLM 预测，几乎没人系统性地把哲学伦理框架嵌进去——而"该不该抢道""如何与行人博弈"这类问题本质上是伦理问题，不是算力问题。这项工作试图给自动驾驶补上"价值判断"这一层，跨学科方向挺有意思，但实际落地效果还有待验证。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**How IceCube's Sensor Stream Drops Events and How to Recover Them**

✨ 南极冰立方中微子天文台每秒产生数百万个光电倍增管波形，一次短暂的网络抖动就可能丢掉整个事件，在数据中留下空洞——这些空洞会偏置通量测量，甚至伪装成新物理信号。这篇文章给出了检测数据丢失并恢复缺失事件的方法，不用重新设计探测器就能补上这些洞。

📎 [阅读原文](https://dev.to/robust_true_try/how-icecubes-sensor-stream-drops-events-and-how-to-recover-them-3688)

---
*每天一个小技巧，一年就是 365 个进步~*