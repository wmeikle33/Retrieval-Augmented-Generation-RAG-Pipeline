def sentence_chunk(text, max_length=500):
    sentences = text.split(". ")
    chunks = []
    current = ""

    for s in sentences:
        if len(current) + len(s) < max_length:
            current += s + ". "
        else:
            chunks.append(current)
            current = s + ". "

    if current:
        chunks.append(current)

    return chunks