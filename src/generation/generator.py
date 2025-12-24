from transformers import pipeline

# CPU-friendly LLM
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    max_length=256
)

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{query}
"""
    response = generator(prompt)
    return response[0]["generated_text"]
