# query_test.py — thử tìm kiếm
from core.embedding import embed_text
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("products")

query = "vòng tay hoa cỏ ba lá"
vector = embed_text(query)

results = collection.query(
    query_embeddings=[vector],
    n_results=3  # lấy top 3 gần nhất
)

print("🔍 Kết quả tìm kiếm:")
for i, doc in enumerate(results["documents"][0]):
    print(f"\n--- Kết quả #{i+1} ---")
    print(doc)