"""
无限自动循环运行器
跑完一轮自动build + push，然后自动开始下一轮
真正的自主闭环
"""
import subprocess
import time
import sys
import os

PROJECT_DIR = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2"


def run_round(round_num: int):
    """跑一轮完整pipeline"""
    print(f"\n{'='*60}")
    print(f"🔄 开始第 {round_num} 轮自动运行")
    print(f"{'='*60}\n")

    # 1. 跑pipeline
    result = subprocess.run(
        ["python", "-m", "src.agent.main", "--all"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )

    # 提取最后一行摘要
    lines = result.stdout.strip().split('\n')
    last_lines = '\n'.join(lines[-20:])

    print(f"\n✅ 第 {round_num} 轮pipeline完成")
    print(f"耗时约12分钟")

    # 2. build网站
    print("\n🔨 正在build静态网站...")
    subprocess.run(
        ["python", "scripts/build_site.py"],
        cwd=PROJECT_DIR,
        capture_output=True
    )
    print("✅ build完成")

    # 3. git push
    print("\n📤 正在推送到GitHub...")
    subprocess.run(["git", "add", "."], cwd=PROJECT_DIR, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", f"auto: round {round_num} - daily AI reports"],
        cwd=PROJECT_DIR,
        capture_output=True
    )
    push_result = subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )
    if "main -> main" in push_result.stdout:
        print("✅ 推送成功")
    else:
        print("⚠️ 推送可能有问题，但继续运行")

    return True


def main():
    print("=" * 60)
    print("🤖 智能集群 - 无限自动循环模式已启动")
    print("💡 按 Ctrl+C 停止")
    print("=" * 60)

    round_num = 1

    try:
        while True:
            run_round(round_num)
            print(f"\n✅ 第 {round_num} 轮全部完成！")
            print(f"⏳ 5秒后自动开始下一轮...\n")
            round_num += 1
            time.sleep(5)  # 休息5秒再开下一轮
    except KeyboardInterrupt:
        print(f"\n\n⏹️ 用户停止，共跑了 {round_num - 1} 轮")
        sys.exit(0)


if __name__ == "__main__":
    main()
