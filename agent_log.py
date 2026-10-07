"""
智能体监督日志系统
记录所有智能体的每一步操作，写入日志文件
"""
import os
from datetime import datetime

LOG_FILE = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\agent_log.txt"


def log(agent_name: str, action: str, status: str = "OK", detail: str = ""):
    """记录智能体日志"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{agent_name}] [{status}] {action} {detail}\n"

    # 写入文件
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

    # 同时打印到控制台
    print(line.strip())


if __name__ == "__main__":
    log("Supervisor", "日志系统启动", "OK", "开始记录所有智能体操作")
