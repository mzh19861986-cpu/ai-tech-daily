"""给ai-writing-tools生成5个详情页"""
import requests
import os
import subprocess

DEEPSEEK_KEY = "sk-f82f237566274d0785cb2e266b603cc0"

def call_deepseek(prompt):
    resp = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {DEEPSEEK_KEY}"},
        json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}], "max_tokens": 1500},
        timeout=60
    )
    return resp.json()["choices"][0]["message"]["content"]

WEBSITES_DIR = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"
site_path = os.path.join(WEBSITES_DIR, "ai-writing-tools")
tools = ["ChatGPT", "Claude", "Jasper", "Copy.ai", "Notion AI"]

for tool in tools:
    print(f"🔨 正在生成 {tool}...")
    content = call_deepseek(f"请写一个关于{tool}的详细介绍，它是AI写作工具，包含：是什么、适合谁、核心功能、优缺点、怎么用、付费还是免费")
    filename = tool.lower().replace(' ', '-') + ".html"
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tool} - 详细介绍 | AI Writing Tools</title>
    <style>* {{ margin:0; padding:0; box-sizing:border-box; }} body {{ font-family:-apple-system,sans-serif; color:#111; background:#f9fafb; line-height:1.7; }} .container {{ max-width:800px; margin:0 auto; padding:1rem; }} nav {{ padding:1rem 0; border-bottom:1px solid #e5e7eb; margin-bottom:2rem; }} nav a {{ color:#6b7280; text-decoration:none; }} h1 {{ margin-bottom:1rem; }} .content {{ background:white; padding:2rem; border-radius:12px; border:1px solid #e5e7eb; }}</style>
</head>
<body>
    <nav><div class="container"><a href="./">← 返回首页</a></div></nav>
    <div class="container">
        <h1>{tool}</h1>
        <div class="content">{content.replace(chr(10), '<br>')}</div>
    </div>
</body>
</html>"""
    with open(os.path.join(site_path, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {tool} 完成")

subprocess.run(["git", "add", "."], cwd=site_path, capture_output=True)
subprocess.run(["git", "commit", "-m", "feat: add 5 writing tool pages"], cwd=site_path, capture_output=True)
subprocess.run(["git", "push", "origin", "main"], cwd=site_path, capture_output=True)
print("\n✅ ai-writing-tools 5个详情页已完成！")
