"""CrewAI 入门 demo：单个 Agent + Task，调用阿里百炼(DashScope)的 OpenAI 兼容接口。"""

import os

from crewai import Agent, Crew, LLM, Task
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model=os.environ["DASHSCOPE_MODEL"],
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url=os.environ["DASHSCOPE_BASE_URL"],
)

writer = Agent(
    role="科普作家",
    goal="用通俗易懂的语言解释技术概念",
    backstory="你是一名擅长把复杂技术讲清楚的科普作家。",
    llm=llm,
    verbose=True,
)

task = Task(
    description="用 3 句话解释一下什么是 CrewAI 框架。",
    expected_output="一段简洁的中文说明，不超过 3 句话。",
    agent=writer,
)

crew = Crew(agents=[writer], tasks=[task], verbose=True)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n=== 最终结果 ===")
    print(result)
