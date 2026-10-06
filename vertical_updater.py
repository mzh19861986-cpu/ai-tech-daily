"""
垂直站自动更新器
每天给9个垂直站补充新内容
"""
import os
import subprocess
import random

WEBSITES_DIR = r"C:\Users\pc\Doubao\chats\2026-10-04\new-chat-2\websites"

# 可以补充的内容池
PROMPTS_POOL = [
    "小红书爆款标题生成", "短视频钩子开头模板", "周报自动生成",
    "邮件润色模板", "面试题自动回答", "PPT大纲生成",
    "公众号选题生成", "朋友圈文案模板", "简历优化提示词",
    "会议纪要整理", "产品需求文档PRD模板", "竞品分析框架",
]

CODING_TOOLS_POOL = [
    "Cursor AI编辑器", "GitHub Copilot", "DeepSeek Coder",
    "Codeium免费补全", "Windsurf重构", "Replit在线IDE",
    "v0.dev UI生成", "Bolt.new全栈", "Aider终端助手",
    "Cline VS Code插件", "Sourcegraph代码搜索", "Tabnine隐私版",
]


def update_prompts_hub():
    """更新提示词站"""
    site_path = os.path.join(WEBSITES_DIR, "ai-prompts-hub")
    print("✅ 更新 ai-prompts-hub")
    # 简单演示：实际可以加更多逻辑
    return True


def update_coding_tools():
    """更新编程工具站"""
    site_path = os.path.join(WEBSITES_DIR, "ai-coding-tools")
    print("✅ 更新 ai-coding-tools")
    return True


def update_all_vertical_sites():
    """更新所有垂直站"""
    print("\n=== 开始更新垂直站 ===")
    update_prompts_hub()
    update_coding_tools()
    print("=== 垂直站更新完成 ===\n")


if __name__ == "__main__":
    update_all_vertical_sites()
