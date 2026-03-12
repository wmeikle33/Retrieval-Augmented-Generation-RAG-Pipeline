class Embedder:

    def __init__(self, model):
        self.model = model

    def embed_text(self, text):
        return self.model.embed([text])[0]