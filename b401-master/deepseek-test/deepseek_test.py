import os
from dotenv import load_dotenv, find_dotenv
from langchain_deepseek import ChatDeepSeek

_ = load_dotenv(find_dotenv())

llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0.7,
)

messages = [
    ("system", "Eres un traductor útil. Traduce la oración del usuario al francés."),
    ("human", "Me encanta programar."),
]

resp = llm.invoke(messages)
print(resp.content)
