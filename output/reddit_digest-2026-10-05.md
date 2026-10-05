# 💬 Reddit 技术社区热门帖 - 2026-10-05

> 由 AI Agent 自动抓取并摘要 | 共 4 条热门

## 🔥 本周热议

### 1. [[D] Self-Promotion Thread](https://www.reddit.com/r/MachineLearning/comments/1wvi1j8/d_selfpromotion_thread/)
*reddit/r/MachineLearning*

这是个开发者社区的自我推广专帖，任何人都可以在这里发布自己的个人项目、创业产品、博客或合作需求，但必须注明付费和定价要求，禁止短链和聚合链接。值得关注的是，它把平时容易被淹没的个人作品集中到一个可检索的入口，对有推广需求的人是低成本曝光机会，对找工具或合作的人则是一个现成的资源池。

### 2. [Distilling Stockfish on a Billion Positions, Full 3.9B Dataset Available [P]](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/)
*reddit/r/MachineLearning*

有人用10亿个国际象棋局面，把Stockfish的估值函数蒸馏进了一个ResNet/ViT模型——思路是：在有限深度搜索下，估值函数本质上是在逼近它下面那棵树的结果，那就干脆让神经网络直接学这个映射。

更值得关注的是数据本身：完整的39亿局面数据集（来自Lichess 37个月的对局）已经在HuggingFace上公开了。以前想复现这类工作，光搞数据就得脱层皮，现在直接能下载——对做棋类AI或者想研究「搜索+学习」结合的人来说，这是个很实在的基础设施。

### 3. [I have trained a model to predict my blood sugar (Part 2) [P]](https://www.reddit.com/r/MachineLearning/comments/1wy99gd/i_have_trained_a_model_to_predict_my_blood_sugar/)
*reddit/r/MachineLearning*

有人用自己作为1型糖尿病患者的血糖数据，训练了一个只有3万参数的小模型（16层、单注意力头、隐藏维度16），在DGX Spark上不到一小时就跑完了，然后拿它零样本预测自己真实的血糖波动。有意思的点在于：这种极简架构如果真能泛化到真实连续血糖监测数据上，意味着个体化的血糖预测未必需要大模型，边缘设备本地实时推理就够了。

### 4. [Sona: one transformer replaced our 15+ candidate generators, pre-ranker and ranker in an A/B test [R]](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/)
*reddit/r/MachineLearning*

Yandex Music 把推荐系统里 15+ 个候选生成器、预排序和排序模型，全部换成了一个名为 Sona 的单一 Transformer，并在 A/B 测试中验证了效果。这件事值得关注，因为它说明生成式推荐正在从论文走向大规模生产——过去需要多个专用模型拼装的流水线，现在一个端到端模型就能扛下来。

---
*内容来自 Reddit 公开社区，由 AI 自动摘要生成。*