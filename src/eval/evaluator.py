# src/eval/evaluator.py
def is_answer_grounded(answer, context_chunks):
    """
    Simple metric: checks if words in answer appear in context chunks.
    Returns True if grounded, False otherwise.
    """
    context_text = " ".join(context_chunks).lower()
    words = [w for w in answer.lower().split() if len(w) > 3]
    matched = sum(1 for w in words if w in context_text)
    score = matched / (len(words) or 1)  # fraction of words grounded
    return score  # 0-1
