import json
import random
from datetime import datetime
from typing import Dict, List, Any

class VisualAnalysisAgent:
    """视觉分析智能体：识别画作元素"""
    
    def __init__(self):
        # 模拟预训练的画作元素识别能力
        self.recognized_elements = {
            "sun": ["太阳", "圆形发光物体", "黄色圆形"],
            "tree": ["树木", "绿色三角形", "棕色树干"],
            "house": ["房子", "方形屋顶", "窗户"],
            "person": ["人物", "小人", "笑脸"]
        }
    
    def analyze_painting(self, painting_description: str) -> Dict[str, Any]:
        """分析儿童画作，识别其中的元素"""
        print(f"[视觉分析Agent] 正在分析画作: {painting_description}")
        
        # 模拟AI识别过程
        detected_elements = []
        for element, keywords in self.recognized_elements.items():
            for keyword in keywords:
                if keyword in painting_description:
                    detected_elements.append(element)
                    break
        
        # 模拟色彩分析
        colors = ["红色", "蓝色", "黄色", "绿色", "紫色"]
        detected_colors = random.sample(colors, random.randint(1, 3))
        
        return {
            "elements": list(set(detected_elements)),
            "colors": detected_colors,
            "analysis_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

class GuidanceFeedbackAgent:
    """引导反馈智能体：将专业术语转化为童言"""
    
    def __init__(self):
        # 专业术语到童言的映射词典
        self.child_language_dict = {
            "sun": {
                "professional": "太阳的光影处理可以更丰富",
                "childish": "太阳公公在对你笑呢，可以给他画上更灿烂的笑容！"
            },
            "tree": {
                "professional": "树木的层次感需要加强",
                "childish": "大树朋友想穿上更多绿色的叶子衣服"
            },
            "house": {
                "professional": "房屋的透视关系需要调整",
                "childish": "小房子的窗户好像在说'你好呀！'"
            },
            "person": {
                "professional": "人物比例可以更加协调",
                "childish": "小朋友的手手举得高高的，真开心！"
            }
        }
    
    def generate_feedback(self, elements: List[str], colors: List[str], 
                         child_preferences: Dict[str, Any] = None) -> str:
        """生成适合儿童的反馈"""
        print(f"[引导反馈Agent] 正在生成反馈，识别到元素: {elements}")
        
        feedback_parts = []
        
        # 为每个识别到的元素生成童言反馈
        for element in elements[:2]:  # 最多处理两个主要元素
            if element in self.child_language_dict:
                feedback = self.child_language_dict[element]["childish"]
                feedback_parts.append(feedback)
        
        # 添加色彩相关的个性化反馈
        if child_preferences and "favorite_colors" in child_preferences:
            favorite_colors = child_preferences["favorite_colors"]
            common_colors = set(colors) & set(favorite_colors)
            if common_colors:
                color_feedback = f"宝宝喜欢的{', '.join(common_colors)}颜色用得真棒！"
                feedback_parts.append(color_feedback)
        
        # 如果没有识别到特定元素，使用通用反馈
        if not feedback_parts:
            feedback_parts.append("你的画真漂亮！继续加油哦！")
        
        return "。".join(feedback_parts) + "。"

class MemorySystem:
    """记忆系统：存储孩子的偏好信息"""
    
    def __init__(self):
        # 模拟向量数据库存储
        self.child_memories = {}
    
    def save_preferences(self, child_id: str, elements: List[str], 
                        colors: List[str]) -> None:
        """保存孩子的色彩偏好到记忆系统"""
        if child_id not in self.child_memories:
            self.child_memories[child_id] = {
                "favorite_colors": [],
                "frequent_elements": [],
                "interaction_count": 0
            }
        
        memory = self.child_memories[child_id]
        
        # 更新色彩偏好（模拟向量数据库的相似度计算）
        for color in colors:
            if color not in memory["favorite_colors"]:
                memory["favorite_colors"].append(color)
        
        # 更新常用元素
        for element in elements:
            if element not in memory["frequent_elements"]:
                memory["frequent_elements"].append(element)
        
        memory["interaction_count"] += 1
        memory["last_interaction"] = datetime.now().isoformat()
        
        print(f"[记忆系统] 已更新 {child_id} 的偏好记忆")
    
    def get_preferences(self, child_id: str) -> Dict[str, Any]:
        """获取孩子的偏好信息"""
        return self.child_memories.get(child_id, {
            "favorite_colors": ["红色", "蓝色", "黄色"],
            "frequent_elements": [],
            "interaction_count": 0
        })

def main():
    """主函数：模拟AI美术助教的工作流程"""
    print("=" * 50)
    print("AI美术助教系统启动")
    print("=" * 50)
    
    # 初始化多智能体系统
    visual_agent = VisualAnalysisAgent()
    feedback_agent = GuidanceFeedbackAgent()
    memory_system = MemorySystem()
    
    # 模拟两个孩子和他们的画作
    children = [
        {"id": "child_001", "name": "小明", "painting": "我画了一个大大的黄色太阳和绿色的树"},
        {"id": "child_002", "name": "小红", "painting": "画里有红色房子和笑脸小人"}
    ]
    
    for child in children:
        print(f"\n🎨 正在处理 {child['name']} 的画作...")
        
        # 步骤1: 视觉分析智能体分析画作
        analysis_result = visual_agent.analyze_painting(child["painting"])
        
        # 步骤2: 从记忆系统获取孩子的历史偏好
        preferences = memory_system.get_preferences(child["id"])
        
        # 步骤3: 引导反馈智能体生成个性化反馈
        feedback = feedback_agent.generate_feedback(
            analysis_result["elements"],
            analysis_result["colors"],
            preferences
        )
        
        # 步骤4: 输出反馈结果
        print(f"\n💬 给 {child['name']} 的反馈:")
        print(f"   识别到的元素: {', '.join(analysis_result['elements'])}")
        print(f"   使用的颜色: {', '.join(analysis_result['colors'])}")
        print(f"   AI反馈: {feedback}")
        
        # 步骤5: 更新记忆系统
        memory_system.save_preferences(
            child["id"],
            analysis_result["elements"],
            analysis_result["colors"]
        )
        
        # 显示互动统计
        updated_prefs = memory_system.get_preferences(child["id"])
        print(f"   历史互动次数: {updated_prefs['interaction_count']}次")
        print(f"   偏好颜色: {', '.join(updated_prefs['favorite_colors'][:3])}")
    
    print("\n" + "=" * 50)
    print("AI美术助教系统运行完成")
    print("=" * 50)
    
    # 显示系统总结
    print("\n📊 系统运行统计:")
    total_interactions = sum(
        memory_system.get_preferences(child["id"])["interaction_count"]
        for child in children
    )
    print(f"   总互动次数: {total_interactions}")
    print(f"   服务孩子数量: {len(children)}")

if __name__ == "__main__":
    main()