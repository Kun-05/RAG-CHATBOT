# data/indexing.py
from data.loader import doc_file_da_nang, danh_sach_file 
from data.chunking import chunk_products, chunk_text
from core.embedding import embed_many
from core.vector_store import CustomVectorDB
from config import VECTOR_DB_PATH

# Khởi tạo Custom Vector DB
db = CustomVectorDB(VECTOR_DB_PATH)
files = danh_sach_file()

for file in files:
    data = doc_file_da_nang(file)
    chunks = []
    
    if isinstance(data, list):
        # File .js trả về danh sách sản phẩm
        chunks = chunk_products(data)
    elif isinstance(data, str) and data.strip():
        # File .pdf, .txt trả về văn bản dạng chuỗi
        from config import CHUNK_SIZE
        chunks = chunk_text(data, chunk_size=CHUNK_SIZE)
        
    if not chunks:
        continue

    print(f"⏳ Đang embed {len(chunks)} chunks từ {file}...")
    embedded = embed_many(chunks)
    
    # Lưu vào Custom JSON Vector DB
    db.save(embedded)
    print(f"✅ Đã lưu {len(embedded)} vectors vào {VECTOR_DB_PATH}.")

print(f"\n🎉 Tổng số document trong DB: {len(db.data)}")