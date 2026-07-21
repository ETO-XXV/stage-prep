from fastapi import FastAPI
from pydantic import BaseModel

import os
from dotenv import load_dotenv

import subprocess

from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



try:
    print("kill your self \n")
    a = 3/0 
except:
    print("err")


