import ollama

MAX_CONTEXT_CHUNKS = 3

def generate_answer(query, context_chunks):
    if not context_chunks:
        return "I don't know based on the provided context."

    # Limit to max chunks
    context = "\n\n".join(context_chunks[:MAX_CONTEXT_CHUNKS])

    prompt = f"""
You are a strict retrieval-augmented assistant.

Rules:
- Answer using ONLY the context provided.
- Do NOT add any extra words, greetings, or filler.
- Copy information exactly from the context.
- If the answer is not in the context EXACTLY as asked, respond with:
"I don't know based on the provided context."
- Keep replies factual and short

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.0, "num_predict": 256}
    )

    return response["message"]["content"].strip()
