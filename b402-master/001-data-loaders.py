import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

from langchain_openai import ChatOpenAI

chatModel = ChatOpenAI(model="gpt-5", temperature=1)

from langchain_community.document_loaders import TextLoader

loader = TextLoader("./data/be-good.txt")
loaded_data = loader.load()

print("\n----------\n")
print("Loaded TXT file:")
print("\n----------\n")
# print(loaded_data)

print("\n----------\n")

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('./data/Street_Tree_List.csv')
loaded_data = loader.load()

print("\n----------\n")
print("Loaded CSV file:")
print("\n----------\n")
# print(loaded_data)

print("\n----------\n")

# ✅ Usamos BSHTMLLoader en lugar de UnstructuredHTMLLoader
from langchain_community.document_loaders import BSHTMLLoader

loader = BSHTMLLoader('./data/100-startups.html', open_encoding="utf-8")
loaded_data = loader.load()

print("\n----------\n")
print("Loaded HTML page:")
print("\n----------\n")
# print(loaded_data)

print("\n----------\n")

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('./data/5pages.pdf')
loaded_data = loader.load_and_split()

print("\n----------\n")
print("Loaded PDF file:")
print("\n----------\n")
# print(loaded_data[0].page_content)

print("\n----------\n")

from langchain_community.document_loaders import WikipediaLoader

name = "JFK"
loader = WikipediaLoader(query=name, load_max_docs=1)
loaded_data = loader.load()[0].page_content

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("human", "Answer this {question}, here is some extra {context}"),
    ]
)

messages = chat_template.format_messages(
    question="What was the full name of JFK?",
    context=loaded_data
)

response = chatModel.invoke(messages)

print("\n----------\n")
print("Respond from Wikipedia: What was the full name of JFK?")
print("\n----------\n")
print(response.content)
print("\n----------\n")
