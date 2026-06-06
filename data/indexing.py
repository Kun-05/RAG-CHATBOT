from data.loader import doc_file_da_nang, danh_sach_file  # ✅ thêm import
from data.chunking import chunk_products

from core.embedding import embed_many
import chromadb

# Khởi tạo ChromaDB lưu local
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="products")

files = danh_sach_file()

for file in files:
    data = doc_file_da_nang(file)

    if isinstance(data, list):      # file .js → trả về list product
        chunks = chunk_products(data)
        print(f"📦 Đang embed {len(chunks)} chunks từ {file}...")
        embedded = embed_many(chunks)

        # Lưu vào ChromaDB
        collection.add(
            ids=[f"product_{i}" for i in range(len(embedded))],
            documents=[e["text"] for e in embedded],
            embeddings=[e["vector"] for e in embedded],
        )
        print(f"✅ Đã lưu {len(embedded)} vectors vào ChromaDB.")

print(f"\n🎉 Tổng số document trong DB: {collection.count()}")