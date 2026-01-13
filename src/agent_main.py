from src.agent.privacy_rag_agent import PrivacyAgent
from src.generation.generator import generate_answer
from src.retrieval.retriever import retrieve_chunks
from src.ingest import collection

privacy_agent = PrivacyAgent()

while True:
    query = input("\nAsk a question (type 'q' to quit): ")
    if query.lower() == "q":
        break

    context = retrieve_chunks(collection, query, top_k=2, min_docs=1)
    raw_answer = generate_answer(query, context)

    safe_answer, score, report_path = privacy_agent.run(
        query=query,
        rag_answer=raw_answer,
        retrieved_chunks=context
    )

    print("\n--- FINAL ANSWER (SAFE) ---")
    print(safe_answer)

    print(f"\nPrivacy Risk Score: {score}")
    print(f"Report Saved: {report_path}")
