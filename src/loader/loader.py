import csv

def load_text(file_path):
    """Load a plain text file and return its content as a single string."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_csv_as_text(file_path, columns=None):
    """Convert CSV rows into structured natural language text."""
    rows_as_text = []

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            parts = []
            for col, val in row.items():
                if val and val.strip():
                    if columns is None or col in columns:
                        parts.append(f"{col}: {val.strip()}")
            if parts:
                rows_as_text.append(" | ".join(parts))

    return "\n".join(rows_as_text)

def chunk_text(text, chunk_size=200, overlap=40):
    """Split the text into chunks of approximately chunk_size words."""
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start += chunk_size - overlap

    return chunks

def chunk_csv_rows(file_path):
    chunks = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            chunk = " | ".join([f"{k}: {v}" for k, v in row.items()])
            chunks.append(chunk)
    return chunks
