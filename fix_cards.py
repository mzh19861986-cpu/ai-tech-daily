"""修改ai-coding-tools首页，把卡片链接指向详情页"""
import os

path = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites\ai-coding-tools\index.html"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 前5个卡片指向真正的详情页
links = [
    "./github-copilot.html",
    "./cursor.html",
    "./windsurf.html",
    "./codellama.html",
    "./tabnine.html",
]

for link in links:
    html = html.replace('<div class="card">', f'<a href="{link}" class="card">', 1)

# 剩下的卡片指向#
html = html.replace('<div class="card">', '<a href="#" class="card">')

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("✅ ai-coding-tools首页卡片链接已修改")
