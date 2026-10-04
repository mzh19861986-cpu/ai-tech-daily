# 5 分钟部署上线指南

> 照着做，完了之后每天早上自动生成三份技术日报。

---

## 第 1 步：建 GitHub 仓库

1. 打开 https://github.com/new
2. 仓库名随便起，比如 `ai-tech-daily`
3. 选 **Public**（公开，Actions 免费）
4. 不要勾选 README/gitignore/license（本地已经有了）
5. 点 **Create repository**

---

## 第 2 步：把代码 push 上去

打开终端，进入项目目录，执行：

```bash
cd C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2

git init
git add .
git commit -m "init: AI agent multi-pipeline"
git branch -M main
git remote add origin https://github.com/<你的用户名>/<仓库名>.git
git push -u origin main
```

---

## 第 3 步：配置 Secrets

进入仓库 → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

添加这 3 个：

| Name | Value |
|------|-------|
| `OPENAI_API_KEY` | `<你的 Gemini API Key>` |
| `OPENAI_BASE_URL` | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| `OPENAI_MODEL` | `gemini-3.8-flash` |

---

## 第 4 步：手动跑一次验证

1. 仓库 → **Actions** 标签
2. 左边选 **AI Daily Reports**
3. 点 **Run workflow** → 绿色按钮
4. 等 5-10 分钟跑完（Gemini 限流，慢一点正常）
5. 跑完后看 `output/` 目录，应该有 3 份日报

---

## 跑完之后你会得到什么

每天自动生成 3 份 markdown 日报：
- `ai_daily-YYYY-MM-DD.md` — 英文版技术日报
- `ai_daily_cn-YYYY-MM-DD.md` — 中文版技术日报（AI 自动翻译）
- `ai_deepdive-YYYY-MM-DD.md` — 热门 3 条深度分析

全部自动 commit 到仓库，你可以直接拿去发公众号、小红书、或者挂 Cloudflare Pages 放广告。

---

## 常见问题

**Q: 跑失败了怎么办？**
A: 点进 Actions 里的失败记录，看红色报错。最常见的是 Gemini 限流，等一分钟再手动跑一次就行。

**Q: 怎么加更多数据源？**
A: 改 `src/agent/agents/fetcher.py`，加一个 `_fetch_xxx()` 方法就行。

**Q: 想换别的 AI 模型？**
A: 改 Secrets 里的三个变量就行，不用改代码。
