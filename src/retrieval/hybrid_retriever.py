class HybridRetriever:
    def __init__(self, vector_retriever, keyword_retriever):
        self.vector_retriever = vector_retriever
        self.keyword_retriever = keyword_retriever

    def retrieve(self, query, top_k=5):
        vec_results = self.vector_retriever.retrieve(query, top_k=top_k)
        kw_results = self.keyword_retriever.retrieve(query, top_k=top_k)
        return self.merge_results(vec_results, kw_results)[:top_k]

    def merge_results(self, vec_results, kw_results):
        return vec_results + kw_results