import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.sources = []

    def add(self, embeddings, texts, sources):
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)
        self.sources.extend(sources)

    def search(self, query_embedding, top_k=5):
        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"), top_k
        )
        results = []
        for i in indices[0]:
            if i < len(self.texts):
                results.append((self.texts[i], self.sources[i]))
        return results
