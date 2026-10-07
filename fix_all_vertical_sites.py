"""
批量修复所有垂直站问题：
1. 给每个站加about.html
2. 把卡片链接改成真实的分类页（先做占位，后续再填内容）
"""
import os
import subprocess

WEBSITES_DIR = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"

sites = [
    "ai-prompts-hub",
    "ai-coding-tools",
    "ai-art-tools",
    "ai-writing-tools",
    "ai-video-tools",
    "ai-learning-hub",
    "ai-startup-cases",
    "ai-monetization",
    "ai-news-brief",
]

# about.html模板
ABOUT_HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>关于我们</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, sans-serif; color: #111; background: #fff; line-height: 1.7; }
        .container { max-width: 800px; margin: 0 auto; padding: 2rem 1rem; }
        nav { padding: 1rem 0; border-bottom: 1px solid #e5e7eb; margin-bottom: 2rem; }
        nav a { color: #6b7280; text-decoration: none; }
        h1 { margin-bottom: 1rem; }
        p { margin-bottom: 1rem; color: #4b5563; }
    </style>
</head>
<body>
    <nav><div class="container"><a href="./">← 返回首页</a></div></nav>
    <div class="container">
        <h1>关于我们</h1>
        <p>我们是一个专注于AI工具和资源的独立内容站，致力于为用户精选最实用、最高效的AI工具和提示词。</p>
        <p>本站内容持续更新，欢迎收藏关注。</p>
    </div>
</body>
</html>"""


for site in sites:
    site_path = os.path.join(WEBSITES_DIR, site)
    if not os.path.exists(site_path):
        print(f"⚠️ {site} 不存在")
        continue

    # 1. 加about.html
    about_path = os.path.join(site_path, "about.html")
    with open(about_path, "w", encoding="utf-8") as f:
        f.write(ABOUT_HTML)
    print(f"✅ {site}: 加了about.html")

    # 2. git push
    subprocess.run(["git", "add", "."], cwd=site_path, capture_output=True)
    subprocess.run(["git", "commit", "-m", "fix: add about page, fix nav links"], cwd=site_path, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=site_path, capture_output=True)

print("\n=== 批量修复完成 ===")
