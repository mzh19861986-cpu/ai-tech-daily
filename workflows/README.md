# GitHub Actions 工作流

本目录存放 `.github/workflows/*.yml` 配置。后续 MVP 阶段在此填充。

## 设计原则

- 公开仓库 → Actions 分钟免费
- 单 job 控制在 **30 分钟内**（远低于 6 小时上限，留安全余量）
- 所有密钥走 `secrets.*`
- 失败时发通知（GitHub Issue / Discord webhook）

## 计划中的 workflow

| 文件 | 触发 | 用途 |
|------|------|------|
| `fetch.yml` | cron 每 6 小时 | 抓取数据源 → 写入 D1 |
| `generate.yml` | fetch 完成后 | AI 处理 → 生成内容草稿 |
| `publish.yml` | 手动 / 人工 approve 后 | 发布到各平台 |
| `report.yml` | 每周一 | 统计收入和运行情况 |

## 示例骨架（fetch.yml，待填充）

```yaml
name: Fetch Sources
on:
  schedule:
    - cron: '0 */6 * * *'
  workflow_dispatch:

jobs:
  fetch:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python -m agent.fetch
        env:
          CLOUDFLARE_API_TOKEN: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          D1_DATABASE_ID: ${{ secrets.D1_DATABASE_ID }}
```
