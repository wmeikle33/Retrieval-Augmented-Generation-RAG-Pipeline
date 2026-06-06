from pathlib import Path
import pickle

import faiss
from sentence_transformers import SentenceTransformer


DOCS_DIR = Path("demo/sample_docs")
INDEX_DIR = Path("demo/local_index")
INDEX_DIR.mkdir(parents=True, exist_ok=True)


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")

    chunks = []
    metadata = []

    for path in DOCS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for i, chunk in enumerate(chunk_text(text)):
            chunks.append(chunk)
            metadata.append({"source": str(path), "chunk_id": i})

    embeddings = model.encode(chunks, convert_to_numpy=True, normalize_embeddings=True)

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, str(INDEX_DIR / "index.faiss"))

    with open(INDEX_DIR / "metadata.pkl", "wb") as f:
        pickle.dump({"chunks": chunks, "metadata": metadata}, f)

    print(f"Indexed {len(chunks)} chunks from {len(list(DOCS_DIR.glob('*.md')))} documents.")


if __name__ == "__main__":
