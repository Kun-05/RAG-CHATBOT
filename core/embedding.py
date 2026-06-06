import requests
import json

OLLAMA_URL = "http://localhost:11434/api/embeddings"
EMBED_MODEL = "nomic-embed-text"

def embed_text(text: str) -> list[float]:
    """
    Gửi 1 đoạn text → nhận về vector embedding.
    """
    response = requests.post(OLLAMA_URL, json={
        "model": EMBED_MODEL,
        "prompt": text
    })
    
    if response.status_code != 200:
        print(f"Lỗi Ollama: {response.status_code} - {response.text}")
        return None
    
    return response.json()["embedding"]


def embed_many(chunks: list[str]) -> list[dict]:
    """
    Embed toàn bộ danh sách chunk.
    Trả về list { "text": ..., "vector": [...] }
    """
    results = []
    
    for i, chunk in enumerate(chunks):
        print(f"  Đang embed chunk {i+1}/{len(chunks)}...", end="\r")
        vector = embed_text(chunk)
        
        if vector:
            results.append({
                "text": chunk,
                "vector": vector
            })
    
    print(f"\n✅ Embed xong {len(results)}/{len(chunks)} chunks.")
    return results