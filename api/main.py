import os
import shutil
from fastapi import FastAPI, HTTPException, UploadFile, File
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


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload a PDF, TXT, or DOCX file into storage/ for indexing."""
    ALLOWED_EXTENSIONS = {".pdf", ".txt", ".md", ".docx", ".csv", ".json"}
    _, ext = os.path.splitext(file.filename)
    if ext.lower() not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{ext}'. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    os.makedirs("storage", exist_ok=True)
    dest = os.path.join("storage", file.filename)
    with open(dest, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"message": f"Uploaded '{file.filename}' to storage/", "path": dest}


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
