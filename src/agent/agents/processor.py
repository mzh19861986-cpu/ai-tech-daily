"""
子 Agent 2: ProcessorAgent - AI 处理
负责把原始数据变成结构化内容（摘要、翻译、分类、深度分析）。
"""
from __future__ import annotations
import time
from typing import List, Dict

from .base import BaseAgent, AgentResult
from ..config import config


class ProcessorAgent(BaseAgent):
    name = "processor"
    description = "用 AI 把原始数据处理成结构化内容"

    # 限流：Gemini 免费 tier 每分钟 5 次，两次调用间隔至少 13 秒
    MIN_INTERVAL_SEC = 10
    _last_call_time: float = 0

    def _rate_limit(self):
        """简单的固定窗口限流"""
        elapsed = time.time() - self._last_call_time
        if elapsed < self.MIN_INTERVAL_SEC:
            wait = self.MIN_INTERVAL_SEC - elapsed
            self.logger.debug(f"限流等待 {wait:.1f}s...")
            time.sleep(wait)
        self._last_call_time = time.time()

    def run(self, items: List[Dict] = None, pipeline_name: str = "default") -> AgentResult:
        if not items:
            return AgentResult(success=True, data=[], items_processed=0)

        # 每个 pipeline 只处理前 5 条，控制 API 调用次数和运行时间
        items = items[:5]
        processed = []
        for item in items:
            try:
                result = self._process_item(item, pipeline_name)
                processed.append(result)
            except Exception as e:
                self.logger.warning(f"处理失败: {item.get('title','')[:30]}... -> {e}")

        # 深度分析 pipeline：只保留 top 3 热门
        if pipeline_name == "ai_deepdive":
            processed = self._select_top_for_deepdive(processed)

        # 打分简报：按分数从高到低排序
        if pipeline_name == "scored_briefing":
            processed.sort(key=lambda x: x.get("score", 0), reverse=True)
            processed = processed[:10]  # 只保留 top 10

        # Reddit digest：只保留 Reddit 来源，按点赞排序
        if pipeline_name == "reddit_digest":
            processed = [x for x in processed if "reddit" in x.get("source", "")]
            processed.sort(key=lambda x: x.get("score", 0) if isinstance(x.get("score"), (int, float)) else 0, reverse=True)
            processed = processed[:15]

        return AgentResult(
            success=True,
            data=processed,
            items_processed=len(processed),
        )

    def _process_item(self, item: Dict, pipeline_name: str = "default") -> Dict:
        """处理单条内容：摘要 + 分类 + 按需翻译"""
        title = item.get("title", "")
        summary = item.get("summary", "")

        # AI 摘要
        if config.openai_api_key:
            ai_summary = self._ai_summarize(title, summary)
        else:
            ai_summary = summary[:200] + "..." if len(summary) > 200 else summary

        result = {
            "source": item.get("source", ""),
            "title": title,
            "url": item.get("url", ""),
            "summary": ai_summary,
            "body": ai_summary,
            "original_summary": summary,
            "language": "en",
            "category": self._categorize(title + " " + summary),
        }

        # 中文翻译 pipeline：加中文标题和摘要
        if pipeline_name == "ai_daily_cn":
            result["title_cn"] = self._translate(title)
            result["summary_cn"] = self._translate(ai_summary)
            result["language"] = "zh"

        # 深度分析 pipeline：生成更长的分析
        if pipeline_name == "ai_deepdive":
            result["deep_analysis"] = self._deep_analyze(title, summary)

        # 打分简报 pipeline：AI 给每条打分
        if pipeline_name == "scored_briefing":
            result["score"] = self._score_item(title, summary)

        return result

    def _select_top_for_deepdive(self, items: List[Dict]) -> List[Dict]:
        """选最热门的 3 条做深度分析（按来源权重排序）"""
        source_weight = {"hackernews": 10, "lobsters": 8, "arxiv": 5, "github_trending": 7}
        sorted_items = sorted(
            items,
            key=lambda x: source_weight.get(x.get("source", ""), 1),
            reverse=True,
        )
        return sorted_items[:3]

    def _call_llm(self, system_prompt: str, user_prompt: str, max_tokens: int = 200) -> str:
        """统一调用 LLM：先试 Gemini，失败自动切 DeepSeek fallback"""
        from openai import OpenAI

        # 主模型：Gemini
        if config.openai_api_key:
            try:
                self._rate_limit()
                client = OpenAI(api_key=config.openai_api_key, base_url=config.openai_base_url)
                resp = client.chat.completions.create(
                    model=config.openai_model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    max_tokens=max_tokens,
                )
                return resp.choices[0].message.content.strip()
            except Exception as e:
                self.logger.warning(f"主模型(Gemini)失败: {e}")

        # 备用模型：DeepSeek
        if config.deepseek_api_key:
            try:
                self._rate_limit()
                client = OpenAI(api_key=config.deepseek_api_key, base_url=config.deepseek_base_url)
                resp = client.chat.completions.create(
                    model=config.deepseek_model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    max_tokens=max_tokens,
                )
                return resp.choices[0].message.content.strip()
            except Exception as e:
                self.logger.warning(f"备用模型(DeepSeek)失败: {e}")

        return ""

    def _ai_summarize(self, title: str, context: str) -> str:
        """调用 LLM 生成摘要"""
        result = self._call_llm(
            system_prompt="你是技术内容编辑，用 2 句话总结这条新闻的核心价值。",
            user_prompt=f"标题: {title}\n内容: {context[:1000]}",
            max_tokens=150,
        )
        if result:
            return result
        return context[:200]

    def _translate(self, text: str) -> str:
        """翻译成中文（降级：无 key 时返回原文）"""
        result = self._call_llm(
            system_prompt="把下面的内容翻译成简体中文，保持技术准确性，简洁自然。",
            user_prompt=text[:800],
            max_tokens=300,
        )
        if result:
            return result
        return f"[待翻译] {text[:50]}"

    def _deep_analyze(self, title: str, context: str) -> str:
        """深度分析（降级：无 key 时返回原文）"""
        result = self._call_llm(
            system_prompt="你是资深技术分析师。对下面这条内容做深度分析：1) 它是什么 2) 为什么重要 3) 对行业/开发者的影响。用 3-4 句话。",
            user_prompt=f"标题: {title}\n内容: {context[:1500]}",
            max_tokens=400,
        )
        if result:
            return result
        return f"[深度分析待启用] {context[:300]}"

    def _score_item(self, title: str, context: str) -> float:
        """AI 给内容打 0-10 分（降级：无 key 时给默认分）"""
        result = self._call_llm(
            system_prompt="你是技术内容编辑。给下面这条技术新闻打个热度分 0-10 分（10 分是重大突破/爆款）。只回复一个数字。",
            user_prompt=f"标题: {title}\n内容: {context[:500]}",
            max_tokens=10,
        )
        if result:
            try:
                return float(result.strip().split()[0])
            except:
                pass
        return 5.0

    def _categorize(self, text: str) -> str:
        """关键词分类"""
        t = text.lower()
        if any(k in t for k in ["ai", "llm", "model", "gpt", "agent", "machine learning"]):
            return "ai_ml"
        if any(k in t for k in ["github", "open source", "python", "javascript", "rust"]):
            return "devtools"
        if any(k in t for k in ["startup", "funding", "yc", "venture", "cloudflare"]):
            return "startup"
        if any(k in t for k in ["paper", "arxiv", "research", "study"]):
            return "research"
        return "general"
