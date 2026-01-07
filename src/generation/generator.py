import ollama

MAX_CONTEXT_CHUNKS = 3

def trim_context(context_chunks, max_chunks=MAX_CONTEXT_CHUNKS):
    """Limit context by number of chunks."""
    return context_chunks[:max_chunks]

def generate_answer(query, context_chunks):
    if not context_chunks:
        return "I don't know"

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a retrieval-augmented assistant.

Rules:
- Use ONLY the provided context
- Do NOT mix domains
- Do NOT combine information from multiple rows
- Answer ONLY using one row that matches the query
- On not explicitly mantion entire row if you can answer using value of that key
- If multiple rows match, list them separately
- If the answer is not explicitly present, say "I don't know"
- Do NOT infer or assume
- Keep the answer short and factual

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0.2,
            "num_predict": 256
        }
    )

    return response["message"]["content"].strip()
