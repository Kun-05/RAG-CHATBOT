import os
import shutil
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import RedirectResponse, StreamingResponse
from pydantic import BaseModel
from typing import Optional

# Import cả 2 hàm từ rag.py
from core.rag import ask, ask_stream

app = FastAPI(title="RAG Chatbot API")

class ChatRequest(BaseModel):
    query: str
    top_k: Optional[int] = None
    stream: Optional[bool] = False

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
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
        if req.stream:
            # Trả về dữ liệu chạy chữ từ từ
            return StreamingResponse(ask_stream(q), media_type="text/event-stream")
        else:
            # Trả về 1 cục text ngay lập tức (dự phòng)
            answer = ask(q)
            return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))