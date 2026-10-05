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
    <meta name="description" content="{description}">
    <meta name="keywords" content="AI, 人工智能, 技术日报, GitHub, 开源工具, Product Hunt, 开发技巧, LLM, AI Agent">
    <meta name="author" content="AI Tech Daily">
    <meta property="og:title" content="{title} - AI Tech Daily">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "AI Tech Daily",
      "description": "每天 5 分钟，了解 AI 圈最重要的事。由 AI Agent 自动抓取、分析、生成。",
      "url": "https://mzh19861986-cpu.github.io/ai-tech-daily/"
    }}
    </script>
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans SC', Roboto, sans-serif;
            max-width: 720px; margin: 0 auto; padding: 2rem 1.5rem; line-height: 1.7;
            color: #1a1a1a;
            background: #ffffff;
            transition: background 0.3s, color 0.3s;
            -webkit-font-smoothing: antialiased;
        }}
        body.dark {{
            color: #e6e6e6;
            background: #0a0a0a;
        }}
        body.dark h2 {{ color: #e6e6e6; border-top-color: #2a2a2a; }}
        body.dark a {{ color: #60a5fa; }}
        body.dark .meta {{ color: #888; }}
        body.dark .nav {{ background: rgba(20,20,20,0.8); border-color: #2a2a2a; }}
        body.dark .post-list li {{ background: #1a1a1a; border-color: #2a2a2a; }}
        body.dark .post-list li:hover {{ background: #222; border-color: #333; }}
        body.dark .post-list a {{ color: #e6e6e6; }}
        body.dark div[style*="background: #fafafa"] {{ background: #1a1a1a !important; border-color: #2a2a2a !important; }}
        h1, h2, h3 {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans SC', Roboto, sans-serif;
            line-height: 1.3;
        }}
        h1 {{
            border-bottom: none; padding-bottom: 0.5rem;
            font-weight: 700; font-size: 2rem;
        }}
        h2 {{ margin-top: 2.5rem; color: #1a1a1a; font-weight: 600; font-size: 1.35rem; }}
        h3 {{ margin-top: 2rem; color: #1a1a1a; font-weight: 600; font-size: 1.15rem; }}
        p {{ margin: 1rem 0; }}
        code {{
            background: #f4f4f4; padding: 0.2em 0.4em; border-radius: 4px;
            font-size: 0.9em; font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
        }}
        pre {{
            background: #1a1a1a; color: #e6e6e6; padding: 1.25rem; border-radius: 10px;
            overflow-x: auto; margin: 1.5rem 0;
        }}
        pre code {{ background: none; padding: 0; }}
        blockquote {{
            border-left: 3px solid #eaeaea; margin: 1.5rem 0; padding: 0.5rem 1rem;
            color: #666;
        }}
        a {{ color: #1a1a1a; text-decoration: none; font-weight: 500; }}
        a:hover {{ opacity: 0.7; }}
        .meta {{ color: #6a737d; font-size: 0.9rem; margin-bottom: 2rem; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }}
        .nav {{
            margin-bottom: 2rem; padding: 0.75rem 1rem;
            background: rgba(255,255,255,0.8); backdrop-filter: blur(10px);
            border-radius: 8px; border: 1px solid #eaeaea;
        }}
        .nav a {{ margin-right: 1.5rem; font-weight: 500; }}
        .post-list {{ list-style: none; padding: 0; }}
        .post-list li {{
            padding: 1.25rem; margin-bottom: 0.75rem;
            border: 1px solid #eaeaea;
            border-radius: 10px;
            transition: all 0.2s ease;
            background: #ffffff;
        }}
        .post-list li:hover {{
            border-color: #d0d0d0;
            background: #fafafa;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }}
        .post-list li:last-child {{ border-bottom: none; }}
        .post-list a {{ font-size: 1.05rem; font-weight: 600; color: #1a1a1a; }}
        .post-list .date {{ color: #999; font-size: 0.8rem; margin-right: 0.75rem; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }}
        .newsletter-box {{
            background: #1a1a1a;
            color: white; padding: 2rem; border-radius: 12px; margin: 2.5rem 0;
        }}
        .newsletter-box h3 {{ margin-top: 0; font-size: 1.25rem; font-weight: 600; }}
        .newsletter-box input {{
            width: 100%; padding: 0.75rem 1rem; border: none; border-radius: 8px;
            margin: 0.75rem 0; font-size: 0.95rem;
        }}
        .newsletter-box button {{
            background: white; color: #1a1a1a; border: none;
            padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600;
            cursor: pointer; font-size: 0.95rem; transition: all 0.2s;
        }}
        .newsletter-box button:hover {{ opacity: 0.9; }}
        .sponsor-box {{
            background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
            border: none; padding: 1.5rem; border-radius: 12px; margin: 1.5rem 0;
            text-align: center; box-shadow: 0 4px 15px rgba(253,203,110,0.3);
        }}
        .content {{
            background: transparent;
            padding: 1rem 0;
        }}
        .content h2 {{
            margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid #e1e4e8;
        }}
        .content p {{ margin: 1.2rem 0; }}
        .content blockquote {{
            border-left: 3px solid #6c5ce7; padding-left: 1rem;
            margin-left: 0; color: #636e72; font-style: italic;
        }}
        .content code {{
            background: #f1f3f5; padding: 0.2rem 0.4rem; border-radius: 4px;
            font-family: 'SF Mono', Monaco, monospace; font-size: 0.9rem;
        }}
        .article-meta {{
            color: #95a5a6; font-size: 0.9rem; margin-bottom: 2rem;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        .share-buttons {{
            margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid #e1e4e8;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        .share-buttons a {{
            display: inline-block; margin-right: 1rem; padding: 0.5rem 1rem;
            border-radius: 8px; font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <nav class="nav">
        <a href="./">🏠 Home</a>
        <a href="./tools.html">🛠️ Tools</a>
        <a href="./monetization.html">💰 Monetize</a>
        <a href="./about.html">ℹ️ About</a>
        <a href="./status.html">📊 Status</a>
        <a href="./sponsor.html">💛 Sponsor</a>
        <a href="./feed.xml">📡 RSS</a>
        <input type="search" id="searchInput" placeholder="🔍 搜索文章..." style="float: right; padding: 0.3rem 0.8rem; border: 1px solid #ddd; border-radius: 20px; font-size: 0.9rem; width: 150px;">
        <button onclick="document.body.classList.toggle('dark')" style="float: right; background: none; border: 1px solid #ddd; border-radius: 20px; padding: 0.3rem 0.8rem; cursor: pointer; font-size: 0.9rem; margin-right: 0.5rem;">🌙 暗色</button>
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
            <li>🐳 <a href="https://www.docker.com/" target="_blank">Docker</a> - 容器化部署</li>
            <li>📊 <a href="https://www.postman.com/" target="_blank">Postman</a> - API 测试工具</li>
        </ul>
    </div>

    <div class="sponsor-box">
        <p>☕ 觉得有用？请我喝杯咖啡支持一下！</p>
        <a href="https://github.com/sponsors/mzh19861986-cpu" style="color: #d63031; font-weight: bold;">GitHub Sponsors →</a>
    </div>
    <footer style="margin-top: 4rem; padding: 2rem 0; border-top: 1px solid #eaeaea; color: #999; font-size: 0.85rem; text-align: center;">
        <p style="margin: 0 0 0.5rem 0;">由 AI Agent 自动生成 | 每日更新</p>
        <p style="margin: 0;">
            <a href="./about.html" style="color: #666;">关于</a> · 
            <a href="./tools.html" style="color: #666;">工具库</a> · 
            <a href="./sponsor.html" style="color: #666;">赞助</a> · 
            <a href="./feed.xml" style="color: #666;">RSS</a> · 
            <a href="https://github.com/mzh19861986-cpu/ai-tech-daily" style="color: #666;">GitHub</a>
        </p>
    </footer>

    <script>
    // 简单的前端搜索
    document.getElementById('searchInput')?.addEventListener('input', function(e) {{
        const query = e.target.value.toLowerCase();
        const items = document.querySelectorAll('.post-list li');
        items.forEach(item => {{
            const text = item.textContent.toLowerCase();
            item.style.display = text.includes(query) ? '' : 'none';
        }});
    }});
    </script>
</body>
</html>
"""


def md_to_html(md_path: Path) -> tuple[str, str]:
    """把 markdown 文件转成 HTML，返回 (title, html_body)"""
    text = md_path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1) if title_match else md_path.stem

    html_body = md.markdown(text, extensions=["fenced_code", "tables"])

    # 从正文提取 description（第一段非标题文字）
    lines = text.split('\n')
    description = ""
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('>') and not line.startswith('|') and len(line) > 20:
            description = line[:120]
            break

    # 从文件名提取日期
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", md_path.stem)
    date_str = date_match.group(1) if date_match else ""

    # 加文章元信息和分享按钮
    html_body = f'<p class="article-meta">📅 {date_str} | 🤖 AI 自动生成</p>\n' + html_body
    html_body += '''
    <div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid #eaeaea;">
        <strong style="font-weight: 600;">觉得有用？</strong>
        <a href="https://twitter.com/intent/tweet?text=Check%20this%20out&url=https://mzh19861986-cpu.github.io/ai-tech-daily/" style="display: inline-block; margin-left: 1rem; padding: 0.5rem 1rem; background: #1a1a1a; color: white; border-radius: 8px; text-decoration: none; font-size: 0.9rem; font-weight: 500;" target="_blank">🐦 分享到 Twitter</a>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://mzh19861986-cpu.github.io/ai-tech-daily/" style="display: inline-block; margin-left: 0.5rem; padding: 0.5rem 1rem; background: #fafafa; color: #1a1a1a; border: 1px solid #eaeaea; border-radius: 8px; text-decoration: none; font-size: 0.9rem; font-weight: 500;" target="_blank">💼 分享到 LinkedIn</a>
    </div>
    '''

    return title, html_body, description


def build_index(posts: list[dict]) -> str:
    """构建首页"""
    sorted_posts = sorted(posts, key=lambda x: x["date"], reverse=True)
    posts_html = "\n".join([
        f'<li><span class="date">{p["date"]}</span><a href="{p["slug"]}.html">{p["title"]}</a></li>'
        for p in sorted_posts
    ])
    content = f"""
    <div style="text-align: center; padding: 3rem 0 2rem 0;">
        <h1 style="font-size: 2.75rem; margin-bottom: 0.75rem; font-weight: 800; letter-spacing: -0.02em;">AI Tech Daily</h1>
        <p style="font-size: 1.25rem; color: #666; margin-bottom: 1rem; font-weight: 500;">每天 5 分钟，了解 AI 圈最重要的事</p>
        <p style="color: #888; max-width: 520px; margin: 0 auto 2rem auto; line-height: 1.6;">
            由 AI Agent 自动抓取、分析、生成。覆盖 AI 新闻、开源工具、新品发布、开发技巧。
            全部免费，每日更新。
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; margin-bottom: 3rem;">
            <a href="#latest" style="padding: 0.75rem 1.5rem; background: #1a1a1a; color: white; border-radius: 8px; text-decoration: none; font-weight: 500;">开始阅读 →</a>
            <a href="./tools.html" style="padding: 0.75rem 1.5rem; background: white; color: #1a1a1a; border: 1px solid #eaeaea; border-radius: 8px; text-decoration: none; font-weight: 500;">浏览工具库</a>
        </div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0;">
        <div style="background: #fafafa; padding: 1.5rem; border-radius: 10px; border: 1px solid #eaeaea; text-align: center;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">📰</div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; font-weight: 600;">每日新闻</h3>
            <p style="color: #888; margin: 0; font-size: 0.875rem;">追踪 AI 圈最新动态</p>
        </div>
        <div style="background: #fafafa; padding: 1.5rem; border-radius: 10px; border: 1px solid #eaeaea; text-align: center;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">🛠️</div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; font-weight: 600;">开源工具</h3>
            <p style="color: #888; margin: 0; font-size: 0.875rem;">发现好用的 AI 工具</p>
        </div>
        <div style="background: #fafafa; padding: 1.5rem; border-radius: 10px; border: 1px solid #eaeaea; text-align: center;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">💡</div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; font-weight: 600;">实用技巧</h3>
            <p style="color: #888; margin: 0; font-size: 0.875rem;">每天学一个 AI 技巧</p>
        </div>
        <div style="background: #fafafa; padding: 1.5rem; border-radius: 10px; border: 1px solid #eaeaea; text-align: center;">
            <div style="font-size: 1.75rem; margin-bottom: 0.5rem;">⚡</div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.05rem; font-weight: 600;">3 分钟快讯</h3>
            <p style="color: #888; margin: 0; font-size: 0.875rem;">快速掌握核心动态</p>
        </div>
    </div>

    <div style="background: #fafafa; border: 1px solid #eaeaea; padding: 1.5rem; border-radius: 10px; margin: 2rem 0;">
        <h3 style="margin-top:0; font-weight: 600;">🛠️ 开发者推荐工具</h3>
        <p style="margin-bottom: 1rem; color: #666; font-size: 0.9rem;">这些是我们每天都在用的效率工具，推荐给你：</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.5rem;">
            <div style="padding: 0.5rem 0;">🤖 <a href="https://deepseek.com/" target="_blank" style="color: #1a1a1a; font-weight: 500;">DeepSeek API</a></div>
            <div style="padding: 0.5rem 0;">📝 <a href="https://www.notion.so/" target="_blank" style="color: #1a1a1a; font-weight: 500;">Notion</a></div>
            <div style="padding: 0.5rem 0;">☁️ <a href="https://vercel.com/" target="_blank" style="color: #1a1a1a; font-weight: 500;">Vercel</a></div>
            <div style="padding: 0.5rem 0;">💻 <a href="https://github.com/" target="_blank" style="color: #1a1a1a; font-weight: 500;">GitHub</a></div>
            <div style="padding: 0.5rem 0;">🐳 <a href="https://www.docker.com/" target="_blank" style="color: #1a1a1a; font-weight: 500;">Docker</a></div>
            <div style="padding: 0.5rem 0;">📊 <a href="https://www.postman.com/" target="_blank" style="color: #1a1a1a; font-weight: 500;">Postman</a></div>
            <div style="padding: 0.5rem 0;">🔍 <a href="https://www.figma.com/" target="_blank" style="color: #1a1a1a; font-weight: 500;">Figma</a></div>
            <div style="padding: 0.5rem 0;">⌨️ <a href="https://cursor.sh/" target="_blank" style="color: #1a1a1a; font-weight: 500;">Cursor</a></div>
            <div style="padding: 0.5rem 0;">🤖 <a href="https://chat.openai.com/" target="_blank" style="color: #1a1a1a; font-weight: 500;">ChatGPT Plus</a></div>
            <div style="padding: 0.5rem 0;">🧠 <a href="https://claude.ai/" target="_blank" style="color: #1a1a1a; font-weight: 500;">Claude</a></div>
        </div>
    </div>

    <h2>📂 内容分类</h2>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0 2rem 0;">
        <span style="background: #6c5ce7; color: white; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.9rem;">📰 每日日报</span>
        <span style="background: #00b894; color: white; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.9rem;">🛠️ 开源工具</span>
        <span style="background: #fdcb6e; color: #2d3436; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.9rem;">🚀 新品发布</span>
        <span style="background: #74b9ff; color: #2d3436; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.9rem;">✨ Prompt 技巧</span>
        <span style="background: #e17055; color: white; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.9rem;">📚 深度分析</span>
    </div>

    <h2>⭐ 今日头条</h2>
    <div style="background: #1a1a1a; color: white; padding: 1.75rem; border-radius: 12px; margin-bottom: 2rem;">
        <p style="opacity: 0.7; font-size: 0.85rem; margin: 0 0 0.5rem 0;">{sorted_posts[0]['date']}</p>
        <h3 style="font-size: 1.35rem; margin: 0 0 0.75rem 0; font-weight: 600;">
            <a href="{sorted_posts[0]['slug']}.html" style="color: white;">{sorted_posts[0]['title']}</a>
        </h3>
        <p style="opacity: 0.7; margin: 0; font-size: 0.9rem;">今天最重要的内容，先看这篇 →</p>
    </div>

    <h2>📰 最新日报</h2>
    <ul class="post-list">
        {posts_html}
    </ul>

    <div style="text-align: center; margin-top: 3rem; padding: 1.5rem; background: #f8f9fa; border-radius: 12px;">
        <p style="margin: 0; color: #636e72;">觉得有用？</p>
        <p style="margin: 0.5rem 0 1rem 0;">
            <a href="./sponsor.html" style="color: #d63031; font-weight: bold;">💛 赞助我们</a>
            &nbsp;·&nbsp;
            <a href="https://github.com/mzh19861986-cpu/ai-tech-daily" style="color: #0366d6;">⭐ Star on GitHub</a>
        </p>
    </div>
    """
    return TEMPLATE.format(title="Home", description="AI Tech Daily - 每天 5 分钟了解 AI 圈最重要的事。AI 自动生成的技术日报，追踪 AI 新闻、开源工具、新品发布、开发技巧。", content=content)


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
    <h1>📊 智能体集群监控面板</h1>
    <p class="meta">母体 Orchestrator 管控 7 个子智能体 | 全自动闭环运行</p>

    <h2>🧠 母体 Orchestrator</h2>
    <div style="background: #1a1a1a; color: white; padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">
        <h3 style="margin-top: 0;">🎯 母体状态：✅ 正常运行</h3>
        <p style="margin-bottom: 0;">统一调度所有子智能体，任务拆解、派发、监控、安防兜底</p>
    </div>

    <h2>🤖 子智能体列表</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin: 1rem 0;">
        <div style="padding: 1rem; background: #fafafa; border: 1px solid #eaeaea; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">🔍 FetcherAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">抓取 7 个数据源</p>
            <p style="margin: 0.5rem 0 0 0; color: #4caf50; font-weight: 500;">✅ 运行中</p>
        </div>
        <div style="padding: 1rem; background: #fafafa; border: 1px solid #eaeaea; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">⚙️ ProcessorAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">DeepSeek AI 处理 + 翻译</p>
            <p style="margin: 0.5rem 0 0 0; color: #4caf50; font-weight: 500;">✅ 运行中</p>
        </div>
        <div style="padding: 1rem; background: #fafafa; border: 1px solid #eaeaea; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">📝 PublisherAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">生成静态 HTML 并部署</p>
            <p style="margin: 0.5rem 0 0 0; color: #4caf50; font-weight: 500;">✅ 运行中</p>
        </div>
        <div style="padding: 1rem; background: #fafafa; border: 1px solid #eaeaea; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">📈 MonitorAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">监控运行状态和收益</p>
            <p style="margin: 0.5rem 0 0 0; color: #4caf50; font-weight: 500;">✅ 运行中</p>
        </div>
        <div style="padding: 1rem; background: #e8f5e9; border: 2px solid #4caf50; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">📣 PromoterAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">生成推广文案、目录站提交</p>
            <p style="margin: 0.5rem 0 0 0; color: #4caf50; font-weight: 500;">✅ 新上线</p>
        </div>
        <div style="padding: 1rem; background: #e8f5e9; border: 2px solid #4caf50; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">💰 MonetizerAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">分析变现机会、优化变现入口</p>
            <p style="margin: 0.5rem 0 0 0; color: #4caf50; font-weight: 500;">✅ 新上线</p>
        </div>
        <div style="padding: 1rem; background: #e8f5e9; border: 2px solid #4caf50; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">🔄 IterationAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">分析数据、发现问题、提出优化</p>
            <p style="margin: 0.5rem 0 0 0; color: #4caf50; font-weight: 500;">✅ 新上线</p>
        </div>
        <div style="padding: 1rem; background: #fff3e0; border: 2px solid #ff9800; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">🔭 OpportunityScoutAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">全网抓资源、抓机会、抓热点</p>
            <p style="margin: 0.5rem 0 0 0; color: #ff9800; font-weight: 500;">✅ 最新上线</p>
        </div>
        <div style="padding: 1rem; background: #ffebee; border: 2px solid #f44336; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">✅ QualityControlAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">内容审查、工具验证、质量筛选</p>
            <p style="margin: 0.5rem 0 0 0; color: #f44336; font-weight: 500;">✅ 质量把关</p>
        </div>
        <div style="padding: 1rem; background: #f3e5f5; border: 2px solid #9c27b0; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">🧬 EvolutionAgent</h4>
            <p style="margin: 0; color: #666; font-size: 0.9rem;">集群进化、自动分裂新智能体</p>
            <p style="margin: 0.5rem 0 0 0; color: #9c27b0; font-weight: 500;">🧬 自主进化</p>
        </div>
    </div>

    <h2>🔄 完整闭环流程</h2>
    <div style="background: #f5f5f5; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; font-family: monospace; font-size: 0.9rem;">
        <p style="margin: 0 0 0.5rem 0;">
            <strong>内容生产链：</strong>
            Fetcher → Processor → Publisher → Monitor
        </p>
        <p style="margin: 0 0 0.5rem 0;">
            <strong>增长变现链：</strong>
            Promoter → Monetizer → Iteration
        </p>
        <p style="margin: 0;">
            <strong>完整闭环：</strong>
            内容 → 推广 → 变现 → 迭代 → 优化内容 🔁
        </p>
    </div>

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
        <li>✅ 变现指南页面</li>
        <li>⏳ 联盟营销链接（待申请）</li>
    </ul>

    <div style="margin-top: 2rem; padding: 1rem; background: #e8f5e9; border-left: 4px solid #4caf50;">
        <strong>💡 说明：</strong>本系统由母体 Orchestrator 管控，7 个子智能体并行运行，
        自动抓取数据 → DeepSeek AI 处理 → 生成内容 → 发布 → 推广 → 变现 → 迭代优化。
        全自动滚动运行，持续进化。
    </div>
    """
    return TEMPLATE.format(title="Status", description="AI Tech Daily 系统运行状态 - 查看所有 pipeline 运行情况和数据源状态。", content=content)


def build_sponsor() -> str:
    """构建赞助页面"""
    content = """
    <h1>💛 赞助我们</h1>
    <p class="meta">支持这个项目持续运行，让更多开发者看到优质内容</p>

    <h2>为什么赞助？</h2>
    <p>AI Tech Daily 是一个完全由 AI Agent 自动运行的技术日报系统：</p>
    <ul>
        <li>🤖 10+ 个子智能体并行工作，每天自动抓取、分析、生成内容</li>
        <li>📰 覆盖 AI 新闻、GitHub 热门项目、Product Hunt 新品、开发技巧</li>
        <li>💸 全部免费，没有付费墙，所有人都能看</li>
    </ul>

    <h2>你的赞助会用来做什么？</h2>
    <ul>
        <li>☁️ 支付服务器和 API 费用（DeepSeek、Gemini 等）</li>
        <li>🚀 开发更多自动化 pipeline，扩展内容覆盖</li>
        <li>📈 优化网站体验，加更多有用功能</li>
    </ul>

    <div style="background: #1a1a1a; color: white; padding: 2rem; border-radius: 12px; text-align: center; margin: 2rem 0;">
        <h3 style="margin-top: 0; font-weight: 600;">☕ 请我喝杯咖啡</h3>
        <p style="opacity: 0.8;">哪怕一杯咖啡的钱，也是对我们的巨大支持</p>
        <a href="https://github.com/sponsors/mzh19861986-cpu" style="display: inline-block; background: white; color: #1a1a1a; padding: 0.75rem 1.75rem; border-radius: 8px; text-decoration: none; font-weight: 600; margin-top: 1rem;">
            通过 GitHub Sponsors 赞助 →
        </a>
    </div>

    <h2>品牌合作 / 广告</h2>
    <p>我们也接受品牌赞助和产品推荐合作：</p>
    <ul>
        <li>📧 邮箱：待添加</li>
        <li>💬 格式：在每日日报中推荐你的产品</li>
        <li>📊 受众：开发者、AI 爱好者、技术决策者</li>
    </ul>
    """
    return TEMPLATE.format(title="Sponsor", description="支持 AI Tech Daily 持续运行。赞助这个项目，让更多开发者看到优质 AI 内容。", content=content)


def build_about() -> str:
    """构建 About 页面"""
    content = """
    <h1>ℹ️ About</h1>
    <p class="meta">关于 AI Tech Daily</p>

    <h2>这是什么？</h2>
    <p>
        <strong>AI Tech Daily</strong> 是一个完全由 AI Agent 自动运行的技术日报系统。
        它每天自动从 7 个数据源抓取最新内容，用 DeepSeek AI 进行分析、总结、分类，
        然后生成多份不同角度的日报，发布到这个网站。
    </p>

    <h2>它是怎么工作的？</h2>
    <p>整个系统由一个"母体" Orchestrator 管控，多个"子智能体"并行工作：</p>
    <ul>
        <li>🔍 <strong>Fetcher Agent</strong>：从 Hacker News、Lobsters、GitHub Trending、Product Hunt、Dev.to 等数据源抓取内容</li>
        <li>🧠 <strong>Processor Agent</strong>：用 DeepSeek AI 生成摘要、翻译、深度分析、打分</li>
        <li>📝 <strong>Publisher Agent</strong>：把内容整理成不同格式的日报</li>
        <li>🛡️ <strong>Security Agent</strong>：检查内容合规性</li>
        <li>📊 <strong>Monitor Agent</strong>：监控运行状态</li>
    </ul>

    <h2>为什么做这个？</h2>
    <p>
        信息太多了，每天要看好几个网站才能知道 AI 圈发生了什么。
        这个项目就是想帮大家节省时间——每天花 5 分钟看我们的日报，就能了解最重要的事。
    </p>

    <h2>谁在运营？</h2>
    <p>
        一个喜欢折腾自动化的开发者，用 AI Agent 搭了这套系统，让它自己跑。
        所有代码都在 <a href="https://github.com/mzh19861986-cpu/ai-tech-daily">GitHub</a> 上，欢迎 Star 和提 Issue。
    </p>

    <h2>❓ 常见问题</h2>
    <h3>Q: 这个网站是人工写的吗？</h3>
    <p>A: 不是。所有内容都是 AI Agent 自动抓取、自动生成的，每天自动更新。</p>

    <h3>Q: 每天什么时候更新？</h3>
    <p>A: 每天自动更新，一般早上就能看到新的日报。</p>

    <h3>Q: 可以订阅吗？</h3>
    <p>A: 可以！用 RSS Feed 订阅，或者留下邮箱订阅 Newsletter。</p>

    <h3>Q: 内容准确吗？</h3>
    <p>A: 内容由 AI 生成，仅供参考。重要信息请自行核实。</p>

    <div style="margin-top: 2.5rem; padding: 1.75rem; background: #fafafa; border: 1px solid #eaeaea; border-radius: 10px; text-align: center;">
        <p style="margin: 0 0 0.5rem 0; font-weight: 600; color: #1a1a1a;">有问题或建议？</p>
        <p style="margin: 0; color: #666;">
            <a href="https://github.com/mzh19861986-cpu/ai-tech-daily/issues" style="color: #1a1a1a; font-weight: 500;">在 GitHub 提 Issue →</a>
        </p>
    </div>
    """
    return TEMPLATE.format(title="About", description="关于 AI Tech Daily - 一个完全由 AI Agent 自动运行的技术日报系统，每天自动抓取、分析、生成 AI 相关内容。", content=content)


def build_tools_ranking() -> str:
    """构建最佳 AI 工具榜单页面"""
    tools = [
        {"rank": 1, "name": "DeepSeek API", "desc": "高性价比大模型 API，开发者必备", "url": "https://deepseek.com/", "category": "AI大模型"},
        {"rank": 2, "name": "ChatGPT Plus", "desc": "最流行的 AI 助手，通用能力强", "url": "https://chat.openai.com/", "category": "AI助手"},
        {"rank": 3, "name": "Claude", "desc": "Anthropic 出品，长文本处理强", "url": "https://claude.ai/", "category": "AI助手"},
        {"rank": 4, "name": "Cursor", "desc": "AI 代码编辑器，程序员效率神器", "url": "https://cursor.sh/", "category": "开发工具"},
        {"rank": 5, "name": "Notion", "desc": "笔记+项目管理+AI 写作", "url": "https://www.notion.so/", "category": "效率工具"},
        {"rank": 6, "name": "Vercel", "desc": "前端一键部署，开发者友好", "url": "https://vercel.com/", "category": "开发工具"},
        {"rank": 7, "name": "GitHub", "desc": "代码托管与协作平台", "url": "https://github.com/", "category": "开发工具"},
        {"rank": 8, "name": "Docker", "desc": "容器化部署，开发者必备", "url": "https://www.docker.com/", "category": "开发工具"},
        {"rank": 9, "name": "Postman", "desc": "API 测试与调试工具", "url": "https://www.postman.com/", "category": "开发工具"},
        {"rank": 10, "name": "Figma", "desc": "设计协作工具", "url": "https://www.figma.com/", "category": "设计工具"},
        {"rank": 11, "name": "Midjourney", "desc": "AI 绘画，设计必备", "url": "https://www.midjourney.com/", "category": "AI设计"},
        {"rank": 12, "name": "ElevenLabs", "desc": "AI 语音生成，超逼真", "url": "https://elevenlabs.io/", "category": "AI音频"},
        {"rank": 13, "name": "Jasper", "desc": "AI 写作助手，营销文案神器", "url": "https://www.jasper.ai/", "category": "AI写作"},
        {"rank": 14, "name": "Copy.ai", "desc": "AI 文案生成，转化率高", "url": "https://www.copy.ai/", "category": "AI写作"},
        {"rank": 15, "name": "Surfer SEO", "desc": "AI SEO 优化工具", "url": "https://surferseo.com/", "category": "营销工具"},
        {"rank": 16, "name": "Writesonic", "desc": "AI 博客写作，快速生成", "url": "https://writesonic.com/", "category": "AI写作"},
        {"rank": 17, "name": "Synthesia", "desc": "AI 数字人视频生成", "url": "https://www.synthesia.io/", "category": "AI视频"},
        {"rank": 18, "name": "Pictory", "desc": "AI 视频制作，图文转视频", "url": "https://pictory.ai/", "category": "AI视频"},
        {"rank": 19, "name": "Merlin AI", "desc": "浏览器 AI 助手，全网可用", "url": "https://www.getmerlin.in/", "category": "AI助手"},
        {"rank": 20, "name": "Systeme.io", "desc": "AI 营销自动化平台", "url": "https://systeme.io/", "category": "营销工具"},
        {"rank": 21, "name": "Perplexity", "desc": "AI 搜索引擎，答案精准", "url": "https://www.perplexity.ai/", "category": "AI助手"},
        {"rank": 22, "name": "Gemma", "desc": "Google 开源大模型，本地可跑", "url": "https://ai.google.dev/gemma", "category": "AI大模型"},
        {"rank": 23, "name": "Llama 3", "desc": "Meta 开源大模型，性能强", "url": "https://llama.meta.com/", "category": "AI大模型"},
        {"rank": 24, "name": "Hugging Face", "desc": "AI 模型社区，开源模型大全", "url": "https://huggingface.co/", "category": "AI大模型"},
        {"rank": 25, "name": "Replicate", "desc": "一键运行开源 AI 模型", "url": "https://replicate.com/", "category": "AI大模型"},
        {"rank": 26, "name": "LangChain", "desc": "AI Agent 开发框架", "url": "https://www.langchain.com/", "category": "开发工具"},
        {"rank": 27, "name": "LlamaIndex", "desc": "RAG 数据框架，知识库必备", "url": "https://www.llamaindex.ai/", "category": "开发工具"},
        {"rank": 28, "name": "Midjourney", "desc": "AI 绘画，设计必备", "url": "https://www.midjourney.com/", "category": "AI设计"},
        {"rank": 29, "name": "DALL-E 3", "desc": "OpenAI 文生图模型", "url": "https://openai.com/dall-e-3/", "category": "AI设计"},
        {"rank": 30, "name": "Stable Diffusion", "desc": "开源 AI 绘画模型", "url": "https://stability.ai/", "category": "AI设计"},
    ]
    tools_html = "\n".join([
        f'''
        <div class="tool-card" data-category="{t["category"]}" style="display: flex; align-items: center; padding: 1.25rem; margin: 0.75rem 0; background: #fafafa; border-radius: 10px; border: 1px solid #eaeaea; transition: all 0.2s;">
            <div style="font-size: 1.5rem; font-weight: 700; color: #999; margin-right: 1rem; min-width: 36px;">{t["rank"]}</div>
            <div style="flex: 1;">
                <h3 style="margin: 0 0 0.25rem 0; font-size: 1.05rem; font-weight: 600;">{t["name"]} <span style="font-size: 0.75rem; font-weight: 500; color: #666; background: #eaeaea; padding: 0.15rem 0.5rem; border-radius: 12px; margin-left: 0.5rem;">{t["category"]}</span></h3>
                <p style="margin: 0; color: #666; font-size: 0.9rem;">{t["desc"]}</p>
            </div>
            <a href="{t["url"]}" target="_blank" style="padding: 0.5rem 1rem; background: #1a1a1a; color: white; border-radius: 8px; text-decoration: none; font-size: 0.9rem; font-weight: 500;">访问 →</a>
        </div>
        '''
        for t in tools
    ])
    
    # 获取所有分类
    categories = list(set([t["category"] for t in tools]))
    categories.sort()
    category_buttons = '<button class="cat-btn active" data-cat="all" style="padding: 0.5rem 1rem; margin: 0.25rem; background: #1a1a1a; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 0.9rem;">全部</button>'
    for cat in categories:
        category_buttons += f'<button class="cat-btn" data-cat="{cat}" style="padding: 0.5rem 1rem; margin: 0.25rem; background: #f0f0f0; color: #333; border: none; border-radius: 8px; cursor: pointer; font-size: 0.9rem;">{cat}</button>'
    
    search_and_filter = f'''
    <div style="margin: 1.5rem 0;">
        <input type="text" id="toolSearch" placeholder="搜索工具名称..." style="width: 100%; padding: 0.75rem 1rem; border: 1px solid #eaeaea; border-radius: 10px; font-size: 1rem; margin-bottom: 1rem; box-sizing: border-box;">
        <div style="display: flex; flex-wrap: wrap; gap: 0.25rem;">
            {category_buttons}
        </div>
    </div>
    <script>
    // 搜索功能
    document.getElementById('toolSearch').addEventListener('input', function(e) {{
        const query = e.target.value.toLowerCase();
        document.querySelectorAll('.tool-card').forEach(card => {{
            const name = card.querySelector('h3').textContent.toLowerCase();
            const desc = card.querySelectorAll('p')[0].textContent.toLowerCase();
            if (name.includes(query) || desc.includes(query)) {{
                card.style.display = 'flex';
            }} else {{
                card.style.display = 'none';
            }}
        }});
    }});
    // 分类筛选
    document.querySelectorAll('.cat-btn').forEach(btn => {{
        btn.addEventListener('click', function() {{
            document.querySelectorAll('.cat-btn').forEach(b => {{
                b.classList.remove('active');
                b.style.background = '#f0f0f0';
                b.style.color = '#333';
            }});
            this.classList.add('active');
            this.style.background = '#1a1a1a';
            this.style.color = 'white';
            const cat = this.dataset.cat;
            document.querySelectorAll('.tool-card').forEach(card => {{
                if (cat === 'all' || card.dataset.category === cat) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }});
    }});
    </script>
    '''
    
    content = f"""
    <h1>🏆 最佳 AI 工具榜单</h1>
    <p class="meta">我们每天都在用的效率工具，按推荐度排序 | 2026 年 10 月更新</p>

    <p>这些是我们团队每天都在使用的 AI 工具和开发者工具，经过实际使用验证，推荐给你：</p>

    {search_and_filter}

    {tools_html}

    <div style="margin-top: 2rem; padding: 1.5rem; background: #e8f5e9; border-radius: 8px;">
        <p style="margin: 0;"><strong>💡 说明：</strong>我们可能会通过链接获得推荐佣金，但不影响我们的推荐。我们只推荐自己真正在用的工具。</p>
    </div>
    """
    return TEMPLATE.format(title="AI Tools Ranking", description="最佳 AI 工具榜单 - 我们每天都在用的效率工具，按推荐度排序。包含 DeepSeek、Cursor、ChatGPT、Claude 等热门 AI 工具。", content=content)


def build_monetization() -> str:
    """构建 AI 变现指南页面"""
    content = """
    <h1>💰 AI 变现指南</h1>
    <p class="meta">全网筛选的高价值 AI 变现项目和方法 | 2026 年 10 月更新</p>

    <h2>🚀 被动收入方向</h2>
    <p>这些是目前最值得尝试的 AI 被动收入方向：</p>

    <h3>1. AI 工具联盟营销</h3>
    <p>推荐好用的 AI 工具，获得 recurring 佣金（20-50%）：</p>
    <ul>
        <li><strong>Jasper AI</strong>：25-30% recurring，12 个月</li>
        <li><strong>ElevenLabs</strong>：20% recurring，12 个月</li>
        <li><strong>Copy.ai</strong>：45% 首月佣金</li>
        <li><strong>Surfer SEO</strong>：25% recurring</li>
        <li><strong>Writesonic</strong>：30% recurring</li>
    </ul>

    <h3>2. 自动化内容站</h3>
    <p>用 AI Agent 自动生成内容，通过广告和联盟营销变现：</p>
    <ul>
        <li>✅ 就像这个网站一样！自动生成 AI 日报</li>
        <li>✅ 垂直领域内容站（SEO 工具、编程、设计）</li>
        <li>✅ 对比评测站（AI 工具对比）</li>
    </ul>

    <h3>3. 小而美的 AI 工具</h3>
    <p>不要做微信，做解决一个极小痛点的工具：</p>
    <ul>
        <li>电商卖家批量生成白底图</li>
        <li>小红书博主一键转卡片</li>
        <li>简历优化 / 面试模拟工具</li>
        <li>按月订阅 19-49 元，日活 100 人就能月入几千</li>
    </ul>

    <h3>4. AI 自动化服务</h3>
    <p>帮本地小企业做 AI 自动化：</p>
    <ul>
        <li>聊天机器人接入</li>
        <li>社交媒体自动发帖</li>
        <li>邮件营销自动化</li>
        <li>收费：$500-$2000/项目 + $200-$500/月维护</li>
    </ul>

    <h3>5. AI 数字产品</h3>
    <p>做一次，卖无数次：</p>
    <ul>
        <li>AI 提示词合集（Prompt Pack）</li>
        <li>Notion / Obsidian 模板</li>
        <li>AI 工具使用课程 / 电子书</li>
        <li>数字产品商店：Gumroad / Lemon Squeezy</li>
        <li>定价：$9 - $49，一次制作持续卖</li>
    </ul>

    <h3>6. 短视频 / 内容创作</h3>
    <p>用 AI 批量做内容：</p>
    <ul>
        <li>YouTube Shorts / TikTok / 小红书</li>
        <li>AI 生成文案 + AI 配音 + AI 剪辑</li>
        <li>每天发 3-5 条，起号后接广告</li>
        <li>中视频计划 / 创作者基金</li>
    </ul>

    <h2>📊 收入预期</h2>
    <div style="background: #fafafa; border: 1px solid #eaeaea; padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0;">
        <p style="margin: 0 0 0.5rem 0;"><strong>新手期（1-3 个月）：</strong>$100 - $500/月</p>
        <p style="margin: 0 0 0.5rem 0;"><strong>成长期（3-6 个月）：</strong>$500 - $2000/月</p>
        <p style="margin: 0;"><strong>成熟期（6-12 个月）：</strong>$2000 - $5000+/月</p>
    </div>

    <h2>🎯 我们的变现方式</h2>
    <p>这个网站目前的变现方式：</p>
    <ul>
        <li>💛 GitHub Sponsors 赞助</li>
        <li>📧 Newsletter 订阅（未来加广告）</li>
        <li>🛠️ 推荐工具联盟链接（待申请）</li>
        <li>📊 AI 咨询服务（未来开放）</li>
    </ul>

    <div style="margin-top: 2rem; padding: 1.75rem; background: #1a1a1a; color: white; border-radius: 12px; text-align: center;">
        <p style="margin: 0 0 1rem 0; font-weight: 600;">想一起交流 AI 变现？</p>
        <a href="https://github.com/mzh19861986-cpu/ai-tech-daily/issues" style="display: inline-block; background: white; color: #1a1a1a; padding: 0.75rem 1.5rem; border-radius: 8px; text-decoration: none; font-weight: 600;">在 GitHub 讨论 →</a>
    </div>
    """
    return TEMPLATE.format(title="AI Monetization Guide", description="AI 变现指南 - 全网筛选的高价值 AI 变现项目和方法，包含联盟营销、自动化内容站、小工具、自动化服务等方向。", content=content)


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
        title, html_body, description = md_to_html(md_file)
        slug = md_file.stem
        date_match = re.search(r"(\d{4}-\d{2}-\d{2})", slug)
        date = date_match.group(1) if date_match else ""

        full_html = TEMPLATE.format(title=title, description=description, content=html_body)
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

    # 生成赞助页面
    sponsor_html = build_sponsor()
    (SITE_DIR / "sponsor.html").write_text(sponsor_html, encoding="utf-8")
    print("Generated sponsor.html")

    # 生成 About 页面
    about_html = build_about()
    (SITE_DIR / "about.html").write_text(about_html, encoding="utf-8")
    print("Generated about.html")

    # 生成工具榜单页面
    tools_html = build_tools_ranking()
    (SITE_DIR / "tools.html").write_text(tools_html, encoding="utf-8")
    print("Generated tools.html")

    # 生成 AI 变现指南页面
    monetization_html = build_monetization()
    (SITE_DIR / "monetization.html").write_text(monetization_html, encoding="utf-8")
    print("Generated monetization.html")

    # 生成 RSS feed
    rss_xml = build_rss(posts)
    (SITE_DIR / "feed.xml").write_text(rss_xml, encoding="utf-8")
    print("Generated feed.xml")

    # 生成 sitemap.xml
    base_url = "https://mzh19861986-cpu.github.io/ai-tech-daily"
    sitemap_urls = [f"{base_url}/", f"{base_url}/about.html", f"{base_url}/status.html", f"{base_url}/sponsor.html", f"{base_url}/tools.html", f"{base_url}/monetization.html"]
    for p in posts:
        sitemap_urls.append(f"{base_url}/{p['slug']}.html")
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sitemap_urls:
        sitemap_xml += f"  <url><loc>{url}</loc></url>\n"
    sitemap_xml += "</urlset>"
    (SITE_DIR / "sitemap.xml").write_text(sitemap_xml, encoding="utf-8")
    print("Generated sitemap.xml")

    # 生成 robots.txt
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""
    (SITE_DIR / "robots.txt").write_text(robots_txt, encoding="utf-8")
    print("Generated robots.txt")

    # 生成 Google Search Console 验证文件
    google_verify_file = "google7301fce51f92c8d0.html"
    google_verify_content = "google-site-verification: google7301fce51f92c8d0.html"
    (SITE_DIR / google_verify_file).write_text(google_verify_content, encoding="utf-8")
    print(f"Generated {google_verify_file}")


if __name__ == "__main__":
    main()
