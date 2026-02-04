# RAG Support Bot

This project implements a Question & Answer support bot using Retrieval Augmented Generation (RAG).

## Architecture
1. Crawl website pages
2. Clean extracted text
3. Chunk text
4. Generate embeddings
5. Store embeddings in FAISS
6. Retrieve relevant chunks
7. Answer questions strictly from retrieved content

## Tech Stack
- Python
- FastAPI
- BeautifulSoup
- Sentence Transformers
- FAISS

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
