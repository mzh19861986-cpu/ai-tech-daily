# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 5 条

## 技巧 1

**Tufte's Razor: an interactive guide to the data-ink ratio**

✨ 爱德华·塔夫特（Edward Tufte）提出的「数据墨水比」概念，主张图表中的每一个像素都应该服务于数据本身——多余的边框、网格线、渐变填充都是「噪声」。这个交互式指南用可视化演示帮你直观感受：同一组数据，去除冗余元素后信息传达反而更清晰。如果你经常做图表或报表，花五分钟玩一遍会比读十篇文章都管用。

📎 [阅读原文](https://tuftesrazor.scienceux.org/)

## 技巧 2

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这个工作把中国哲学智慧（比如中庸、变通这些思路）引入到自动驾驶决策中，用来指导大语言模型的推理过程。具体做法是用检索增强生成（RAG）给LLM提供哲学原则作为决策参考，让自动驾驶在面对复杂路况时不只是算数值最优解，还能兼顾社会规范和伦理权衡。值得关注的点在于：它代表了一种新趋势——不再纯靠数学优化做自动驾驶决策，而是尝试让AI参考人类文化中的价值判断框架，这对解决自动驾驶的「道德困境」问题（比如电车难题类场景）提供了工程化的新思路。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 3

**Learning to Learn a Language: in-context learning of natural language from a synthetic non-linguistic prior [R]**

✨ 这篇论文把 TabPFN 那种"先用合成数据训练、再在推理时纯靠上下文学习"的思路，从表格数据搬到了自然语言上——模型只在一个合成的、非语言的先验上训练过，却能通过 in-context learning 学会一门真实语言。

值得关注的点在于：它挑战了"要学语言就得先喂大量真实语料"的默认假设，说明语言习得能力本身可能可以从无关的合成结构中涌现出来，这对理解 in-context learning 的机制、以及低资源场景下的语言建模都挺有启发。

📎 [阅读原文](https://www.reddit.com/r/MachineLearning/comments/1wyzhdw/learning_to_learn_a_language_incontext_learning/)

## 技巧 4

**Decision records for AI agents: how to keep what the team decided from being forgotten**

✨ 团队和 AI 编码助手达成的架构决策，往往止步于当次对话——新会话一开始，agent 就「失忆」了，周三可能就给你 v1 API 偷偷加回两个新端点，还贴心地附上测试。

这篇文章提出用「决策记录」来治这个病：把每次定下的规则（比如「v1 只修安全漏洞」）落成 agent 能读到的持久文档，而不是指望它跨会话记住。

值得关注是因为，AI 写代码的能力早就够用了，真正拖后腿的是它不知道你们**当初为什么这么定**——而这个坑，每个用 agent 做长期项目的团队都会踩。

📎 [阅读原文](https://dev.to/oaleviola/decision-records-for-ai-agents-how-to-keep-what-the-team-decided-from-being-forgotten-2li4)

## 技巧 5

**How to Vet a Developer to Fix Your Vibe-Coded App**

✨ 招聘开发者修 vibe-coded 应用（用 AI 快速生成但结构混乱的 App），最大的坑不是找不到人，而是你无法从回复中判断谁靠谱——报价两天的、建议推倒重建的、要你直接给数据库权限的，三种回答都可能对，区别只在你看不出来的技术细节里。这条内容的真正价值是点破了这个信息不对称：vibe coding 让开发门槛降低，但让「评估修复方案」变得更难，因为它把判断力从写代码转移到了识人上。

📎 [阅读原文](https://dev.to/manveer-banxal/how-to-vet-a-developer-to-fix-your-vibe-coded-app-1aji)

---
*每天一个小技巧，一年就是 365 个进步~*