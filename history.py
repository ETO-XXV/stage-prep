from groq import Groq
from dotenv import load_dotenv
import os
import json
from pprint import pprint


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "you are an expert in {subject} and u always answer in {language} and return the text in JSON format with a single key called 'answer' and the value is the answer to the question,make sure everything is in a JSON format",
        ),
        MessagesPlaceholder(variable_name="history"),
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




Conversation_history = []


chain = prompt | model | JsonOutputParser()



while True:
    user_input = input("user : ")

    if user_input.lower() == "exit":
        print("until we meet again !")
        break

    else:
        
        
        
        response = chain.invoke(
            {"subject": "philosophy", 
             "language": "francais", 
             "question": user_input , 
             "history" : Conversation_history }
        )
        print()
        print(response["answer"])
        print()
        
        json_response = json.dumps(response,ensure_ascii=False)
        
        Conversation_history.append(HumanMessage(content=user_input))
        
        Conversation_history.append(AIMessage(content=json_response))


# result = model.invoke(messages)



for m in Conversation_history:
    print(f"{m.type} : {m.content}")



