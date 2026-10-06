# ✨ 每日 AI Prompt 技巧 - 2026-10-06

> 从今天的 AI 圈热点里提炼出来的实用 Prompt 技巧 | 共 5 条

## 1. 💡 技巧 1

**这篇文章没有提供具体的 Prompt 技巧，也没有明确的 AI 使用建议可供提炼。内容仅为标题「Sharing AI Progress in Mathematics」，正文为空，无法据此总结出可用的 Prompt 工程最佳实践。**

📎 来源：[Sharing AI Progress in Mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/)

## 2. 💡 技巧 2

**这篇文章没有提供可提炼的 Prompt 技巧或 AI 使用建议；它只是 OpenAI 发布的一则公告/资源索引，说明其公开了一批数学手稿与配套证明工件（proof artifacts），但没有展开具体方法、提示词或使用指南。

如果必须从中归纳一条与 AI 相关的实践建议，只能是：**优先查阅第一手材料/配套工件来验证 AI 的数学产出。****

📎 来源：[Mathematical manuscripts and supporting proof artifacts produced by OpenAI](https://github.com/openai/math)

## 3. 💡 技巧 3

**这篇文章没有提供具体内容（标题和正文为空），因此无法从中提炼 Prompt 技巧或使用建议。

**建议**：请把 EmbeddingGemma 2 的正文、讨论或相关说明粘贴过来，我就能帮你提取可复用的 Prompt 技巧，或总结其中关于更好使用 AI 的建议。

如果你手头只有这个标题，可以先告诉我它的大致内容方向（比如是讲嵌入模型、多模态检索，还是模型部署），我也可以基于常见实践先给出一版通用建议。**

📎 来源：[EmbeddingGemma 2: An open, lightweight multimodal embedding model](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)

## 4. 💡 技巧 4

**这篇文章主要讲的是用 AI 辅助开发开源 AI 加速器（OpenTPU），并没有专门的 Prompt 技巧。可提炼的最佳实践是：**把复杂硬件项目拆成小模块，让 AI 逐个生成、迭代和验证，而不是一次性要求 AI 产出完整设计**。这样更容易调试、纠错，也更符合 AI 在长链路工程任务中的能力边界。**

📎 来源：[OpenTPU – An open-source AI accelerator, developed by AI](https://github.com/FeSens/openTPU)

## 5. 💡 技巧 5

**这篇文章的核心 Prompt 技巧是：**让 AI 主动为你撰写“下一步指令建议”，即让模型生成给用户看的推荐提示词**。

实践中可以这样用：在完成一次任务后，追加一句提示，如“请根据当前上下文，给我 3 个我接下来最可能想让你做的下一步指令建议，用简洁的一句话分别写出”。这样做能把模型对上下文的理解转化为可直接采用的后续 Prompt，减少你自己构思指令的成本，也让多轮交互更顺畅。**

📎 来源：[Claude Code’s suggested message feature: I think the real customer is the model](https://www.zohaib.cc/blog/smartest-claude-code-feature)

---
*试试这些技巧，你的 AI 输出质量会肉眼可见地提升！*