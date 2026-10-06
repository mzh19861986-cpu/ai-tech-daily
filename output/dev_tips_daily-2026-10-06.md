# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 2 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这篇论文把中国哲学智慧（比如儒家的"中庸"、道家的"顺应自然"）引入自动驾驶的决策框架中，让大语言模型在复杂路况下做判断时，不只看安全和效率的数字指标，还融入伦理与社会规范的考量。它的价值在于：当自动驾驶面对"该不该让、该怎么让"这类没有标准答案的道德困境时，这套检索增强的方法能让LLM参考哲学原则做出更符合人类价值直觉的决策——这是纯数值优化和传统序列预测做不到的。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**Learning to Learn a Language: in-context learning of natural language from a synthetic non-linguistic prior [R]**

✨ 这篇论文把 TabPFN 那套「先验拟合网络」的思路从表格数据搬到了自然语言上——他们只用合成的、非语言的数据预训练一个模型，结果这个模型能在推理时仅靠上下文（in-context）学会一门真实语言的运作方式。

值得关注的点在于：它挑战了「要学语言必须先喂大量语言数据」的默认假设，说明上下文学习能力可以来自完全非语言的先验训练，这对理解大模型的泛化机制和降低对真实语料的依赖都有启发。

📎 [阅读原文](https://www.reddit.com/r/MachineLearning/comments/1wyzhdw/learning_to_learn_a_language_incontext_learning/)

---
*每天一个小技巧，一年就是 365 个进步~*