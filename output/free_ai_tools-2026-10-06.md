# 🆓 今日免费 AI 工具汇总 - 2026-10-06

> 精选免费好用的 AI 工具 | AI 帮你筛过，只留真正有用的 | 共 2 个

## 1. [Adobe Creative Suite Cleanroom Port to Rust](https://github.com/storytold/photocraft)

**👥 适合谁：** 最适合**系统级程序员和 Rust 开发者**——尤其是对 Adobe 底层算法、图形/图像处理管线或高性能多媒体工具链有逆向研究与重实现兴趣的人。

**🚀 怎么开始：** 直接克隆仓库后运行 `cargo build --release` 即可本地编译使用，无需 API key 或联网授权；这是社区对 Adobe 创意套件部分功能的 Rust 重写，功能覆盖有限，别指望完全替代原版。

**📝 简介：** Adobe 正在用 Rust 从头重写 Creative Suite 的核心组件，采用「洁净室」方式——不参考原有 C++ 代码，仅凭 API 文档和公开规范重新实现。这标志着主流商业软件首次大规模用 Rust 替代 C++ 处理图像渲染和文件解析等敏感模块，既规避了内存安全漏洞，也为跨平台部署铺路。

## 2. [Tapo (Rust/Python library) now speaks TP-Link's TPAP protocol](https://mihai.dinculescu.dev/posts/tapo-speaks-tpap/)

**👥 适合谁：** 最适合想用 Rust 或 Python 直接控制 TP-Link 智能设备（如智能插座、灯泡）、喜欢折腾自动化脚本的独立开发者和智能家居玩家。

**🚀 怎么开始：** Tapo 是一个用于控制 TP-Link 智能设备的 Rust/Python 库，现在它支持 TPAP 协议了。你可以在项目中通过 pip 或 cargo 安装它，提供设备 IP 和账号密码即可开始使用，无需本地部署或额外 API key。

**📝 简介：** Tapo 是一个用 Rust 写的 Python 库，现在能直接跟 TP-Link 的智能设备说上话了——它实现了 TP-Link 私有的 TPAP 协议，所以你可以用代码控制 Tapo 系列插座、灯泡、摄像头这些硬件，不用再依赖官方 App 或云服务。值得关注是因为它绕开了厂商的云端限制，让本地自动化（比如跟 Home Assistant 集成）变得更干净、更可靠，而且 Rust 底层保证了性能，Python 接口又降低了使用门槛。

---
*收藏起来，慢慢试！觉得有用记得分享给朋友~*