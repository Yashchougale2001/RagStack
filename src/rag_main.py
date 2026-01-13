# rag_main.py

from src.retrieval.retriever import retrieve_chunks
from src.generation.generator import generate_answer
from src.ingest import collection
from src.privacy.privacy_meter import PrivacyMeter
from src.privacy.privacy_report import save_privacy_report


def safe_answer(answer: str) -> bool:
    """Hard filter to prevent hallucinations."""
    bad_phrases = [
        "here is an example",
        "for example",
        "sure, here",
        "based on the provided context"  # LLM fallback pattern
    ]
    answer_lower = answer.lower()
    return not any(p in answer_lower for p in bad_phrases)


def main():
    print("\n🔍 Strict RAG System (Zero-Hallucination Mode). Type 'q' to exit.")

    while True:
        query = input("\nAsk a question: ").strip()

        if query.lower() == "q":
            print("Exiting...")
            break

        # 1. Retrieve relevant chunks
        context_chunks = retrieve_chunks(collection, query, top_k=3, min_docs=1, min_score=0.30)

        if not context_chunks:
            print("\n❌ No relevant context found — refusing to hallucinate.")
            continue

        # 2. Generate answer from model + chunks
        answer = generate_answer(query, context_chunks)

        # Hallucination guard
        if not safe_answer(answer):
            print("\n❌ Blocked: Model attempted to hallucinate.")
            continue

        # 3. Privacy check
        pm = PrivacyMeter(query, context_chunks)
        risk_score, pii_data, redacted_chunks = pm.evaluate()

        # 4. Save privacy report
        report_path = save_privacy_report(
            query=query,
            answer=answer,
            context=context_chunks,
            risk_score=risk_score,
            pii_data=pii_data
        )

        # 5. Output
        print("\n==================== RESULT ====================")
        print("Answer:", answer)
        print("Privacy Score:", risk_score)
        print("PII Detected:", pii_data)
        print("Report Saved:", report_path)
        print("================================================\n")


if __name__ == "__main__":
    main()
