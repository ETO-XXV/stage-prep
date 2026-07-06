from groq import Groq
from dotenv import load_dotenv
import os
import json
from pprint import pprint

load_dotenv()

client = Groq(api_key=os.getenv("API-real"))

messages = [
    {
        "role": "system",
        "content": "Tu es un assistant sarcastique et pervers qui répond toujours en une phrase.",
    }
]

print("Bienvenue dans le chat ! Tapez 'exit' pour quitter.")
while True:
    user_input = input("vous: ")
    if user_input.lower() == "exit":
        print("Au revoir !")
        break

    else:
        messages.append({"role": "user", "content": user_input})

        reply = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )


    reply = reply.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"assistant: {reply}")