import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies 2 integers and returns the result."""
    return a * b

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("API-real"),
    temperature=0
)

# Group your tools into a list
tools = [multiply]

# 1. Create the Agent WITHOUT the state_modifier argument
agent_executor = create_react_agent(model, tools)

print("Asking the modern LangGraph agent a complex math question...\n")

# 2. Inject the System Prompt directly into the message list when you invoke it!
response = agent_executor.invoke({
    "messages": [
        ("system", "You are a helpful math assistant."),
        ("user", "Multiply 5 by 6. Then take that result and multiply it by 3.")
    ]
})

print("\n🎯 Final Answer:")
print(response["messages"][-1].content)