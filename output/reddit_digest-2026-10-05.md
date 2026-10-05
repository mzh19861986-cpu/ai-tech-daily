# 💬 Reddit 技术社区热门帖 - 2026-10-05

> 由 AI Agent 自动抓取并摘要 | 共 4 条热门

## 🔥 本周热议

### 1. [[D] Self-Promotion Thread](https://www.reddit.com/r/MachineLearning/comments/1wvi1j8/d_selfpromotion_thread/)
*reddit/r/MachineLearning*

这是一个开发者社区的自我推广帖，允许大家发布个人项目、创业产品、合作需求或博客，但要求标明付费和定价信息，禁止短链接和聚合网站。值得关注的是，它把分散的“求关注”内容集中到一个帖子里，避免刷屏，同时明确规则来维持信任。如果你有东西想推，这就是那个合规的入口。

### 2. [Distilling Stockfish on a Billion Positions, Full 3.9B Dataset Available [P]](https://www.reddit.com/r/MachineLearning/comments/1wxz5qq/distilling_stockfish_on_a_billion_positions_full/)
*reddit/r/MachineLearning*

有人把顶级国际象棋引擎 Stockfish 的估值函数蒸馏进了一个 ResNet/ViT 神经网络，训练数据是来自 37 个月 Lichess 对局的 10 亿个棋局位置；完整 3.9B 数据集已在 Hugging Face 开源。值得关注的是它背后的思路——有限深度搜索下的估值函数其实是在逼近它下面那棵搜索树的结果，这意味着神经网络有机会用一次前向传播学到原本需要大量搜索才能得到的判断，对做棋类 AI 或搜索加速的人很有参考价值。

### 3. [Top ARC-ΑGI-3 scores on Kaggle just went from 7% to 56% [N]](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)
*reddit/r/MachineLearning*

ARC-AGI-3的Kaggle基准测试分数在30天内从7%飙升到56%，而参赛者只能使用小型本地模型。这意味着在专门为"人类更强"而设计的测试上，小模型加外挂框架已经反超了普通人。如果这个曲线不是过拟合或刷榜，那它比大多数大厂发布会更值得关注——因为这是在受限条件下发生的真实跃升。

### 4. [the official ICLR template .bib has had Bengio listed twice since 2019 [D]](https://www.reddit.com/r/MachineLearning/comments/1wxe9qx/the_official_iclr_template_bib_has_had_bengio/)
*reddit/r/MachineLearning*

ICLR 官方 LaTeX 模板里自带的示例 .bib 文件，从 2019 年起就把《Deep Learning》这本书的作者写成「Goodfellow, Bengio, Courville, Bengio」——Bengio 出现两次，还多出一个不存在的 volume 1。这纯粹是无害的笔误，但考虑到 ICLR 刚经历过作者用 LLM 编造参考文献的风波，官方模板自己抄错五年，实在有点讽刺。

---
*内容来自 Reddit 公开社区，由 AI 自动摘要生成。*