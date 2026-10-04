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
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.7; color: #333; }}
        h1 {{ border-bottom: 2px solid #e1e4e8; padding-bottom: 0.5rem; }}
        h2 {{ margin-top: 2rem; color: #24292e; }}
        a {{ color: #0366d6; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .meta {{ color: #6a737d; font-size: 0.9rem; margin-bottom: 2rem; }}
        .nav {{ margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 1px solid #e1e4e8; }}
        .nav a {{ margin-right: 1rem; }}
        .post-list {{ list-style: none; padding: 0; }}
        .post-list li {{ padding: 0.8rem 0; border-bottom: 1px solid #f1f3f5; }}
        .post-list .date {{ color: #6a737d; font-size: 0.9rem; margin-right: 1rem; }}
    </style>
</head>
<body>
    <nav class="nav">
        <a href="/">🏠 Home</a>
        <a href="https://github.com/mzh19861986-cpu/ai-tech-daily">GitHub</a>
    </nav>
    {content}
    <footer style="margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #e1e4e8; color: #6a737d; font-size: 0.85rem;">
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
    <h2>最新日报</h2>
    <ul class="post-list">
        {posts_html}
    </ul>
    """
    return TEMPLATE.format(title="Home", content=content)


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


if __name__ == "__main__":
    main()
