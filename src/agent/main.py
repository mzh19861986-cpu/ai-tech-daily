"""
入口文件 - 命令行：
    python -m src.agent.main --pipeline ai_daily
    python -m src.agent.main --all                    # 跑全部 pipeline
    python -m src.agent.main --pipeline ai_daily --dry-run
"""
import argparse
import json
import logging
import sys

from .config import config
from .db import init_db
from .orchestrator import Orchestrator


ALL_PIPELINES = ["ai_daily", "ai_daily_cn", "ai_deepdive", "scored_briefing", "weekly_digest", "reddit_digest", "github_tools"]


def setup_logging():
    level = getattr(logging, config.log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def main():
    parser = argparse.ArgumentParser(description="AI Agent 被动收益自动化")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pipeline", help="要运行的单个 pipeline 名称")
    group.add_argument("--all", action="store_true", help="运行全部 pipeline")
    parser.add_argument("--dry-run", action="store_true", help="试运行，不实际发布")
    args = parser.parse_args()

    setup_logging()
    log = logging.getLogger("main")

    missing = config.validate_required()
    if missing:
        log.warning(f"缺少配置: {missing}（将使用降级模式运行）")

    init_db()
    orch = Orchestrator()

    if args.all:
        log.info(f"运行全部 pipeline: {ALL_PIPELINES}")
        result = orch.run_multiple(ALL_PIPELINES, dry_run=args.dry_run or config.dry_run)
    else:
        result = orch.run_pipeline(args.pipeline, dry_run=args.dry_run or config.dry_run)

    print("\n=== RUN REPORT ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # 有 pipeline 失败就非零退出
    if isinstance(result, dict) and result.get("pipelines"):
        failed = [k for k, v in result["pipelines"].items() if v.get("error")]
        if failed:
            sys.exit(1)
    elif result.get("error"):
        sys.exit(1)


if __name__ == "__main__":
    main()
