"""
进化智能体 - EvolutionAgent
负责：分析集群不足、决定下一步任务、自动分裂新智能体、持续进化
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import List, Dict

from .base import BaseAgent, AgentResult


class EvolutionPlan:
    """进化计划"""
    def __init__(self, name: str, reason: str, new_agents: List[str], next_tasks: List[str]):
        self.name = name
        self.reason = reason
        self.new_agents = new_agents
        self.next_tasks = next_tasks
        self.created_at = datetime.now().isoformat()


class EvolutionAgent(BaseAgent):
    """进化智能体：分析集群不足、自动分裂新智能体、决定下一步任务"""

    name = "evolution"
    description = "分析集群不足、自动分裂新智能体、决定下一步任务、持续进化"

    def __init__(self):
        super().__init__()
        self.evolution_history: List[EvolutionPlan] = []

    def analyze_cluster_gaps(self, current_agents: List[str]) -> Dict:
        """分析当前集群的不足"""
        gaps = []
        
        # 检查缺少的能力
        all_needed_agents = {
            "FetcherAgent": "抓取数据",
            "ProcessorAgent": "AI 加工",
            "QualityControlAgent": "质量把关",
            "PublisherAgent": "发布输出",
            "MonitorAgent": "监控状态",
            "OpportunityScoutAgent": "发现机会",
            "PromoterAgent": "推广引流",
            "MonetizerAgent": "变现优化",
            "IterationAgent": "迭代改进",
            "AutoLoopAgent": "自动调度",
        }
        
        for agent_name, purpose in all_needed_agents.items():
            if agent_name not in current_agents:
                gaps.append({
                    "missing": agent_name,
                    "purpose": purpose,
                    "priority": "high",
                })
        
        return {"gaps": gaps, "total_gaps": len(gaps)}

    def suggest_new_agents(self) -> List[Dict]:
        """建议需要新增的智能体"""
        new_agents = [
            {
                "name": "SeoAgent",
                "purpose": "SEO 优化智能体",
                "description": "自动优化网站 SEO，提交搜索引擎，分析关键词排名",
                "priority": "high",
                "reason": "目前 SEO 还靠手动，需要自动化",
            },
            {
                "name": "AnalyticsAgent",
                "purpose": "数据分析智能体",
                "description": "分析网站流量、用户行为、转化率，给出优化建议",
                "priority": "medium",
                "reason": "现在还没有流量数据分析",
            },
            {
                "name": "CommunityAgent",
                "purpose": "社区运营智能体",
                "description": "自动在 Reddit、HN、V2EX 等社区发帖推广",
                "priority": "medium",
                "reason": "推广现在还靠手动",
            },
        ]
        return new_agents

    def plan_next_tasks(self) -> List[Dict]:
        """规划下一步任务"""
        tasks = [
            {
                "priority": 1,
                "task": "申请 AI 工具联盟计划",
                "description": "申请 Jasper、ElevenLabs 等联盟计划，替换工具链接",
                "impact": "高",
            },
            {
                "priority": 2,
                "task": "写深度测评文章",
                "description": "写 10 篇热门 AI 工具深度测评，抢 SEO 流量",
                "impact": "高",
            },
            {
                "priority": 3,
                "task": "提交到 AI 目录站",
                "description": "提交网站到 5-10 个 AI 工具目录，获得反向链接",
                "impact": "中",
            },
            {
                "priority": 4,
                "task": "做数字产品",
                "description": "做一个 AI Prompt 合集，在 Gumroad 上卖",
                "impact": "中",
            },
        ]
        return tasks

    def run(self, **kwargs) -> AgentResult:
        """执行进化规划"""
        self.logger.info("=== 开始集群进化分析 ===")
        
        current_agents = kwargs.get("current_agents", [])
        
        # 分析不足
        gaps = self.analyze_cluster_gaps(current_agents)
        
        # 建议新智能体
        new_agents = self.suggest_new_agents()
        
        # 规划下一步任务
        next_tasks = self.plan_next_tasks()
        
        # 生成进化计划
        plan = EvolutionPlan(
            name="v2.0 进化计划",
            reason="增加 SEO 自动化、数据分析、社区运营能力",
            new_agents=[a["name"] for a in new_agents],
            next_tasks=[t["task"] for t in next_tasks],
        )
        self.evolution_history.append(plan)
        
        result_data = {
            "current_agents": len(current_agents),
            "gaps": gaps,
            "suggested_new_agents": new_agents,
            "next_tasks": next_tasks,
            "evolution_plan": plan,
        }
        
        self.logger.info(f"进化分析完成: 发现 {gaps['total_gaps']} 个缺口，建议新增 {len(new_agents)} 个智能体，规划 {len(next_tasks)} 个任务")
        
        return AgentResult(
            success=True,
            data=result_data,
            items_processed=len(new_agents) + len(next_tasks),
        )
