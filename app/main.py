from fastapi import FastAPI

from app.routers.retriever import retriever_router

app = FastAPI()
app.include_router(retriever_router)