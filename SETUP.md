# 部署配置指南

> 代码骨架已经全部写好，下面是你需要亲自操作的部分。
> 按顺序做完，就能在 GitHub 上自动跑起来。

---

## 第一步：创建 GitHub 仓库

1. 在 GitHub 上新建一个仓库（建议**公开**，Actions 分钟免费）
2. 把本地代码 push 上去：
   ```bash
   git init
   git add .
   git commit -m "init: AI agent passive income skeleton"
   git remote add origin https://github.com/<你的用户名>/<仓库名>.git
   git push -u origin main
   ```

---

## 第二步：配置 GitHub Secrets

进入仓库 → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

按需要添加以下 Secret：

| Secret 名称 | 是否必须 | 用途 | 获取方式 |
|-------------|---------|------|----------|
| `OPENAI_API_KEY` | ⭐ 推荐 | AI 摘要/内容生成 | [platform.openai.com](https://platform.openai.com/api-keys) |
| `OPENAI_BASE_URL` | 可选 | 用国产便宜模型时填 | DeepSeek: `https://api.deepseek.com/v1` |
| `OPENAI_MODEL` | 可选 | 指定模型名 | 默认 `gpt-4o-mini`，DeepSeek 填 `deepseek-chat` |
| `DISCORD_WEBHOOK` | 可选 | 运行结果推送到 Discord | Discord 服务器设置 → 整合 →  webhook |

> 💡 **不配 OPENAI_API_KEY 也能跑**，会自动降级用原文截断，只是内容质量差一点。

---

## 第三步：验证运行

1. 进入仓库 → **Actions** 标签
2. 左边选 **AI Daily Report**
3. 点 **Run workflow** → **Run workflow**（手动触发一次）
4. 看运行日志是否绿色通过
5. 运行成功后，`output/` 目录会多一个当天的 markdown 日报

---

## 第四步（可选）：扩展变现

跑通第一步后，再逐步加变现渠道：

### A. 挂 Google AdSense
1. 把 `output/` 目录的内容部署到 Cloudflare Pages
2. 申请 AdSense 审核（需要有一定内容量后再申请）

### B. 加更多数据源
在 `src/agent/agents/fetcher.py` 里加新的 `_fetch_xxx()` 方法：
- Reddit（需要申请 Reddit App 拿 client_id）
- Product Hunt（需要 token）
- 你感兴趣的任何 RSS 源

### C. 加多语言
在 `processor.py` 里加翻译步骤，把英文内容翻成中文/日文等。

---

## 配置优先级

| 阶段 | 配什么 | 能跑通什么 |
|------|--------|-----------|
| 🥉 最小可跑 | 不配任何 Secret | 抓 HN → 生成日报（降级模式） |
| 🥈 质量提升 | OPENAI_API_KEY | AI 摘要质量大幅提升 |
| 🥇 闭环变现 | + Cloudflare Pages + AdSense | 有真实流量开始赚钱 |

---

## 需要你告诉我 / 配合的

1. **你想用哪个 LLM？** OpenAI 官方、DeepSeek、还是 Gemini？
2. **你有 GitHub 账号吗？** 需要你自己建仓库 push 代码（我没法替你操作你的 GitHub）
3. **第一版先跑通哪个方向？** 我默认做了 AI 日报，你也可以说先做别的
