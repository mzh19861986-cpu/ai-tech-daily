"""
配置管理 - 所有密钥从环境变量读取，不硬编码。
GitHub Actions 里对应 Secrets，本地开发用 .env 文件。
"""
import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Config:
    # === 数据库 ===
    db_path: str = field(default_factory=lambda: os.getenv("DB_PATH", "data/agent.db"))

    # === AI / LLM ===
    llm_provider: str = field(default_factory=lambda: os.getenv("LLM_PROVIDER", "openai"))
    openai_api_key: Optional[str] = field(default_factory=lambda: os.getenv("OPENAI_API_KEY"))
    openai_base_url: Optional[str] = field(default_factory=lambda: os.getenv("OPENAI_BASE_URL"))
    openai_model: str = field(default_factory=lambda: os.getenv("OPENAI_MODEL", "gpt-4o-mini"))

    # === 备用 LLM（DeepSeek）===
    deepseek_api_key: Optional[str] = field(default_factory=lambda: os.getenv("DEEPSEEK_API_KEY"))
    deepseek_base_url: str = field(default_factory=lambda: os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1"))
    deepseek_model: str = field(default_factory=lambda: os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))

    # === Cloudflare（D1/KV/Workers）===
    cloudflare_account_id: Optional[str] = field(default_factory=lambda: os.getenv("CLOUDFLARE_ACCOUNT_ID"))
    cloudflare_api_token: Optional[str] = field(default_factory=lambda: os.getenv("CLOUDFLARE_API_TOKEN"))
    d1_database_id: Optional[str] = field(default_factory=lambda: os.getenv("D1_DATABASE_ID"))

    # === 数据源 API ===
    reddit_client_id: Optional[str] = field(default_factory=lambda: os.getenv("REDDIT_CLIENT_ID"))
    reddit_client_secret: Optional[str] = field(default_factory=lambda: os.getenv("REDDIT_CLIENT_SECRET"))
    producthunt_token: Optional[str] = field(default_factory=lambda: os.getenv("PRODUCTHUNT_TOKEN"))

    # === 发布平台 ===
    github_token: Optional[str] = field(default_factory=lambda: os.getenv("GITHUB_TOKEN"))
    discord_webhook: Optional[str] = field(default_factory=lambda: os.getenv("DISCORD_WEBHOOK"))

    # === 运行模式 ===
    dry_run: bool = field(default_factory=lambda: os.getenv("DRY_RUN", "false").lower() == "true")
    log_level: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))

    def validate_required(self, pipeline_name: str = "") -> list[str]:
        """检查必要配置是否齐全，返回缺失项列表"""
        missing = []
        if self.llm_provider == "openai" and not self.openai_api_key:
            missing.append("OPENAI_API_KEY")
        return missing


config = Config()
