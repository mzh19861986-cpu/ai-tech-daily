# 💡 每日开发技巧 - 2026-10-06

> 每天学一个实用技巧，效率慢慢提上来 | 共 5 条

## 技巧 1

**Retrieval-Augmented Large Language Model Decision-Making for Autonomous Driving Guided by Chinese Philosophical Wisdom**

✨ 这篇论文尝试把中国哲学智慧（比如中庸、无为而治这类思路）引入自动驾驶的决策系统，结合检索增强的大语言模型，让车辆在复杂交通场景中更好地平衡安全、效率和社会规范。值得关注的是，它跳出了纯数值优化和传统LLM决策的框架，第一次系统性地把哲学伦理维度纳入自动驾驶的决策逻辑——这可能是解决"电车难题"类伦理困境的一条新路径，而不只是靠堆算力硬算。

📎 [阅读原文](https://arxiv.org/abs/2610.03948)

## 技巧 2

**Learning to Learn a Language: in-context learning of natural language from a synthetic non-linguistic prior [R]**

✨ 这篇论文把 TabPFN 那套「先验拟合网络」的思路搬到了自然语言上：模型先在一个纯合成、非语言的数据分布上训练，之后不用微调，直接靠上下文就能学会一门真实语言的任务。

值得关注的点在于，它验证了「元学习能力」可以跨模态迁移——在合成任务里学到的「如何从上下文里找规律」，能直接用于理解自然语言，这给少样本甚至零样本的语言适应提供了一条新路径。对关心 ICL 本质和低资源语言处理的人来说，这篇值得一读。

📎 [阅读原文](https://www.reddit.com/r/MachineLearning/comments/1wyzhdw/learning_to_learn_a_language_incontext_learning/)

## 技巧 3

**How to Start Selling Website Templates and UI Kits as a Beginner: A Complete Step-by-Step Guide for Designers, Developers, and Freelancers**

✨ 卖网站模板和UI套件，说白了就是把你做过的界面设计打包成可复用的产品，放到Gumroad、UI8这类平台上反复卖——做一次，卖多次。对设计师和开发者来说，这是从“接一单赚一单”的打工模式转向被动收入的最现实路径，尤其适合已经有一定Figma或前端基础、但还没精力做SaaS产品的人。

📎 [阅读原文](https://dev.to/amacaprislegacies/how-to-start-selling-website-templates-and-ui-kits-as-a-beginner-a-complete-step-by-step-guide-for-1ig1)

## 技巧 4

**Learning Go as a Ruby Developer #7: Finally Understanding Pointers**

✨ 一位 Ruby 开发者分享了他学习 Go 指针的心路历程——从最初把指针当成 C++ 遗留的"可怕概念"，到最终理解其本质。核心价值在于：Go 把内存地址和引用传递显式暴露给开发者，这跟 Ruby 的隐式处理方式截然不同，对习惯了动态语言的程序员来说是一个需要刻意跨越的思维转变。

📎 [阅读原文](https://dev.to/shroukabozeid/learning-go-as-a-ruby-developer-7-finally-understanding-pointers-4lkk)

## 技巧 5

**Ubuntu Cloud Images on a Mac: Why the Disk Is 3.5 GB, Why You Can't Log In, and How to Fix Both**

✨ Ubuntu 的 cloud image 在 Mac 上跑会遇到两个坑：磁盘只有 3.5 GB、而且没有可用账户登录。根本原因是这类镜像默认由云平台的初始化服务（cloud-init）来扩容和创建用户，本地虚拟机里没有这套东西，自然就卡住了。好消息是这两个问题都能手动解决，不需要换镜像。

📎 [阅读原文](https://dev.to/wango/ubuntu-cloud-images-on-a-mac-why-the-disk-is-35-gb-why-you-cant-log-in-and-how-to-fix-both-4fbc)

---
*每天一个小技巧，一年就是 365 个进步~*