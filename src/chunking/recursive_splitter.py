def recursive_split(text):
    separators = ["\n\n", "\n", ".", " "]

    for sep in separators:
        parts = text.split(sep)
        if max(len(p) for p in parts) < 500:
            return parts

    return [text]
