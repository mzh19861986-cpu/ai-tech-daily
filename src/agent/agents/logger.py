"""
日志智能体 - LoggerAgent
负责：收集所有智能体的运行日志、异常告警、性能监控
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import List, Dict

from .base import BaseAgent, AgentResult


class LogEntry:
    def __init__(self, agent: str, level: str, message: str):
        self.agent = agent
        self.level = level
        self.message = message
        self.time = datetime.now().isoformat()


class LoggerAgent(BaseAgent):
    """日志智能体：收集所有智能体的运行日志、异常告警、性能监控"""

    name = "logger"
    description = "收集所有智能体的运行日志、异常告警、性能监控"

    def __init__(self):
        super().__init__()
        self.logs: List[LogEntry] = []
        self.errors: List[LogEntry] = []

    def log(self, agent: str, level: str, message: str):
        """记录日志"""
        entry = LogEntry(agent, level, message)
        self.logs.append(entry)
        if level == "ERROR":
            self.errors.append(entry)

    def get_error_report(self) -> Dict:
        """获取错误报告"""
        return {
            "total_errors": len(self.errors),
            "recent_errors": [f"{e.agent}: {e.message}" for e in self.errors[-5:]],
        }

    def run(self, **kwargs) -> AgentResult:
        """执行日志收集任务"""
        self.logger.info("=== 开始日志收集 ===")
        
        # 记录一些示例日志
        self.log("fetcher", "INFO", "抓取完成")
        self.log("processor", "INFO", "AI 处理完成")
        
        error_report = self.get_error_report()
        
        result_data = {
            "total_logs": len(self.logs),
            "errors": error_report,
        }
        
        self.logger.info(f"日志收集完成: {len(self.logs)} 条日志, {len(self.errors)} 个错误")
        
        return AgentResult(
            success=True,
            data=result_data,
            items_processed=len(self.logs),
        )
