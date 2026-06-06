# rag.py
import requests
from core.retriever import retrieve

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask(question: str) -> str:
    # Bước 1: Lấy context từ ChromaDB
    chunks = retrieve(question, top_k=3)
    context = "\n\n".join(chunks)

    # Bước 2: Ghép prompt
    prompt = f"""Bạn là trợ lý tư vấn sản phẩm trang sức.
Dựa vào thông tin sản phẩm dưới đây để trả lời câu hỏi của khách hàng.
Chỉ trả lời dựa trên thông tin được cung cấp, không tự bịa thêm.

=== THÔNG TIN SẢN PHẨM ===
{context}

=== CÂU HỎI ===
{question}

=== TRẢ LỜI ==="""

    # Bước 3: Gửi cho Mistral
    response = requests.post(OLLAMA_URL, json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]


# Test thử
if __name__ == "__main__":
    while True:
        question = input("\n🧑 Bạn hỏi: ")
        if question.lower() in ["exit", "quit"]:
            break
        answer = ask(question)
        print(f"\n🤖 Mistral: {answer}")