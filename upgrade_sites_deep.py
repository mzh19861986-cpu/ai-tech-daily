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
            {"name": "产品经理提示词", "desc": "写PRD、画流程图、做用户调研，PM效率神器", "tags": ["产品", "PM"]},
            {"name": "设计师提示词", "desc": "UI设计、配色方案、原型描述，设计师辅助", "tags": ["设计", "UI"]},
            {"name": "数据分析提示词", "desc": "写SQL、做分析、可视化图表，数据分析师助手", "tags": ["数据", "分析"]},
            {"name": "视频脚本提示词", "desc": "写短视频脚本、分镜、旁白，创作者必备", "tags": ["视频", "创作"]},
            {"name": "电商运营提示词", "desc": "写商品标题、详情页、客服话术，电商运营", "tags": ["电商", "运营"]},
            {"name": "SEO优化提示词", "desc": "写SEO标题、meta描述、关键词布局", "tags": ["SEO", "推广"]},
            {"name": "面试准备提示词", "desc": "准备面试题、模拟面试、写简历", "tags": ["求职", "面试"]},
            {"name": "心理咨询提示词", "desc": "情绪疏导、压力管理、自我反思", "tags": ["心理", "健康"]},
            {"name": "翻译润色提示词", "desc": "中英互译、学术润色、邮件润色", "tags": ["翻译", "润色"]},
            {"name": "小红书文案提示词", "desc": "写小红书笔记、爆款标题、种草文案", "tags": ["小红书", "种草"]},
            {"name": "公众号文章提示词", "desc": "写公众号文章、爆款选题、排版建议", "tags": ["公众号", "文章"]},
            {"name": "短视频文案提示词", "desc": "写抖音/快手脚本、口播文案、钩子开头", "tags": ["抖音", "短视频"]},
            {"name": "PPT制作提示词", "desc": "写PPT大纲、每页内容、演讲备注", "tags": ["PPT", "演示"]},
            {"name": "报告撰写提示词", "desc": "写周报、月报、年度总结，职场必备", "tags": ["职场", "报告"]},
            {"name": "邮件撰写提示词", "desc": "写商务邮件、求职信、跟进邮件", "tags": ["邮件", "商务"]},
            {"name": "会议纪要提示词", "desc": "整理会议记录、提炼行动项、写跟进邮件", "tags": ["会议", "效率"]},
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
            {"name": "Codeium", "desc": "免费AI代码补全，支持多IDE", "tags": ["免费", "补全"]},
            {"name": "Amazon CodeWhisperer", "desc": "AWS出品，安全扫描+代码生成", "tags": ["AWS", "安全"]},
            {"name": "Replit AI", "desc": "在线IDE内置AI，全栈开发", "tags": ["在线IDE", "全栈"]},
            {"name": "Sourcery", "desc": "AI代码重构，自动优化代码质量", "tags": ["重构", "代码质量"]},
            {"name": "Codiga", "desc": "AI代码审查+安全分析", "tags": ["代码审查", "安全"]},
            {"name": "Continue", "desc": "开源AI编程助手，VS Code插件", "tags": ["开源", "VS Code"]},
            {"name": "Cline", "desc": "VS Code AI编程助手，自动改代码", "tags": ["VS Code", "自动改"]},
            {"name": "Aider", "desc": "终端AI编程助手，Git集成", "tags": ["终端", "Git"]},
            {"name": "Devin", "desc": "AI软件工程师，自动完成任务", "tags": ["AI工程师", "自动"]},
            {"name": "GPT Engineer", "desc": "一句话生成完整项目", "tags": ["项目生成", "一键"]},
            {"name": "Bolt.new", "desc": "浏览器里AI全栈开发", "tags": ["浏览器", "全栈"]},
            {"name": "v0.dev", "desc": "Vercel出品，AI生成UI组件", "tags": ["UI", "Vercel"]},
            {"name": "Figma AI", "desc": "Figma内置AI设计转代码", "tags": ["Figma", "设计转代码"]},
        ]
    },
]

base_dir = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"

# 先做前两个，看看效果
for site in websites:
    print(f"\n=== Upgrading {site['name']} to {len(site['tools'])} items ===")
    
    # 读取现有HTML，然后替换内容
    site_path = os.path.join(base_dir, site["name"])
    with open(os.path.join(site_path, "index.html"), "r", encoding="utf-8") as f:
        html = f.read()
    
    # 生成新的cards
    cards_html = ""
    card_template = """            <div class="card">
                <h3>{name}</h3>
                <div>
{tags}
                </div>
                <p>{desc}</p>
            </div>
"""
    for tool in site["tools"]:
        tags_html = ""
        for tag in tool["tags"]:
            tags_html += f'                    <span class="tag">{tag}</span>\n'
        cards_html += card_template.format(
            name=tool["name"],
            tags=tags_html.rstrip(),
            desc=tool["desc"]
        )
    
    # 替换grid部分
    import re
    # 找到 <div class="grid"> 到 </div> 的部分
    pattern = r'(<div class="grid">).*?(</div>\s*</div>\s*<footer>)'
    replacement = f'\\1\n{cards_html}        \\2'
    new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    
    with open(os.path.join(site_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"  ✅ {len(site['tools'])} items now")
    
    # Git push
    subprocess.run(["git", "add", "."], cwd=site_path, check=True)
    subprocess.run(["git", "commit", "-m", f"expand: {len(site['tools'])} items now"], cwd=site_path, capture_output=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=site_path, check=True, capture_output=True)
    print(f"  ✅ Pushed to GitHub")

print("\n=== First 2 sites upgraded! ===")
