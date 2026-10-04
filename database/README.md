# 数据库设计说明

## 选型

推荐 **Cloudflare D1**（SQLite 兼容，免费 5GB），理由：
- 和 Cloudflare Workers/Pages 同一生态，延迟低
- GitHub Actions 可以直接用 REST API 写入
- 免费额度够早期使用

备选：Supabase（PostgreSQL，功能更全，免费 500MB）。

## 表结构概览

```
sources ──1:N──> pipelines ──1:N──> content_items ──1:N──> publications ──1:N──> revenue
                     │                                                    │
                     └──1:N──> runs                                       │
sources ──1:N──> compliance_checks                                        │
platforms ──1:N──> publications                                            │
platforms ──1:N──> revenue                                                │
```

## 核心表说明

### sources（数据源）
Agent 从哪里抓数据。每条记录对应一个 RSS/API/网页。
- `robots_checked`：上线前必须人工确认并标记为 1
- `rate_limit`：每秒请求数，默认保守值

### pipelines（任务流水线）
定义"从某个数据源 → 经过哪些步骤 → 产出什么"。
- `steps_json` 示例：
  ```json
  ["fetch", "filter_quality", "summarize", "translate:en->zh", "draft"]
  ```

### content_items（内容产物）
Agent 生成的文章/视频脚本/数据集条目。
- `status` 流转：draft → approved → published / failed
- `quality_score`：AI 自评，低于阈值的自动丢弃，不发布

### platforms / publications / revenue
变现闭环：
- `platforms.account_ref` 只存 GitHub Secret 的名字，**不存密钥明文**
- `revenue` 通过 webhook 回调写入，不依赖人工记账

### runs（运行日志）
每次 pipeline 执行留痕，方便排错和统计成本。

## 安全约束

- 所有第三方 API 密钥存 **GitHub Secrets**，数据库只存引用名
- 公开仓库里数据库 schema 可以公开，但**迁移数据（migrations）和真实数据绝不提交**
- `.gitignore` 必须包含 `*.db`、`*.sqlite`

## 部署方式

1. 在 Cloudflare 控制台创建 D1 数据库
2. 用 `npx wrangler d1 execute <db-name> --file=./schema.sql` 初始化
3. GitHub Actions 里通过 Cloudflare API 或 Workers 绑定写入
