"""
子 Agent 1: FetcherAgent - 数据抓取
负责从各公开数据源抓取原始内容。
"""
from __future__ import annotations
import feedparser
import html
import re
import requests
from typing import List, Dict


def _strip_html(text: str) -> str:
    """简单清理 HTML 标签和转义字符"""
    if not text:
        return ""
    text = re.sub(r'<a[^>]*>.*?</a>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    return text.strip()

from .base import BaseAgent, AgentResult
from ..config import config


class FetcherAgent(BaseAgent):
    name = "fetcher"
    description = "从公开数据源抓取原始内容"

    HN_FEED = "https://news.ycombinator.com/rss"
    LOBSTERS_FEED = "https://lobste.rs/rss"
    ARXIV_FEED = "https://rss.arxiv.org/rss/cs.AI"
    GH_TRENDING_URL = "https://github.com/trending?since=daily"

    HEADERS = {"User-Agent": "AI-Agent-Daily/0.2 (personal project; contact: none)"}

    def run(self, pipeline_name: str = "default") -> AgentResult:
        items = []

        # 1. Hacker News
        hn_items = self._fetch_hn()
        items.extend(hn_items)
        self.logger.info(f"Hacker News: {len(hn_items)} 条")

        # 2. Lobsters（技术社区）
        lobsters_items = self._fetch_lobsters()
        items.extend(lobsters_items)
        self.logger.info(f"Lobsters: {len(lobsters_items)} 条")

        # 3. ArXiv AI/ML 论文
        arxiv_items = self._fetch_arxiv()
        items.extend(arxiv_items)
        self.logger.info(f"ArXiv AI: {len(arxiv_items)} 条")

        # 4. GitHub Trending
        gh_items = self._fetch_github_trending()
        items.extend(gh_items)
        self.logger.info(f"GitHub Trending: {len(gh_items)} 条")

        # 5. Reddit 热门技术帖
        reddit_items = self._fetch_reddit()
        items.extend(reddit_items)
        self.logger.info(f"Reddit: {len(reddit_items)} 条")

        return AgentResult(
            success=True,
            data=items,
            items_processed=len(items),
        )

    def _fetch_hn(self, limit: int = 15) -> List[Dict]:
        """抓取 Hacker News 头条"""
        try:
            resp = requests.get(self.HN_FEED, timeout=15, headers=self.HEADERS)
            feed = feedparser.parse(resp.content)
            items = []
            for entry in feed.entries[:limit]:
                items.append({
                    "source": "hackernews",
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "summary": _strip_html(entry.get("summary", ""))[:500],
                    "published": entry.get("published", ""),
                })
            return items
        except Exception as e:
            self.logger.error(f"HN 抓取失败: {e}")
            return []

    def _fetch_lobsters(self, limit: int = 10) -> List[Dict]:
        """抓取 Lobsters 技术社区"""
        try:
            resp = requests.get(self.LOBSTERS_FEED, timeout=15, headers=self.HEADERS)
            feed = feedparser.parse(resp.content)
            items = []
            for entry in feed.entries[:limit]:
                items.append({
                    "source": "lobsters",
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "summary": entry.get("summary", "")[:300],
                    "published": entry.get("published", ""),
                })
            return items
        except Exception as e:
            self.logger.error(f"Lobsters 抓取失败: {e}")
            return []

    def _fetch_arxiv(self, limit: int = 10) -> List[Dict]:
        """抓取 ArXiv AI 方向最新论文"""
        try:
            resp = requests.get(self.ARXIV_FEED, timeout=15, headers=self.HEADERS)
            feed = feedparser.parse(resp.content)
            items = []
            for entry in feed.entries[:limit]:
                items.append({
                    "source": "arxiv",
                    "title": entry.get("title", "").replace("\n", " ").strip(),
                    "url": entry.get("link", ""),
                    "summary": entry.get("summary", "")[:400],
                    "published": entry.get("published", ""),
                })
            return items
        except Exception as e:
            self.logger.error(f"ArXiv 抓取失败: {e}")
            return []

    def _fetch_github_trending(self, limit: int = 10) -> List[Dict]:
        """抓取 GitHub Trending 每日热门仓库（简单 HTML 解析）"""
        try:
            resp = requests.get(self.GH_TRENDING_URL, timeout=15, headers=self.HEADERS)
            html = resp.text

            # 用正则提取仓库名和描述
            repo_pattern = r'<h2 class="h3 lh-condensed">\s*<a href="/([^"]+)"'
            repos = re.findall(repo_pattern, html)

            desc_pattern = r'<p class="col-9 color-fg-muted my-1 pr-4">\s*(.*?)\s*</p>'
            descs = re.findall(desc_pattern, html, re.DOTALL)

            items = []
            for i, repo in enumerate(repos[:limit]):
                desc = descs[i].strip() if i < len(descs) else ""
                items.append({
                    "source": "github_trending",
                    "title": repo,
                    "url": f"https://github.com/{repo}",
                    "summary": desc,
                    "published": "",
                })
            return items
        except Exception as e:
            self.logger.error(f"GitHub Trending 抓取失败: {e}")
            return []

    def _fetch_reddit(self, limit: int = 15) -> List[Dict]:
        """抓取 Reddit 热门技术 subreddit 帖子（用 RSS）"""
        subreddits = ["MachineLearning", "programming", "LocalLLaMA"]
        items = []
        headers = {**self.HEADERS, "User-Agent": "ai-tech-daily/1.0"}
        per_sub = max(limit // len(subreddits), 3)
        for sub in subreddits:
            try:
                url = f"https://www.reddit.com/r/{sub}/hot/.rss?limit={per_sub}"
                resp = requests.get(url, timeout=15, headers=headers)
                feed = feedparser.parse(resp.content)
                for entry in feed.entries[:per_sub]:
                    items.append({
                        "source": f"reddit/r/{sub}",
                        "title": entry.get("title", ""),
                        "url": entry.get("link", ""),
                        "summary": _strip_html(entry.get("summary", ""))[:400],
                        "published": entry.get("published", ""),
                        "score": 0,
                    })
            except Exception as e:
                self.logger.warning(f"Reddit r/{sub} 抓取失败: {e}")
        return items
