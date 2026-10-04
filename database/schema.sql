-- ============================================================
-- AI Agent 被动收益自动化 - 数据库 Schema
-- 兼容 SQLite / Cloudflare D1
-- ============================================================

-- 1. 数据源：定义 Agent 从哪里抓数据
CREATE TABLE IF NOT EXISTS sources (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL UNIQUE,          -- 数据源名称
    type          TEXT NOT NULL,                 -- rss / api / html / github_trending
    url           TEXT NOT NULL,                 -- 抓取入口
    schedule_cron TEXT NOT NULL DEFAULT '0 */6 * * *',  -- 抓取频率
    rate_limit    INTEGER DEFAULT 60,            -- 每分钟最大请求数
    robots_checked INTEGER DEFAULT 0,           -- 是否已检查 robots.txt (0/1)
    is_active     INTEGER DEFAULT 1,             -- 是否启用
    last_fetched  TEXT,                          -- 上次抓取时间 ISO8601
    created_at    TEXT DEFAULT (datetime('now')),
    updated_at    TEXT DEFAULT (datetime('now'))
);

-- 2. 任务流水线：定义 Agent 做什么
CREATE TABLE IF NOT EXISTS pipelines (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL UNIQUE,          -- 流水线名称
    description   TEXT,
    source_id     INTEGER REFERENCES sources(id), -- 输入数据源
    steps_json    TEXT NOT NULL,                 -- JSON 数组：处理步骤
    output_type   TEXT NOT NULL,                 -- article / video / api_response / dataset
    schedule_cron TEXT NOT NULL,                 -- 执行频率
    is_active     INTEGER DEFAULT 1,
    created_at    TEXT DEFAULT (datetime('now')),
    updated_at    TEXT DEFAULT (datetime('now'))
);

-- 3. 内容条目：Agent 生成的产物
CREATE TABLE IF NOT EXISTS content_items (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    pipeline_id   INTEGER REFERENCES pipelines(id),
    source_item_id TEXT,                         -- 原始数据源 ID（去重用）
    title         TEXT NOT NULL,
    body_markdown TEXT,
    summary       TEXT,
    language      TEXT DEFAULT 'en',
    status        TEXT DEFAULT 'draft',          -- draft / approved / published / failed
    quality_score REAL,                          -- AI 自评质量分 0-10
    created_at    TEXT DEFAULT (datetime('now')),
    published_at  TEXT
);

-- 4. 发布平台
CREATE TABLE IF NOT EXISTS platforms (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL UNIQUE,          -- adsense / gumroad / stripe / medium ...
    type          TEXT NOT NULL,                 -- ad / digital_product / api / sponsorship
    account_ref   TEXT NOT NULL,                 -- 密钥引用名（存 GitHub Secret 名，不存明文）
    payout_minimum REAL DEFAULT 0,               -- 最低提现额
    is_active     INTEGER DEFAULT 1,
    created_at    TEXT DEFAULT (datetime('now'))
);

-- 5. 发布记录：内容发到了哪个平台
CREATE TABLE IF NOT EXISTS publications (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    content_id    INTEGER REFERENCES content_items(id),
    platform_id   INTEGER REFERENCES platforms(id),
    external_url  TEXT,                          -- 发布后的外部链接
    external_id   TEXT,                          -- 平台侧 ID
    status        TEXT DEFAULT 'pending',        -- pending / published / failed
    error_msg     TEXT,
    published_at  TEXT,
    created_at    TEXT DEFAULT (datetime('now'))
);

-- 6. 收入记录
CREATE TABLE IF NOT EXISTS revenue (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    platform_id   INTEGER REFERENCES platforms(id),
    publication_id INTEGER REFERENCES publications(id),
    amount        REAL NOT NULL,                 -- 收入金额
    currency      TEXT DEFAULT 'USD',
    occurred_at   TEXT NOT NULL,                 -- 收入发生时间
    raw_payload   TEXT,                          -- 原始回调 JSON
    created_at    TEXT DEFAULT (datetime('now'))
);

-- 7. 运行日志：每次 pipeline 执行的记录
CREATE TABLE IF NOT EXISTS runs (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    pipeline_id   INTEGER REFERENCES pipelines(id),
    trigger_type  TEXT NOT NULL,                 -- scheduled / manual / webhook
    status        TEXT DEFAULT 'running',       -- running / success / failed / timeout
    items_fetched INTEGER DEFAULT 0,
    items_published INTEGER DEFAULT 0,
    error_msg     TEXT,
    started_at    TEXT DEFAULT (datetime('now')),
    finished_at   TEXT
);

-- 8. 合规检查记录
CREATE TABLE IF NOT EXISTS compliance_checks (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id     INTEGER REFERENCES sources(id),
    check_type    TEXT NOT NULL,                 -- robots_txt / terms_of_service / copyright
    result        TEXT NOT NULL,                 -- pass / fail / warning
    details       TEXT,
    checked_at    TEXT DEFAULT (datetime('now'))
);

-- ============================================================
-- 索引
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_content_status ON content_items(status);
CREATE INDEX IF NOT EXISTS idx_runs_pipeline ON runs(pipeline_id, started_at DESC);
CREATE INDEX IF NOT EXISTS idx_revenue_platform ON revenue(platform_id, occurred_at DESC);
CREATE INDEX IF NOT EXISTS idx_publications_content ON publications(content_id);

-- ============================================================
-- 初始示例数据
-- ============================================================
INSERT OR IGNORE INTO sources (name, type, url, schedule_cron) VALUES
    ('Hacker News', 'rss', 'https://news.ycombinator.com/rss', '0 */6 * * *'),
    ('GitHub Trending', 'html', 'https://github.com/trending', '0 0 * * *'),
    ('Product Hunt', 'api', 'https://api.producthunt.com/v2/api/graphql', '0 8 * * *');
