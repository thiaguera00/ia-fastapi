from fastapi import APIRouter, HTTPException, Depends
from app.api.v1.dtos.langchain_dto import QueryRequest, QueryResponse
from app.services.langchain_services import LangChainService

def router(service: LangChainService) -> APIRouter:
    router = APIRouter()

    @router.post("/query", response_model=QueryResponse)
    async def query_langchain(request: QueryRequest):
        try:
            response = service.process_query(request.query)
            return QueryResponse(result=response)
        except Exception as e:
            raise HTTPException(status_code=500, detail="error")

    return router
