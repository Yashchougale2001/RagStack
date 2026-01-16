# from src.retrieval.retriever import retrieve_chunks
# from src.generation.generator import generate_answer
# from src.ingest import collection

# while True:
#     query = input("\nAsk a question (type 'q' to quit): ")
#     if query.lower() == "q":
#         break

#     context = retrieve_chunks(collection, query, top_k=2, min_docs=1)
#     answer = generate_answer(query, context)
    
#     print("\n--Answer--")
#     print(answer)

#     # Optional: show sources
#     # for i, chunk in enumerate(context):
#     #     print(f"[{i}] {chunk[:150]}...")
from src.db.vector_store import create_vector_store
from src.retrieval.retriever import retrieve_chunks
from src.generation.generator import generate_answer

# Load the existing persisted DB
collection = create_vector_store()

while True:
    query = input("\nAsk a question (type 'q' to quit): ")
    if query.lower() == "q":
        break

    context = retrieve_chunks(collection, query, top_k=2, min_docs=1)
    answer = generate_answer(query, context)

    print("\n--Answer--")
    print(answer)
