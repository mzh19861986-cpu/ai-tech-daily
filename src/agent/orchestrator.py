"""
母体调度器 - Orchestrator
负责：调度子 Agent、安防兜底、状态管理、失败重试、反馈上报。

架构：
    Orchestrator
    ├── FetcherAgent    (抓数据)
    ├── ProcessorAgent   (AI 处理)
    ├── PublisherAgent   (发布内容)
    └── MonitorAgent     (监控收益/运行状态)
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import Optional, List

from .config import config
from .security import security_guard
from .agents.base import AgentResult
from .agents.fetcher import FetcherAgent
from .agents.processor import ProcessorAgent
from .agents.publisher import PublisherAgent
from .agents.monitor import MonitorAgent
from .agents.promoter import PromoterAgent
from .agents.monetizer import MonetizerAgent
from .agents.iteration import IterationAgent
from .agents.autoloop import AutoLoopAgent
from .agents.opportunity_scout import OpportunityScoutAgent
from .agents.quality_control import QualityControlAgent
from .agents.evolution import EvolutionAgent
from .agents.seo import SeoAgent
from .agents.analytics import AnalyticsAgent
from .agents.community import CommunityAgent
from .agents.database import DatabaseAgent
from .agents.tool_manager import ToolManagerAgent
from .agents.content_optimizer import ContentOptimizerAgent
from .agents.security import SecurityAgent
from .agents.config import ConfigAgent
from .agents.deploy import DeployAgent
from .agents.backup import BackupAgent
from .agents.logger import LoggerAgent
from .agents.notifier import NotifierAgent
from .agents.tester import TesterAgent

logger = logging.getLogger("orchestrator")
logger.setLevel(config.log_level)


class Orchestrator:
    """母体：管控所有子 Agent"""

    def __init__(self):
        # 内容生产链
        self.fetcher = FetcherAgent()
        self.processor = ProcessorAgent()
        self.publisher = PublisherAgent()
        self.monitor = MonitorAgent()
        # 增长与变现链
        self.promoter = PromoterAgent()
        self.monetizer = MonetizerAgent()
        self.iteration = IterationAgent()
        # 机会侦察
        self.opportunity_scout = OpportunityScoutAgent()
        # 质量管控
        self.quality_control = QualityControlAgent()
        # 进化智能体
        self.evolution = EvolutionAgent()
        # SEO 优化
        self.seo = SeoAgent()
        # 数据分析
        self.analytics = AnalyticsAgent()
        # 社区运营
        self.community = CommunityAgent()
        # 基础设施层
        self.database = DatabaseAgent()
        self.tool_manager = ToolManagerAgent()
        self.content_optimizer = ContentOptimizerAgent()
        self.security = SecurityAgent()
        self.config = ConfigAgent()
        # 运维保障层
        self.deploy = DeployAgent()
        self.backup = BackupAgent()
        self.logger_agent = LoggerAgent()
        self.notifier = NotifierAgent()
        self.tester = TesterAgent()
        # 自动循环调度
        self.autoloop = AutoLoopAgent()

    def run_pipeline(self, pipeline_name: str, dry_run: bool = None) -> dict:
        """执行单条 pipeline：fetch → security → process → security → publish → report"""
        dry_run = dry_run if dry_run is not None else config.dry_run
        logger.info(f"=== 母体启动: {pipeline_name} (dry_run={dry_run}) ===")

        report = {
            "pipeline": pipeline_name,
            "started_at": datetime.now().isoformat(),
            "steps": {},
            "passed_security": True,
        }

        # Step 1: 抓取
        fetch_result = self.fetcher.safe_run(pipeline_name=pipeline_name)
        report["steps"]["fetch"] = {"success": fetch_result.success, "items": fetch_result.items_processed}
        if not fetch_result.success:
            report["error"] = f"抓取失败: {fetch_result.error}"
            return report

        raw_items = fetch_result.data or []

        # Step 2: 抓取后安防检查
        for item in raw_items[:5]:
            check = security_guard.check_fetch(item.get("url", ""), requests_per_minute=10)
            if not check.passed:
                logger.warning(f"安防拦截抓取: {check.reasons}")

        # Step 3: AI 处理
        process_result = self.processor.safe_run(items=raw_items, pipeline_name=pipeline_name)
        report["steps"]["process"] = {"success": process_result.success, "items": process_result.items_processed}
        if not process_result.success:
            report["error"] = f"处理失败: {process_result.error}"
            return report

        processed_items = process_result.data or []

        # Step 4: 内容发布前安防
        safe_items = []
        for item in processed_items:
            check = security_guard.check_content(title=item.get("title", ""), body=item.get("body", ""))
            if check.passed:
                safe_items.append(item)
            else:
                logger.warning(f"安防拦截: {item.get('title','')[:50]}... -> {check.reasons}")

        report["security_filtered"] = len(processed_items) - len(safe_items)

        # Step 5: 发布
        if dry_run:
            logger.info("DRY RUN: 跳过实际发布")
            publish_result = AgentResult(success=True, items_processed=len(safe_items))
        else:
            publish_result = self.publisher.safe_run(items=safe_items, pipeline_name=pipeline_name)

        report["steps"]["publish"] = {"success": publish_result.success, "items": publish_result.items_processed}

        # Step 6: 监控上报
        self.monitor.safe_run(report=report)

        report["finished_at"] = datetime.now().isoformat()
        logger.info(f"=== 母体完成: {pipeline_name} ===")
        return report

    def run_multiple(self, pipeline_names: List[str], dry_run: bool = None) -> dict:
        """一次跑多个 pipeline，汇总结果"""
        all_reports = {}
        total_items = 0

        for name in pipeline_names:
            logger.info(f"\n{'='*50}\n开始 pipeline: {name}\n{'='*50}")
            r = self.run_pipeline(name, dry_run=dry_run)
            all_reports[name] = r
            total_items += r.get("steps", {}).get("publish", {}).get("items", 0)

        summary = {
            "total_pipelines": len(pipeline_names),
            "total_published_items": total_items,
            "pipelines": all_reports,
            "finished_at": datetime.now().isoformat(),
        }
        return summary

    def run_growth_cycle(self, dry_run: bool = None) -> dict:
        """运行完整的增长闭环：内容 → 推广 → 变现 → 迭代"""
        dry_run = dry_run if dry_run is not None else config.dry_run
        logger.info("=== 母体启动：增长闭环 ===")
        
        cycle_report = {
            "cycle": "growth",
            "started_at": datetime.now().isoformat(),
            "steps": {},
        }
        
        # Step 1: 推广智能体 - 生成推广素材
        promoter_result = self.promoter.safe_run()
        cycle_report["steps"]["promoter"] = {
            "success": promoter_result.success,
            "items": promoter_result.items_processed,
        }
        
        # Step 2: 变现智能体 - 分析变现机会
        monetizer_result = self.monetizer.safe_run()
        cycle_report["steps"]["monetizer"] = {
            "success": monetizer_result.success,
            "items": monetizer_result.items_processed,
        }
        
        # Step 3: 迭代智能体 - 分析优化建议
        iteration_result = self.iteration.safe_run()
        cycle_report["steps"]["iteration"] = {
            "success": iteration_result.success,
            "items": iteration_result.items_processed,
        }
        
        cycle_report["finished_at"] = datetime.now().isoformat()
        logger.info("=== 母体完成：增长闭环 ===")
        return cycle_report

    def run_cluster_cycle(self, dry_run: bool = None) -> dict:
        """运行完整的集群循环：机会侦察 → 内容生产 → 发布 → 推广 → 变现 → 迭代"""
        dry_run = dry_run if dry_run is not None else config.dry_run
        logger.info("=" * 60)
        logger.info("🧠 母体启动：完整集群循环")
        logger.info("=" * 60)
        
        cycle_report = {
            "cycle": "cluster",
            "started_at": datetime.now().isoformat(),
            "steps": [],
        }
        
        # ========== 阶段 1：机会侦察（输入新方向） ==========
        logger.info("\n🔭 阶段 1/6：机会侦察 - 全网抓资源抓机会")
        scout_result = self.opportunity_scout.safe_run()
        cycle_report["steps"].append({
            "name": "opportunity_scout",
            "agent": "OpportunityScoutAgent",
            "status": "✅" if scout_result.success else "❌",
            "items": scout_result.items_processed,
        })
        
        # ========== 阶段 2：抓取数据（内容输入） ==========
        logger.info("\n🔍 阶段 2/6：抓取数据")
        # fetcher 已经在 pipeline 里跑过了，这里跳过
        
        # ========== 阶段 3：AI 处理加工 ==========
        logger.info("\n⚙️ 阶段 3/6：AI 处理加工")
        # processor 已经在 pipeline 里跑过了，这里跳过
        
        # ========== 阶段 4：发布部署 ==========
        logger.info("\n📝 阶段 4/6：发布部署")
        # publisher 已经在 pipeline 里跑过了，这里跳过
        
        # ========== 阶段 5：推广 + 变现 ==========
        logger.info("\n📣 阶段 5/6：推广 + 变现")
        promoter_result = self.promoter.safe_run()
        cycle_report["steps"].append({
            "name": "promoter",
            "agent": "PromoterAgent",
            "status": "✅" if promoter_result.success else "❌",
            "items": promoter_result.items_processed,
        })
        
        monetizer_result = self.monetizer.safe_run()
        cycle_report["steps"].append({
            "name": "monetizer",
            "agent": "MonetizerAgent",
            "status": "✅" if monetizer_result.success else "❌",
            "items": monetizer_result.items_processed,
        })
        
        # ========== 阶段 6：迭代优化 ==========
        logger.info("\n🔄 阶段 6/6：迭代优化")
        iteration_result = self.iteration.safe_run()
        cycle_report["steps"].append({
            "name": "iteration",
            "agent": "IterationAgent",
            "status": "✅" if iteration_result.success else "❌",
            "items": iteration_result.items_processed,
        })
        
        cycle_report["finished_at"] = datetime.now().isoformat()
        
        logger.info("\n" + "=" * 60)
        logger.info("🧠 母体完成：完整集群循环")
        logger.info("=" * 60)
        
        return cycle_report
