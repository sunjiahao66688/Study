import Config
from langchain.chat_models import init_chat_model
model = init_chat_model(model="deepseek-chat")

"""
response = model.invoke("你是谁？")
print(response.content)
"""

"""
response = model.invoke(
    [
        {"role":"system","content":input("System：")},
        {"role":"user","content":input("User：")},    
    ]
)
print(response.content)
"""

"""
response = model.stream("你是谁？")
for chunk in response:
    print(chunk.content,end="",flush=True)
print()
"""

"""
from langchain.agents import create_agent
agent = create_agent(model=model)
# agent = create_agent(model="deepseek-chat")
response = agent.invoke({
    "messages" : [
        {"role":"user","content":input("User：")}
    ]
})
print(response)
messages = agent.stream(
    {"messages" : [{"role":"user","content":input("User：")}]},
    stream_mode = "messages"
)
for token,metadata in messages:
    if token.content:
        print(token.content,end="",flush=True)
print()
"""