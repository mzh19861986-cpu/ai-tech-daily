"""
Agent 基类 - 所有子智能体继承这个。
"""
from __future__ import annotations
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Optional

from ..config import config


@dataclass
class AgentResult:
    success: bool
    data: Any = None
    error: Optional[str] = None
    items_processed: int = 0


class BaseAgent(ABC):
    """所有子智能体的基类"""

    name: str = "base"
    description: str = ""

    def __init__(self):
        self.logger = logging.getLogger(f"agent.{self.name}")
        self.logger.setLevel(config.log_level)

    @abstractmethod
    def run(self, **kwargs) -> AgentResult:
        """子类实现具体逻辑"""
        ...

    def safe_run(self, **kwargs) -> AgentResult:
        """带异常捕获的安全执行"""
        self.logger.info(f"[{self.name}] 开始执行")
        try:
            result = self.run(**kwargs)
            self.logger.info(f"[{self.name}] 完成, success={result.success}")
            return result
        except Exception as e:
            self.logger.error(f"[{self.name}] 失败: {e}")
            return AgentResult(success=False, error=str(e))
