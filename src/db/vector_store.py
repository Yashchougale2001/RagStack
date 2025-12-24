import chromadb
from chromadb.utils import embedding_functions

def create_vector_store():
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    client = chromadb.Client()
    collection = client.get_or_create_collection(
        name="knowledge_base",
        embedding_function=embedding_function
    )

    return collection


def add_chunks_to_db(collection, chunks):
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    collection.add(documents=chunks, ids=ids)
    print(f"Stored {len(chunks)} chunks in ChromaDB.")


def query_chunks(collection, query, top_k=3):
    results = collection.query(query_texts=[query], n_results=top_k)
    return results["documents"][0]
