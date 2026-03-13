def batch_texts(texts, batch_size=32):
    for i in range(0, len(texts), batch_size):
        yield texts[i:i+batch_size]
