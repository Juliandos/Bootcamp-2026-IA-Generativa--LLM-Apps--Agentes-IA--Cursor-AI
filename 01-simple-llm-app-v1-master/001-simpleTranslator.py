# from fastapi import FastAPI
# from langserve import add_routes
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv, find_dotenv
# import os

# # --- Cargar variables de entorno ---
# _ = load_dotenv(find_dotenv())
# openai_api_key = os.environ["OPENAI_API_KEY"]

# # --- Modelo LLM ---
# llm = ChatOpenAI(model="gpt-3.5-turbo")
# parser = StrOutputParser()

# # --- Cadena 1: Traductor ---
# translate_system_template = "Translate the following into {language}:"
# translate_prompt_template = ChatPromptTemplate.from_messages([
#     ("system", translate_system_template),
#     ("user", "{text}")
# ])
# translate_chain = translate_prompt_template | llm | parser

# # --- Cadena 2: Resumen ---
# summarize_system_template = "Summarize the following text in a concise way:"
# summarize_prompt_template = ChatPromptTemplate.from_messages([
#     ("system", summarize_system_template),
#     ("user", "{text}")
# ])
# summarize_chain = summarize_prompt_template | llm | parser

# # --- Crear la aplicación FastAPI ---
# app = FastAPI(
#     title="LangServe MultiTool",
#     version="1.0",
#     description="LangServe app with translation and summarization endpoints",
# )

# # --- Agregar las rutas LangServe ---
# add_routes(app, translate_chain, path="/translate")
# add_routes(app, summarize_chain, path="/summarize")

# # --- Ejecutar servidor ---
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)

from fastapi import FastAPI
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os

# --- Cargar variables de entorno ---
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

# --- Modelo LLM ---
llm = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

# --- Plantilla con "modo" ---
system_template = """
You are a helpful assistant. Perform the following task based on the selected mode:

- If mode = "translate", translate the given text into the target {language}.
- If mode = "summarize", summarize the given text in a concise and clear way.

Mode: {mode}
Text: {text}
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template)
])

# --- Cadena completa ---
chain = prompt_template | llm | parser

# --- Crear la app FastAPI ---
app = FastAPI(
    title="LangServe Multi-Tool",
    version="1.0",
    description="Single endpoint for translation and summarization",
)

# --- Agregar una sola ruta ---
add_routes(app, chain, path="/chain")

# --- Ejecutar servidor ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
