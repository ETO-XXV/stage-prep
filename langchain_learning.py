from groq import Groq
from dotenv import load_dotenv
import os
import json
from pprint import pprint

# Generation steps :
#   1- Initialize the Groq client
#   2- Load the API key from the .env file
#   3- Create a prompt template that specifies the fields
#   4- Create a chain that combines the prompt template, the model, and the output parser
#   5- Invoke the chain with the input data and get the response
#   6- Print the response in JSON format


from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()



prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an expert in {subject} and u always answer in {language} and return the text in JSON format with a single key called 'response' and the value is the answer to the question"),
        ("user", "{question}"),
    ]
)

# messages = prompt.format_messages(
#     subject="AI", language="japanese", question="what is a transformer?"
# )

# for m in messages:
#     print(f"[{m.type}]: {m.content}")

model = ChatGroq(
    model="llama-3.3-70b-versatile", api_key=os.getenv("API-real"), temperature=1
)


chain = prompt | model | JsonOutputParser()



response = chain.invoke(
    { "subject": "AI", "language": "francais", "question": "what is a bankai?" }
)

# result = model.invoke(messages)

print()
print(response["response"])
print()
pprint(response)


