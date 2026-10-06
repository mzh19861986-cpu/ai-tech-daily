# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 2 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这篇论文尝试把中国哲学智慧引入自动驾驶决策，让大语言模型在处理复杂交通博弈时不仅算得对，还能“讲道理”——比如在电车难题类场景里，与其硬套功利主义最大化，不如用儒家“中庸”或道家“无为”的思路去找更柔性的解法。值得关注的是它点出了当前自动驾驶的一个真实短板：纯数值优化和常规LLM都缺乏伦理框架，而中国哲学恰好提供了一套现成的、非西方的价值权衡逻辑，这可能是AI伦理本土化的一条新路径。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**How do you connect a blockchain node with multiple trading bots without adding TCP/HTTP overhead?**

✨ **一句话总结**：go-ipc 用本地 IPC 替代 TCP/HTTP，让区块链节点和多个交易机器人直接通信，省掉网络层开销。

**为什么值得关注**：交易机器人对延迟极度敏感，每多一层网络协议就多一份延迟和故障点。这个方案把节点和机器人之间的通信压到进程间级别，每个机器人拿独立的事件订阅管道和独立的交易提交通道，互不干扰。如果你在跑高频交易或多策略并行，这种架构比传统的"再包一层 RPC"干净得多。

📎 [阅读原文](https://dev.to/seiji_ito_2ab3f2c476cf649/how-do-you-connect-a-blockchain-node-with-multiple-trading-bots-without-adding-tcphttp-overhead-54db)

---
*每天一个小技巧，一年就是 365 个进步~*