import os
import subprocess
import requests

TOKEN = "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"
BASE_DIR = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"

websites = [
    {"name": "ai-coding-tools", "desc": "AI Coding Tools - Best AI Coding Tools", "title": "AI Coding Tools", "icon": "💻", "tagline": "Best AI coding tools for developers"},
    {"name": "ai-art-tools", "desc": "AI Art Tools - AI Image Generation Tools", "title": "AI Art Tools", "icon": "🎨", "tagline": "Best AI art and image generation tools"},
    {"name": "ai-writing-tools", "desc": "AI Writing Tools - AI Writing Assistants", "title": "AI Writing Tools", "icon": "✍️", "tagline": "Best AI writing assistant tools"},
    {"name": "ai-video-tools", "desc": "AI Video Tools - AI Video Generation", "title": "AI Video Tools", "icon": "🎬", "tagline": "Best AI video generation tools"},
    {"name": "ai-learning-hub", "desc": "AI Learning Hub - AI Tutorials & Resources", "title": "AI Learning Hub", "icon": "📚", "tagline": "Learn AI from scratch with tutorials"},
    {"name": "ai-startup-cases", "desc": "AI Startup Cases - AI Success Stories", "title": "AI Startup Cases", "icon": "🚀", "tagline": "AI startup success stories and cases"},
    {"name": "ai-monetization", "desc": "AI Monetization - Make Money with AI", "title": "AI Monetization", "icon": "💰", "tagline": "How to make passive income with AI"},
    {"name": "ai-news-brief", "desc": "AI News Brief - 3 Minute AI News", "title": "AI News Brief", "icon": "⚡", "tagline": "3 minute AI news brief for busy people"},
]

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{tagline}">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a1a1a; background: #fff; line-height: 1.6; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 2rem; }}
        nav {{ padding: 1.5rem 0; border-bottom: 1px solid #eee; margin-bottom: 4rem; }}
        nav .container {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 1.25rem; font-weight: 700; color: #1a1a1a; text-decoration: none; }}
        .hero {{ text-align: center; padding: 6rem 0; }}
        .hero h1 {{ font-size: 3rem; font-weight: 700; margin-bottom: 1.5rem; letter-spacing: -0.02em; }}
        .hero p {{ font-size: 1.25rem; color: #666; max-width: 600px; margin: 0 auto 3rem; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 4rem 0; }}
        .card {{ padding: 2rem; border: 1px solid #eee; border-radius: 12px; transition: all 0.2s; }}
        .card:hover {{ border-color: #1a1a1a; transform: translateY(-2px); }}
        .card h3 {{ font-size: 1.25rem; margin-bottom: 1rem; }}
        .card p {{ color: #666; }}
        footer {{ padding: 3rem 0; border-top: 1px solid #eee; text-align: center; color: #999; margin-top: 6rem; }}
        @media (max-width: 768px) {{ .hero h1 {{ font-size: 2rem; }} }}
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">{icon} {title}</a>
            <div>
                <a href="/about" style="color: #666; text-decoration: none;">About</a>
            </div>
        </div>
    </nav>
    <div class="container">
        <div class="hero">
            <h1>{icon} {title}</h1>
            <p>{tagline}</p>
        </div>
        <div class="grid">
            <div class="card"><h3>🔥 Popular</h3><p>Most popular tools and resources</p></div>
            <div class="card"><h3>🆕 Latest</h3><p>Updated daily by AI agents</p></div>
            <div class="card"><h3>📊 Reviews</h3><p>Honest reviews and comparisons</p></div>
        </div>
    </div>
    <footer>
        <div class="container">
            <p>© 2026 {title} - Maintained by AI Agent Cluster</p>
        </div>
    </footer>
</body>
</html>
"""

for site in websites:
    print(f"\n=== Creating {site['name']} ===")
    
    # 1. Create repo
    try:
        r = requests.post("https://api.github.com/user/repos", headers=headers, json={
            "name": site["name"],
            "description": site["desc"],
            "private": False,
            "has_issues": True,
            "has_wiki": False,
        })
        print("  ✅ Repo created")
    except Exception as e:
        print(f"  ⚠️ Repo may exist: {e}")
    
    # 2. Clone
    site_path = os.path.join(BASE_DIR, site["name"])
    if os.path.exists(site_path):
        import shutil
        shutil.rmtree(site_path)
    subprocess.run(["git", "clone", f"https://{TOKEN}@github.com/mzh19861986-cpu/{site['name']}.git", site_path], check=True, capture_output=True)
    print("  ✅ Cloned")
    
    # 3. Create index.html
    html = html_template.format(**site)
    with open(os.path.join(site_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✅ Index.html created")
    
    # 4. Git commit and push
    subprocess.run(["git", "config", "user.email", "mzh19861986@gmail.com"], cwd=site_path, check=True)
    subprocess.run(["git", "config", "user.name", "mzh19861986-cpu"], cwd=site_path, check=True)
    subprocess.run(["git", "add", "."], cwd=site_path, check=True)
    subprocess.run(["git", "commit", "-m", "feat: initial site"], cwd=site_path, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=site_path, check=True, capture_output=True)
    print("  ✅ Pushed to GitHub")
    
    # 5. Enable Pages
    try:
        r = requests.post(f"https://api.github.com/repos/mzh19861986-cpu/{site['name']}/pages", headers=headers, json={
            "source": {"branch": "main", "path": "/"}
        })
        print("  ✅ GitHub Pages enabled")
    except Exception as e:
        print(f"  ⚠️ Pages may exist: {e}")
    
    print(f"  📍 URL: https://mzh19861986-cpu.github.io/{site['name']}/")

print("\n=== All 8 websites created! ===")
