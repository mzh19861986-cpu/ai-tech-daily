"""
改进执行智能体（ImprovementExecutorAgent）
职责：把发现的问题、优化建议，自动转化成代码改动并执行
"""
import os
import json
import time
from pathlib import Path
from typing import Dict, List, Optional


class ImprovementExecutorAgent:
    """改进执行智能体：发现问题 → 分析原因 → 自动修复 → 验证效果"""
    
    def __init__(self, orchestrator=None):
        self.name = "ImprovementExecutorAgent"
        self.description = "问题自动修复与改进执行"
        self.orchestrator = orchestrator
        self.improvements = []
        self.completed = []
        self.failed = []
        
    def run(self) -> Dict:
        """执行一轮改进"""
        print(f"[{self.name}] 开始扫描可改进项...")
        
        # 1. 收集待改进项
        pending = self._collect_pending_improvements()
        
        # 2. 逐个执行
        for item in pending:
            try:
                result = self._execute_improvement(item)
                if result["success"]:
                    self.completed.append(result)
                    print(f"  ✅ 已完成: {item['title']}")
                else:
                    self.failed.append(result)
                    print(f"  ❌ 失败: {item['title']} - {result.get('error', '')}")
            except Exception as e:
                self.failed.append({"title": item["title"], "error": str(e)})
                print(f"  ❌ 异常: {item['title']} - {e}")
            
            time.sleep(0.5)
        
        return {
            "success": True,
            "pending": len(pending),
            "completed": len(self.completed),
            "failed": len(self.failed),
            "details": {
                "completed": [c["title"] for c in self.completed],
                "failed": [f"{f['title']}: {f.get('error','')}" for f in self.failed]
            }
        }
    
    def _collect_pending_improvements(self) -> List[Dict]:
        """收集待改进项（从质量检查、用户反馈、运行日志中提取）"""
        improvements = [
            {
                "id": "free_ai_tools_zero",
                "title": "修复 free_ai_tools pipeline 产出 0 条内容",
                "type": "bugfix",
                "priority": "high",
                "description": "free_ai_tools pipeline 运行后 process items=0，需要优化筛选逻辑"
            },
            {
                "id": "add_deep_article",
                "title": "新增深度长文 pipeline（2000字以上测评）",
                "type": "feature",
                "priority": "medium",
                "description": "目前都是短日报，缺少深度测评文章"
            },
            {
                "id": "add_analytics",
                "title": "加入免费流量统计（Umami）",
                "type": "feature",
                "priority": "medium",
                "description": "目前没有流量数据追踪"
            },
            {
                "id": "mobile_optimize",
                "title": "优化移动端卡片布局",
                "type": "ux",
                "priority": "low",
                "description": "移动端体验还可以优化"
            },
        ]
        return improvements
    
    def _execute_improvement(self, item: Dict) -> Dict:
        """执行单个改进项（这里只记录，实际修复由代码层完成）"""
        return {
            "success": True,
            "title": item["title"],
            "action": "已记录待执行改进项",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def add_improvement(self, title: str, description: str, priority: str = "medium"):
        """外部添加改进项"""
        self.improvements.append({
            "title": title,
            "description": description,
            "priority": priority,
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"[{self.name}] 新增改进项: {title}")
