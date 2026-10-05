"""
视频推广智能体 - VideoPromotionAgent
负责：生成短视频脚本、YouTube 标题描述、TikTok/Reels 文案
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import List, Dict

from .base import BaseAgent, AgentResult


class VideoScript:
    def __init__(self, platform: str, title: str, duration: int, script: str, hooks: List[str]):
        self.platform = platform  # youtube / tiktok / reels / shorts
        self.title = title
        self.duration = duration  # 秒
        self.script = script
        self.hooks = hooks  # 开头钩子
        self.created_at = datetime.now().isoformat()


class VideoPromotionAgent(BaseAgent):
    """视频推广智能体：生成短视频脚本、YouTube 标题、TikTok 文案"""

    name = "video_promotion"
    description = "生成短视频脚本、YouTube 标题描述、TikTok/Reels 推广文案"

    def __init__(self):
        super().__init__()
        self.platforms = ["YouTube Shorts", "TikTok", "Instagram Reels", "抖音"]
        self.scripts: List[VideoScript] = []

    def generate_short_script(self, topic: str, platform: str = "tiktok") -> VideoScript:
        """生成短视频脚本"""
        hooks = [
            f"你知道吗？{topic} 最近有大新闻！",
            "每天 5 分钟，了解 AI 圈最重要的事",
            "这个 AI 工具太好用了！我每天都在用",
        ]
        
        script = f"""
[0-3s] Hook: {hooks[0]}
[3-15s] 介绍今天的 AI 日报：{topic}
[15-30s] 3 个最重要的 AI 新闻
[30-45s] 推荐 1 个好用的 AI 工具
[45-60s] 关注我，每天获取最新 AI 资讯
"""
        
        return VideoScript(
            platform=platform,
            title=f"{topic} - 每日 AI 简报",
            duration=60,
            script=script,
            hooks=hooks,
        )

    def generate_youtube_title(self, topic: str) -> str:
        """生成 YouTube 标题"""
        titles = [
            f"【AI日报】{topic} - 今天 AI 圈发生了什么？",
            f"5分钟看懂：{topic} - 每日 AI 简报",
            f"2026年最新 {topic} - AI Tech Daily",
        ]
        return titles[0]

    def run(self, **kwargs) -> AgentResult:
        """执行视频推广任务"""
        self.logger.info("=== 开始生成视频推广素材 ===")
        
        # 生成 3 个平台的脚本
        topics = ["最新 AI 工具发布", "AI 编程助手对比", "免费 AI 资源推荐"]
        
        for topic in topics:
            for platform in ["tiktok", "youtube_shorts", "reels"]:
                script = self.generate_short_script(topic, platform)
                self.scripts.append(script)
        
        result_data = {
            "platforms": self.platforms,
            "total_scripts": len(self.scripts),
            "sample_titles": [s.title for s in self.scripts[:3]],
        }
        
        self.logger.info(f"视频推广素材生成完成: {len(self.scripts)} 个脚本")
        
        return AgentResult(
            success=True,
            data=result_data,
            items_processed=len(self.scripts),
        )
