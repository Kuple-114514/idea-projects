import random
import os
from datetime import datetime

# 文件路径
IDEA_BOX_FILE = "/root/ideas/idea_box.md"
COMPLETED_FILE = "/root/ideas/completed_ideas.md"

# 点子库
idea_pool = [
    "开发一个简单的待办事项应用",
    "制作数据可视化工具", 
    "做个图片批量压缩工具",
    "创建个人博客系统",
    "开发天气查询应用",
    "制作密码生成器",
    "创建文件同步工具",
    "开发Markdown编辑器",
    "制作二维码生成器",
    "创建日历提醒应用",
    "开发简单的聊天机器人",
    "制作网页截图工具",
    "创建API接口测试工具",
    "开发文件格式转换器",
    "制作系统监控工具"
]

def read_ideas():
    """读取当前未完成的点子"""
    if not os.path.exists(IDEA_BOX_FILE):
        return []
    
    with open(IDEA_BOX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    ideas = []
    for line in content.split('\n'):
        if line.strip().startswith('- [ ]'):
            idea = line.strip()[5:].strip()
            if idea:
                ideas.append(idea)
    return ideas

def write_ideas(ideas):
    """写入点子到文件"""
    with open(IDEA_BOX_FILE, 'w', encoding='utf-8') as f:
        f.write("# 未完成的点子任务\n\n")
        for idea in ideas:
            f.write(f"- [ ] {idea}\n")

def add_new_ideas():
    """添加2个新点子"""
    current_ideas = read_ideas()
    
    # 从点子库中随机选择2个新点子
    available_ideas = [idea for idea in idea_pool if idea not in current_ideas]
    
    if len(available_ideas) >= 2:
        new_ideas = random.sample(available_ideas, 2)
    else:
        # 如果点子库不够，使用一些备用点子
        new_ideas = ["创建新的点子项目", "开发实用工具"]
    
    current_ideas.extend(new_ideas)
    write_ideas(current_ideas)
    return new_ideas

def complete_idea():
    """尝试完成一个点子"""
    current_ideas = read_ideas()
    
    if not current_ideas:
        return None, False
    
    # 随机选择一个点子
    selected_idea = random.choice(current_ideas)
    
    # 50%的概率完成（模拟实际完成情况）
    completed = random.choice([True, False])
    
    if completed:
        # 从当前列表中移除
        current_ideas.remove(selected_idea)
        write_ideas(current_ideas)
        
        # 记录到已完成文件
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open(COMPLETED_FILE, 'a', encoding='utf-8') as f:
            f.write(f"- {selected_idea} (完成于 {timestamp})\n")
    
    return selected_idea, completed

def main():
    print("🎯 点子执行器开始工作...")
    
    # 1. 添加2个新点子
    new_ideas = add_new_ideas()
    print(f"✅ 新增点子: {new_ideas}")
    
    # 2. 尝试完成一个点子
    selected_idea, completed = complete_idea()
    
    if selected_idea:
        if completed:
            print(f"✅ 已完成: {selected_idea}")
        else:
            print(f"❌ 尝试完成: {selected_idea}（随机未完成）")
    else:
        print("📭 当前没有待办点子")
    
    # 3. 显示当前状态
    current_ideas = read_ideas()
    print(f"\n📋 当前剩余点子 ({len(current_ideas)}个):")
    for i, idea in enumerate(current_ideas, 1):
        print(f"  {i}. {idea}")

if __name__ == "__main__":
    main()
