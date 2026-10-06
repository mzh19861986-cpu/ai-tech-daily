"""
网站实时监测智能体
定期检查10个网站的状态、功能、错误
"""
import requests
import time
from datetime import datetime

SITES = [
    ("主站 ai-tech-daily", "https://mzh19861986-cpu.github.io/ai-tech-daily/"),
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


def check_all_sites():
    """检查所有网站状态"""
    print(f"\n🔍 === 网站实时监测 {datetime.now().strftime('%H:%M:%S')} ===")

    ok_count = 0
    error_count = 0

    for name, url in SITES:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                # 检查有没有内容
                if "card" in resp.text or "日报" in resp.text or "AI" in resp.text:
                    print(f"  ✅ {name} - 200 OK，内容正常")
                    ok_count += 1
                else:
                    print(f"  ⚠️ {name} - 200 OK，但好像没内容？")
            else:
                print(f"  ❌ {name} - HTTP {resp.status_code}")
                error_count += 1
        except Exception as e:
            print(f"  ❌ {name} - 连接失败: {str(e)[:50]}")
            error_count += 1

    print(f"\n📊 监测结果: {ok_count} 个正常, {error_count} 个异常\n")
    return error_count == 0


if __name__ == "__main__":
    check_all_sites()
