import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key,
    model="openai/gpt-oss-120b"
)

response = llm.invoke("Explica qué es el modelo GPT‑OSS en términos sencillos.")
print(response.content)