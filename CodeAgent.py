import Config
from langchain.tools import tool
@tool
def writeFile(filename,content):
    """
    Write content to local file
    Args:
        filename : File path
        content : What to write
    """
    with open(filename,"a") as f:
        f.write(content)
    return "Write Successfully"
import os
@tool
def execCommand(cmd):
    """
    Execute command
    Args:
        cmd : Shell command to be executed
    """
    os.system(cmd)
    return "Execute Successfully"
@tool
def createFolder(path):
    """
    Create folder
    Args:
        path : Folder path
    """
    os.mkdir(path)
    return "Create Successfully"
@tool
def changeFolder(path):
    """
    Switch working directory
    Args:
        path : Directory path, directory must exist
    """
    os.chdir(path)
    return "Change Successfully"
@tool
def listFile():
    """
    Lists the files and folders in the current directory
    """
    return f"File and Folder : {os.listdir()}"

from langchain.agents import create_agent

agent = create_agent(
    "deepseek-chat",
    tools = [writeFile,execCommand,createFolder,changeFolder,listFile]
)

response = agent.invoke({
    "messages" : [
        {
            "role":"user",
            "content":input("User：")
        }
    ]
})
from langchain_core.messages import AIMessage,HumanMessage,ToolMessage
for i in response["messages"]:
    if isinstance(i,HumanMessage):
        print(f"Human：{i.content}")
    elif isinstance(i,AIMessage):
        print(f"AI：{i.content}")
    elif isinstance(i,ToolMessage):
        print(f"Tool：{i.content}")
    else:
        pass
    print()