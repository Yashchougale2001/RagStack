# from src.db.vector_store import query_chunks

# def retrieve_chunks(collection, query, top_k=3, min_docs=1):
#     results = query_chunks(collection, query, top_k=top_k)
    
#     # Filter out empty chunks
#     filtered = [r for r in results if r.strip()]
    
#     if len(filtered) < min_docs:
#         print("⚠️ Not enough relevant chunks found. Returning empty context.")
#         return []
    
#     return filtered
# from src.db.vector_store import query_chunks


# def retrieve_chunks(collection, query, top_k=3, min_docs=1, min_score=0.30):
#     results = query_chunks(collection, query, top_k=top_k)

#     filtered = []
#     for r in results:
#         text = r.get("text", "")
#         score = r.get("score", 0)

#         if text.strip() and score >= min_score:
#             filtered.append(text)

#     if len(filtered) < min_docs:
#         print("⚠️ Not enough relevant chunks found. Returning empty context.")
#         return []

#     return filtered
from src.db.vector_store import query_chunks
def retrieve_chunks(collection, query, top_k=3, min_docs=1):
    results = query_chunks(collection, query, top_k=top_k)

    filtered = [str(r) for r in results if r]

    if len(filtered) < min_docs:
        print("⚠️ Not enough relevant chunks found.")
        return []

    return filtered

