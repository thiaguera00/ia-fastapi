import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def init_llm():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY não encontrada no ambiente. Verifique o arquivo .env.")

    return ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", api_key=api_key)
