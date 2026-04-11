from dotenv import load_dotenv

load_dotenv()

from langchain.tools import tool

@tool
def getWeather(location):
    """
    Get the weather in a given location
    Args:
        location : city name or coordinates
    """
    return f"Current weather in {location} is sunny"

@tool
def writeNote(content,filename):
    """
    Write notes to the local directory
    Args:
        content : Content of notes
        filename : Note file path
    """
    with open(filename,"w") as f:
        f.write(content)
    return "Write Successfully"

import time
@tool
def getDate():
    """
    Get the current time
    """
    tm = time.localtime()
    return f"Year:{tm.tm_year},Month:{tm.tm_mon},Day:{tm.tm_mday}"    

from langchain.agents import create_agent

agent = create_agent(
    "deepseek-chat",
    tools = [getWeather,writeNote,getDate]
)

response = agent.invoke({
    "messages" : [
        {
            "role":"user",
            "content":f"今天{input("Loc：")}的天气怎么样?帮我把天气记到笔记里，标注上准确日期"
        }
    ]
})
print(response)