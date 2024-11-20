from fastapi import FastAPI
from app.api.v1.controllers.langchain_controller import router as langchain_router
from app.core.llm import init_llm
from app.services.langchain_services import LangChainService

app = FastAPI(
    title="LangChain API",
    description="API utilizando LangChain como biblioteca",
    version="1.0.0",
)

llm = init_llm()
langchain_service = LangChainService(llm)

app.include_router(langchain_router(langchain_service), prefix="/api/v1/langchain")
