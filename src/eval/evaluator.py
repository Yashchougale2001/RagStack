def evaluate_answer(answer, context):
    if "I don't know" in answer:
        return "NO_ANSWER"

    if not context:
        return "UNFAITHFUL"

    overlap = sum(
        1 for c in context
        if any(word.lower() in c.lower() for word in answer.split())
    )

    if overlap == 0:
        return "UNFAITHFUL"

    if len(answer.split()) < 5:
        return "LOW_CONFIDENCE"

    return "OK"
