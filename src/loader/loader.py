def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text, chunk_size=100, overlap=20):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks
