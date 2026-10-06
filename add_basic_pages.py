import os
import subprocess

websites = [
    {"name": "ai-prompts-hub", "title": "AI Prompts Hub", "icon": "✨", "tagline": "精选高质量 AI 提示词"},
    {"name": "ai-coding-tools", "title": "AI Coding Tools", "icon": "💻", "tagline": "最好用的 AI 编程工具"},
    {"name": "ai-art-tools", "title": "AI Art Tools", "icon": "🎨", "tagline": "AI 绘画工具大全"},
    {"name": "ai-writing-tools", "title": "AI Writing Tools", "icon": "✍️", "tagline": "AI 写作助手推荐"},
    {"name": "ai-video-tools", "title": "AI Video Tools", "icon": "🎬", "tagline": "AI 视频工具大全"},
    {"name": "ai-learning-hub", "title": "AI Learning Hub", "icon": "📚", "tagline": "AI 学习资源大全"},
    {"name": "ai-startup-cases", "title": "AI Startup Cases", "icon": "🚀", "tagline": "AI 创业成功案例"},
    {"name": "ai-monetization", "title": "AI Monetization", "icon": "💰", "tagline": "AI 被动收入方法"},
    {"name": "ai-news-brief", "title": "AI News Brief", "icon": "⚡", "tagline": "3分钟AI新闻简报"},
]

base_dir = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"

about_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>关于 - {title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #111827; background: #fff; line-height: 1.6; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 0 2rem; }}
        nav {{ padding: 1.5rem 0; border-bottom: 1px solid #e5e7eb; margin-bottom: 3rem; }}
        nav .container {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 1.25rem; font-weight: 700; color: #111827; text-decoration: none; }}
        .nav-links a {{ margin-left: 1.5rem; color: #6b7280; text-decoration: none; font-size: 0.95rem; }}
        .content {{ padding: 2rem 0; }}
        h1 {{ font-size: 2rem; margin-bottom: 1.5rem; }}
        h2 {{ font-size: 1.5rem; margin: 2rem 0 1rem; }}
        p {{ margin-bottom: 1rem; color: #374151; }}
        footer {{ padding: 3rem 0; border-top: 1px solid #e5e7eb; text-align: center; color: #9ca3af; margin-top: 4rem; }}
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">{icon} {title}</a>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/about.html">关于</a>
            </div>
        </div>
    </nav>
    <div class="container content">
        <h1>ℹ️ 关于 {title}</h1>
        <p>{tagline}，我们精选了这个领域最实用的工具和资源，帮你节省时间，快速找到你需要的东西。</p>
        
        <h2>我们做什么？</h2>
        <p>我们每天收集、测试、整理 AI 领域的优质工具和资源，只保留真正好用的，去掉那些噱头大于实用的。每个推荐都经过实际使用验证。</p>
        
        <h2>我们的受众</h2>
        <p>AI 开发者、产品经理、创业者、自由职业者，以及所有想用 AI 提升效率的人。</p>
        
        <h2>联系我们</h2>
        <p>如果你有好的工具推荐，或者想合作，欢迎通过 GitHub 联系我们。</p>
    </div>
    <footer>
        <div class="container">
            <p>© 2026 {title}</p>
        </div>
    </footer>
</body>
</html>
"""

robots_txt = """User-agent: *
Allow: /
Sitemap: https://mzh19861986-cpu.github.io/{name}/sitemap.xml
"""

sitemap_template = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://mzh19861986-cpu.github.io/{name}/</loc></url>
  <url><loc>https://mzh19861986-cpu.github.io/{name}/about.html</loc></url>
</urlset>
"""

for site in websites:
    print(f"\n=== Adding pages to {site['name']} ===")
    site_path = os.path.join(base_dir, site["name"])
    
    # About page
    about_html = about_template.format(
        title=site["title"],
        icon=site["icon"],
        tagline=site["tagline"]
    )
    with open(os.path.join(site_path, "about.html"), "w", encoding="utf-8") as f:
        f.write(about_html)
    print("  ✅ about.html")
    
    # robots.txt
    with open(os.path.join(site_path, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt.format(name=site["name"]))
    print("  ✅ robots.txt")
    
    # sitemap.xml
    with open(os.path.join(site_path, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_template.format(name=site["name"]))
    print("  ✅ sitemap.xml")
    
    # Git push
    subprocess.run(["git", "add", "."], cwd=site_path, check=True)
    subprocess.run(["git", "commit", "-m", "add: about page, robots.txt, sitemap.xml"], cwd=site_path, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=site_path, check=True, capture_output=True)
    print("  ✅ Pushed to GitHub")

print("\n=== All sites have basic pages now! ===")
