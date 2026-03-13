from sentence_transformers import SentenceTransformer
from .base import BaseEmbedder

class HFEmbedder(BaseEmbedder):

    def __init__(self, config):
        self.model = SentenceTransformer(config["model"])

    def embed_documents(self, texts):
        return self.model.encode(texts, normalize_embeddings=True)

    def embed_query(self, text):
        return self.embed_documents([text])[0]
