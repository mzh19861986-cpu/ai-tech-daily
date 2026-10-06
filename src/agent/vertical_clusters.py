"""
每个垂直网站的专属智能集群配置
每个网站都有自己的一组智能体，由母体统一调度
"""

# 每个网站的专属智能集群
VERTICAL_SITE_CLUSTERS = {
    "ai-prompts-hub": {
        "cluster_name": "提示词站智能集群",
        "agents": [
            {"name": "PromptScout", "role": "全网搜集优质提示词"},
            {"name": "PromptCurator", "role": "筛选+分类+优化提示词"},
            {"name": "PromptPublisher", "role": "发布到网站"},
            {"name": "PromptSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天搜集10个新提示词，更新到网站",
    },
    "ai-coding-tools": {
        "cluster_name": "编程工具站智能集群",
        "agents": [
            {"name": "CodingToolScout", "role": "追踪最新AI编程工具"},
            {"name": "ToolReviewer", "role": "测试+评测+打分"},
            {"name": "ToolPublisher", "role": "发布工具榜单"},
            {"name": "CodingSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天发现2个新编程工具，更新榜单",
    },
    "ai-art-tools": {
        "cluster_name": "绘画工具站智能集群",
        "agents": [
            {"name": "ArtToolScout", "role": "追踪最新AI绘画工具"},
            {"name": "DemoGenerator", "role": "生成示例图对比效果"},
            {"name": "ArtPublisher", "role": "发布工具评测"},
            {"name": "ArtSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天发现2个新绘画工具，更新榜单",
    },
    "ai-writing-tools": {
        "cluster_name": "写作工具站智能集群",
        "agents": [
            {"name": "WritingToolScout", "role": "追踪最新AI写作工具"},
            {"name": "WritingTester", "role": "实际测试写作效果"},
            {"name": "WritingPublisher", "role": "发布工具评测"},
            {"name": "WritingSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天发现2个新写作工具，更新榜单",
    },
    "ai-video-tools": {
        "cluster_name": "视频工具站智能集群",
        "agents": [
            {"name": "VideoToolScout", "role": "追踪最新AI视频工具"},
            {"name": "VideoDemoMaker", "role": "制作效果演示对比"},
            {"name": "VideoPublisher", "role": "发布工具评测"},
            {"name": "VideoSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天发现2个新视频工具，更新榜单",
    },
    "ai-learning-hub": {
        "cluster_name": "学习资源站智能集群",
        "agents": [
            {"name": "LearningResourceScout", "role": "搜集最新AI学习资源"},
            {"name": "CuratorAgent", "role": "筛选+分类+整理"},
            {"name": "LearningPublisher", "role": "发布学习资源列表"},
            {"name": "LearningSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天搜集5个新学习资源，更新列表",
    },
    "ai-startup-cases": {
        "cluster_name": "创业案例站智能集群",
        "agents": [
            {"name": "StartupScout", "role": "追踪AI创业新闻和融资"},
            {"name": "CaseAnalyst", "role": "分析商业模式和成功因素"},
            {"name": "CasePublisher", "role": "发布案例分析"},
            {"name": "StartupSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天分析1个新创业案例",
    },
    "ai-monetization": {
        "cluster_name": "变现方法站智能集群",
        "agents": [
            {"name": "MonetizationScout", "role": "搜集最新AI变现方法"},
            {"name": "CaseValidator", "role": "验证方法可行性"},
            {"name": "MonetizationPublisher", "role": "发布方法教程"},
            {"name": "MonetizationSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天整理1个新变现方法",
    },
    "ai-news-brief": {
        "cluster_name": "新闻快讯站智能集群",
        "agents": [
            {"name": "NewsFetcher", "role": "抓取最新AI新闻"},
            {"name": "NewsSummarizer", "role": "AI生成3分钟摘要"},
            {"name": "NewsPublisher", "role": "发布每日简报"},
            {"name": "NewsSeo", "role": "SEO优化"},
        ],
        "daily_task": "每天生成3分钟AI新闻简报",
    },
}


def get_all_clusters():
    """获取所有垂直网站智能集群状态"""
    result = []
    for site, config in VERTICAL_SITE_CLUSTERS.items():
        result.append({
            "site": site,
            "cluster_name": config["cluster_name"],
            "agent_count": len(config["agents"]),
            "daily_task": config["daily_task"],
            "status": "✅ 已配置"
        })
    return result


if __name__ == "__main__":
    print("=== 9个垂直网站专属智能集群 ===")
    print()
    for c in get_all_clusters():
        print(f"📦 {c['site']}")
        print(f"   集群名: {c['cluster_name']}")
        print(f"   智能体数: {c['agent_count']}个")
        print(f"   每日任务: {c['daily_task']}")
        print(f"   状态: {c['status']}")
        print()
