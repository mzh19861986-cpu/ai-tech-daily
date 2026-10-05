# 📊 每周技术精选周报 - 2026-10-05

> 由 AI Agent 自动汇总整理 | 共 2 条精选

## 🎯 本周概览

- 精选内容：2 条
- 数据来源：Hacker News / Lobsters / ArXiv / GitHub Trending
- 生成时间：2026-10-05

## 📝 精选内容

## 📌 综合

### 1. [ncdu: NCurses Disk Usage (an updated fork)](https://github.com/rcalixte/ncdu)
*lobsters*
`ncdu` 是一个基于 NCurses 的磁盘占用分析工具，最近有人接手维护并发布了更新版分支。它能让你在终端里用方向键直观地浏览各个目录占了多少空间，比 `du` 加 `sort` 那套组合命令好用得多，适合快速定位硬盘被谁吃掉了。

## 🛠️ 开发工具

### 1. [Rust's derive often implies inline](https://yossarian.net/til/post/rust-s-derive-often-implies-inline/)
*lobsters*
Rust 的 `#[derive]` 宏在展开时，会自动给生成的 impl 加上 `#[inline]` 属性，这意味着编译器更倾向于把这些方法内联到调用处，而不是留作独立的函数调用。这个行为平时容易被忽略，但对性能敏感的热路径代码影响不小——它解释了为什么某些派生出来的 trait 方法（比如 `PartialEq`、`Hash`）在 benchmark 里表现得比手写实现还快，也提醒你手写 impl 时可能需要手动补上 `#[inline]` 才能对齐。


---
*本周报由 AI 自动汇总生成，精选自公开技术社区。*