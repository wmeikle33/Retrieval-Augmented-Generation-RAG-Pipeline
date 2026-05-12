@dataclass
class Config:
    # Embeddings
    embedding_provider: str = os.getenv(
        "EMBEDDING_PROVIDER",
        "huggingface",
    )

    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2",
    )
