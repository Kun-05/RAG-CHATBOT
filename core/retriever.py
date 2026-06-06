# retrieval.py
import chromadb
from core.embedding import embed_text

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("products")

def retrieve(query: str, top_k: int = 3) -> list[str]:
    vector = embed_text(query)
    results = collection.query(
        query_embeddings=[vector],
        n_results=top_k
    )
    return results["documents"][0]  # list các chunk liên quan