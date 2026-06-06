from pathlib import Path
import pickle
import sys

import faiss
from sentence_transformers import SentenceTransformer


INDEX_DIR = Path("demo/local_index")


def main():
    query = " ".join(sys.argv[1:]) or "What is retrieval-augmented generation?"

    model = SentenceTransformer("all-MiniLM-L6-v2")

    index = faiss.read_index(str(INDEX_DIR / "index.faiss"))

    with open(INDEX_DIR / "metadata.pkl", "rb") as f:
        store = pickle.load(f)

    query_embedding = model.encode([query], convert_to_numpy=True, normalize_embeddings=True)

    scores, indices = index.search(query_embedding, k=3)

    print(f"\nQuestion: {query}\n")
    print("Retrieved chunks:\n")

    for rank, idx in enumerate(indices[0], start=1):
        chunk = store["chunks"][idx]
        meta = store["metadata"][idx]

        print(f"[{rank}] Source: {meta['source']} | Chunk: {meta['chunk_id']}")
        print(f"Score: {scores[0][rank - 1]:.4f}")
        print(chunk[:500])
        print("-" * 80)


if __name__ == "__main__":
    main()
