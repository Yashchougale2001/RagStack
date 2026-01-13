import re

class PIIDetector:
    def __init__(self):
        self.patterns = {
            "email": re.compile(r"[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}"),
            "phone": re.compile(r"\b(?:\+?\d{1,3})?[-.\s]??\d{3,5}[-.\s]??\d{4,10}\b"),
            "aadhaar": re.compile(r"\b\d{4}\s\d{4}\s\d{4}\b"),
            "pan": re.compile(r"[A-Z]{5}[0-9]{4}[A-Z]"),
            "address": re.compile(r"\b\d{1,3} [A-Za-z ]+ (Street|St|Road|Rd|Nagar|Colony)\b"),
            "name": re.compile(r"\b[A-Za-z]{3,20} [A-Za-z]{3,20}\b")
        }

    def detect(self, text):
        results = {}
        for key, pattern in self.patterns.items():
            matches = pattern.findall(text)
            if matches:
                results[key] = matches
        return results
