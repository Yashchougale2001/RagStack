# src/agents/privacy_agent.py

from src.privacy.privacy_meter import PrivacyMeter
from src.privacy.privacy_report import save_privacy_report

class PrivacyAgent:
    """
    Post-RAG agent that evaluates sensitive data risk, 
    redacts PII, and generates a structured privacy report.
    """

    def __init__(self):
        pass

    def run(self, query, rag_answer, retrieved_chunks):
        """
        Executes privacy evaluation pipeline.
        Returns:
            - safe_answer (string)
            - risk_score (int)
            - report_path (string)
        """

        # 1️⃣ Detect PII + risk score + redacted context
        meter = PrivacyMeter(query, retrieved_chunks)
        risk_score, pii, redacted_chunks = meter.evaluate()

        # 2️⃣ If PII detected → redact answer too
        safe_answer = rag_answer
        if pii:
            print("⚠️ Sensitive data detected. Redacting output...")
            for key, vals in pii.items():
                for v in vals:
                    safe_answer = safe_answer.replace(v, "[*****]")

        # 3️⃣ Save full report
        report_path = save_privacy_report(
            query=query,
            answer=safe_answer,
            context=redacted_chunks,
            risk_score=risk_score,
            pii_data=pii
        )

        return safe_answer, risk_score, report_path
