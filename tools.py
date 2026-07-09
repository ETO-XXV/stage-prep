import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
# Import all message types needed for the execution loop
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from pprint import pprint


load_dotenv()   

# 1. Define the tool with strict typing and a clear docstring
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies 2 integers and returns the result."""
    return a * b 

# 2. Initialize the model (temperature=0 for logical tasks)
model = ChatGroq(
    model="llama-3.3-70b-versatile", 
    api_key=os.getenv("API-real"), 
    temperature=0
)

# 3. Bind the tool to the model
model_with_tools = model.bind_tools([multiply])

# 4. Set up the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful math assistant."),
    ("user", "{question}"),
])

# 5. Create the chain (Notice: No StrOutputParser, so we keep the raw AIMessage)
chain = prompt | model_with_tools

# --- EXECUTION PHASE ---

user_question = "multiply 5 and 6" 
print(f"User: {user_question}\n")

# Step A: The model analyzes the question and requests a tool
response = chain.invoke({"question": user_question})

pprint(response.model_dump())  # Inspect the raw AIMessage to see if it requested a tool

# Step B: Check if the model asked to use a tool
if response.tool_calls:
    tool_call = response.tool_calls[0]
    print(f"1. AI requested tool: '{tool_call['name']}' with args: {tool_call['args']}")
    
    # Step C: Execute the actual Python function
    math_result = multiply.invoke(tool_call["args"])
    print(f"2. Python calculated: {math_result}")
    
    # Step D: Reconstruct the conversation timeline
    conversation_history = [
        HumanMessage(content=user_question),                 # 1. User's prompt
        response,                                            # 2. AI's tool request
        ToolMessage(content=str(math_result), tool_call_id=tool_call["id"]) # 3. Tool's output
    ]
    
    # Step E: Send the timeline back to the AI for the final answer
    print("3. Sending the result back to the AI...")
    final_response = model_with_tools.invoke(conversation_history)
    
    print("\nFinal AI Response:")
    print(final_response.content)

else:
    # Fallback just in case the AI decided to answer directly without a tool
    print("\nFinal AI Response:")
    print(response.content)