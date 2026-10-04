"""
把 output/ 目录下的 markdown 日报转成静态 HTML 网站，部署到 GitHub Pages。
"""
import os
import re
from pathlib import Path
from datetime import datetime

import markdown as md

ROOT = Path(__file__).parent.parent
OUTPUT_DIR = ROOT / "output"
SITE_DIR = ROOT / "site"

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - AI Tech Daily</title>
    <meta name="description" content="AI 自动生成的技术日报，每日更新，追踪最新 AI 动态、开源工具和技术趋势">
    <style>
        * {{ box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 760px; margin: 0 auto; padding: 2rem 1.5rem; line-height: 1.7; color: #24292e; background: #fafbfc; }}
        h1 {{ border-bottom: 2px solid #e1e4e8; padding-bottom: 0.5rem; }}
        h2 {{ margin-top: 2rem; color: #24292e; }}
        a {{ color: #0366d6; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .meta {{ color: #6a737d; font-size: 0.9rem; margin-bottom: 2rem; }}
        .nav {{ margin-bottom: 2rem; padding: 1rem; background: white; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
        .nav a {{ margin-right: 1rem; }}
        .post-list {{ list-style: none; padding: 0; }}
        .post-list li {{ padding: 1rem; margin-bottom: 0.8rem; background: white; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); transition: transform 0.2s; }}
        .post-list li:hover {{ transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
        .post-list .date {{ color: #6a737d; font-size: 0.85rem; margin-right: 1rem; }}
        .newsletter-box {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1.5rem; border-radius: 8px; margin: 2rem 0; }}
        .newsletter-box h3 {{ margin-top: 0; }}
        .newsletter-box input {{ width: 100%; padding: 0.6rem; border: none; border-radius: 4px; margin: 0.5rem 0; }}
        .newsletter-box button {{ background: white; color: #667eea; border: none; padding: 0.6rem 1.5rem; border-radius: 4px; font-weight: bold; cursor: pointer; }}
        .sponsor-box {{ background: #fff3cd; border: 1px solid #ffeaa7; padding: 1rem; border-radius: 8px; margin: 1.5rem 0; text-align: center; }}
        .content {{ background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <nav class="nav">
        <a href="/">🏠 Home</a>
        <a href="/status.html">📊 Status</a>
        <a href="https://github.com/mzh19861986-cpu/ai-tech-daily">GitHub</a>
        <a href="/feed.xml">📡 RSS</a>
        <a href="https://github.com/sponsors/mzh19861986-cpu">❤️ Sponsor</a>
    </nav>
    <div class="content">
    {content}
    </div>
    <div class="newsletter-box">
        <h3>📬 订阅每日 Newsletter</h3>
        <p>每天早上收到最新的 AI 技术日报，直接发到你的邮箱。</p>
        <form action="https://buttondown.email/api/emails/embed-subscribe/ai-tech-daily" method="post" target="popupwindow" onsubmit="window.open('https://buttondown.email/ai-tech-daily', 'popupwindow')">
            <input type="email" name="email" placeholder="you@example.com" required>
            <button type="submit">免费订阅</button>
        </form>
    </div>

    <div style="background: #f0f7ff; border: 1px solid #cce5ff; padding: 1rem; border-radius: 8px; margin: 1.5rem 0;">
        <h4 style="margin-top: 0;">🛠️ 你可能也喜欢</h4>
        <ul style="text-align: left; margin: 0.5rem 0; padding-left: 1.2rem;">
            <li>🤖 <a href="https://deepseek.com/" target="_blank">DeepSeek API</a> - 高性价比大模型，开发者必备</li>
            <li>📝 <a href="https://www.notion.so/" target="_blank">Notion</a> - 笔记+项目管理神器</li>
            <li>☁️ <a href="https://vercel.com/" target="_blank">Vercel</a> - 前端一键部署</li>
        </ul>
    </div>

    <div class="sponsor-box">
        <p>☕ 觉得有用？请我喝杯咖啡支持一下！</p>
        <a href="https://github.com/sponsors/mzh19861986-cpu" style="color: #d63031; font-weight: bold;">GitHub Sponsors →</a>
    </div>
    <footer style="margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #e1e4e8; color: #6a737d; font-size: 0.85rem; text-align: center;">
        <p>由 AI Agent 自动生成 | 每日更新 | <a href="https://github.com/mzh19861986-cpu/ai-tech-daily">Star on GitHub</a></p>
    </footer>
</body>
</html>
"""


def md_to_html(md_path: Path) -> tuple[str, str]:
    """把 markdown 文件转成 HTML，返回 (title, html_body)"""
    text = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1) if title_match else md_path.stem

    html_body = md.markdown(text, extensions=["fenced_code", "tables"])
    return title, html_body


def build_index(posts: list[dict]) -> str:
    """构建首页"""
    posts_html = "\n".join([
        f'<li><span class="date">{p["date"]}</span><a href="{p["slug"]}.html">{p["title"]}</a></li>'
        for p in sorted(posts, key=lambda x: x["date"], reverse=True)
    ])
    content = f"""
    <h1>🤖 AI Tech Daily</h1>
    <p class="meta">AI 自动抓取、AI 摘要、每日更新 | 共 {len(posts)} 篇</p>

    <div class="sponsor-box" style="background: #e3f2fd; border-color: #90caf9;">
        <h3 style="margin-top:0;">🛠️ 开发者推荐工具</h3>
        <p style="margin-bottom: 0.5rem;">这些是我们每天都在用的效率工具，推荐给你：</p>
        <ul style="text-align: left; display: inline-block; margin: 0.5rem 0;">
            <li>🔧 <a href="https://github.com/sponsors" target="_blank">GitHub Sponsors</a> - 支持开源项目</li>
            <li>☁️ <a href="https://pages.github.com/" target="_blank">GitHub Pages</a> - 免费托管静态网站</li>
            <li>🤖 <a href="https://deepseek.com/" target="_blank">DeepSeek</a> - 高性价比 AI 大模型</li>
        </ul>
    </div>

    <h2>最新日报</h2>
    <ul class="post-list">
        {posts_html}
    </ul>
    """
    return TEMPLATE.format(title="Home", content=content)


def build_status() -> str:
    """构建系统状态页"""
    pipelines = [
        {"name": "ai_daily", "cn": "英文技术日报", "status": "✅ 运行中", "items": 2},
        {"name": "ai_daily_cn", "cn": "中文技术日报", "status": "✅ 运行中", "items": 2},
        {"name": "ai_deepdive", "cn": "深度分析", "status": "✅ 运行中", "items": 2},
        {"name": "scored_briefing", "cn": "AI 热度排行榜", "status": "✅ 运行中", "items": 2},
        {"name": "weekly_digest", "cn": "每周精选", "status": "✅ 运行中", "items": 2},
        {"name": "github_tools", "cn": "GitHub 工具推荐", "status": "✅ 运行中", "items": 8},
        {"name": "free_ai_tools", "cn": "免费 AI 工具汇总", "status": "✅ 运行中", "items": 1},
        {"name": "reddit_digest", "cn": "Reddit 摘要", "status": "❌ 数据源不可达", "items": 0},
    ]
    sources = [
        {"name": "Hacker News", "status": "✅ 正常"},
        {"name": "Lobsters", "status": "✅ 正常"},
        {"name": "ArXiv AI 论文", "status": "❌ 抓取失败"},
        {"name": "GitHub Trending", "status": "✅ 已修复"},
        {"name": "Reddit", "status": "❌ 连接超时"},
        {"name": "Product Hunt", "status": "⏳ 待验证"},
        {"name": "Dev.to", "status": "⏳ 待验证"},
    ]
    rows = "\n".join([
        f"<tr><td>{p['name']}</td><td>{p['cn']}</td><td>{p['status']}</td><td>{p['items']} 条/次</td></tr>"
        for p in pipelines
    ])
    src_rows = "\n".join([
        f"<tr><td>{s['name']}</td><td>{s['status']}</td></tr>"
        for s in sources
    ])
    content = f"""
    <h1>📊 系统状态 Dashboard</h1>
    <p class="meta">多 Agent 自动化系统实时状态</p>

    <h2>🤖 子智能体（Pipeline）</h2>
    <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
        <tr style="background: #f5f5f5;"><th style="padding: 0.5rem; border: 1px solid #ddd;">Pipeline</th><th style="padding: 0.5rem; border: 1px solid #ddd;">中文名</th><th style="padding: 0.5rem; border: 1px solid #ddd;">状态</th><th style="padding: 0.5rem; border: 1px solid #ddd;">每次产出</th></tr>
        {rows}
    </table>

    <h2>📡 数据源状态</h2>
    <table style="width:100%; border-collapse: collapse; margin: 1rem 0;">
        <tr style="background: #f5f5f5;"><th style="padding: 0.5rem; border: 1px solid #ddd;">数据源</th><th style="padding: 0.5rem; border: 1px solid #ddd;">状态</th></tr>
        {src_rows}
    </table>

    <h2>💰 变现入口</h2>
    <ul>
        <li>✅ GitHub Sponsors 赞助按钮</li>
        <li>✅ Newsletter 订阅框</li>
        <li>✅ RSS Feed 订阅</li>
        <li>✅ 推荐工具区块（首页）</li>
        <li>⏳ 联盟营销链接（待加）</li>
    </ul>

    <div style="margin-top: 2rem; padding: 1rem; background: #e8f5e9; border-left: 4px solid #4caf50;">
        <strong>💡 说明：</strong>本系统由母体 Orchestrator 管控，多个子 Agent 并行运行，
        自动抓取数据 → DeepSeek AI 处理 → 生成内容 → 发布到 GitHub Pages。
        全自动滚动运行，持续迭代新方向。
    </div>
    """
    return TEMPLATE.format(title="Status", content=content)


def build_rss(posts: list[dict]) -> str:
    """生成 RSS feed"""
    base_url = "https://mzh19861986-cpu.github.io/ai-tech-daily"
    items_xml = "\n".join([
        f"""<item>
            <title>{p['title']}</title>
            <link>{base_url}/{p['slug']}.html</link>
            <pubDate>{p['date']}</pubDate>
            <guid>{base_url}/{p['slug']}.html</guid>
        </item>"""
        for p in sorted(posts, key=lambda x: x["date"], reverse=True)[:20]
    ])
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>AI Tech Daily</title>
    <link>{base_url}</link>
    <description>AI 自动生成的技术日报，每日更新</description>
    <language>zh-CN</language>
    {items_xml}
</channel>
</rss>"""


def main():
    SITE_DIR.mkdir(exist_ok=True)
    posts = []

    if not OUTPUT_DIR.exists():
        print("output/ directory not found, skipping")
        return

    for md_file in sorted(OUTPUT_DIR.glob("*.md")):
        title, html_body = md_to_html(md_file)
        slug = md_file.stem
        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", slug)
        date = date_match.group(1) if date_match else ""

        full_html = TEMPLATE.format(title=title, content=html_body)
        (SITE_DIR / f"{slug}.html").write_text(full_html, encoding="utf-8")
        posts.append({"title": title, "slug": slug, "date": date})
        print(f"Generated: {slug}.html")

    index_html = build_index(posts)
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"Generated index.html with {len(posts)} posts")

    # 生成系统状态页
    status_html = build_status()
    (SITE_DIR / "status.html").write_text(status_html, encoding="utf-8")
    print("Generated status.html")

    # 生成 RSS feed
    rss_xml = build_rss(posts)
    (SITE_DIR / "feed.xml").write_text(rss_xml, encoding="utf-8")
    print("Generated feed.xml")


if __name__ == "__main__":
    main()
