class Redactor:
    def __init__(self, placeholder="[REDACTED]"):
        self.placeholder = placeholder

    def redact(self, text, pii_dict):
        for key, values in pii_dict.items():
            for val in values:
                text = text.replace(val, self.placeholder)
        return text
