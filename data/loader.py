import os
import csv
import json

def doc_file_da_nang(file_path):
    """
    Hàm đọc file
    """
    # Tách lấy đuôi file
    _, ext = os.path.splitext(file_path)
    ext = ext.lower() # Đưa về chữ thường để so sánh
    
    toan_bo_van_ban = ""
    
    print(f"Đang xử lý file định dạng: {ext} ...")
    
    try:
        # 1. Nhóm file văn bản thuần túy (Dùng thư viện gốc của Python)
        if ext in ['.txt', '.md', '.sql', '.js']:
            with open(file_path, 'r', encoding='utf-8') as f:
                toan_bo_van_ban = f.read()
                
        # 2. Nhóm file PDF (Dùng pypdf)
        elif ext == '.pdf':
            import pypdf
            reader = pypdf.PdfReader(file_path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    toan_bo_van_ban += text + "\n"
                    
        # 3. Nhóm file Word (Dùng python-docx)
        elif ext in ['.doc', '.docx']:
            import docx
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                toan_bo_van_ban += para.text + "\n"
                
        # 4. Nhóm file CSV (Bảng tính)
        elif ext == '.csv':
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    # Nối các cột lại bằng dấu cách
                    toan_bo_van_ban += " ".join(row) + "\n"
                    
        # 5. Nhóm file JSON
        elif ext == '.json':
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Chuyển dữ liệu JSON thành chuỗi chữ để AI đọc được
                toan_bo_van_ban = json.dumps(data, ensure_ascii=False, indent=2)
                
        else:
            print(f"Cảnh báo: Hệ thống chưa hỗ trợ định dạng {ext}")
            return None
            
    except Exception as e:
        print(f"Lỗi khi đọc file {file_path}: {e}")
        return None
        
    return toan_bo_van_ban


def danh_sach_file(thu_muc_goc="storage"):
    """
    Hàm lấy danh sách tất cả file trong thư mục gốc (storage) và các thư mục con.
    """
    list_file = []
    for root, dirs, files in os.walk(thu_muc_goc):
        for file in files:
            file_path = os.path.join(root, file)
            list_file.append(file_path)
    return list_file
            
if len(danh_sach_file()) == 0:
    print("Thư mục rỗng, cho tôi rác!")

for file in danh_sach_file():
    if os.path.exists(file):
        noi_dung = doc_file_da_nang(file)
        if noi_dung: 
            print(f"-> Thành công! Đã đọc được {len(noi_dung)} ký tự từ {file}.\n")
            print(noi_dung[:300]) 
            print("...")
        else:
            print(f"-> Bỏ qua file: {file} (Không có nội dung hoặc không hỗ trợ).\n")
        
