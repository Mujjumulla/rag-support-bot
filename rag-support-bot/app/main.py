from fastapi import FastAPI
from pydantic import BaseModel

from app.crawler import crawl_website
from app.cleaner import clean_text
from app.chunker import chunk_text
from app.embeddings import generate_embeddings, model
from app.vector_store import VectorStore
from app.rag import generate_answer

app = FastAPI(title="RAG Support Bot")

vector_store = None

class QuestionRequest(BaseModel):
    question: str

@app.on_event("startup")
def startup():
    global vector_store

    start_url = "https://example.com"  # CHANGE THIS

    pages = crawl_website(start_url)
    texts = []
    sources = []

    for page in pages:
        cleaned = clean_text(page["text"])
        chunks = chunk_text(cleaned)

        for chunk in chunks:
            texts.append(chunk)
            sources.append(page["url"])

    embeddings = generate_embeddings(texts)
    vector_store = VectorStore(dim=len(embeddings[0]))
    vector_store.add(embeddings, texts, sources)

@app.post("/ask")
def ask_question(req: QuestionRequest):
    query_embedding = model.encode(req.question)
    retrieved = vector_store.search(query_embedding)

    answer, sources = generate_answer(req.question, retrieved)

    return {
        "question": req.question,
        "answer": answer,
        "sources": sources
    }
