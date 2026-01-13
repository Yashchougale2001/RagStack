from src.db.vector_store import query_chunks

def retrieve_chunks(collection, query, top_k=3, min_docs=1):
    results = query_chunks(collection, query, top_k=top_k)
    
    # Filter out empty chunks
    filtered = [r for r in results if r.strip()]
    
    if len(filtered) < min_docs:
        print("⚠️ Not enough relevant chunks found. Returning empty context.")
        return []
    
    return filtered
