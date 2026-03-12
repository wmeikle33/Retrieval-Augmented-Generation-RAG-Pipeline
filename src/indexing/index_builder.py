def build_index(chunks, vector_store):
    texts = [chunk["content"] for chunk in chunks]
    vectors = [chunk["embedding"] for chunk in chunks]
    metadata = [chunk["metadata"] for chunk in chunks]

    vector_store.add(vectors, metadata)