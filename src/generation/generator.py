import ollama

MAX_CONTEXT_CHUNKS = 3

def generate_answer(query, context_chunks):
    if not context_chunks:
        return "I don't know based on the provided context."

    # Limit to max chunks
    context = "\n\n".join(context_chunks[:MAX_CONTEXT_CHUNKS])

    prompt = f"""
You are a strict RAG assistant. 
Rules:
1. ONLY answer using the provided context.
2. If the context does not contain the answer, reply exactly:
   "I don't know based on the provided context."
3. NEVER add examples, extra content, assumptions, or fabricated details.
4. Do not guess. Do not generalize.

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
