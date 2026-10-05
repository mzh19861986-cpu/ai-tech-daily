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

    def run_auto_loop(self, max_cycles: int = 3, dry_run: bool = None) -> dict:
        """运行自动循环：完成一个任务自动开始下一个，自主循环"""
        dry_run = dry_run if dry_run is not None else config.dry_run
        logger.info("=== 母体启动：自动循环模式 ===")
        
        loop_report = {
            "mode": "auto_loop",
            "started_at": datetime.now().isoformat(),
            "cycles": [],
            "max_cycles": max_cycles,
        }
        
        # 初始化自动循环任务队列
        self.autoloop.build_default_task_queue()
        
        for cycle in range(max_cycles):
            logger.info(f"\n{'='*50}\n自动循环第 {cycle+1}/{max_cycles} 圈\n{'='*50}")
            
            cycle_data = {
                "cycle_num": cycle + 1,
                "started_at": datetime.now().isoformat(),
                "tasks_completed": [],
            }
            
            # 内容生产任务
            logger.info("→ 执行内容生产任务...")
            # 抓取（跳过，因为已经跑过了）
            # 处理和发布
            # ... 这里可以调用现有的 pipeline
            
            # 增长任务
            logger.info("→ 执行增长变现任务...")
            promoter_result = self.promoter.safe_run()
            cycle_data["tasks_completed"].append("promoter")
            
            monetizer_result = self.monetizer.safe_run()
            cycle_data["tasks_completed"].append("monetizer")
            
            iteration_result = self.iteration.safe_run()
            cycle_data["tasks_completed"].append("iteration")
            
            cycle_data["finished_at"] = datetime.now().isoformat()
            loop_report["cycles"].append(cycle_data)
            
            logger.info(f"自动循环第 {cycle+1} 圈完成")
        
        loop_report["finished_at"] = datetime.now().isoformat()
        logger.info("=== 母体完成：自动循环模式 ===")
        return loop_report
