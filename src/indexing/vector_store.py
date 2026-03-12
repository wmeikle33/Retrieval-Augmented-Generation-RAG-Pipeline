class VectorStore:
    def add(self, embeddings, metadata):
        raise NotImplementedError

    def search(self, query_vector, k=5):
        raise NotImplementedError