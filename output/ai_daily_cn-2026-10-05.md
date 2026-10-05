# 技术日报（中文版）- 2026-10-05

> 由 AI Agent 自动生成并翻译 | 共 2 条

## 🤖 AI / 大模型

### 1. [F1车手在巴林遭遇软件故障，因赛车动力缺失而感到沮丧。](https://www.motorsport.com/f1/news/horrible-totally-unacceptable-powerless-f1-drivers-frustrated-by-bahrain-f1-software-glitch/10861968/)
*hackernews*
During the Bahrain F1 race, a driver encountered a software glitch that briefly disabled the steering wheel's electronic system, causing a loss of power steering and some control functions. Such 'drive-by-wire' system failures are extremely rare in F1, yet they directly expose the high dependence of modern race cars on software reliability—when the steering wheel becomes a computer, a crash could mean losing control.

## 📌 综合

### 1. [在消费级硬件（RTX 4090）上以100T/s运行Qwen 3.8 Flash Next（125B）](https://github.com/Niko1221/Strata)
*hackernews*
Someone ran the latest Qwen 3.8 Flash Next from Tongyi Qianwen—a 125B-parameter large model—on two RTX 4090s. A single card's VRAM couldn't hold it at all, but by compressing the weights to 4-bit quantization and then splitting them across GPUs, they managed a generation speed of 100 tokens/sec. The key point is that this inference speed is already close to what many people pay for on cloud APIs, while the entire hardware cost is about $5,000. If this can be reproduced reliably, it means local private deployment of 100B-class models has truly become feasible for individuals and small teams.

---
*本报告由 AI Agent 自动抓取公开信息并翻译生成，仅供参考。*