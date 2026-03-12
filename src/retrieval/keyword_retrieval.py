class KeywordRetriever:
    def __init__(self, bm25_index):
        self.bm25_index = bm25_index

    def retrieve(self, query, top_k=5):
        return self.bm25_index.search(query, k=top_k)