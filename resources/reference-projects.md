# 同类参考项目

## 一、自动化收入 / Agent 变现

### 1. MoneyPrinterV2
- **仓库**：`FujiwaraChoki/MoneyPrinterV2`
- **定位**：自动化在线收入的 Python 应用，模块化架构
- **可借鉴**：流水线设计、模块化任务定义、多平台发布
- **注意**：项目偏激进，需自行过滤违规部分

### 2. OpenClaw
- **定位**：开源多 Agent 自动化执行引擎，内置商业化能力（收益统计、订单对账、多账号矩阵）
- **可借鉴**：Skill/指令/调度的分层设计、内置变现闭环
- **注意**：防风控/多账号部分涉及灰色地带，谨慎参考

### 3. GPT Researcher
- **仓库**：`assafelovic/gpt-researcher`（28.9k+ stars）
- **定位**：深度研究 Agent，自动规划调研流程、抓取信息、生成带引用的报告
- **可借鉴**：研究任务拆解、报告生成 pipeline、引用管理

### 4. Agent that pays its own bills（x402 案例）
- **技术栈**：Python stdlib + Cloudflare Workers/KV + GitHub Pages + Windows Task Scheduler
- **模式**：Agent 自动在 MoltJobs 上投标并完成任务，用 x402 微支付覆盖 API 成本
- **可借鉴**：Agent 自付成本的闭环思路

## 二、内容聚合 / 日报类

### 5. AI 日报（Cloudflare Workers + GitHub Actions）
- **来源**：掘金 HashTang 的文章
- **模式**：每天 UTC 00:00 抓 HN、GitHub Trending、Product Hunt、HuggingFace、Reddit 12 个子版、V2EX、Google Trends
- **成本**：约 $2.5/月
- **可借鉴**：多源抓取 → AI 摘要 → 发布的完整闭环

### 6. 80+ 网站零成本运营栈
- **技术栈**：Cloudflare DNS + GitHub Actions cron + g4f.dev 免 key AI
- **模式**：Git-as-DB，定时爬虫 → commit JSON → 静态站
- **可借鉴**：极致低成本架构

## 三、Agent 框架

### 7. AutoAgent (HKUDS)
- **定位**：全自动化零代码 LLM Agent 框架，支持 Web Agent 和 Coding Agent
- **可借鉴**：Agent 自动化任务拆解

### 8. MetaGPT
- **仓库**：`FoundationAgents/MetaGPT`（70k+ stars）
- **定位**：软件公司式多角色协作（PM、开发、测试）
- **可借鉴**：多 Agent 角色分工

### 9. Crawl4AI
- **仓库**：~80k stars，Apache-2.0
- **定位**：AI 友好的网页爬虫，输出 LLM-ready markdown / JSON
- **可借鉴**：作为 Agent 的网页数据获取层

## 四、微 SaaS / 边缘变现

### 10. RepoAccess
- **定位**：卖私有 GitHub repo 访问权，Cloudflare Worker 单文件运行
- **模式**：买家付款 → 自动邀请进 GitHub team → 退款/拒付自动收回
- **可借鉴**：支付 → 权限自动联动的闭环

### 11. x402 微支付 API
- **定位**：按次付费的 API 结算协议
- **案例**：有人 2 天建了 26 个 MCP server 用 x402 变现
- **可借鉴**：超小额 API 变现的支付层

---

## 调研来源
- GitHub Awesome Lists、Indie Hackers、掘金、腾讯云开发者社区、CSDN
