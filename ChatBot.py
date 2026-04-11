
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("API_KEY")
store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
        store[session_id].add_message(SystemMessage(content=os.getenv("SYSTEM_PROMPT")))
    return store[session_id]
    
def trim_history(session_id,max_rounds = 3):
    history = store.get(session_id)
    if not history:
        return
    messages = history.messages
    system_msgs = [m for m in messages if isinstance(m,SystemMessage)]
    other_msgs = [m for m in messages if not isinstance(m,SystemMessage)]
    max_other = max_rounds*2
    if len(other_msgs) > max_other:
        other_msgs = other_msgs[-max_other:]
    history.messages = system_msgs + other_msgs
    
model = ChatOpenAI(
    model = "deepseek-chat",
    api_key = DEEPSEEK_API_KEY,
    base_url = "https://api.deepseek.com/v1",
    temperature = 0.7
)

chain = RunnableWithMessageHistory(model, get_session_history)


session_config = {"configurable": {"session_id": "user-123"}}
while True:
    res = chain.stream([HumanMessage(content=input("User："))], config=session_config)
    for i in res:
        print(i.content,end="")
    print()
    trim_history("user-123",3)


