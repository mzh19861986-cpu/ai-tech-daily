# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 5 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这篇论文尝试把中国哲学智慧引入自动驾驶决策——不是简单套用伦理原则，而是用「中庸」「审时度势」这类思维来指导 LLM 在复杂路况下平衡安全、效率和社会规范。值得关注的点在于：它代表了一种新趋势，即不再把哲学伦理当成事后道德审查，而是直接嵌入实时驾驶决策的推理逻辑中。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**Learning to Learn a Language: in-context learning of natural language from a synthetic non-linguistic prior [R]**

✨ 这篇论文把 TabPFN 的思路搬到了语言学习上：先让模型只接触合成数据，再让它纯靠上下文（in-context learning）去学一门真实语言，全程不更新权重。值得关注的是，它证明"从零合成预训练"这条路可能不依赖海量真实语料，就能让模型具备学习新语言的能力——对低资源语言和可解释性研究都是一个有意思的信号。

📎 [阅读原文](https://www.reddit.com/r/MachineLearning/comments/1wyzhdw/learning_to_learn_a_language_incontext_learning/)

## 技巧 3

**How to Make AI Write High-Quality Code in .NET**

✨ AI 写 .NET 代码速度飞快，但“看起来能用”和“经得起 review”往往是两码事——这是很多团队实际踩过的坑。这篇内容分享的是一套让 AI 智能体写出高质量 .NET 代码的方法，作者把自己多年打磨可读、可维护代码的经验，转化成了对 AI 的指令。如果你正在用 AI 辅助 .NET 开发却总在代码审查环节返工，值得一看。

📎 [阅读原文](https://dev.to/antonmartyniuk/how-to-make-ai-write-high-quality-code-in-net-2d4l)

## 技巧 4

**How to Calculate Physical Display Dimensions & Screen Sizes Accurately**

✨ 买显示器或电视时只看对角线尺寸（比如27寸、55寸）很容易踩坑——同样的对角线，16:9和21:9的实际宽高差别巨大，桌面放不下或者挂架装不上都是这么来的。这篇指南会讲清屏幕尺寸的计算逻辑，以及宽高比如何直接影响实际显示面积，帮你在下单前算准物理尺寸。

📎 [阅读原文](https://dev.to/screensizecalc/how-to-calculate-physical-display-dimensions-screen-sizes-accurately-57ga)

## 技巧 5

**How to Fix Shopify Liquid Errors: A Practical Troubleshooting Guide**

✨ Shopify 的 Liquid 模板报 `Unknown tag 'endif'`，通常是因为 `{% endif %}` 前面缺少配对的 `{% if %}`，或者 if 标签被写在了另一个逻辑块里导致嵌套错位。这类错误值得关注，因为 Liquid 是 Shopify 主题渲染的核心，一个标签错位就可能让整个页面白屏——排查时按 if/endif、for/endfor、case/endcase 成对检查标签闭合即可快速定位。

📎 [阅读原文](https://dev.to/amaanmirzaa/how-to-fix-shopify-liquid-errors-a-practical-troubleshooting-guide-44o0)

---
*每天一个小技巧，一年就是 365 个进步~*