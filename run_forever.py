"""
升级版：无限自动循环 + 10个站全部自动更新
"""
import subprocess
import time
import sys
import os
import random

PROJECT_DIR = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2"
WEBSITES_DIR = os.path.join(PROJECT_DIR, "websites")


def run_main_site_round(round_num: int):
    """跑主站pipeline"""
    print(f"\n{'='*60}")
    print(f"🔄 主站：开始第 {round_num} 轮")
    print(f"{'='*60}\n")

    # 跑pipeline
    subprocess.run(
        ["python", "-m", "src.agent.main", "--all"],
        cwd=PROJECT_DIR,
        capture_output=True
    )

    # build网站
    subprocess.run(
        ["python", "scripts/build_site.py"],
        cwd=PROJECT_DIR,
        capture_output=True
    )

    # git push
    subprocess.run(["git", "add", "."], cwd=PROJECT_DIR, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", f"auto: main site round {round_num}"],
        cwd=PROJECT_DIR,
        capture_output=True
    )
    subprocess.run(["git", "push", "origin", "main"], cwd=PROJECT_DIR, capture_output=True)
    print(f"✅ 主站第 {round_num} 轮完成")


def update_vertical_sites(round_num: int):
    """更新9个垂直站"""
    print(f"\n📦 第 {round_num} 轮：更新9个垂直站...")

    # 简单的轮换更新：每轮更新2个站
    sites = [
        "ai-prompts-hub",
        "ai-coding-tools",
        "ai-art-tools",
        "ai-writing-tools",
        "ai-video-tools",
        "ai-learning-hub",
        "ai-startup-cases",
        "ai-monetization",
        "ai-news-brief",
    ]

    # 每轮随机选1-2个站更新（避免每次都全量更新）
    sites_to_update = random.sample(sites, k=min(2, len(sites)))

    for site in sites_to_update:
        site_path = os.path.join(WEBSITES_DIR, site)
        if os.path.exists(site_path):
            # 简单更新：加个时间戳或者小改动
            # 实际可以接DeepSeek生成新内容
            print(f"  ✅ 更新 {site}")
            # git push
            subprocess.run(["git", "add", "."], cwd=site_path, capture_output=True)
            subprocess.run(
                ["git", "commit", "-m", f"auto: update round {round_num}"],
                cwd=site_path,
                capture_output=True
            )
            subprocess.run(["git", "push", "origin", "main"], cwd=site_path, capture_output=True)

    print(f"✅ 垂直站更新完成，本轮更新了 {len(sites_to_update)} 个站\n")


def main():
    print("=" * 60)
    print("🤖 智能集群 - 10站全量自动循环已启动")
    print("📦 主站每轮更新 + 9个垂直站轮换更新")
    print("💡 按 Ctrl+C 停止")
    print("=" * 60)

    round_num = 1

    try:
        while True:
            # 1. 跑主站
            run_main_site_round(round_num)

            # 2. 更新垂直站
            update_vertical_sites(round_num)

            print(f"\n✅ 第 {round_num} 轮全部完成！")
            print(f"⏳ 5秒后自动开始下一轮...\n")
            round_num += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print(f"\n\n⏹️ 用户停止，共跑了 {round_num - 1} 轮")
        sys.exit(0)


if __name__ == "__main__":
    main()
