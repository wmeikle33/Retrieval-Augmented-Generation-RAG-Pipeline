class VectorRetriever:
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query, top_k=5):
        query_vec = self.embedder.embed([query])[0]
        return self.vector_store.search(query_vec, k=top_k)