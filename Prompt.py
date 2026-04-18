import Config
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from pydantic import BaseModel

f = open("Prompt.md","r")
agent = create_agent(
    model = "deepseek-chat",
    system_prompt  = f.read()
)
f.close()

"""
class CityInfo(BaseModel):
    location : str
    description : str

agent = create_agent(
    model = "deepseek-chat",
    system_prompt  = "你是一个科幻作家，根据用户的提问创建一个太空之都",
    response_format = CityInfo
    
)
"""

for token,metadata in agent.stream(
    {"messages" : [HumanMessage(input("User："))]},
    stream_mode = "messages"
):
    print(token.content,end="",flush=True)

"""
res = agent.invoke(
    {"messages" : [HumanMessage(input("User："))]}
)
print(res['structured_response'])
"""