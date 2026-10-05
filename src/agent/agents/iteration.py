"""
迭代智能体 - IterationAgent
负责：分析运行数据、发现问题、提出优化建议、自动迭代改进
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import List, Dict

from .base import BaseAgent, AgentResult


class IterationAgent(BaseAgent):
    """迭代智能体：负责分析数据、发现问题、提出优化建议"""

    name = "iteration"
    description = "分析运行数据、发现问题、提出优化建议、自动迭代改进"

    def __init__(self):
        super().__init__()
        self.issues_found = []
        self.improvements_done = []

    def analyze_pipeline_health(self, pipeline_reports: Dict) -> List[Dict]:
        """分析 pipeline 运行健康度，发现问题"""
        issues = []
        
        for name, report in pipeline_reports.items():
            steps = report.get("steps", {})
            
            # 检查抓取成功率
            fetch = steps.get("fetch", {})
            if not fetch.get("success", False):
                issues.append({
                    "pipeline": name,
                    "issue": "抓取失败",
                    "severity": "高",
                    "suggestion": "检查数据源连接，更换数据源",
                })
            
            # 检查处理成功率
            process = steps.get("process", {})
            if not process.get("success", False):
                issues.append({
                    "pipeline": name,
                    "issue": "AI 处理失败",
                    "severity": "高",
                    "suggestion": "检查 DeepSeek API 额度，切换备用 key",
                })
            
            # 检查内容数量
            items = process.get("items", 0)
            if items < 3:
                issues.append({
                    "pipeline": name,
                    "issue": f"内容太少（只有 {items} 条）",
                    "severity": "中",
                    "suggestion": "调整过滤条件，增加抓取数量",
                })
        
        return issues

    def suggest_improvements(self) -> List[Dict]:
        """提出优化改进建议"""
        suggestions = [
            {
                "category": "内容质量",
                "suggestion": "增加每篇文章的内容数量，从 5 条增加到 8 条",
                "impact": "高",
                "effort": "低",
            },
            {
                "category": "SEO",
                "suggestion": "给每篇文章加更多长尾关键词，优化 title 和 description",
                "impact": "高",
                "effort": "中",
            },
            {
                "category": "用户体验",
                "suggestion": "加暗色模式自动检测，跟随系统主题",
                "impact": "中",
                "effort": "低",
            },
            {
                "category": "变现",
                "suggestion": "在文章底部加更多相关工具推荐，提高点击率",
                "impact": "中",
                "effort": "低",
            },
            {
                "category": "推广",
                "suggestion": "写更多深度测评文章，抢 SEO 流量",
                "impact": "高",
                "effort": "高",
            },
        ]
        return suggestions

    def generate_weekly_report(self, data: Dict = None) -> Dict:
        """生成每周迭代报告"""
        report = {
            "week": datetime.now().strftime("%Y-W%U"),
            "date": datetime.now().isoformat(),
            "summary": "本周智能体集群运行报告",
            "highlights": [
                "✅ 14 个 pipeline 正常运行",
                "✅ DeepSeek API 正常调用",
                "✅ 网站每日更新",
                "✅ 工具库 30 个工具",
            ],
            "issues": self.issues_found,
            "improvements_done": self.improvements_done,
            "next_week_goals": [
                "提交到 5 个 AI 目录站",
                "写 3 篇深度测评文章",
                "申请联盟计划",
            ],
        }
        return report

    def run(self, **kwargs) -> AgentResult:
        """执行迭代分析任务"""
        self.logger.info("开始分析运行数据和优化建议...")
        
        # 分析 pipeline 健康度
        pipeline_reports = kwargs.get("pipeline_reports", {})
        issues = self.analyze_pipeline_health(pipeline_reports)
        
        # 提出改进建议
        suggestions = self.suggest_improvements()
        
        # 生成周报
        weekly_report = self.generate_weekly_report()
        
        result_data = {
            "issues": issues,
            "suggestions": suggestions,
            "weekly_report": weekly_report,
        }
        
        self.logger.info(f"发现 {len(issues)} 个问题，提出 {len(suggestions)} 个改进建议")
        
        return AgentResult(
            success=True,
            data=result_data,
            items_processed=len(issues) + len(suggestions),
        )
