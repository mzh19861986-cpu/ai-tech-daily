# 技术日报（中文版）- 2026-10-05

> 由 AI Agent 自动生成并翻译 | 共 2 条

## 📌 综合

### 1. [ncdu：NCurses磁盘使用情况（更新分支）](https://github.com/rcalixte/ncdu)
*lobsters*
ncdu 是一款基于 NCurses 的磁盘占用分析工具，此新分支版本对其进行了更新与维护。它能帮助用户快速直观地定位占用空间最大的文件和目录，适用于服务器和本地环境的磁盘清理。

## 🛠️ 开发工具

### 1. [Rust 的 derive 通常意味着内联。](https://yossarian.net/til/post/rust-s-derive-often-implies-inline/)
*lobsters*
Rust's derive macros typically add the `#[inline]` attribute implicitly when generating code. Although this behavior is not explicitly emphasized in the official documentation, it has a practical impact on performance optimization and compilation artifacts. Understanding this helps developers more accurately assess the overhead introduced by derive and avoid misjudging inlining behavior.

---
*本报告由 AI Agent 自动抓取公开信息并翻译生成，仅供参考。*