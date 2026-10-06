#!/usr/bin/env python3
"""质量管控智能体：检查所有日报内容，有问题直接修复"""
import os
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 项目根目录
ROOT = Path(__file__).parent.parent
OUTPUT_DIR = ROOT / "output"

# DeepSeek API
import requests

def get_deepseek_key():
    """轮询获取 DeepSeek key"""
    keys = os.getenv("DEEPSEEK_API_KEYS", "").split(",")
    keys = [k.strip() for k in keys if k.strip()]
    if not keys:
        raise ValueError("No DeepSeek API keys found")
    # 简单轮询
    get_deepseek_key.index = getattr(get_deepseek_key, 'index', 0)
    key = keys[get_deepseek_key.index % len(keys)]
    get_deepseek_key.index += 1
    return key

def call_deepseek(prompt, system_prompt="你是一个专业的内容质量审核编辑"):
    """调用 DeepSeek API"""
    api_key = get_deepseek_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 2000
    }
    try:
        resp = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"⚠️ DeepSeek API error: {e}")
        return None

def check_article(file_path: Path):
    """检查单篇文章"""
    print(f"\n=== 🔍 检查: {file_path.name} ===")
    content = file_path.read_text(encoding='utf-8')
    
    # 检查问题清单
    issues = []
    
    # 1. 内容太短
    if len(content) < 500:
        issues.append("内容过短 (<500字符)")
    
    # 2. 有截断的 "..." 在结尾（不是故意的）
    if content.endswith("...") and not any(x in content for x in ["...", "…"]):
        issues.append("内容结尾有截断...")
    
    # 3. 标题格式问题
    if not content.startswith("# "):
        issues.append("缺少一级标题")
    
    # 4. 空内容
    if len(content.strip()) < 200:
        issues.append("内容近乎为空")
    
    # 5. 检查是否有乱码或奇怪字符
    weird_chars = ['锟', '斤', '拷', '诧', '夎', '夊']
    if any(c in content for c in weird_chars):
        issues.append("可能有编码乱码")
    
    if issues:
        print(f"⚠️ 发现问题: {issues}")
        return issues, content
    else:
        print(f"✅ 内容正常")
        return [], content

def fix_article(file_path: Path, content: str, issues: list):
    """用 DeepSeek 修复文章"""
    print(f"🔧 修复中: {file_path.name}")
    
    prompt = f"""请修复以下 AI 日报内容，保持原有的结构和风格，但要：
1. 补全不完整的句子
2. 去掉乱码和奇怪字符
3. 让内容更通顺、更专业
4. 保持 markdown 格式
5. 不要改变标题和主要内容

发现的问题：{issues}

原始内容：
{content}

请直接输出修复后的完整 markdown 内容："""
    
    fixed = call_deepseek(prompt)
    if fixed:
        # 清理一下，去掉可能的 markdown 代码块
        if fixed.startswith("```"):
            fixed = fixed.split("```")[1]
            if fixed.startswith("markdown"):
                fixed = fixed[8:]
        file_path.write_text(fixed.strip(), encoding='utf-8')
        print(f"✅ 已修复: {file_path.name}")
        return True
    else:
        print(f"❌ 修复失败: {file_path.name}")
        return False

def main():
    print("=" * 60)
    print("🔍 质量管控智能体 - 全站内容检查")
    print("=" * 60)
    
    md_files = sorted(OUTPUT_DIR.glob("*.md"))
    print(f"\n找到 {len(md_files)} 篇文章")
    
    all_issues = {}
    fixed_count = 0
    
    for f in md_files:
        issues, content = check_article(f)
        if issues:
            all_issues[f.name] = issues
            # 自动修复
            if fix_article(f, content, issues):
                fixed_count += 1
        time.sleep(1)  # 限流
    
    print("\n" + "=" * 60)
    print("📊 质量检查报告")
    print("=" * 60)
    print(f"总文章数: {len(md_files)}")
    print(f"发现问题: {len(all_issues)} 篇")
    print(f"已自动修复: {fixed_count} 篇")
    
    if all_issues:
        print("\n问题详情:")
        for name, issues in all_issues.items():
            print(f"  - {name}: {', '.join(issues)}")
    
    return all_issues

if __name__ == "__main__":
    main()
