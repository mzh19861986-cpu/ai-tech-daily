# ✨ 每日 AI Prompt 技巧 - 2026-10-05

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章内容极少（仅有一个指向 lobste.rs 评论页的链接），没有提供实质性的正文内容可供提炼 Prompt 技巧。

基于标题 "Claude Says" 和常见讨论主题，无法可靠推断具体建议。**建议提供完整文章正文后再进行分析**，否则提炼内容会有臆测风险。

（如果你能粘贴该讨论帖的具体评论内容，我可以立即为你总结出可用的 AI 使用建议或 Prompt 技巧。）**

📎 来源：[Claude Says](https://ohhfishal.net/Posts/claude)

## 2. 💡 技巧 2

**这篇文章没有明显的 Prompt 技巧。它讨论的是 flow matching 模型的约束采样方法 MintFlow，属于生成模型/机器学习研究。

如果要说与"使用 AI"相关的启发，只能提炼出其核心思路：**对预训练生成模型施加约束时，采用"最小轨迹干预"策略，在满足约束的同时尽量少地偏离原有数据分布**。但这属于模型采样方法，而非 Prompt 工程建议。**

📎 来源：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

## 3. 💡 技巧 3

**这篇文章的核心建议可以提炼为以下 Prompt 技巧：

**让 Agent 在每次做小决策（选模型、选工具、判断相关性/注入）时，优先用单次前向即可输出的快速分类模型，而不是每次都调用大 LLM；但要用配对评估+自我审计来验证这些快速决策的可靠性，避免"快而不准"。**

用法示例：把"该用哪个工具/这段检索文本是否相关/是否含注入"这类判断，封装成一个输出类别概率的轻量分类器调用，只在低置信度时才回退到 LLM**

📎 来源：[Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses](https://arxiv.org/abs/2610.02267)

## 4. 💡 技巧 4

**从这篇摘要看，它本身没有提出可交互的 Prompt 技巧，但给出了一个**可复用的 LLM 两阶段分类流水线**思路，可提炼为：

**最佳实践：** 对大规模非结构化文档（如年报）做主题披露识别时，采用“两阶段分类流水线”——先用 LLM 做粗筛（判断是否涉及 AI 风险/响应披露），再对命中样本做细分类（判断披露类型与深度），并保持流程可复现。

**1-2 句话说明：** 把复杂判断拆**

📎 来源：[The AI Risk Observatory: What Can We Learn from AI Disclosures in Annual Reports About Societal Resilience?](https://arxiv.org/abs/2610.02281)

## 5. 💡 技巧 5

**从这篇论文中提炼的 Prompt 技巧：

**在长任务链的工具调用场景中，与其让 AI 一次性规划全部步骤，不如让它对候选的下一步动作进行「比较式价值评估」——即同时给出几个可行动作并判断哪个相对更好，而非直接要求绝对评分。**

理由：论文指出最终结果奖励在长交互轨迹上的信用分配很弱，而比较式的相对评估比让模型单独给每一步打绝对分更可靠、更容易实现，能帮助 Agent 在每一步都选到更优的下一步动作。**

📎 来源：[Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2610.02330)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*