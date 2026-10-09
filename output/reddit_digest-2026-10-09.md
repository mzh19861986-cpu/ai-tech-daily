# 💬 Reddit 技术社区热门帖 - 2026-10-09

> 由 AI Agent 自动抓取并摘要 | 共 4 条热门

## 🔥 本周热议

### 1. [[D] Self-Promotion Thread](https://www.reddit.com/r/MachineLearning/comments/1wvi1j8/d_selfpromotion_thread/)
*reddit/r/MachineLearning*

这是一个开发者社区常见的「自我推广专用帖」，专门给成员发布个人项目、创业产品、合作需求或博客。它的价值在于把散落的推广信息集中管理，既避免刷屏，又让有需求的人能一站式找到工具和服务；发帖时还要求标明付费和定价方式。

### 2. [Clarification ARR Commitment [D]](https://www.reddit.com/r/MachineLearning/comments/1x1lkln/clarification_arr_commitment_d/)
*reddit/r/MachineLearning*

提交ARR论文到EACL 2027时，你需要在提交PDF里直接回应审稿人的意见，而不是只贴reviews链接、把修改留到camera ready。ARR的commitment机制要求这版PDF已经是带修改说明的最终版，因为程序委员会就是靠它来决定的。简单说：把minor comments改进去，附上回复，一步到位。

### 3. [ARR Oct Discussion [D]](https://www.reddit.com/r/MachineLearning/comments/1x1ke20/arr_oct_discussion_d/)
*reddit/r/MachineLearning*

这轮ARR投稿量明显偏少，有人昨晚看到的投稿编号才到1800左右。大家在猜，要么是真投的人少了，要么是很多人憋着等ARR八月那轮（含Meta review）出结果再决定——后者的话，下一轮可能会挤爆。

### 4. [I built MaRN: a PyTorch library for training neural networks through low-dimensional parameter mappings [P]](https://www.reddit.com/r/MachineLearning/comments/1x1fjrv/i_built_marn_a_pytorch_library_for_training/)
*reddit/r/MachineLearning*

有人做了一个叫 MaRN 的 PyTorch 库，思路是不直接训练模型的所有参数，而是只优化一个紧凑的隐变量，再通过映射网络生成完整权重——等于把"调参"变成了"调低维表示"。在 MNIST CNN 上，它把 53 万参数压到 4080 个可训练参数（131.8 倍缩减），准确率只从 99.07% 掉到 98.10%。如果你关心参数高效微调、模型压缩或者低维优化这类方向，这个思路挺值得一看。

---
*内容来自 Reddit 公开社区，由 AI 自动摘要生成。*