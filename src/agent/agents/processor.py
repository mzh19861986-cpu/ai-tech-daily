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

    # 限流：Gemini 免费 tier 每分钟 5 次，间隔 6 秒
    MIN_INTERVAL_SEC = 6
    _last_call_time: float = 0

    # DeepSeek 多 key 轮询
    _deepseek_key_index: int = 0

    def _get_next_deepseek_key(self) -> str:
        """轮询 DeepSeek 多 key，分散额度"""
        keys = []
        # 先读逗号分隔的多 key
        import os
        keys_str = os.getenv("DEEPSEEK_API_KEYS", "")
        if keys_str:
            keys = [k.strip() for k in keys_str.split(",") if k.strip()]
        # 再读单数的
        if config.deepseek_api_key and config.deepseek_api_key not in keys:
            keys.append(config.deepseek_api_key)
        if not keys:
            return None
        idx = self._deepseek_key_index % len(keys)
        self._deepseek_key_index += 1
        return keys[idx]

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

        # 先按 pipeline 过滤，再限制条数
        if pipeline_name == "github_tools":
            # GitHub 工具推荐：先过滤出 GitHub Trending，再取前 8 条
            filtered = [x for x in items if x.get("source") == "github_trending"]
            items = filtered[:8]
        elif pipeline_name == "reddit_digest":
            # Reddit 摘要：先过滤出 Reddit 来源
            filtered = [x for x in items if "reddit" in x.get("source", "")]
            items = filtered[:15]
        elif pipeline_name == "ai_prompts":
            # AI Prompt 汇总：只保留 AI 相关内容（按标题关键词过滤）
            ai_keywords = ["ai", "llm", "gpt", "agent", "model", "prompt", "gemini", "claude"]
            filtered = [x for x in items if any(k in x.get("title", "").lower() for k in ai_keywords)]
            items = filtered[:5]
        elif pipeline_name == "product_hunt_daily":
            # Product Hunt 每日新品：只保留 Product Hunt 来源
            filtered = [x for x in items if x.get("source") == "producthunt"]
            items = filtered[:8]
        elif pipeline_name == "devto_daily":
            # Dev.to 热门技术文章：只保留 Dev.to 来源
            filtered = [x for x in items if x.get("source") == "devto"]
            items = filtered[:5]
        elif pipeline_name == "dev_tips_daily":
            # 每日开发技巧：从 Dev.to 和 Lobsters 里选实用技巧类文章
            tips_keywords = ["tip", "trick", "guide", "how to", "tutorial", "learn", "best practice"]
            filtered = [x for x in items if any(k in x.get("title", "").lower() for k in tips_keywords)]
            items = filtered[:3]
        elif pipeline_name == "ai_qa_daily":
            # 每日 AI 问答：选 AI 相关的内容，做成 Q&A
            ai_keywords = ["ai", "llm", "gpt", "agent", "model", "gemini", "claude"]
            filtered = [x for x in items if any(k in x.get("title", "").lower() for k in ai_keywords)]
            items = filtered[:3]
        elif pipeline_name == "ai_brief_3min":
            # 3 分钟快讯：选前 3 条最重要的新闻
            items = items[:3]
        else:
            # 其他 pipeline：只处理前 2 条，控制 API 调用次数
            items = items[:2]

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

        # 免费 AI 工具汇总：只保留 AI/工具类内容
        if pipeline_name == "free_ai_tools":
            processed = [x for x in processed if x.get("category") in ["ai_ml", "devtools"]]
            processed = processed[:6]

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

        # GitHub 工具推荐：生成"为什么你需要它"
        if pipeline_name == "github_tools":
            result["why_useful"] = self._explain_utility(title, summary)

        # 免费 AI 工具汇总：生成"适合谁 + 怎么开始用"
        if pipeline_name == "free_ai_tools":
            result["who_for"] = self._explain_audience(title, summary)
            result["how_to_start"] = self._explain_how_to_start(title, summary)

        # AI Prompt 汇总：提炼好用的 Prompt 技巧
        if pipeline_name == "ai_prompts":
            result["prompt_tip"] = self._extract_prompt_tip(title, summary)

        # Product Hunt 新品：生成"这个产品是干什么的 + 为什么值得试"
        if pipeline_name == "product_hunt_daily":
            result["what_is_it"] = self._explain_utility(title, summary)

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
        """统一调用 LLM：DeepSeek 多 key 轮询 + 重试，失败 fallback 到 Gemini"""
        from openai import OpenAI

        # 主模型：DeepSeek 多 key 轮询，带重试
        deepseek_key = self._get_next_deepseek_key()
        if deepseek_key:
            for attempt in range(3):  # 重试 3 次
                try:
                    self._rate_limit()
                    client = OpenAI(
                        api_key=deepseek_key,
                        base_url=config.deepseek_base_url,
                        timeout=30.0,  # 30 秒超时
                        max_retries=2,
                    )
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
                    self.logger.warning(f"主模型(DeepSeek)第{attempt+1}次失败: {str(e)[:100]}")
                    time.sleep(2 * (attempt + 1))  # 指数退避

        # 备用模型：Gemini
        if config.openai_api_key:
            try:
                self._rate_limit()
                client = OpenAI(
                    api_key=config.openai_api_key,
                    base_url=config.openai_base_url,
                    timeout=30.0,
                )
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
                self.logger.warning(f"备用模型(Gemini)失败: {str(e)[:100]}")

        return ""

    def _ai_summarize(self, title: str, context: str) -> str:
        """调用 LLM 生成高质量摘要"""
        result = self._call_llm(
            system_prompt="""你是资深科技编辑，擅长用简洁的语言提炼技术新闻的核心价值。
要求：
1. 用 2-3 句话总结
2. 说清楚「是什么」和「为什么值得关注」
3. 语气专业但不生硬，像给朋友推荐好东西
4. 不要套话，要有信息量""",
            user_prompt=f"标题: {title}\n内容: {context[:1000]}",
            max_tokens=200,
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

    def _explain_utility(self, title: str, context: str) -> str:
        """解释这个工具/项目对开发者有什么用"""
        result = self._call_llm(
            system_prompt="你是技术博主。用 1-2 句话告诉读者，这个开源项目能帮他解决什么具体问题，为什么值得试试。语气要实用、不夸张。",
            user_prompt=f"项目名: {title}\n描述: {context[:800]}",
            max_tokens=120,
        )
        if result:
            return result
        return "一个有趣的开源项目，可以看看它是怎么实现的。"

    def _explain_audience(self, title: str, context: str) -> str:
        """解释这个工具适合谁用"""
        result = self._call_llm(
            system_prompt="你是工具测评博主。用一句话说明这个 AI 工具最适合哪类人用（比如：独立开发者、内容创作者、学生、企业团队）。",
            user_prompt=f"工具名: {title}\n描述: {context[:600]}",
            max_tokens=60,
        )
        if result:
            return result
        return "适合对 AI 感兴趣的开发者。"

    def _explain_how_to_start(self, title: str, context: str) -> str:
        """解释怎么开始用这个工具"""
        result = self._call_llm(
            system_prompt="你是工具教程博主。用 1-2 句话告诉读者，怎么快速开始用这个工具（比如：直接打开网页就能用、需要 API key、需要本地部署）。",
            user_prompt=f"工具名: {title}\n描述: {context[:600]}",
            max_tokens=80,
        )
        if result:
            return result
        return "打开链接看看官方文档就知道了。"

    def _extract_prompt_tip(self, title: str, context: str) -> str:
        """从内容里提炼一个好用的 Prompt 技巧"""
        result = self._call_llm(
            system_prompt="你是 Prompt 工程专家。从下面这篇文章/讨论里，提炼出一个可以直接用的 AI Prompt 技巧或最佳实践，用 1-2 句话说明。如果没有明显的 Prompt 内容，就总结这篇文章里关于如何更好使用 AI 的建议。",
            user_prompt=f"标题: {title}\n内容: {context[:800]}",
            max_tokens=120,
        )
        if result:
            return result
        return "多用具体例子和上下文，AI 输出质量会明显提升。"

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
