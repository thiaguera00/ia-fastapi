import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LangChain API"
    langchain_model: str = "gemini"

    class Config:
        env_file = ".env"

settings = Settings()
