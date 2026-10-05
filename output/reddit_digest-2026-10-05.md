# 💬 Reddit 技术社区热门帖 - 2026-10-05

> 由 AI Agent 自动抓取并摘要 | 共 4 条热门

## 🔥 本周热议

### 1. [[D] Self-Promotion Thread](https://www.reddit.com/r/MachineLearning/comments/1wvi1j8/d_selfpromotion_thread/)
*reddit/r/MachineLearning*

这是一个供开发者展示个人项目、创业产品、协作需求的推广帖，要求注明付费方式和定价，禁止短链、聚合站和自动订阅链接。

**为什么值得关注**：如果你想找早期项目、副业点子或合作机会，这类帖子是低成本“逛一圈”的好地方——同时它也用明确的规则（禁滥用、违者封号）维持了信息质量，比一般广告区靠谱。

### 2. [Distilling Stockfish on a Billion Positions, Full 3.9B Dataset Available [P]](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/)
*reddit/r/MachineLearning*

有人把 Stockfish 的估值函数蒸馏进了一个 ResNet/ViT 模型，训练数据用了 10 亿个棋局，完整数据集则高达 39 亿个局面，全部来自 Lichess 37 个月的真实对局，现已开源在 Hugging Face 上。值得关注的是：这相当于让小网络学会“模仿”Stockfish 在有限深度下对整棵搜索树的判断，如果能成立，就意味着可以用极低成本逼近顶级引擎的棋力——对做棋类 AI 或想研究“搜索能否被网络吸收”的人来说，这份数据集本身就是稀缺资源。

### 3. [Sona: one transformer replaced our 15+ candidate generators, pre-ranker and ranker in an A/B test [R]](https://www.reddit.com/r/MachineLearning/comments/1wy4qxm/sona_one_transformer_replaced_our_15_candidate/)
*reddit/r/MachineLearning*

Yandex Music 把原本需要 15+ 个候选生成器、预排序和排序模型协作的推荐系统，换成了一个叫 Sona 的端到端 Transformer，并在线上 A/B 测试中验证了效果。这件事值得关注的点在于：它证明了生成式推荐的「单模型吃全流程」思路不只是论文里的漂亮结论，而是能在真实大规模音乐推荐场景中跑通并替代传统多组件流水线。

### 4. [Withdrawing an accepted paper before camera-ready due to zero funding? (ACML 2026 / OpenReview) [D]](https://www.reddit.com/r/MachineLearning/comments/1wy2irf/withdrawing_an_accepted_paper_before_cameraready/)
*reddit/r/MachineLearning*

顶会论文被接收却因没钱注册和参会而撤稿，这揭示了学术出版体系中一个不太被公开讨论的现实：没有经费的研究者即使工作被认可，也可能被迫放弃发表机会。ACML 作为 CCF-C 类会议，注册费加上差旅通常需要几千到上万元人民币，对没有课题经费支撑的学生或独立研究者来说是一道硬门槛。值得注意的是，会议论文一旦撤稿，通常不会自动转入期刊或其他发表渠道，之前投入的审稿周期就白费了。

---
*内容来自 Reddit 公开社区，由 AI 自动摘要生成。*