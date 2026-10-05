# ❓ 每日 AI 问答 - 2026-10-05

> 关于 AI 你可能想问的问题 | 每天一个问题，搞懂一个概念

## Q1: Anthropic wants your thoughts on AI？

**A:** Anthropic 正在公开征集公众对 AI 发展的看法和担忧，试图在 AI 治理和伦理规范上引入更多外部声音。这事值得关注，因为头部 AI 公司主动向用户和公众要反馈，正在成为行业争夺「负责任 AI」话语权的新动作。

📎 更多阅读：[Anthropic wants your thoughts on AI](https://www.anthropic.com/research/your-thoughts-on-ai)

## Q2: Spending on AI Is Becoming Almost Impossible for Businesses to Budget？

**A:** 企业给AI花钱这件事，正在从“项目预算”变成“填不满的坑”——训练成本、推理调用费、数据治理开销层层叠加，连CFO都很难预测下季度要烧多少。值得关注的是，这暴露了一个结构性矛盾：AI的投入产出节奏和传统IT预算周期根本不匹配，企业要么被迫转向按用量付费的灵活模式，要么就得接受预算永远追不上账单。

📎 更多阅读：[Spending on AI Is Becoming Almost Impossible for Businesses to Budget](https://www.wsj.com/tech/personal-tech/ai-token-spending-businesses-431ee94a)

## Q3: Claude Says？

**A:** 这条讨论围绕 Anthropic 的 Claude 模型在输出中出现的某种特定行为或表述展开，社区成员就它的可信度、边界和潜在影响交换了看法。之所以值得留意，是因为它触及一个更普遍的问题：当模型开始「自信地」说出某些内容时，我们该如何判断它是真实理解还是模式匹配。如果你在用 Claude 或评估 LLM 的可靠性，这类一线观察比官方宣传更有参考价值。

📎 更多阅读：[Claude Says](https://ohhfishal.net/Posts/claude)

## Q4: Reverse Engineering Comanche Terrain Maps？

**A:** 有人把 1992 年经典直升机模拟游戏《Comanche: Maximum Overkill》的地形数据逆向出来了——这套地形系统当年靠体素渲染实现了远超同期游戏的地貌细节。值得关注是因为它揭示了 NovaLogic 那套体素引擎的内部数据格式，对复古游戏保存和引擎考古都挺有参考价值。

📎 更多阅读：[Reverse Engineering Comanche Terrain Maps](https://pikuma.com/blog/comanche-maps-reverse-engineering)

## Q5: MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching？

**A:** **一句话总结**：这篇论文提出 MintFlow，一种对 flow matching 生成轨迹做最小干预的约束采样方法——只在该动手的地方动手，而不是把整条生成路径推倒重来。

**为什么值得关注**：现有的约束采样器有个老毛病，为了满足观测数据或物理定律这类硬约束，往往会把样本推离预训练时学到的数据分布，生成结果既不符合约束也不像真实数据。MintFlow 的思路是只在轨迹上做「最小必要修改」，理论上能更好地兼顾约束满足和分布保真度。对做科学计算、逆问题、物理仿真生成这类需要「既要合规又要真实」的应用，是个值得跟进的方向。

📎 更多阅读：[MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

---
*有问题想问？欢迎在 GitHub 提 Issue~*