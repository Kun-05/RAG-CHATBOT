def chunk_products(products):
    chunks = []

    for p in products:
        chunk = f"""
Name of product: {p['title']}
Price: {p['price']} VND
Discount: {p['discountPercentage']}%
stockQuantity: {p['stockQuantity']}
description: {p['description']}
"""
        chunks.append(chunk.strip())
    return chunks


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    """Chia văn bản từ PDF thành các đoạn (chunk) với kỹ thuật sliding window."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks