"""
垂直站内容建设智能体
用DeepSeek自动生成每个垂直站的详细内容
给每个卡片做真正的详情页
"""
import os
import requests
import json

# 加载DeepSeek keys，从环境变量读
DEEPSEEK_KEYS = os.getenv("DEEPSEEK_API_KEYS", "").split(",")

def call_deepseek(prompt):
    """调用DeepSeek生成内容"""
    key = DEEPSEEK_KEYS[0]  # 简单用第一个key
    resp = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000
        },
        timeout=30
    )
    return resp.json()["choices"][0]["message"]["content"]


def build_prompts_detail():
    """给ai-prompts-hub生成详情页"""
    print("🔨 正在建设ai-prompts-hub详情页...")

    # 生成写作类提示词详情
    content = call_deepseek("""
请给我写5个高质量的写作类AI提示词，每个包含：
- 提示词标题
- 适用场景
- 完整的提示词模板（可以直接复制给ChatGPT用）
- 使用示例

要求：实用、可直接用、不要太泛。
""")

    # 保存成writing.html
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>写作类提示词 - AI Prompts Hub</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, sans-serif; color: #111; background: #f9fafb; line-height: 1.7; }}
        .container {{ max-width: 800px; margin: 0 auto; padding: 2rem 1rem; }}
        nav {{ padding: 1rem 0; border-bottom: 1px solid #e5e7eb; margin-bottom: 2rem; }}
        nav a {{ color: #6b7280; text-decoration: none; }}
        h1 {{ font-size: 1.8rem; margin-bottom: 1rem; }}
        .content {{ background: white; padding: 2rem; border-radius: 12px; border: 1px solid #e5e7eb; }}
        pre {{ background: #f3f4f6; padding: 1rem; border-radius: 8px; overflow-x: auto; margin: 1rem 0; }}
    </style>
</head>
<body>
    <nav><div class="container"><a href="./">← 返回首页</a></div></nav>
    <div class="container">
        <h1>✍️ 写作类提示词大全</h1>
        <div class="content">
            {content.replace(chr(10), '<br>').replace('```', '<pre>').replace('```', '</pre>')}
        </div>
    </div>
</body>
</html>"""

    path = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites\ai-prompts-hub\writing.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 生成 writing.html")


if __name__ == "__main__":
    build_prompts_detail()
