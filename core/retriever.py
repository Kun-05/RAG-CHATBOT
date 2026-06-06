# core/retriever.py
from core.embedding import embed_text
from core.vector_store import CustomVectorDB
from config import VECTOR_DB_PATH

db = CustomVectorDB(VECTOR_DB_PATH)

def retrieve(query: str, top_k: int = 3) -> list[str]:
    # Biến query thành vector
    query_vector = embed_text(query)
    if not query_vector:
        return []
    
    # Reload lại file json để đảm bảo có dữ liệu mới nhất
    db._load()
    # Tìm kiếm bằng Cosine Similarity tự làm
    results = db.search(query_vector, top_k=top_k)
    return results