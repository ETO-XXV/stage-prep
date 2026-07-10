import os
from dotenv import load_dotenv
import subprocess
from pprint import pprint
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq


path = "tools.py"
result = subprocess.run(f"cat {path}", capture_output=True, text=True , shell=True)
print(result.stdout)
print("#############################################################################################")
pprint(result.__dict__)  # Inspect the raw AIMessage to see if it requested a tool
