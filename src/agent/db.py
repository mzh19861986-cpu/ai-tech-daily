"""
数据库层 - 本地用 SQLite，生产可切换 Cloudflare D1。
Schema 定义在 database/schema.sql。
"""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from .config import config


def get_db() -> sqlite3.Connection:
    Path(config.db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(config.db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """初始化数据库表"""
    schema_path = Path(__file__).parent.parent.parent / "database" / "schema.sql"
    if schema_path.exists():
        conn = get_db()
        conn.executescript(schema_path.read_text(encoding="utf-8"))
        conn.commit()
        conn.close()


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# === 便捷函数 ===

def log_run(pipeline_id: int, trigger_type: str = "scheduled") -> int:
    """开始一次运行，返回 run_id"""
    conn = get_db()
    cur = conn.execute(
        "INSERT INTO runs (pipeline_id, trigger_type, status) VALUES (?, ?, 'running')",
        (pipeline_id, trigger_type),
    )
    conn.commit()
    run_id = cur.lastrowid
    conn.close()
    return run_id


def finish_run(run_id: int, status: str, items_fetched: int = 0,
               items_published: int = 0, error_msg: str = None):
    conn = get_db()
    conn.execute(
        """UPDATE runs SET status=?, items_fetched=?, items_published=?,
           error_msg=?, finished_at=? WHERE id=?""",
        (status, items_fetched, items_published, error_msg, now_iso(), run_id),
    )
    conn.commit()
    conn.close()


def save_content(pipeline_id: int, title: str, body: str, summary: str = "",
                source_item_id: str = "", language: str = "en") -> int:
    conn = get_db()
    cur = conn.execute(
        """INSERT INTO content_items (pipeline_id, source_item_id, title, body_markdown,
           summary, language, status) VALUES (?, ?, ?, ?, ?, ?, 'draft')""",
        (pipeline_id, source_item_id, title, body, summary, language),
    )
    conn.commit()
    cid = cur.lastrowid
    conn.close()
    return cid
