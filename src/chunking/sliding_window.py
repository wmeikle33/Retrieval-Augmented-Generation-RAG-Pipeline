def sliding_window(tokens, size=200, overlap=50):
    chunks = []
    step = size - overlap

    for i in range(0, len(tokens), step):
        chunks.append(tokens[i:i+size])

    return chunks