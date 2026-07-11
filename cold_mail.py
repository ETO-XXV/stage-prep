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

load_dotenv()


# Your Objective: You are going to build a FastAPI backend that takes details about a
# target company from a user, sends those details to the Groq LLM to write a personalized
# cold email, and returns that email to the user.

# The Specs:
# Method: POST (Because you are receiving a payload of data).

# Input Payload: A company name, their industry, and the product you are trying to sell them.

# Processing: The Groq API processes the data.

# Output: A JSON dictionary containing the AI-generated email.

app = FastAPI()


class Informations(BaseModel):
    name: str
    industry: str
    product: str


@app.post("/coldMail")
def CM(payload: Informations):
    name = payload.name
    industry = payload.industry
    product = payload.product

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "you are an expert in sending professional mails , you search for the the company that the user gave you and you check their industry ,you write a mail in detail to ask about the product,you always answer in {language}, and return the text in JSON format with a single key called 'mail' and the value is the mail that you generated",
            ),
            ("user", "hello , can u help me with writing an email to the company {company} , they work in the {industry} field , i want to ask them about the different information and price of this product {product}"),
        ]
    )
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key = os.getenv("API-real"),
        temperature = 0,
    )
    
    chain = prompt | model | JsonOutputParser()
    
    response = chain.invoke(
        {
            "language" : "english",
            "company" : name,
            "industry" : industry,
            "product" : product
        }
    )
    return {
        "status": "success",
        "message": f"AI-generated cold email for {name} in the {industry} sector regarding {product}.",
        "email_content": response["mail"],
    }
