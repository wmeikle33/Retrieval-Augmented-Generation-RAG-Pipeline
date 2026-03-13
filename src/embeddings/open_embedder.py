from openai import OpenAI
from .base import BaseEmbedder

class OpenAIEmbedder(BaseEmbedder):

    def __init__(self, config):
        self.client = OpenAI()
        self.model = config["model"]

    def embed_documents(self, texts):

        response = self.client.embeddings.create(
            model=self.model,
            input=texts
        )

        return [e.embedding for e in response.data]

    def embed_query(self, text):
        return self.embed_documents([text])[0]
