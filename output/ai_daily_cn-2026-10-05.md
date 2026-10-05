# 技术日报（中文版）- 2026-10-05

> 由 AI Agent 自动生成并翻译 | 共 2 条

## 📌 综合

### 1. [ncdu：NCurses磁盘使用情况（一个更新的分支）](https://github.com/rcalixte/ncdu)
*lobsters*
ncdu 是一个用 NCurses 编写的磁盘占用分析工具，其新分支最近更新了——你可以把它理解为命令行版的「磁盘空间可视化」，用方向键就能逐层深入目录，一眼看出哪个文件夹在悄悄占用你的硬盘空间。

值得关注的原因很实际：原版 ncdu 已经多年未维护，这个分支接过了接力棒，修复了 bug、跟进了新系统兼容性。对经常通过 SSH 登录服务器清理磁盘的人来说，它依然是那个「装完就再也不想用 du 了」的顺手工具。

## 🛠️ 开发工具

### 1. [Rust的derive通常意味着内联。](https://yossarian.net/til/post/rust-s-derive-often-implies-inline/)
*lobsters*
Rust 的 `#[derive]` 宏（比如自动生成 `Clone`、`Debug` 等实现）在大多数情况下，生成的代码会自动带上 `#[inline]` 属性，让编译器倾向于将这些小函数内联展开。这个细节平时容易被忽略，但它意味着你随手 derive 出来的 trait 方法在优化后往往不留函数调用开销——理解这一点，有助于判断何时该手写实现、何时放心交给 derive。

---
*本报告由 AI Agent 自动抓取公开信息并翻译生成，仅供参考。*