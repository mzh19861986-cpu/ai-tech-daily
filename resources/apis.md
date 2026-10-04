# 可用 API 清单

## 一、公开数据源（合规可抓）

| 数据源 | 内容 | 免费额度 | 备注 |
|--------|------|----------|------|
| Hacker News API | 科技新闻 | 免费无限 | Firebase 接口 |
| GitHub Trending | 趋势仓库 | 无官方 API，需爬页面 | 遵守 robots.txt |
| Reddit API | 社区内容 | 60 次/分钟（OAuth） | 需申请 app |
| Product Hunt API | 产品发布 | 免费有额度 | 需申请 token |
| HuggingFace API | 模型/数据集趋势 | 免费 | — |
| V2EX API | 国内技术社区 | 免费 | 有频率限制 |
| Google Trends | 搜索趋势 | pytrends 非官方 | 不稳定 |
| ArXiv API | 论文 | 免费 | OAI-PMH 接口 |
| Wikipedia API | 百科 | 免费 | 需加 User-Agent |

## 二、AI / LLM API

| 服务 | 免费额度 | 备注 |
|------|----------|------|
| Gemini API | 15 RPM 免费层 | 适合内容生成 |
| DeepSeek API | 注册送额度 | 极低价 |
| OpenAI API | 无免费层 | gpt-4o-mini 很便宜 |
| Groq | 免费快速推理 | 速度快 |
| Ollama（本地） | 免费 | 需自托管，GitHub Actions 跑不动大模型 |

## 三、支付 / 账单 API

| 服务 | 用途 |
|------|------|
| Stripe API | 创建支付链接、查询收入 |
| x402 | 微支付结算 |
| AdSense API | 收益查询（需审核） |

## 四、部署 / 基础设施 API

| 服务 | 用途 |
|------|------|
| Cloudflare API | 部署 Workers/Pages、操作 D1/KV |
| Supabase API | 数据库操作 |
| Vercel API | 部署（商业需 Pro） |

## 五、翻译 / 多语言

| 服务 | 免费额度 |
|------|----------|
| Google Translate | 免费 50 万字符/月 |
| DeepL | 免费 50 万字符/月 |
| LibreTranslate（自托管） | 免费 |
