import os
import json
import re
from data.loader import doc_file_da_nang
from data.chunking import chunk_products

if __name__ == "__main__":
    FILE_PATH = "storage/Product.js"  # 👉 Đổi đường dẫn nếu cần

    print("=" * 60)
    print("CHUNK TEST - Kiểm tra pipeline loader → chunking")
    print("=" * 60)

    # Bước 1: Load file
    data = doc_file_da_nang(FILE_PATH)

    if data is None:
        print("❌ Không đọc được file. Kiểm tra lại đường dẫn.")
        exit()

    if not isinstance(data, list):
        print(f"❌ Kết quả trả về không phải list. Nhận được: {type(data)}")
        exit()

    print(f"✅ Load thành công! Tổng số product: {len(data)}\n")

    # Bước 2: Chunk
    chunks = chunk_products(data)
    print(f"✅ Chunk thành công! Tổng số chunk: {len(chunks)}\n")

    # Bước 3: In từng chunk để kiểm tra
    print("=" * 60)
    print("CHI TIẾT TỪNG CHUNK:")
    print("=" * 60)

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk #{i+1} ---")
        print(chunk)

    # Bước 4: Kiểm tra data bất thường
    print("\n" + "=" * 60)
    print("KIỂM TRA DỮ LIỆU BẤT THƯỜNG:")
    print("=" * 60)

    co_loi = False
    for p in data:
        discount = p.get('discountPercentage', 0)
        if discount > 100:
            print(f"⚠️  [{p['title']}] discountPercentage = {discount} (có vẻ sai, nên là ≤ 100%)")
            co_loi = True
        if p.get('stockQuantity', 0) < 0:
            print(f"⚠️  [{p['title']}] stockQuantity âm: {p['stockQuantity']}")
            co_loi = True

    if not co_loi:
        print("✅ Không phát hiện dữ liệu bất thường.")

    print("\n✅ Test hoàn tất!")