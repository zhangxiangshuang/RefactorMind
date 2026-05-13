import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# 1. 加载环境变量
load_dotenv()

# 2. 初始化大模型 (这里预留了接入 MiMo 的位置)
# 当你获得 MiMo Token 后，只需替换 base_url 和 api_key 即可进行模型对比评测
llm = ChatOpenAI(
    model_name="gpt-4-turbo",  # 可替换为 "mimo-pro" 等小米模型名称
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1
)

# 3. 定义多 Agent 角色与提示词
# 感知层 Agent：负责解析代码坏味道
code_parser_prompt = ChatPromptTemplate.from_template(
    "你是一个资深代码审查专家。请分析以下 Python 代码，识别其中的坏味道（如长函数、重复代码等）：\n\n{code_snippet}"
)

# 决策层 Agent：负责生成长链推理的重构方案
planning_prompt = ChatPromptTemplate.from_template(
    "基于以下代码坏味道分析结果，请给出一个安全的重构路径，并附带回滚预案：\n\n{analysis_result}"
)

# 4. 构建工作流
def refactor_workflow(code_snippet):
    print(f"🚀 [Orchestrator] 开始对代码片段进行重构分析...")
    
    # 步骤1：感知层 - 解析代码
    parser_chain = LLMChain(llm=llm, prompt=code_parser_prompt)
    analysis_result = parser_chain.run(code_snippet=code_snippet)
    print(f"🔍 [CodeParserAgent] 识别到的坏味道：\n{analysis_result}\n")
    
    # 步骤2：决策层 - 规划重构路径
    planning_chain = LLMChain(llm=llm, prompt=planning_prompt)
    refactor_plan = planning_chain.run(analysis_result=analysis_result)
    print(f"🧠 [PlanningAgent] 生成的重构方案：\n{refactor_plan}\n")
    
    return refactor_plan

# 5. 模拟真实运行入口
if __name__ == "__main__":
    # 模拟一段带有坏味道的遗留代码
    legacy_code = """
def process_data(data):
    # 这是一个又长又乱的函数，包含了数据清洗、计算和打印
    cleaned = []
    for item in data:
        if item > 0:
            cleaned.append(item * 2)
    total = 0
    for c in cleaned:
        total += c
    print(f"Total is {total}")
    """
    
    # 触发工作流
    refactor_workflow(legacy_code)
