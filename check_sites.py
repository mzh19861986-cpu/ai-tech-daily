import requests

sites = [
    "ai-tech-daily",
    "ai-prompts-hub",
    "ai-coding-tools",
    "ai-art-tools",
    "ai-writing-tools",
    "ai-video-tools",
    "ai-learning-hub",
    "ai-startup-cases",
    "ai-monetization",
    "ai-news-brief"
]

print("Checking 10 websites...\n")

online = 0
building = 0

for site in sites:
    url = f"https://mzh19861986-cpu.github.io/{site}/"
    try:
        r = requests.head(url, timeout=10)
        if r.status_code == 200:
            print(f"✅ {site:20s} - Online (200)")
            online += 1
        else:
            print(f"⚠️ {site:20s} - Status {r.status_code}")
    except Exception as e:
        print(f"⏳ {site:20s} - Building (Pages deploying...)")
        building += 1

print(f"\n=== Summary: {online}/10 online, {building}/10 building ===")
