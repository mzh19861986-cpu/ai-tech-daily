"""
推广智能体 - PromoterAgent
负责：生成推广文案、准备目录站提交信息、跟踪推广效果
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import List, Dict

from .base import BaseAgent, AgentResult


class PromoterAgent(BaseAgent):
    """推广智能体：负责网站推广和目录站提交"""

    name = "promoter"
    description = "生成推广文案、准备目录站提交信息、跟踪推广效果"

    def __init__(self):
        super().__init__()
        self.submission_sites = [
            {
                "name": "There's An AI For That",
                "url": "https://theresanaiforthat.com/submit/",
                "type": "AI目录站",
                "free": True,
            },
            {
                "name": "AI Tool Guru",
                "url": "https://aitoolguru.com/submit/",
                "type": "AI目录站",
                "free": True,
            },
            {
                "name": "What The AI",
                "url": "https://whattheai.com/submit/",
                "type": "AI目录站",
                "free": True,
            },
            {
                "name": "Indie Hackers",
                "url": "https://www.indiehackers.com/new-post",
                "type": "社区",
                "free": True,
            },
            {
                "name": "Hacker News",
                "url": "https://news.ycombinator.com/submit",
                "type": "社区",
                "free": True,
            },
        ]

    def generate_submission_text(self, site_name: str = None) -> Dict:
        """生成目录站提交文案"""
        site_url = "https://mzh19861986-cpu.github.io/ai-tech-daily/"
        
        submission = {
            "name": "AI Tech Daily",
            "url": site_url,
            "tagline": "每天 5 分钟，了解 AI 圈最重要的事",
            "description": "由 AI Agent 自动抓取、分析、生成的 AI 技术日报。覆盖 AI 新闻、开源工具、新品发布、开发技巧。全部免费，每日更新。",
            "category": "AI Tools / News",
            "pricing": "Free",
            "features": [
                "每日自动更新 AI 技术新闻",
                "中文翻译版，适合国内开发者",
                "精选 AI 工具推荐",
                "变现指南，帮助你用 AI 赚钱",
                "纯静态网站，加载速度快",
            ],
        }
        
        if site_name == "Indie Hackers":
            submission["post_title"] = "Show HN: I built an AI Agent that generates daily tech news reports"
            submission["post_body"] = f"""
Hi HN! 👋

I built an AI Agent system that automatically:
1. Fetches news from Hacker News, GitHub Trending, Dev.to, Product Hunt
2. Uses DeepSeek AI to analyze and summarize the news
3. Translates to Chinese
4. Generates a static website with 14 different daily reports
5. Auto-deploys to GitHub Pages every day

The site is live here: {site_url}

It's completely free and open source. Would love to hear your feedback!
            """
        
        return submission

    def generate_social_posts(self) -> List[str]:
        """生成社交媒体推广文案"""
        posts = [
            "🤖 AI Tech Daily - 每天 5 分钟，了解 AI 圈最重要的事！\n\n✅ 每日自动更新\n✅ 中文翻译版\n✅ 精选 AI 工具\n✅ 变现指南\n\n👉 https://mzh19861986-cpu.github.io/ai-tech-daily/",
            "🚀 我做了一个 AI 自动生成的技术日报网站！\n\n🤖 由 AI Agent 自动抓取、分析、生成\n📰 覆盖 AI 新闻、开源工具、新品发布\n🇨🇳 中文翻译版，适合国内开发者\n\n快来看看吧！",
            "💡 每天花 5 分钟了解 AI 圈发生了什么？\n\n我们的 AI 日报每天自动生成：\n• 热门 AI 新闻\n• 开源工具推荐\n• 开发技巧分享\n• 变现方法指南\n\n全部免费，每日更新！",
        ]
        return posts

    def run(self, **kwargs) -> AgentResult:
        """执行推广任务"""
        self.logger.info("开始生成推广素材...")
        
        # 生成提交文案
        submissions = {}
        for site in self.submission_sites:
            submissions[site["name"]] = self.generate_submission_text(site["name"])
        
        # 生成社交媒体文案
        social_posts = self.generate_social_posts()
        
        result_data = {
            "submissions": submissions,
            "social_posts": social_posts,
            "submission_sites": self.submission_sites,
        }
        
        self.logger.info(f"生成了 {len(submissions)} 份提交文案和 {len(social_posts)} 条社交媒体文案")
        
        return AgentResult(
            success=True,
            data=result_data,
            items_processed=len(submissions) + len(social_posts),
        )
