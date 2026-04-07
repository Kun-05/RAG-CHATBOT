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
