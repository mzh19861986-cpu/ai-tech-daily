"""
修复所有垂直站：
1. 把根路径 / 改成相对路径 ./
2. 重新push完整内容
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
    site_path = os.path.join(WEBSITES_DIR, site)
    index_path = os.path.join(site_path, "index.html")

    if not os.path.exists(index_path):
        print(f"⚠️ {site}: index.html 不存在")
        continue

    # 读取文件
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 修正路径：把 href="/" 改成 href="./"，href="/about.html" 改成 href="./about.html"
    # 注意不要改 /assets 之类的，只改导航和链接
    html = html.replace('href="/"', 'href="./"')
    html = html.replace('href="/about.html"', 'href="./about.html"')

    # 写回
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ {site}: 路径已修正")

    # git add + commit + push
    subprocess.run(["git", "add", "."], cwd=site_path, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "fix: correct relative paths and push full content"],
        cwd=site_path,
        capture_output=True
    )
    result = subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=site_path,
        capture_output=True,
        text=True
    )
    if "main -> main" in result.stdout:
        print(f"   ✅ push成功")
    else:
        print(f"   ⚠️ push结果: {result.stdout[:100]}")

print("\n=== 全部垂直站修复完成 ===")
