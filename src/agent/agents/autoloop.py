"""
自动循环智能体 - AutoLoopAgent
负责：任务队列管理、自动循环执行、任务优先级排序、完成一个自动开始下一个
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import List, Dict, Optional

from .base import BaseAgent, AgentResult


class Task:
    """任务单元"""
    def __init__(self, name: str, priority: int, category: str, description: str):
        self.name = name
        self.priority = priority  # 1 = 最高
        self.category = category   # content / growth / monetization / iteration
        self.description = description
        self.status = "pending"   # pending / running / done / failed
        self.created_at = datetime.now().isoformat()
        self.finished_at: Optional[str] = None
        self.result: Optional[Dict] = None


class AutoLoopAgent(BaseAgent):
    """自动循环智能体：管理任务队列，自动循环执行"""

    name = "autoloop"
    description = "任务队列管理、自动循环执行、完成一个自动开始下一个"

    def __init__(self):
        super().__init__()
        self.task_queue: List[Task] = []
        self.completed_tasks: List[Task] = []
        self.failed_tasks: List[Task] = []

    def add_task(self, name: str, priority: int, category: str, description: str):
        """添加任务到队列"""
        task = Task(name=name, priority=priority, category=category, description=description)
        self.task_queue.append(task)
        # 按优先级排序
        self.task_queue.sort(key=lambda x: x.priority)
        self.logger.info(f"添加任务: {name} (优先级: {priority})")

    def get_next_task(self) -> Optional[Task]:
        """获取下一个要执行的任务"""
        if not self.task_queue:
            return None
        task = self.task_queue.pop(0)
        task.status = "running"
        self.logger.info(f"开始执行任务: {task.name}")
        return task

    def complete_task(self, task: Task, result: Dict):
        """标记任务完成"""
        task.status = "done"
        task.finished_at = datetime.now().isoformat()
        task.result = result
        self.completed_tasks.append(task)
        self.logger.info(f"任务完成: {task.name}")

    def fail_task(self, task: Task, error: str):
        """标记任务失败"""
        task.status = "failed"
        task.finished_at = datetime.now().isoformat()
        task.result = {"error": error}
        self.failed_tasks.append(task)
        self.logger.error(f"任务失败: {task.name} -> {error}")

    def build_default_task_queue(self):
        """构建默认任务队列"""
        # 内容生产任务（优先级 1-3）
        self.add_task("fetch_news", 1, "content", "抓取最新 AI 新闻")
        self.add_task("process_content", 2, "content", "DeepSeek AI 处理和翻译")
        self.add_task("publish_site", 3, "content", "构建静态网站并部署")
        
        # 增长任务（优先级 4-6）
        self.add_task("generate_promotion", 4, "growth", "生成推广文案和素材")
        self.add_task("analyze_monetization", 5, "monetization", "分析变现机会")
        self.add_task("iterate_improvements", 6, "iteration", "分析数据并提出优化建议")
        
        # 重复循环
        self.add_task("next_cycle", 7, "loop", "开始下一个循环")

    def get_status(self) -> Dict:
        """获取当前状态"""
        return {
            "pending_tasks": len(self.task_queue),
            "completed_tasks": len(self.completed_tasks),
            "failed_tasks": len(self.failed_tasks),
            "recent_completed": [t.name for t in self.completed_tasks[-5:]],
        }

    def run(self, **kwargs) -> AgentResult:
        """执行自动循环调度"""
        self.logger.info("=== 自动循环系统启动 ===")
        
        # 如果队列为空，构建默认队列
        if not self.task_queue:
            self.build_default_task_queue()
            self.logger.info("构建默认任务队列完成")
        
        status = self.get_status()
        self.logger.info(f"当前状态: 待执行 {status['pending_tasks']} 个任务")
        
        return AgentResult(
            success=True,
            data=status,
            items_processed=status["pending_tasks"],
        )
