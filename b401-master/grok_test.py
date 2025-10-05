import os
from dotenv import load_dotenv, find_dotenv
from langchain_xai import ChatXAI

# Cargar variables de entorno
_ = load_dotenv(find_dotenv())
# xai_api_key = os.getenv("GROK_API_KEY")

# if not xai_api_key:
#     raise ValueError("⚠️ No se encontró XAI_API_KEY en tu .env")

# Inicializar modelo Grok 4
grok_chat = ChatXAI(
    model="grok-4",       # o "grok-4-0709" si quieres la última versión
    temperature=0.7,
    xai_api_key=os.getenv("GROK_API_KEY"),
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Mensajes de ejemplo
messages = [
    ("system", "Eres un historiador experto en la familia Kennedy."),
    ("human", "¿Cuántos miembros de la familia murieron trágicamente?")
]

print("\n----------\n")
print("Pregunta al modelo Grok 4:")
print("\n----------\n")

response = grok_chat.invoke(messages)
print(response.content)

# Ejemplo con streaming
print("\n----------\n")
print("Streaming con Grok 4:")
print("\n----------\n")

chat_stream = ChatXAI(model="grok-4", temperature=0.5)
for chunk in chat_stream.stream("Dime un dato curioso sobre Nikola Tesla."):
    print(chunk.content, end="", flush=True)

print("\n\n----------\nFin del streaming\n")
