from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from core.rag import ask

app = FastAPI(title="RAG Chatbot API")


class ChatRequest(BaseModel):
    query: str
    top_k: Optional[int] = None
    stream: Optional[bool] = False


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
    q = req.query.strip() if req.query else ""
    if not q:
        raise HTTPException(status_code=400, detail="'query' is required")

    try:
        # Use existing RAG pipeline (`core.rag.ask`) which returns a string answer.
        answer = ask(q)
        return {"answer": answer}
    except Exception as e:
        # Surface a 503 when downstream services fail (LLM / embedding / DB)
        raise HTTPException(status_code=503, detail=str(e))
