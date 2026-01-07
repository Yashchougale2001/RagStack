import chromadb
from chromadb.utils import embedding_functions

def create_vector_store(persist_dir="chroma_db", embedding_model="BAAI/bge-small-en-v1.5"):
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=embedding_model
    )

    client = chromadb.PersistentClient(path=persist_dir)

    collection = client.get_or_create_collection(
        name="knowledge_base",
        embedding_function=embedding_function
    )

    return collection

def add_chunks_to_db(collection, chunks, source="csv", domain="hr"):
    if not chunks:
        raise ValueError("No chunks to ingest")

    ids = [f"chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"source": source, "domain": domain} for _ in chunks]

    collection.add(
        documents=chunks,
        metadatas=metadatas,
        ids=ids
    )

    count = collection.count()
    print(f"✅ Stored {count} chunks in ChromaDB with source='{source}' and domain='{domain}'.")

def query_chunks(collection, query, top_k=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    return results["documents"][0]
