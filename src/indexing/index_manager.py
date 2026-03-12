class IndexManager:

    def __init__(self, vector_store):
        self.store = vector_store

    def rebuild(self, chunks):
        self.store.clear()
        self.store.add(chunks)