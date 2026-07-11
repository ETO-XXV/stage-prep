import os
from dotenv import load_dotenv
import subprocess
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq


# General steps :
#     1- load the dotenv and the API key 
#     2- define the function using @tool and specify the types staticly
#     3- declare the model and its parameteres
#     4- group the tool (functions names) into a list
#     5- create a react agent with the parameters model and tools
#     6- pass the prompt the invove methode to the agent 
#     7- print the result 


load_dotenv()

@tool
def list() -> str :
    """_summary_
    a function that allows you to list the content (folders and sub-directories) of the current working directory
    Returns:
        str: return the content of the directory as a string
    """
    return subprocess.run(["ls"],  capture_output=True, text=True)

@tool
def cat(path : str) -> str :
    """_summary_
    a function to display the exact content of a file line by line
    Args:
        path (str): the path to the file

    Returns:
        str: the actual content of the file as a string 
    """
    return subprocess.run(f"cat {path}", capture_output=True, text=True , shell=True)





model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key = os.getenv("API-real"),
    temperature = 0
)

tools = [list,cat]

agent = create_react_agent(model, tools)

prompt = "what are the content of the current working directory ? , select one of them that starts with an L and show its content "

response = agent.invoke({
   "messages" : [
    ("system", "You are a helpful assistant that can assist with the management of files and directories."),
    ("user", prompt)
   ]
})

print("\nthe answer:")

print(response["messages"][-1].content)
print("\n\n\n")










# result = subprocess.run(["ls"], capture_output=True, text=True)
# print(result.stdout)
# print("#############################################################################################")
# pprint(result.__dict__)  # Inspect the raw AIMessage to see if it requested a tool

