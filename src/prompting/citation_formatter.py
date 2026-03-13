def add_citations(text, sources):
    for i, src in enumerate(sources):
        text += f"\n[{i+1}] {src}"
    return text