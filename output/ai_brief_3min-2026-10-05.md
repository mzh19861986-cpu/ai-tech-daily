# ⚡ 3 分钟 AI 快讯 - 2026-10-05

> 每天 3 条最重要的 AI 新闻，3 分钟看完

**1. ncdu: NCurses Disk Usage (an updated fork)**

   ncdu 是一个基于 NCurses 的磁盘占用分析工具，最近有人接手维护并发布了更新版本，修复了原版长期停滞的问题。它的价值在于：用终端界面交互式浏览目录大小、快速定位吃空间的“元凶”，比 `du` 挨个翻目录直观得多，服务器上排查磁盘爆满尤其好用。...

**2. Rust's derive often implies inline**

   Rust 的 `#[derive]` 宏在展开时会自动为生成的 trait 方法加上 `#[inline]` 属性，这跟很多人以为「derive 只是生成代码、优化交给 LLVM」的直觉不一样。值得关注是因为它解释了一个常见困惑：为什么用 derive 实现的方法（如 `PartialEq`、`Cl...

**3. Why don’t more developers "use the platform"?**

   网页平台的原生能力这些年涨得飞快——CSS 容器查询、Popover API、原生表单验证、View Transitions，浏览器能干的活早就不止渲染 HTML 了。但大多数开发者依然习惯性地把 React、Vue 和一堆构建工具套在外面，问「为什么不用平台」其实是在问：原生能力到底差在哪，才让大...

---
*3 分钟，掌握 AI 圈动态*