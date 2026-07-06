from groq import Groq
from dotenv import load_dotenv
import os
import json
from pprint import pprint 

load_dotenv()

#print(os.getenv("API-real"))


client = Groq(api_key = os.getenv("API-real"))


reply = client.chat.completions.create(
    model = "llama-3.1-8b-instant" ,
    messages = [
        {"role": "system", "content": "Tu es un assistant sarcastique et pervers qui répond toujours en une phrase."},
        {"role": "user", "content": "Explique-moi c'est quoi un LLM en 3 lignes."}
    ]

)

print(reply.choices[0].message.content)
print("\n")
pprint(reply.model_dump())