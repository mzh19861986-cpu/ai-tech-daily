"""
网站管理智能体 - 10个垂直网站统一管理
每个网站有一个专属子智能体，归母体 Orchestrator 统一调度
"""

# 网站管理智能体列表
SITE_MANAGERS = [
    {
        "name": "MainSiteManager",
        "site": "ai-tech-daily",
        "url": "https://mzh19861986-cpu.github.io/ai-tech-daily/",
        "responsibility": "主站管理：每日14个pipeline运行、内容质量、SEO优化",
        "status": "✅ 运行中"
    },
    {
        "name": "PromptsHubManager",
        "site": "ai-prompts-hub",
        "url": "https://mzh19861986-cpu.github.io/ai-prompts-hub/",
        "responsibility": "提示词站管理：持续更新优质提示词、分类整理、用户体验优化",
        "status": "✅ 运行中"
    },
    {
        "name": "CodingToolsManager",
        "site": "ai-coding-tools",
        "url": "https://mzh19861986-cpu.github.io/ai-coding-tools/",
        "responsibility": "编程工具站管理：追踪最新AI编程工具、更新榜单、评测对比",
        "status": "✅ 运行中"
    },
    {
        "name": "ArtToolsManager",
        "site": "ai-art-tools",
        "url": "https://mzh19861986-cpu.github.io/ai-art-tools/",
        "responsibility": "绘画工具站管理：追踪最新AI绘画工具、效果对比、教程整理",
        "status": "✅ 运行中"
    },
    {
        "name": "WritingToolsManager",
        "site": "ai-writing-tools",
        "url": "https://mzh19861986-cpu.github.io/ai-writing-tools/",
        "responsibility": "写作工具站管理：追踪最新AI写作工具、场景化推荐、效果对比",
        "status": "✅ 运行中"
    },
    {
        "name": "VideoToolsManager",
        "site": "ai-video-tools",
        "url": "https://mzh19861986-cpu.github.io/ai-video-tools/",
        "responsibility": "视频工具站管理：追踪最新AI视频工具、效果评测、教程整理",
        "status": "✅ 运行中"
    },
    {
        "name": "LearningHubManager",
        "site": "ai-learning-hub",
        "url": "https://mzh19861986-cpu.github.io/ai-learning-hub/",
        "responsibility": "学习资源站管理：收集整理AI学习资源、课程推荐、学习路径规划",
        "status": "✅ 运行中"
    },
    {
        "name": "StartupCasesManager",
        "site": "ai-startup-cases",
        "url": "https://mzh19861986-cpu.github.io/ai-startup-cases/",
        "responsibility": "创业案例站管理：追踪AI创业案例、融资动态、商业模式分析",
        "status": "✅ 运行中"
    },
    {
        "name": "MonetizationManager",
        "site": "ai-monetization",
        "url": "https://mzh19861986-cpu.github.io/ai-monetization/",
        "responsibility": "变现方法站管理：收集AI变现方法、案例分析、实操教程",
        "status": "✅ 运行中"
    },
    {
        "name": "NewsBriefManager",
        "site": "ai-news-brief",
        "url": "https://mzh19861986-cpu.github.io/ai-news-brief/",
        "responsibility": "新闻快讯站管理：3分钟AI快讯、每日热点、重要事件追踪",
        "status": "✅ 运行中"
    },
]


class SiteManager:
    """网站管理智能体基类"""
    
    def __init__(self, site_config):
        self.name = site_config["name"]
        self.site = site_config["site"]
        self.url = site_config["url"]
        self.responsibility = site_config["responsibility"]
        self.status = site_config["status"]
    
    def report_status(self):
        return {
            "name": self.name,
            "site": self.site,
            "url": self.url,
            "responsibility": self.responsibility,
            "status": self.status
        }


# 创建所有网站管理智能体实例
site_managers = [SiteManager(config) for config in SITE_MANAGERS]


def get_all_site_managers():
    """获取所有网站管理智能体状态"""
    return [manager.report_status() for manager in site_managers]


if __name__ == "__main__":
    print("=== 网站管理智能体列表（10个）===")
    for m in get_all_site_managers():
        print(f"  {m['status']} {m['name']} -> {m['site']}")
        print(f"    职责: {m['responsibility']}")
        print(f"    地址: {m['url']}")
        print()
