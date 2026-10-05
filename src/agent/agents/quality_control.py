"""
质量管控智能体 - QualityControlAgent
负责：内容质量审查、工具质量验证、素材筛选修改、严格执行质量标准
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import List, Dict

from .base import BaseAgent, AgentResult


class QualityCheckResult:
    """质量检查结果"""
    def __init__(self, item_name: str, passed: bool, score: int, issues: List[str], suggestions: List[str]):
        self.item_name = item_name
        self.passed = passed
        self.score = score  # 0-100
        self.issues = issues
        self.suggestions = suggestions
        self.checked_at = datetime.now().isoformat()


class QualityControlAgent(BaseAgent):
    """质量管控智能体：筛选、审查、验证内容和工具质量"""

    name = "quality_control"
    description = "内容质量审查、工具质量验证、素材筛选修改、严格执行质量标准"

    def __init__(self):
        super().__init__()
        self.quality_threshold = 70  # 及格分数
        self.content_standards = {
            "min_length": 100,        # 最少字数
            "max_length": 2000,      # 最多字数
            "require_title": True,    # 必须有标题
            "require_source": True,   # 必须有来源
            "no_duplicate": True,    # 不能重复
            "no_low_quality": True,   # 不能低质量
        }
        self.tool_standards = {
            "must_have_name": True,
            "must_have_description": True,
            "must_have_url": True,
            "must_be_legit": True,    # 必须是真实可用的
            "no_scam": True,          # 不能是诈骗工具
        }
        self.check_results: List[QualityCheckResult] = []

    def check_content_quality(self, title: str, body: str, source: str = "") -> QualityCheckResult:
        """检查内容质量"""
        issues = []
        suggestions = []
        score = 100
        
        # 检查标题
        if not title or len(title) < 5:
            issues.append("标题太短或缺失")
            score -= 20
            suggestions.append("补充更清晰的标题")
        
        # 检查正文长度
        if len(body) < self.content_standards["min_length"]:
            issues.append(f"内容太短（只有 {len(body)} 字）")
            score -= 30
            suggestions.append("增加更多详细内容")
        elif len(body) > self.content_standards["max_length"]:
            issues.append(f"内容太长（{len(body)} 字）")
            score -= 10
            suggestions.append("精简内容")
        
        # 检查来源
        if self.content_standards["require_source"] and not source:
            issues.append("缺少信息来源")
            score -= 15
            suggestions.append("补充原文链接")
        
        # 检查是否是低质量内容
        if "待翻译" in body or "TODO" in body:
            issues.append("内容未完成（有待翻译/TODO标记）")
            score -= 40
            suggestions.append("完成翻译和内容生成")
        
        passed = score >= self.quality_threshold
        
        result = QualityCheckResult(
            item_name=title[:30] if title else "未知",
            passed=passed,
            score=score,
            issues=issues,
            suggestions=suggestions,
        )
        self.check_results.append(result)
        
        return result

    def check_tool_quality(self, name: str, description: str, url: str) -> QualityCheckResult:
        """检查工具质量"""
        issues = []
        suggestions = []
        score = 100
        
        # 检查名称
        if not name:
            issues.append("缺少工具名称")
            score -= 25
        
        # 检查描述
        if not description or len(description) < 10:
            issues.append("工具描述太短或缺失")
            score -= 25
            suggestions.append("补充更详细的工具描述")
        
        # 检查 URL
        if not url or not url.startswith("http"):
            issues.append("缺少有效官网链接")
            score -= 30
            suggestions.append("补充正确的官网 URL")
        
        # 检查是否是常见的正规工具
        known_legit_tools = [
            "openai", "anthropic", "google", "meta", "microsoft",
            "github", "vercel", "notion", "figma", "midjourney",
        ]
        is_legit = any(legit in url.lower() for legit in known_legit_tools)
        if not is_legit:
            score -= 10
            suggestions.append("验证工具是否真实可用")
        
        passed = score >= self.quality_threshold
        
        result = QualityCheckResult(
            item_name=name or "未知工具",
            passed=passed,
            score=score,
            issues=issues,
            suggestions=suggestions,
        )
        self.check_results.append(result)
        
        return result

    def filter_low_quality_content(self, items: List[Dict]) -> List[Dict]:
        """过滤低质量内容，只保留合格的"""
        passed_items = []
        for item in items:
            result = self.check_content_quality(
                title=item.get("title", ""),
                body=item.get("body", ""),
                source=item.get("source", ""),
            )
            if result.passed:
                passed_items.append(item)
            else:
                self.logger.warning(f"过滤低质量内容: {item.get('title','')[:30]}... (得分: {result.score})")
        
        self.logger.info(f"内容筛选: {len(passed_items)}/{len(items)} 通过质量检查")
        return passed_items

    def get_quality_report(self) -> Dict:
        """获取质量报告"""
        if not self.check_results:
            return {"total": 0, "passed": 0, "failed": 0, "avg_score": 0}
        
        total = len(self.check_results)
        passed = sum(1 for r in self.check_results if r.passed)
        avg_score = sum(r.score for r in self.check_results) / total
        
        return {
            "total": total,
            "passed": passed,
            "failed": total - passed,
            "pass_rate": f"{passed/total*100:.1f}%",
            "avg_score": f"{avg_score:.1f}/100",
            "recent_issues": [r.issues for r in self.check_results[-5:] if r.issues],
        }

    def run(self, **kwargs) -> AgentResult:
        """执行质量管控任务"""
        self.logger.info("=== 开始质量检查 ===")
        
        # 检查内容质量
        sample_content = [
            {"title": "测试内容 1", "body": "这是一段测试内容，长度足够。", "source": "hackernews"},
            {"title": "测试内容 2", "body": "短", "source": ""},
        ]
        passed = self.filter_low_quality_content(sample_content)
        
        # 获取质量报告
        report = self.get_quality_report()
        
        self.logger.info(f"质量检查完成: {report['passed']}/{report['total']} 通过，平均得分 {report['avg_score']}")
        
        return AgentResult(
            success=True,
            data={
                "report": report,
                "passed_count": len(passed),
            },
            items_processed=report["total"],
        )
