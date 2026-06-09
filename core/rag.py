# rag.py
import requests
import json
from core.retriever import retrieve

OLLAMA_URL = "http://localhost:11434/api/generate"

def build_prompt(question: str, context: str) -> str:
    return f"""Bạn là một nhân viên phục vụ (Barista) nhiệt tình và am hiểu về cà phê tại quán.
Dựa vào Menu và thông tin sản phẩm trong phần "TÀI LIỆU" dưới đây, hãy tư vấn cho khách hàng.

QUY TẮC BẮT BUỘC:
1. LUÔN LUÔN trả lời bằng Tiếng Việt thân thiện, lịch sự.
2. Nếu khách hỏi món không có trong Menu, hãy nói xin lỗi và gợi ý một món đồ uống khác tương tự có trong Menu.
3. Có thể chủ động hỏi khách muốn uống size nào (S/M/L) hoặc có thêm topping (trân châu, kem cheese) không nếu phù hợp.

=== TÀI LIỆU (MENU QUÁN) ===
{context}

=== CÂU HỎI CỦA KHÁCH ===
{question}

Tư vấn của bạn:"""

def ask(question: str) -> str:
    # Bước 1: Lấy context từ CustomVectorDB
    chunks = retrieve(question, top_k=3)
    context = "\n\n".join(chunks)

    # Bước 2: Ghép prompt
    prompt = build_prompt(question, context)

    # Bước 3: Gửi cho Mistral
    response = requests.post(OLLAMA_URL, json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]
def ask_stream(question: str):
    chunks = retrieve(question, top_k=3)
    context = "\n\n".join(chunks)

    prompt = build_prompt(question, context)

    # Gửi request yêu cầu Ollama trả về dạng Stream
    response = requests.post(OLLAMA_URL, json={
        "model": "mistral",
        "prompt": prompt,
        "stream": True # Bật stream ở phía Ollama
    }, stream=True) # Bật stream ở phía thư viện requests

    # Đọc từng dòng dữ liệu Ollama đẩy về
    for line in response.iter_lines():
        if line:
            # Giải mã chuỗi JSON từ bytes
            chunk_data = json.loads(line.decode("utf-8"))
            if "response" in chunk_data:
                # Bắn từng chữ ra ngoài cho FastAPI
                yield chunk_data["response"]  


# Test thử
if __name__ == "__main__":
    print("\n--- TEST STREAMING ---")
    while True:
        question = input("\n🧑 Bạn hỏi: ")
        if question.lower() in ["exit", "quit"]:
            break
            
        print("\n🤖 Mistral: ", end="", flush=True)
        # Gọi thử hàm stream để xem chữ chạy ra trên terminal
        for word in ask_stream(question):
            print(word, end="", flush=True)
        print()