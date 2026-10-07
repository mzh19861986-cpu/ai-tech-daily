"""
紧急修复：所有垂直站导航路径
把 href="/" 改成 href="./"
把 href="/about.html" 改成 href="./about.html"
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

for site in sites:
    index_path = os.path.join(WEBSITES_DIR, site, "index.html")
    if not os.path.exists(index_path):
        continue

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 修复路径
    html = html.replace('href="/"', 'href="./"')
    html = html.replace('href="/about.html"', 'href="./about.html"')

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ {site}: 导航路径已修正")

    # push
    site_path = os.path.join(WEBSITES_DIR, site)
    subprocess.run(["git", "add", "."], cwd=site_path, capture_output=True)
    subprocess.run(["git", "commit", "-m", "fix: correct nav relative paths"], cwd=site_path, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=site_path, capture_output=True)

print("\n=== 所有垂直站导航路径已修复 ===")
