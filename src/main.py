from src.retrieval.retriever import retrieve_chunks
from src.generation.generator import generate_answer
from src.db.vector_store import create_vector_store
from src.ingest import config

collection = create_vector_store(embedding_model=config["embedding_model"])

while True:
    query = input("\nAsk a question (type 'q' to quit): ")
    if query.lower() == "q":
        break

    context = retrieve_chunks(collection, query, top_k=2, min_docs=1)
    answer = generate_answer(query, context)
    
    print("\n--Answer--")
    print(answer)

    # Optional: show sources
    # for i, chunk in enumerate(context):
    #     print(f"[{i}] {chunk[:150]}...")
