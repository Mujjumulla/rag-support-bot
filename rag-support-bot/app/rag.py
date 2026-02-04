from app.embeddings import model

def generate_answer(question, retrieved_chunks):
    if not retrieved_chunks:
        return "Answer not found in documentation.", []

    context = "\n\n".join([c[0] for c in retrieved_chunks])
    sources = list(set([c[1] for c in retrieved_chunks]))

    # Simple extractive answer (NO hallucination)
    answer = f"Based on the documentation:\n{context[:800]}"

    return answer, sources
