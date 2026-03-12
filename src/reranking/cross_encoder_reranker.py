class CrossEncoderReranker:

    def __init__(self, model):
        self.model = model

    def rerank(self, query, docs):
        pairs = [(query, d["text"]) for d in docs]
        scores = self.model.predict(pairs)

        for d, s in zip(docs, scores):
            d["rerank_score"] = s

        return sorted(docs, key=lambda x: x["rerank_score"], reverse=True)