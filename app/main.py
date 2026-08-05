from fastapi import FastAPI
from app.api.documents import router
from app.database.init_db import init_db

app = FastAPI(
    title="AI Knowledge Assistant",
    description="An AI-powered document question answering system",
    version="0.1.0",
)

app.include_router(router, prefix="/documents", tags=["Documents"])

init_db()

@app.get("/")
def home():
    return {"message": "AI Knowledge Assistant is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
