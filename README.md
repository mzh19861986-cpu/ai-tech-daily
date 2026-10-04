# AI Agent 被动收益自动化 — 可行性盘点

> 目标：用 AI Agent 在全网自动执行可产生被动收益的工作，在 GitHub 上全自动运行。
> 本文档为第一阶段交付：资源库 + 数据库 schema + 可行性结论。

---

## 一、结论先行

**部分可行，但"全自动全智能躺赚"不现实。** 诚实的判断如下：

| 维度 | 判断 | 说明 |
|------|------|------|
| 技术可行性 | ✅ 可行 | GitHub Actions + Cloudflare Workers + 免费 AI API 可以搭出定时跑的自动化流水线 |
| 法律合规 | ⚠️ 有条件可行 | 只能走"公开数据 + 自己生产内容 + 合法 API"路线；爬虫灰产、批量账号、刷量全部排除 |
| 收益规模 | ❌ 预期要低 | 免费层 + 自动化 = 每月几美元到几百美元量级，不是"睡后收入过万" |
| 全自动化 | ⚠️ 半自动 | 支付/提现/合规审批必须人工或半人工闭环，Agent 不能自己收钱 |
| GitHub 托管 | ⚠️ 有限制 | Actions 单 job 6 小时上限、禁止商业用途滥用、出口 IP 是数据中心 IP 易被封 |

**一句话：能做，但定位是"自动化内容/工具微收入"，不是"AI 替你全网捞钱"。**

---

## 二、GitHub 平台硬限制（必须先记住）

来自 [GitHub 官方条款](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features)：

### 明确禁止
- ❌ 加密货币挖矿
- ❌ 未经授权访问任何服务/设备/数据/账号
- ❌ 将 GitHub Actions 本身作为商业服务转售
- ❌ GitHub Pages 用于商业电商/SaaS 网站

### 技术限制
- 单 job 最长 **6 小时**
- 整个 workflow run 最长 **35 天**
- 公开仓库 Actions 分钟**免费**
- 私有仓库有免费额度，超出按分钟计费
- API 限速：认证后每小时 ~1000 次
- 出口 IP 是 GitHub 数据中心 IP，大量反爬网站会直接封

### 推论
- GitHub Actions **只适合定时短任务**（每天跑一次、每次几分钟），不适合常驻服务
- 常驻 API 服务要放在 **Cloudflare Workers**（免费商用、10 万次/天）
- 数据库用 **Cloudflare D1/KV** 或 **Supabase**，不要靠 GitHub 文件当数据库

---

## 三、可行的被动收益模式（按推荐度排序）

### 🟢 第一梯队（合规、技术成熟、已有成功案例）

1. **内容聚合站 + AdSense / 联盟营销**
   - 每天定时抓取公开数据源（HN、GitHub Trending、Reddit、Product Hunt）
   - AI 生成多语言摘要/翻译/解读
   - 部署到 Cloudflare Pages，挂 Google AdSense 或联盟链接
   - 参考：掘金那篇 "Cloudflare Workers + GitHub Actions AI 日报"

2. **微工具 / API 服务 + 按次付费**
   - 用 AI 做一个单点工具（如 HS Code 分类、图片压缩、文本翻译 API）
   - 部署在 Cloudflare Workers，用 x402 / Stripe 收款
   - GitHub Actions 只负责定时维护/更新

3. **开源项目 + GitHub Sponsors**
   - 把自动化工具本身开源，靠赞助和 Stars 变现
   - 门槛：项目要有真实使用价值，不是玩具

### 🟡 第二梯队（可行但有摩擦）

4. **数字产品自动化生成**
   - AI 自动生成 Notion 模板、Resume 模板、壁纸、Prompt 包
   - 挂 Gumroad / Lemon Squeezy 自动发货
   - 需要人工做一次产品模板，Agent 只负责变体生成和上架

5. **定时简报 / Newsletter 订阅**
   - 每天/每周自动抓行业信息，AI 整理成简报
   - 用 Buttondown / Beehiiv 发邮件，靠订阅费或广告变现
   - 需要持续维护内容质量

### 🔴 第三梯队（高风险/大概率不可行）

6. **大规模爬虫抓数据卖数据集** — 违反多数网站 ToS，数据清洗成本极高
7. **批量社媒账号自动发帖** — 平台反作弊严格，极易封号
8. **自动接任务/自动投标（如 Upwork/MoltJobs）** — 需要实名认证和人工交付，Agent 做不了最后一公里
9. **自动交易 / 量化** — 资金风险极大，不在本项目范围

---

## 四、推荐技术架构

```
┌─────────────────────────────────────────────────┐
│  GitHub 仓库（公开）                              │
│  ├─ .github/workflows/*.yml  ← 定时触发          │
│  ├─ src/agent/               ← Agent 核心代码    │
│  └─ data/                    ← JSON 数据快照      │
└──────────────┬──────────────────────────────────┘
               │ 每 N 小时 cron 触发
               ▼
┌─────────────────────────────────────────────────┐
│  GitHub Actions Runner（6h 内跑完）              │
│  ├─ 抓取公开数据源（Crawl4AI / requests）         │
│  ├─ AI 处理（LLM API：摘要/翻译/改写）           │
│  ├─ 写入数据库（Cloudflare D1 / Supabase）       │
│  └─ 提交产物（commit JSON / 触发部署）            │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────┐
│  Cloudflare 边缘层（免费商用）                   │
│  ├─ Pages：静态内容站 / 工具首页                 │
│  ├─ Workers：API 端点 / 支付回调                 │
│  ├─ D1：SQLite 数据库                           │
│  └─ KV：键值缓存                                 │
└──────────────┬──────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────┐
│  变现层（人工配置一次，自动运行）                 │
│  ├─ Google AdSense（内容站）                     │
│  ├─ Stripe / x402（API 付费）                   │
│  ├─ GitHub Sponsors（开源赞助）                  │
│  └─ Gumroad（数字产品）                          │
└─────────────────────────────────────────────────┘
```

---

## 五、下一步建议

1. **先选 1 个方向做 MVP**：推荐"内容聚合站 + AdSense"，技术最简单、闭环最短
2. **不要一上来做多 Agent 全自动化**：先做单流水线（抓 → AI 处理 → 发布），跑通再扩展
3. **人工闭环不能省**：支付账号、税务、内容审核必须有人兜底
4. **先跑 1 个月看真实数据**：再决定要不要加大投入

---

## 目录结构

```
├── README.md               ← 本文件（可行性盘点）
├── resources/              ← 资源库
│   ├── reference-projects.md   同类参考项目
│   ├── tools.md               工具链
│   ├── platforms.md           可变现平台
│   ├── apis.md                可用 API
│   └── compliance.md          合规红线
├── database/               ← 数据库设计
│   ├── schema.sql             SQL schema
│   └── README.md               设计说明
└── workflows/              ← GitHub Actions 工作流（后续填充）
    └── README.md
```
