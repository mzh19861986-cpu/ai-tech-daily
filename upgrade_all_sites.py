import os
import subprocess

websites = [
    {
        "name": "ai-prompts-hub",
        "title": "AI Prompts Hub",
        "icon": "✨",
        "tagline": "精选高质量 AI 提示词，让 ChatGPT/Claude 更好用",
        "tools": [
            {"name": "写作类提示词", "desc": "写文案、写文章、写邮件，一键复制直接用", "tags": ["写作", "通用"]},
            {"name": "编程类提示词", "desc": "写代码、debug、code review，程序员效率翻倍", "tags": ["编程", "开发"]},
            {"name": "绘画类提示词", "desc": "Midjourney/SD 提示词模板，出图效果更好", "tags": ["绘画", "设计"]},
            {"name": "营销类提示词", "desc": "写标题、写广告、写朋友圈，转化率更高", "tags": ["营销", "变现"]},
            {"name": "学习类提示词", "desc": "学习新知识、做总结、做笔记，效率提升", "tags": ["学习", "教育"]},
            {"name": "生活类提示词", "desc": "做计划、写简历、搞旅行攻略，生活助手", "tags": ["生活", "实用"]},
        ]
    },
    {
        "name": "ai-coding-tools",
        "title": "AI Coding Tools",
        "icon": "💻",
        "tagline": "最好用的 AI 编程工具推荐，提升开发效率",
        "tools": [
            {"name": "GitHub Copilot", "desc": "AI 代码补全，程序员都在用", "tags": ["代码补全", "付费"]},
            {"name": "Cursor", "desc": "AI 原生编辑器，写代码像聊天一样简单", "tags": ["编辑器", "AI原生"]},
            {"name": "ChatGPT", "desc": "写代码、debug、解释代码，通用编程助手", "tags": ["通用", "免费额度"]},
            {"name": "Claude 3.5", "desc": "长代码理解能力强，适合大型项目", "tags": ["长代码", "免费额度"]},
            {"name": "CodeLlama", "desc": "Meta 开源大模型，可本地部署", "tags": ["开源", "本地部署"]},
            {"name": "Tabnine", "desc": "AI 代码补全，隐私友好", "tags": ["补全", "隐私"]},
            {"name": "Windsurf", "desc": "AI 代码编辑器，自动重构代码", "tags": ["编辑器", "重构"]},
            {"name": "Sourcegraph", "desc": "AI 代码搜索，大代码库神器", "tags": ["搜索", "代码库"]},
            {"name": "DeepSeek Coder", "desc": "国产编程大模型，效果好免费额度多", "tags": ["国产", "编程"]},
        ]
    },
    {
        "name": "ai-art-tools",
        "title": "AI Art Tools",
        "icon": "🎨",
        "tagline": "最好用的 AI 绘画/图像生成工具大全",
        "tools": [
            {"name": "Midjourney", "desc": "最强 AI 绘画工具，艺术效果顶级", "tags": ["付费", "高质量", "艺术"]},
            {"name": "DALL-E 3", "desc": "OpenAI 出品，文字理解能力强", "tags": ["免费额度", "OpenAI", "易上手"]},
            {"name": "Stable Diffusion", "desc": "开源免费，可本地部署，自由度高", "tags": ["开源", "免费", "本地部署"]},
            {"name": "Leonardo AI", "desc": "游戏美术风格强，适合游戏开发者", "tags": ["免费额度", "游戏美术"]},
            {"name": "Ideogram", "desc": "文字渲染能力强，做海报Logo神器", "tags": ["免费额度", "文字设计"]},
            {"name": "Firefly", "desc": "Adobe 出品，商用版权清晰", "tags": ["Adobe", "商用"]},
        ]
    },
    {
        "name": "ai-writing-tools",
        "title": "AI Writing Tools",
        "icon": "✍️",
        "tagline": "最好用的 AI 写作助手，写文章效率翻倍",
        "tools": [
            {"name": "ChatGPT", "desc": "通用写作助手，写文案、文章、邮件", "tags": ["通用", "免费额度"]},
            {"name": "Claude 3.5", "desc": "长文写作能力强，写长文章不跑偏", "tags": ["长文", "免费额度"]},
            {"name": "Jasper", "desc": "营销文案专家，转化率高", "tags": ["营销", "付费"]},
            {"name": "Notion AI", "desc": "笔记内置AI，边写边改", "tags": ["笔记", "免费额度"]},
            {"name": "Grammarly", "desc": "语法检查+AI润色，英文写作必备", "tags": ["语法", "免费额度"]},
            {"name": "Copy.ai", "desc": "营销文案模板多，上手快", "tags": ["营销", "免费额度"]},
        ]
    },
    {
        "name": "ai-video-tools",
        "title": "AI Video Tools",
        "icon": "🎬",
        "tagline": "AI 视频生成/剪辑/配音工具大全",
        "tools": [
            {"name": "Runway ML", "desc": "AI视频生成 pioneer，效果最好", "tags": ["付费", "高质量"]},
            {"name": "Pika Labs", "desc": "免费AI视频生成，Discord用", "tags": ["免费", "Discord"]},
            {"name": "ElevenLabs", "desc": "AI配音，声音克隆", "tags": ["配音", "免费额度"]},
            {"name": "Descript", "desc": "视频编辑像编辑文档一样简单", "tags": ["编辑", "付费"]},
            {"name": "HeyGen", "desc": "AI数字人，做口播视频", "tags": ["数字人", "付费"]},
            {"name": "Synthesia", "desc": "企业级AI数字人视频", "tags": ["数字人", "B端"]},
        ]
    },
    {
        "name": "ai-learning-hub",
        "title": "AI Learning Hub",
        "icon": "📚",
        "tagline": "AI 学习资源大全，从入门到精通",
        "tools": [
            {"name": "Fast.ai", "desc": "免费深度学习课程，动手实践", "tags": ["免费", "深度学习"]},
            {"name": "Coursera AI", "desc": "斯坦福、谷歌等名校AI课程", "tags": ["名校", "证书"]},
            {"name": "Hugging Face", "desc": "NLP学习社区，有大量教程", "tags": ["NLP", "社区"]},
            {"name": "Kaggle", "desc": "数据科学竞赛，边玩边学", "tags": ["竞赛", "数据"]},
            {"name": "DeepLearning.AI", "desc": "吴恩达的AI课程，入门首选", "tags": ["入门", "吴恩达"]},
            {"name": "GitHub Awesome AI", "desc": "最全AI学习资源列表", "tags": ["资源汇总", "GitHub"]},
        ]
    },
    {
        "name": "ai-startup-cases",
        "title": "AI Startup Cases",
        "icon": "🚀",
        "tagline": "AI 创业成功案例，看别人怎么赚钱",
        "tools": [
            {"name": "Midjourney", "desc": "几个人做出来的独角兽，AI绘画标杆", "tags": ["独角兽", "绘画"]},
            {"name": "OpenAI", "desc": "ChatGPT改变世界，AI行业标杆", "tags": ["巨头", "ChatGPT"]},
            {"name": "Cursor", "desc": "AI编辑器，一年估值10亿美金", "tags": ["编辑器", "高速增长"]},
            {"name": "Notion AI", "desc": "在Notion里加AI，用户付费大增", "tags": ["SaaS", "AI增强"]},
            {"name": "Copy.ai", "desc": "AI写作工具，MRR百万美金", "tags": ["写作", "营销"]},
            {"name": "Synthesia", "desc": "AI数字人视频，B端付费", "tags": ["数字人", "B端"]},
        ]
    },
    {
        "name": "ai-monetization",
        "title": "AI Monetization",
        "icon": "💰",
        "tagline": "用 AI 做被动收入的方法大全",
        "tools": [
            {"name": "AI内容站", "desc": "用AI批量生成内容，靠广告赚钱", "tags": ["被动收入", "内容站"]},
            {"name": "AI提示词站", "desc": "卖高质量提示词，一次制作反复卖", "tags": ["数字产品", "提示词"]},
            {"name": "AI咨询", "desc": "帮企业用AI提效，收咨询费", "tags": ["咨询", "高客单价"]},
            {"name": "AI SaaS工具", "desc": "做一个小而美的AI工具，订阅收费", "tags": ["SaaS", "订阅"]},
            {"name": "AI API代理", "desc": "转发AI API，赚差价", "tags": ["API", "轻资产"]},
            {"name": "AI模板销售", "desc": "做Notion/PPT模板，AI辅助生产", "tags": ["模板", "数字产品"]},
        ]
    },
    {
        "name": "ai-news-brief",
        "title": "AI News Brief",
        "icon": "⚡",
        "tagline": "3分钟了解 AI 圈最新动态",
        "tools": [
            {"name": "Hacker News", "desc": "极客圈AI新闻，技术人必看", "tags": ["技术", "极客"]},
            {"name": "Ars Technica AI", "desc": "科技媒体AI板块，深度报道", "tags": ["深度", "媒体"]},
            {"name": "The Batch", "desc": "DeepLearning.AI周报，吴恩达出品", "tags": ["周报", "吴恩达"]},
            {"name": "AI News", "desc": "专门的AI新闻网站，更新快", "tags": ["新闻", "每日更新"]},
            {"name": "Twitter AI", "desc": "关注AI大佬，第一时间知道消息", "tags": ["社交", "快"]},
            {"name": "Reddit r/MachineLearning", "desc": "机器学习社区，讨论深入", "tags": ["社区", "讨论"]},
        ]
    },
]

base_dir = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"

html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{tagline}">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #111827; background: #fff; line-height: 1.6; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 2rem; }}
        nav {{ padding: 1.5rem 0; border-bottom: 1px solid #e5e7eb; margin-bottom: 3rem; }}
        nav .container {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 1.25rem; font-weight: 700; color: #111827; text-decoration: none; }}
        .nav-links a {{ margin-left: 1.5rem; color: #6b7280; text-decoration: none; font-size: 0.95rem; }}
        .nav-links a:hover {{ color: #111827; }}
        .hero {{ text-align: center; padding: 4rem 0 2rem; }}
        .hero h1 {{ font-size: 2.5rem; margin-bottom: 1rem; font-weight: 800; letter-spacing: -0.02em; }}
        .hero p {{ color: #6b7280; max-width: 600px; margin: 0 auto; font-size: 1.125rem; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.5rem; margin: 3rem 0; }}
        .card {{ padding: 1.75rem; border: 1px solid #e5e7eb; border-radius: 12px; transition: all 0.2s; }}
        .card:hover {{ border-color: #111827; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
        .card h3 {{ font-size: 1.2rem; margin-bottom: 0.75rem; font-weight: 600; }}
        .card .tag {{ display: inline-block; padding: 0.2rem 0.6rem; background: #f3f4f6; border-radius: 12px; font-size: 0.8rem; margin-right: 0.5rem; margin-bottom: 0.5rem; color: #4b5563; }}
        .card p {{ color: #6b7280; font-size: 0.95rem; margin-bottom: 1rem; }}
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
    <div class="container">
        <div class="hero">
            <h1>{icon} {title}</h1>
            <p>{tagline}</p>
        </div>
        <div class="grid">
{cards}
        </div>
    </div>
    <footer>
        <div class="container">
            <p>© 2026 {title} - 精选 AI 工具与资源</p>
        </div>
    </footer>
</body>
</html>
"""

card_template = """            <div class="card">
                <h3>{name}</h3>
                <div>
{tags}
                </div>
                <p>{desc}</p>
            </div>
"""

for site in websites:
    print(f"\n=== Upgrading {site['name']} ===")
    
    cards_html = ""
    for tool in site["tools"]:
        tags_html = ""
        for tag in tool["tags"]:
            tags_html += f'                    <span class="tag">{tag}</span>\n'
        cards_html += card_template.format(
            name=tool["name"],
            tags=tags_html.rstrip(),
            desc=tool["desc"]
        )
    
    html = html_template.format(
        title=site["title"],
        icon=site["icon"],
        tagline=site["tagline"],
        cards=cards_html
    )
    
    site_path = os.path.join(base_dir, site["name"])
    with open(os.path.join(site_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✅ Index.html upgraded with {len(site['tools'])} items")
    
    # Git push
    subprocess.run(["git", "add", "."], cwd=site_path, check=True)
    subprocess.run(["git", "commit", "-m", f"upgrade: professional {site['title']} design"], cwd=site_path, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=site_path, check=True, capture_output=True)
    print(f"  ✅ Pushed to GitHub")

print("\n=== All 9 websites upgraded! ===")
