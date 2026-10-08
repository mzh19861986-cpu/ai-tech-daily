"""
真正的垂直站建设智能体
用DeepSeek自动生成每个工具的详情页
"""
import requests
import os

DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "")

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


def build_coding_tool_page(tool_name):
    """生成一个编程工具的详情页"""
    print(f"🔨 正在生成 {tool_name} 详情页...")

    content = call_deepseek(f"""
请写一个关于{tool_name}的详细介绍，包含：
1. 这个工具是什么
2. 适合谁用
3. 核心功能
4. 优缺点
5. 怎么开始用
6. 免费还是付费
要求：实用、客观、真实，不要吹牛逼。
""")

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tool_name} - 详细介绍 | AI Coding Tools</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, sans-serif; color: #111; background: #f9fafb; line-height: 1.7; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 1rem; }}
        nav {{ padding: 1rem 0; border-bottom: 1px solid #e5e7eb; margin-bottom: 2rem; position: sticky; top: 0; background: white; }}
        nav a {{ color: #6b7280; text-decoration: none; }}
        h1 {{ font-size: 1.8rem; margin-bottom: 1rem; }}
        .content {{ background: white; padding: 2rem; border-radius: 12px; border: 1px solid #e5e7eb; }}
        .cta {{ display: inline-block; margin-top: 2rem; padding: 0.75rem 1.5rem; background: #111; color: white; border-radius: 8px; text-decoration: none; }}
    </style>
</head>
<body>
    <nav><div class="container"><a href="./">← 返回首页</a></div></nav>
    <div class="container">
        <h1>💻 {tool_name}</h1>
        <div class="content">
            {content.replace(chr(10), '<br>')}
        </div>
        <a href="https://www.{tool_name.lower().replace(' ', '')}.com" target="_blank" class="cta">访问官网 →</a>
    </div>
</body>
</html>"""

    path = rf"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites\ai-coding-tools\{tool_name.lower().replace(' ', '-')}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 生成完成: {tool_name}")


if __name__ == "__main__":
    # 先做5个最火的编程工具
    tools = ["GitHub Copilot", "Cursor", "Windsurf", "CodeLlama", "Tabnine"]
    for tool in tools:
        build_coding_tool_page(tool)
    print("\n✅ 5个编程工具详情页生成完成！")
