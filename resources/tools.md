# 技术工具链

## 一、运行时 / 托管

| 工具 | 用途 | 免费额度 | 商用 | 备注 |
|------|------|----------|------|------|
| GitHub Actions | 定时任务 / CI | 公开仓库无限 | 有限制 | 单 job 6h 上限；禁止挖矿/商业转售 |
| Cloudflare Workers | 边缘 API | 10 万次/天 | ✅ 免费层可商用 | 常驻服务首选 |
| Cloudflare Pages | 静态站托管 | 无限带宽 | ✅ | 比 Vercel Hobby 宽松，允许商业站 |
| Cloudflare D1 | SQLite 边缘数据库 | 5GB 存储 | ✅ | 适合中小数据量 |
| Cloudflare KV | 键值缓存 | 10 万次/天读 | ✅ | 会话/配置存储 |
| Supabase | 后端即服务 | 500MB DB + 50000 MAU | ✅ | 比 D1 功能全 |
| Vercel Hobby | 前端托管 | 100GB 带宽 | ❌ 收费需升级 Pro | TOS 限制商业用途 |

## 二、爬虫 / 数据获取

| 工具 | 用途 | 备注 |
|------|------|------|
| Crawl4AI | AI 友好网页爬虫 | 输出 markdown/JSON，Apache-2.0，~80k stars |
| Crawlee (Apify) | 爬虫框架 | 内置代理轮换、会话管理、反检测 |
| Playwright | 浏览器自动化 | JS/Python 都有，处理 JS 渲染页面 |
| requests / httpx | 轻量 HTTP | 简单 API 调用 |
| Feedparser | RSS 解析 | 订阅源抓取首选 |

## 三、AI / LLM

| 工具 | 用途 | 成本 | 备注 |
|------|------|------|------|
| g4f.dev (gpt4free) | 免 key 多模型客户端 | $0 | 不稳定，需做 fallback |
| OpenAI API | GPT-4o-mini 等 | 按量 | 稳定，适合生产 |
| DeepSeek API | 国产便宜模型 | 极低价 | 性价比高 |
| Gemini API | Google 模型 | 免费额度大 | 适合内容生成 |

## 四、内容生成 / 发布

| 工具 | 用途 | 备注 |
|------|------|------|
| ffmpeg | 音视频处理 | MoneyPrinter 系列常用 |
| PIL / Pillow | 图片处理 | 缩略图、加水印 |
| markdown → HTML | 内容渲染 | 静态站用 |
| Buttondown / Beehiiv | Newsletter | 邮件订阅变现 |

## 五、支付 / 变现

| 工具 | 用途 | 备注 |
|------|------|------|
| Stripe | 信用卡收款 | 最主流，需公司/个人资质 |
| x402 | API 微支付 | 超小额按次付费 |
| PayPal | 国际收款 | 个人可用 |
| Gumroad | 数字产品销售 | 自动发货，抽成 10% |
| Lemon Squeezy | 数字产品销售 | 包税务，抽成 5% |
| GitHub Sponsors | 开源赞助 | 平台不抽成 |

## 六、开发 / 编排

| 工具 | 用途 |
|------|------|
| n8n | 工作流自动化（自托管免费） |
| LangChain / LlamaIndex | Agent 框架 |
| SQLite / Turso | 本地/边缘数据库 |
| Git LFS | 大文件存储 |
