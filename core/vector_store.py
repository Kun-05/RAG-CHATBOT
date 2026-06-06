# core/vector_store.py
import json
import math
import os

class CustomVectorDB:
    def __init__(self, db_path="db/vector_db.json"):
        self.db_path = db_path
        self.data = []
        self._load()

    def _load(self):
        """Đọc vector từ file JSON"""
        if os.path.exists(self.db_path):
            with open(self.db_path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = []

    def save(self, embedded_chunks: list[dict]):
        """Lưu thêm các chunk mới vào file JSON"""
        self.data.extend(embedded_chunks)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def cosine_similarity(v1: list[float], v2: list[float]) -> float:
        """Thuật toán Cosine Similarity code from scratch"""
        dot_product = sum(a * b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        if mag1 == 0 or mag2 == 0:
            return 0.0
        return dot_product / (mag1 * mag2)

    def search(self, query_vector: list[float], top_k: int = 3) -> list[str]:
        """Tìm kiếm top_k chunks giống với câu hỏi nhất"""
        scored = []
        for item in self.data:
            sim = self.cosine_similarity(query_vector, item["vector"])
            scored.append((sim, item["text"]))
        
        # Sắp xếp giảm dần theo độ tương đồng (similarity)
        scored.sort(key=lambda x: x[0], reverse=True)
        # Trả về text của top K kết quả
        return [text for sim, text in scored[:top_k]]