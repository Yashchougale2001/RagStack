from src.retrieval.retriever import retrieve_chunks
from src.generation.generator import generate_answer
from src.ingest import collection

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
# from src.retrieval.retriever import retrieve_chunks
# from src.generation.generator import generate_answer
# from src.ingest import collection
# from src.privacy.privacy_meter import evaluate_privacy_risk
# from src.privacy.privacy_report import save_privacy_report



# def format_answer(answer, risk_score):
#     """Formats answer with privacy meter score & warnings."""
#     banner = "=" * 50
#     warning = ""

#     if risk_score >= 0.75:
#         warning = "\n⚠️ HIGH PRIVACY RISK DETECTED — Review your data!\n"
#     elif risk_score >= 0.40:
#         warning = "\n⚠️ MEDIUM PRIVACY RISK — Sensitive patterns found.\n"

#     return f"""\n{banner}
    
# PRIVACY METER SCORE: {risk_score:.2f}
# {warning}
# ANSWER:
# {answer}
# {banner}\n"""


# def main():
#     print("\nRAG System Loaded. Type 'q' to exit.")

#     while True:
#         query = input("\nAsk a question: ").strip()
#         if query.lower() == "q":
#             print("\nExiting RAG...")
#             break

#         # Retrieve relevant chunks
#         context = retrieve_chunks(collection, query, top_k=3, min_docs=1)

#         # If no context retrieved → avoid hallucination
#         if not context or len(context) == 0:
#             print("\n[NO RELEVANT DATA FOUND — Avoiding Hallucination]")
#             print("Try rephrasing your question or ingest more data.")
#             continue

#         # Generate the answer
#         answer = generate_answer(query, context)

#         # Compute privacy score
#         risk_score = evaluate_privacy_risk(query, context, answer)
#         report_file = save_privacy_report(query, answer, context, risk_score)
#         print(f"📄 Privacy report generated: {report_file}")


#         # Print formatted output
#         print(format_answer(answer, risk_score))


# if __name__ == "__main__":
#     main()
# from src.retrieval.retriever import retrieve_chunks
# from src.generation.generator import generate_answer
# from src.ingest import collection
# from src.privacy.privacy_meter import PrivacyMeter
# from src.privacy.privacy_report import save_privacy_report


# def format_answer(answer, risk_score):
#     """Formats answer with privacy meter score & warnings."""
#     banner = "=" * 60
#     warning = ""

#     if risk_score >= 75:  # Updated to match PrivacyMeter 0-100 scoring
#         warning = "\n⚠️ HIGH PRIVACY RISK DETECTED — Sensitive data exposed!\n"
#     elif risk_score >= 40:
#         warning = "\n⚠️ MEDIUM PRIVACY RISK — Potential sensitive items found.\n"

#     return f"""\n{banner}

# PRIVACY METER SCORE: {risk_score:.2f}
# {warning}
# ANSWER:
# {answer}

# {banner}\n"""


# def main():
#     print("\n🔍 RAG System Initialized (with Privacy Meter). Type 'q' to exit.")

#     while True:
#         query = input("\nAsk a question: ").strip()
        
#         if query.lower() == "q":
#             print("\nExiting RAG System...")
#             break

#         # -----------------------------
#         # 1. Retrieve relevant chunks
#         # -----------------------------
#         context_chunks = retrieve_chunks(collection, query, top_k=3, min_docs=1)

#         if not context_chunks:
#             print("\n[NO RELEVANT CONTEXT FOUND — Avoiding Hallucination]")
#             print("Try rephrasing your query or ingest more data.")
#             continue

#         # -----------------------------
#         # 2. Generate answer (using LLM + context)
#         # -----------------------------
#         answer = generate_answer(query, context_chunks)

#         # -----------------------------
#         # 3. Evaluate privacy risk
#         # -----------------------------
#         pm = PrivacyMeter(query, context_chunks)
#         risk_score, pii_data, redacted_chunks = pm.evaluate()

#         # Optionally, you could use redacted_chunks to regenerate the answer if needed
#         # answer = generate_answer(query, redacted_chunks)

#         # -----------------------------
#         # 4. Save privacy report
#         # -----------------------------
#         report_file = save_privacy_report(
#             query=query,
#             answer=answer,
#             context=context_chunks,
#             risk_score=risk_score,
#             pii_data=pii_data
#         )

#         print(f"📄 Privacy Report Saved: {report_file}")

#         # -----------------------------
#         # 5. Display formatted output
#         # -----------------------------
#         print(format_answer(answer, risk_score))


# if __name__ == "__main__":
#     main()
# from src.agent.privacy_rag_agent import PrivacyRAGAgent
# import yaml


# def main():
#     print("\n🔍 Privacy-Aware RAG Agent Ready. Type 'q' to exit.")

#     with open("config.yaml") as f:
#         config = yaml.safe_load(f)

#     agent = PrivacyRAGAgent(config)

#     while True:
#         query = input("\nAsk a question: ").strip()
#         if query.lower() == "q":
#             print("Exiting...")
#             break

#         result = agent.run(query)

#         print("\n==================== RESULT ====================")
#         print("Answer:", result["answer"])
#         print("Privacy Score:", result["risk_score"])
#         print("PII Detected:", result["pii"])
#         print("Report Saved At:", result["report_path"])
#         print("================================================\n")


# if __name__ == "__main__":
#     main()
