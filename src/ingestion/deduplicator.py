import hashlib
from typing import List
from dataclasses import dataclass

@dataclass
class Document:
    content: str
    metadata: dict

def normalize_text(text: str) -> str:
    """
    Normalize text for comparison.
    """
    return " ".join(text.lower().split())

def hash_text(text: str) -> str:
    """
    Create a stable hash of the document.
    """
    normalized = normalize_text(text)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

def remove_exact_duplicates(documents: List[Document]) -> List[Document]:
    """
    Remove documents with identical content.
    """
    seen = set()
    unique_docs = []

    for doc in documents:
        doc_hash = hash_text(doc.content)

        if doc_hash not in seen:
            seen.add(doc_hash)
            unique_docs.append(doc)
