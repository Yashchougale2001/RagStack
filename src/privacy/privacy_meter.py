# src/privacy/privacy_meter.py

from .pii_detector import PIIDetector
from .redactor import Redactor

class PrivacyMeter:
    """
    Class to detect PII, compute privacy risk, and redact sensitive info
    from query and retrieved context chunks.
    """

    def __init__(self, query, retrieved_chunks):
        """
        Initialize with:
        - query: user query string
        - retrieved_chunks: list of retrieved context strings
        """
        self.query = query
        self.retrieved_chunks = retrieved_chunks
        self.detector = PIIDetector()
        self.redactor = Redactor()

    def get_privacy_score(self, text):
        """
        Detect PII in text and calculate a privacy risk score.
        Returns:
        - score: int (0-100)
        - pii: dict of detected PII entities
        """
        pii = self.detector.detect(text)
        count = sum(len(v) for v in pii.values())

        if count == 0:
            return 0, pii

        # Weighted scoring (arbitrary, can tune)
        score = min(100, count * 15)
        return score, pii

    def evaluate(self):
        """
        Main method to evaluate privacy risk for query + context.
        Returns:
        - risk_score: int
        - pii: dict of detected PII
        - redacted_chunks: list of strings with PII redacted
        """
        combined_text = self.query + "\n".join(self.retrieved_chunks)

        # Calculate privacy score
        risk_score, pii = self.get_privacy_score(combined_text)

        # Redact PII in retrieved chunks
        redacted_chunks = [
            self.redactor.redact(chunk, pii) for chunk in self.retrieved_chunks
        ]

        return risk_score, pii, redacted_chunks
