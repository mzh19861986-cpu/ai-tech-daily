"""
垂直站独立自动建设智能体
给每个垂直站自动生成5个工具详情页
"""
import requests
import os
import subprocess

DEEPSEEK_KEY = "sk-f82f237566274d0785cb2e266b603cc0"

def call_deepseek(prompt):
    resp = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {DEEPSEEK_KEY}"},
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1500
        },
        timeout=60
    )
    return resp.json()["choices"][0]["message"]["content"]


def build_tool_page(site_path, site_name, tool_name, category):
    """生成一个工具详情页"""
    print(f"🔨 正在生成 {tool_name} 详情页...")

    content = call_deepseek(f"""
请写一个关于{tool_name}的详细介绍，它是一个{category}领域的AI工具，包含：
1. 这个工具是什么
2. 适合谁用
3. 核心功能
4. 优缺点
5. 怎么开始用
6. 免费还是付费
要求：实用、客观、真实。
""")

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tool_name} - 详细介绍 | {site_name}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, sans-serif; color: #111; background: #f9fafb; line-height: 1.7; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 1rem; }}
        nav {{ padding: 1rem 0; border-bottom: 1px solid #e5e7eb; margin-bottom: 2rem; position: sticky; top: 0; background: white; }}
        nav a {{ color: #6b7280; text-decoration: none; }}
        h1 {{ font-size: 1.8rem; margin-bottom: 1rem; }}
        .content {{ background: white; padding: 2rem; border-radius: 12px; border: 1px solid #e5e7eb; }}
    </style>
</head>
<body>
    <nav><div class="container"><a href="./">← 返回首页</a></div></nav>
    <div class="container">
        <h1>{tool_name}</h1>
        <div class="content">
            {content.replace(chr(10), '<br>')}
        </div>
    </div>
</body>
</html>"""

    filename = tool_name.lower().replace(' ', '-').replace('/', '-') + ".html"
    path = os.path.join(site_path, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 生成完成: {tool_name}")
    return filename


if __name__ == "__main__":
    WEBSITES_DIR = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"

    # ai-art-tools：5个绘画工具
    site_path = os.path.join(WEBSITES_DIR, "ai-art-tools")
    tools = ["Midjourney", "DALL-E 3", "Stable Diffusion", "Leonardo AI", "Firefly"]
    for tool in tools:
        build_tool_page(site_path, "AI Art Tools", tool, "AI绘画")

    # push
    subprocess.run(["git", "add", "."], cwd=site_path, capture_output=True)
    subprocess.run(["git", "commit", "-m", "feat: add 5 art tool detail pages"], cwd=site_path, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=site_path, capture_output=True)
    print("\n✅ ai-art-tools 5个详情页已生成并push！")
