# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 5 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这篇论文把中国哲学智慧（比如儒家的中庸、道家的无为）引入自动驾驶决策，用检索增强的大语言模型来指导车辆在复杂交通场景中的判断。有意思的地方在于，它不只是让AI算安全距离和通行效率，而是试图让决策系统学会权衡"过犹不及"和"以柔克刚"这类模糊但实用的处世逻辑——这可能是让自动驾驶真正融入人类交通文化的一条新路子。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**Learning to Learn a Language: in-context learning of natural language from a synthetic non-linguistic prior [R]**

✨ 这篇论文把 TabPFN 那套「先验拟合网络」的思路搬到了自然语言上——先用合成数据训练一个模型，再让它在推理时完全靠上下文（in-context）学会一门真实语言，而不需要任何针对该语言的梯度更新。值得关注的是，它证明了「从合成先验中学会如何学习」这件事可以泛化到自然语言这种高度结构化的领域，为少样本、免微调的语言适应提供了一条新路径。

📎 [阅读原文](https://www.reddit.com/r/MachineLearning/comments/1wyzhdw/learning_to_learn_a_language_incontext_learning/)

## 技巧 3

**How to Make Passive Income as a UI/UX Designer: 10 Practical Ways**

✨ 这篇文章给UI/UX设计师指了条路：别再只靠接单换钱了，试试做能持续产生收入的资产。核心思路是把你已有的设计能力转化成模板、素材包、课程、插件这类"做一次卖多次"的产品——比如在UI8上卖一套设计系统，或者在YouTube做设计教程靠广告分成。值得关注的点在于，这不是让你转行，而是把你现在按项目收费的模式，升级成一份工作能产生多份回报的结构。

📎 [阅读原文](https://dev.to/rowan_merc/how-to-make-passive-income-as-a-uiux-designer-10-practical-ways-35p7)

## 技巧 4

**How to Set Up SSH Keys and Turn Off Password Login**

✨ 用SSH密钥替代密码登录，本质上是用一对数学上不可伪造的密钥取代一个可能被猜到、钓鱼或从泄露库中复用的字符串——服务器只见到签名，永远拿不到你的私钥，密码暴力破解对你彻底失效。它的价值不在于"更安全"的口号，而在于五分钟的配置就能永久关闭整类攻击面，对任何暴露在公网的服务器都是性价比最高的加固动作。

📎 [阅读原文](https://dev.to/vpspioneer/how-to-set-up-ssh-keys-and-turn-off-password-login-4m5)

## 技巧 5

**Test-Time Training Collapses When Agents Learn from Their Own Rollouts**

✨ 最近有篇论文揭示了一个反直觉的结论：让模型在推理时「边跑边学」（test-time training）——用自身生成的 rollout 更新权重——反而会让性能崩塌。问题出在模型学的是自己输出的内容，相当于在自己编的答案上反复强化，错误被当成真理越滚越深。这给当下流行的「推理时权重更新省显存」路线泼了盆冷水：想让模型在推理中持续学习，前提是得有可靠的外部信号，而不是让它自己教自己。

📎 [阅读原文](https://dev.to/reidmarlow/test-time-training-collapses-when-agents-learn-from-their-own-rollouts-5eh3)

---
*每天一个小技巧，一年就是 365 个进步~*