import yaml
from src.db.vector_store import create_vector_store, add_chunks_to_db
from src.loader.loader import load_text, load_csv_as_text, chunk_text
from src.retrieval.retriever import retrieve_chunks
from src.generation.generator import generate_answer
from src.eval.evaluator import evaluate_answer

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Initialize vector store
collection = create_vector_store(embedding_model=config["embedding_model"])

# QA loop
while True:
    query = input("\nAsk a question (type 'exit' to quit): ")
    if query.lower() == "exit":
        break

    context = retrieve_chunks(
        collection,
        query,
        top_k=config["top_k"],
        min_docs=config["min_docs"]
    )

    answer = generate_answer(query, context)
    verdict = evaluate_answer(answer, context)

    print("\nAnswer:")
    print(answer)
    print("\nConfidence:", verdict)

    if context:
        print("\nSources:")
        for i, chunk in enumerate(context):
            print(f"[{i}] {chunk[:100]}...")
