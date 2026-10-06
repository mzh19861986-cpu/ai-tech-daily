# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 2 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这篇论文尝试把中国哲学智慧引入自动驾驶决策，让大语言模型在安全、效率之外，也学会权衡「社会规范」这类软性伦理问题。它的价值在于点出了一个被现有自动驾驶系统长期忽视的维度——机器开车不只是算最优解，还得懂「人情世故」。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**How to Debug Stale Feature Flag Cache: Polling Interval Mismatches**

✨ 特性开关（feature flag）的缓存过期问题，根源往往不在代码逻辑，而在于各进程的轮询间隔不一致——间隔越长控制面流量越省，但两个进程用同一个开关做出不同决策的时间窗口也越长。对定价灰度这类场景，实用做法是在评估时记录决策上下文、按队列而非孤立日志行做对比，并把缓存年龄当成一个有边界的运行条件来管理，而不是指望它永远同步。

📎 [阅读原文](https://dev.to/sladebarrett9642/how-to-debug-stale-feature-flag-cache-polling-interval-mismatches-4g0c)

---
*每天一个小技巧，一年就是 365 个进步~*