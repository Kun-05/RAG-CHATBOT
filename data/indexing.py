from data.loader import doc_file_da_nang, danh_sach_file  # ✅ thêm import
from data.chunking import chunk_products

files = danh_sach_file()

for file in files:
    data = doc_file_da_nang(file)

    if isinstance(data, list):      # file .js → trả về list product
        chunks = chunk_products(data)
        for chunk in chunks:
            print(chunk)

    elif isinstance(data, str):     # file text thường → chunk theo cách khác
        print(data[:200])           # hoặc xử lý tùy ý