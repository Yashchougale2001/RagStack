from src.db.vector_store import query_chunks

# Optional threshold or top_k adjustments
def retrieve_chunks(collection, query, top_k=3, similarity_threshold=0.4):
    chunks = query_chunks(collection, query, top_k=top_k)
    # Currently Chroma handles similarity ranking internally
    return chunks
