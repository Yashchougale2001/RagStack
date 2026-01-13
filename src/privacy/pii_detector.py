import re

class PIIDetector:
    def __init__(self):
        self.patterns = {
            "email": re.compile(r"[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}"),
            "phone": re.compile(r"\b(?:\+?\d{1,3})?[-.\s]??\d{3,5}[-.\s]??\d{4,10}\b"),
            "aadhaar": re.compile(r"\b\d{4}\s\d{4}\s\d{4}\b"),
            "pan": re.compile(r"[A-Z]{5}[0-9]{4}[A-Z]"),
            "address": re.compile(r"\b\d{1,3} [A-Za-z ]+ (Street|St|Road|Rd|Nagar|Colony)\b"),
            "name": re.compile(r"\b[A-Za-z]{3,20} [A-Za-z]{3,20}\b"),
            "patient_id": re.compile(r"\bP\d{3}\b"),  # e.g., P001
            "diagnosis": re.compile(r"[A-Za-z0-9\s\-]+"),  # simple diagnosis words, can be refined
            "admission_date": re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),  # YYYY-MM-DD
            "discharge_date": re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),  # YYYY-MM-DD
            "doctor": re.compile(r"\bDr\. [A-Z][a-z]{2,20}\b"),  # e.g., Dr. Sharma
            "department": re.compile(r"\b[A-Za-z &]+\b"),  # Department names
            "bill_amount": re.compile(r"\b\d{4,6}\b"),  # e.g., 45000
            "date_of_birth": re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),  # e.g., 1975-03-12
            "gender": re.compile(r"\b(M|F)\b"),  # Single-letter gender
        }

    def detect(self, text):
        results = {}
        for key, pattern in self.patterns.items():
            matches = pattern.findall(text)
            if matches:
                results[key] = matches
        return results
