import os

websites = [
    {
        "name": "ai-art-tools",
        "title": "AI Art Tools",
        "icon": "🎨",
        "tagline": "Best AI art and image generation tools",
        "tools": [
            {"name": "Midjourney", "desc": "最强AI绘画工具，艺术效果顶级", "tags": ["付费", "高质量", "艺术"]},
            {"name": "DALL-E 3", "desc": "OpenAI出品，文字理解能力强", "tags": ["免费额度", "OpenAI", "易上手"]},
            {"name": "Stable Diffusion", "desc": "开源免费，可本地部署，自由度高", "tags": ["开源", "免费", "本地部署"]},
            {"name": "Leonardo AI", "desc": "游戏美术风格强，适合游戏开发者", "tags": ["免费额度", "游戏美术"]},
            {"name": "MidJourney", "desc": "照片级真实感，产品摄影神器", "tags": ["付费", "真实感"]},
            {"name": "Ideogram", "desc": "文字渲染能力强，做海报Logo神器", "tags": ["免费额度", "文字设计"]},
        ]
    },
    {
        "name": "ai-writing-tools",
        "title": "AI Writing Tools",
        "icon": "✍️",
        "tagline": "Best AI writing assistant tools",
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
        "tagline": "Best AI video generation tools",
        "tools": [
            {"name": "Runway ML", "desc": "AI视频生成 pioneer，效果最好", "tags": ["付费", "高质量"]},
            {"name": "Pika Labs", "desc": "免费AI视频生成，Discord用", "tags": ["免费", "Discord"]},
            {"name": "Sora", "desc": "OpenAI视频生成，等待开放", "tags": ["OpenAI", "等待开放"]},
            {"name": "ElevenLabs", "desc": "AI配音，声音克隆", "tags": ["配音", "免费额度"]},
            {"name": "Descript", "desc": "视频编辑像编辑文档一样简单", "tags": ["编辑", "付费"]},
            {"name": "HeyGen", "desc": "AI数字人，做口播视频", "tags": ["数字人", "付费"]},
        ]
    },
    {
        "name": "ai-learning-hub",
        "title": "AI Learning Hub",
        "icon": "📚",
        "tagline": "Learn AI from scratch with tutorials",
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
        "tagline": "AI startup success stories and cases",
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
        "tagline": "How to make passive income with AI",
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
        "tagline": "3 minute AI news brief for busy people",
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
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a1a1a; background: #fff; line-height: 1.6; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 2rem; }}
        nav {{ padding: 1.5rem 0; border-bottom: 1px solid #eee; margin-bottom: 3rem; }}
        nav .container {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 1.25rem; font-weight: 700; color: #1a1a1a; text-decoration: none; }}
        .hero {{ text-align: center; padding: 4rem 0 2rem; }}
        .hero h1 {{ font-size: 2.5rem; margin-bottom: 1rem; }}
        .hero p {{ color: #666; max-width: 600px; margin: 0 auto; font-size: 1.1rem; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1.5rem; margin: 3rem 0; }}
        .card {{ padding: 1.5rem; border: 1px solid #eee; border-radius: 12px; transition: all 0.2s; }}
        .card:hover {{ border-color: #1a1a1a; transform: translateY(-2px); }}
        .card h3 {{ font-size: 1.2rem; margin-bottom: 0.5rem; }}
        .card .tag {{ display: inline-block; padding: 0.2rem 0.6rem; background: #f0f0f0; border-radius: 12px; font-size: 0.8rem; margin-right: 0.5rem; margin-bottom: 0.5rem; }}
        .card p {{ color: #666; font-size: 0.9rem; margin-bottom: 1rem; }}
        footer {{ padding: 3rem 0; border-top: 1px solid #eee; text-align: center; color: #999; margin-top: 4rem; }}
    </style>
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">{icon} {title}</a>
            <div>
                <a href="/" style="margin-right: 1.5rem; color: #666; text-decoration: none;">Home</a>
                <a href="/about" style="color: #666; text-decoration: none;">关于</a>
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
            <p>© 2026 {title} - 由 AI 智能集群自动维护更新</p>
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
    print(f"\n=== Updating {site['name']} ===")
    
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
    print(f"  ✅ Index.html updated with {len(site['tools'])} tools")
    
    # Git push
    import subprocess
    subprocess.run(["git", "add", "."], cwd=site_path, check=True)
    subprocess.run(["git", "commit", "-m", f"feat: add {len(site['tools'])} {site['name']} items"], cwd=site_path, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=site_path, check=True, capture_output=True)
    print(f"  ✅ Pushed to GitHub")

print("\n=== All 7 websites updated! ===")
