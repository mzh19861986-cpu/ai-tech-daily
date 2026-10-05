"""
客服智能体 - CustomerServiceAgent
负责：自动回答用户常见问题、收集用户反馈、引导订阅和咨询
"""
from __future__ import annotations
import logging
from datetime import datetime
from typing import List, Dict

from .base import BaseAgent, AgentResult


class FAQ:
    def __init__(self, question: str, answer: str, category: str):
        self.question = question
        self.answer = answer
        self.category = category


class CustomerServiceAgent(BaseAgent):
    """客服智能体：自动回答用户常见问题、收集反馈、引导订阅"""

    name = "customer_service"
    description = "自动回答用户常见问题、收集反馈、引导订阅和咨询"

    def __init__(self):
        super().__init__()
        self.faqs: List[FAQ] = [
            FAQ(
                question="这个网站是做什么的？",
                answer="AI Tech Daily 是一个全自动的 AI 科技日报，由 24 个 AI 智能体自动抓取、分析、生成内容，每天更新最新的 AI 新闻、工具和技巧。",
                category="about",
            ),
            FAQ(
                question="内容是 AI 生成的吗？",
                answer="是的，所有内容都是由 DeepSeek AI 自动生成，经过质量检查后发布。我们的目标是每天提供最有价值的 AI 行业信息。",
                category="content",
            ),
            FAQ(
                question="可以订阅吗？",
                answer="当然可以！在页面底部输入你的邮箱，就可以订阅每日 AI 日报，每天第一时间收到最新的 AI 资讯。",
                category="subscription",
            ),
            FAQ(
                question="怎么联系你们？",
                answer="你可以通过 GitHub Issues 联系我们，或者直接发送邮件。我们也提供 AI 咨询服务，详情请查看 Monetization 页面。",
                category="contact",
            ),
            FAQ(
                question="有哪些 AI 工具推荐？",
                answer="我们精选了 30+ 个最实用的 AI 工具，涵盖文本生成、图像生成、编程助手等类别。你可以在 Tools 页面查看完整列表。",
                category="tools",
            ),
        ]
        self.user_feedback: List[Dict] = []

    def answer_question(self, question: str) -> str:
        """回答用户问题"""
        # 简单匹配
        for faq in self.faqs:
            if any(word in question for word in faq.question.split()):
                return faq.answer
        return "感谢你的提问！我们会尽快回复。你也可以通过 GitHub Issues 联系我们。"

    def collect_feedback(self, feedback: str, email: str = ""):
        """收集用户反馈"""
        self.user_feedback.append({
            "feedback": feedback,
            "email": email,
            "time": datetime.now().isoformat(),
        })
        self.logger.info(f"收到用户反馈: {feedback[:50]}...")

    def run(self, **kwargs) -> AgentResult:
        """执行客服任务"""
        self.logger.info("=== 开始客服任务 ===")
        
        result_data = {
            "total_faqs": len(self.faqs),
            "categories": list(set(f.category for f in self.faqs)),
            "feedback_received": len(self.user_feedback),
        }
        
        self.logger.info(f"客服任务完成: {len(self.faqs)} 个常见问题")
        
        return AgentResult(
            success=True,
            data=result_data,
            items_processed=len(self.faqs),
        )
