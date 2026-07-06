from groq import Groq
from dotenv import load_dotenv
import os
import json
from pprint import pprint

load_dotenv()

client = Groq(api_key=os.getenv("API-real"))


print("Bienvenue dans le chat ! Tapez 'exit' pour quitter.")

stream = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "Tu es un assistant sarcastique et pervers qui répond toujours en une 10 phrase.",
        }
    ],
    temperature=0.7,
    max_tokens=500,
    stream=True,
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
        pprint(chunk.model_dump())        


        
print("\n")