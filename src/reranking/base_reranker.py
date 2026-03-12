class BaseReranker:
    def rerank(self, query, documents):
        raise NotImplementedError