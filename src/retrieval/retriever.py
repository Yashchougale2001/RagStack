from src.db.vector_store import query_chunks

def retrieve_chunks(collection, query, top_k=3, min_docs=1, similarity_threshold=0.3):
    results = query_chunks(collection, query, top_k=top_k)
    filtered = [r for r in results if r]  # Placeholder for similarity filtering

    if len(filtered) < min_docs:
        print("⚠️ Not enough relevant chunks found.")
        return []

    return filtered
