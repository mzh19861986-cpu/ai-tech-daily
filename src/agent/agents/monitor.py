"""
子 Agent 4: MonitorAgent - 监控
负责：运行状态上报、成本统计、异常告警。
第一版只做：写日志 + 可选 Discord webhook 通知。
"""
from __future__ import annotations
import json
import requests
from typing import Dict

from .base import BaseAgent, AgentResult
from ..config import config


class MonitorAgent(BaseAgent):
    name = "monitor"
    description = "监控运行状态，异常时告警"

    def run(self, report: Dict = None) -> AgentResult:
        if report is None:
            report = {}

        # 打印摘要
        self.logger.info(f"运行摘要: {json.dumps(report.get('steps', {}), indent=2)}")

        # 如果配了 Discord webhook，发通知
        if config.discord_webhook and not config.dry_run:
            self._send_discord(report)

        return AgentResult(success=True)

    def _send_discord(self, report: Dict):
        """发送运行报告到 Discord webhook"""
        try:
            pipeline = report.get("pipeline", "unknown")
            steps = report.get("steps", {})
            fetched = steps.get("fetch", {}).get("items", 0)
            published = steps.get("publish", {}).get("items", 0)

            content = (
                f"✅ **{pipeline}** 运行完成\n"
                f"抓取: {fetched} 条 | 发布: {published} 条"
            )
            if report.get("error"):
                content = f"❌ **{pipeline}** 失败\n{report['error']}"

            requests.post(
                config.discord_webhook,
                json={"content": content},
                timeout=10,
            )
        except Exception as e:
            self.logger.warning(f"Discord 通知失败: {e}")
