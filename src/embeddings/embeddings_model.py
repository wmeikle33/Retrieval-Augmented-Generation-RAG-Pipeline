class BaseEmbeddingModel:
    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError