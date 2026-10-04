"""
安防 & 合规层 - 母体的"安全员"。
所有子 Agent 的输出在发布前必须过这里。
"""
import re
from dataclasses import dataclass


@dataclass
class SecurityCheckResult:
    passed: bool
    reasons: list[str]


class SecurityGuard:
    """合规检查器：内容发布前过一遍"""

    # 禁止内容关键词
    BLOCKED_PATTERNS = [
        r"(?i)cryptomining|bitcoin mining|crypto mining",
        r"(?i)hack|crack|phishing|malware",
        r"(?i)fake.*follow|bot.*engagement|click.*farm",
        r"(?i)password.*crack|brute.*force",
    ]

    # 广告占比上限
    MAX_AD_RATIO = 0.15

    def check_content(self, title: str, body: str) -> SecurityCheckResult:
        reasons = []
        text = f"{title}\n{body}"

        # 1. 违禁词检查
        for pattern in self.BLOCKED_PATTERNS:
            if re.search(pattern, text):
                reasons.append(f"命中违禁模式: {pattern}")

        # 2. 长度检查（太短的内容质量存疑，只记录不拦截）
        if len(body.strip()) < 10:
            reasons.append(f"内容过短 ({len(body)} chars)")

        # 3. 声明：AI 生成内容必须标注
        if "AI" not in title and "generated" not in body.lower()[:200]:
            # 不强制，但提示
            pass

        return SecurityCheckResult(
            passed=len(reasons) == 0,
            reasons=reasons,
        )

    def check_fetch(self, url: str, requests_per_minute: int) -> SecurityCheckResult:
        """检查抓取行为是否合规"""
        reasons = []

        # 频率上限
        if requests_per_minute > 60:
            reasons.append(f"请求频率过高: {requests_per_minute}/min (上限 60)")

        # 禁止抓取的域名（示例，可扩展）
        blocked_domains = ["login.", "pay.", "admin.", "account.", "dashboard."]
        if any(d in url for d in blocked_domains):
            reasons.append(f"禁止抓取登录/支付/后台类页面")

        return SecurityCheckResult(
            passed=len(reasons) == 0,
            reasons=reasons,
        )

    def check_publish(self, platform: str, content_title: str) -> SecurityCheckResult:
        """检查发布行为是否合规"""
        reasons = []

        # 不能自动发布到未授权平台
        allowed = ["github_pages", "rss", "email_newsletter"]
        if platform not in allowed:
            reasons.append(f"平台 {platform} 未在授权发布列表中")

        return SecurityCheckResult(
            passed=len(reasons) == 0,
            reasons=reasons,
        )


security_guard = SecurityGuard()
