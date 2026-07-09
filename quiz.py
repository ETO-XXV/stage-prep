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
        "content": "you are a professional agent,wait until the user gives u a topic, be patient and friendly  , first you generate a quize of 5 question for the user about the topic that he gives you , you give the user 4 options for each question , and u give a single questions at a time , u listen to the answer , u correct it if its wrong , then give the next question for a total of 5 times , make the quiz sooo hard",
    }
]


while True:
#     for message in messages:
#         print(f"{message['role']}: {message['content']}")
    
    user_input = input("vous: ")
    if user_input.lower() == "exit":
        print("Au revoir !")
        break
    
    
    else :
        messages.append({"role" : "user", "content" : user_input})
        reply = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages= messages,
            temperature=1,
        )
        messages.append({"role" : "assistant", "content" : reply.choices[0].message.content})
        print()
        print(reply.choices[0].message.content)
        print()
