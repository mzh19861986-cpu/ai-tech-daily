# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 5 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这篇论文把中国哲学智慧（具体是儒家和道家的处世原则）引入自动驾驶决策，让大语言模型在复杂的交通博弈中做出更符合社会规范和伦理的判断。它值得关注的地方在于：现有自动驾驶决策要么靠数值优化、要么靠预测，很少认真处理"该不该抢道""该不该让行"这类涉及社交礼仪和道德权衡的问题——而中国哲学恰好提供了一套处理人际关系张力的现成框架。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**Learning to Learn a Language: in-context learning of natural language from a synthetic non-linguistic prior [R]**

✨ 这篇论文把「先验拟合网络」的思路从表格数据搬到了自然语言上——模型先在合成的非语言数据上预训练，之后不用微调就能在上下文里直接学会一门真实语言。它值得关注的地方在于，这挑战了「语言能力必须靠海量真实文本喂出来」的默认假设，给少样本甚至零微调的语言学习开了一条新路。

📎 [阅读原文](https://www.reddit.com/r/MachineLearning/comments/1wyzhdw/learning_to_learn_a_language_incontext_learning/)

## 技巧 3

**vCluster tutorial: virtual Kubernetes clusters per team**

✨ vCluster 让每个团队在自己的命名空间里跑一个「虚拟 Kubernetes 集群」——它看起来是完整的集群，有独立的 API Server、CRD 和 webhook 配置，实际共享底层宿主集群的计算资源。当团队间因 operator 版本、准入控制策略不同而互相踩脚时，这比给每个团队开一套真集群便宜得多，也比单纯靠 namespace 隔离干净得多。

📎 [阅读原文](https://dev.to/coresolutions/vcluster-tutorial-virtual-kubernetes-clusters-per-team-3bnn)

## 技巧 4

**How to show your Storybook in Azure DevOps without hosting it**

✨ Storybook 是隔离开发和评审 UI 组件的好工具，但在用 Azure DevOps 的团队里，它常常和日常开发流程脱节——要么得单独托管，要么就得本地跑。这篇文章介绍了一个作者自制的方案，让你不用额外部署就能在 Azure DevOps 里直接展示 Storybook，对组件库和开发平台分离的团队来说，值得一看。

📎 [阅读原文](https://dev.to/kvriel/how-to-show-your-storybook-in-azure-devops-without-hosting-it-5cl)

## 技巧 5

**Every control needs an accessible name (Web HIG tip #5)**

✨ 每个按钮都得有个能读出来的名字，尤其是只有图标的按钮——你看到垃圾桶知道是删除，屏幕阅读器用户只听到“按钮”，只能靠猜。这是 Web HIG 无障碍规范里最常被踩的坑，加上 `aria-label` 或可见文字就能解决。

📎 [阅读原文](https://dev.to/frozonfreak/every-control-needs-an-accessible-name-web-hig-tip-5-2e7f)

---
*每天一个小技巧，一年就是 365 个进步~*