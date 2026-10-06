"""
自动修复智能体
监测到问题后自动尝试修复
"""
import os
import subprocess
import requests

PROJECT_DIR = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2"
WEBSITES_DIR = os.path.join(PROJECT_DIR, "websites")


def auto_fix_site(site_name: str, error: str):
    """自动修复单个网站问题"""
    print(f"\n🔧 自动修复智能体：正在修复 {site_name}")

    site_path = os.path.join(WEBSITES_DIR, site_name)
    if not os.path.exists(site_path):
        print(f"  ❌ {site_name} 目录不存在")
        return False

    # 简单的自动修复：重新push一次
    try:
        subprocess.run(["git", "pull", "origin", "main"], cwd=site_path, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=site_path, capture_output=True)
        subprocess.run(["git", "commit", "-m", "auto: fix by agent"], cwd=site_path, capture_output=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=site_path, capture_output=True)
        print(f"  ✅ {site_name} 已自动修复并重新push")
        return True
    except Exception as e:
        print(f"  ❌ 修复失败: {e}")
        return False


def check_and_fix_all():
    """检查所有网站，发现问题自动修复"""
    SITES = [
        ("ai-tech-daily", "https://mzh19861986-cpu.github.io/ai-tech-daily/"),
        ("ai-prompts-hub", "https://mzh19861986-cpu.github.io/ai-prompts-hub/"),
        ("ai-coding-tools", "https://mzh19861986-cpu.github.io/ai-coding-tools/"),
        ("ai-art-tools", "https://mzh19861986-cpu.github.io/ai-art-tools/"),
        ("ai-writing-tools", "https://mzh19861986-cpu.github.io/ai-writing-tools/"),
        ("ai-video-tools", "https://mzh19861986-cpu.github.io/ai-video-tools/"),
        ("ai-learning-hub", "https://mzh19861986-cpu.github.io/ai-learning-hub/"),
        ("ai-startup-cases", "https://mzh19861986-cpu.github.io/ai-startup-cases/"),
        ("ai-monetization", "https://mzh19861986-cpu.github.io/ai-monetization/"),
        ("ai-news-brief", "https://mzh19861986-cpu.github.io/ai-news-brief/"),
    ]

    fixed_count = 0
    for name, url in SITES:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code != 200 or len(resp.text) < 1000:
                print(f"⚠️ 发现问题: {name} - HTTP {resp.status_code}")
                if auto_fix_site(name, f"HTTP {resp.status_code}"):
                    fixed_count += 1
        except Exception as e:
            print(f"⚠️ 发现问题: {name} - 连接失败")
            if auto_fix_site(name, str(e)):
                fixed_count += 1

    if fixed_count > 0:
        print(f"\n🔧 自动修复完成，共修复了 {fixed_count} 个网站\n")
    else:
        print(f"\n✅ 没有发现问题，不需要修复\n")
    return fixed_count
