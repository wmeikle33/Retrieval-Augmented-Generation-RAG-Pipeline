def embed_chunks(chunks, embedder):
    texts = [chunk["content"] for chunk in chunks]

    vectors = embedder.embed(texts)

    for chunk, vector in zip(chunks, vectors):
        chunk["embedding"] = vector

    return chunks