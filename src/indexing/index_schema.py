from dataclasses import dataclass

@dataclass
class IndexedChunk:
    id: str
    text: str
    embedding: list
    metadata: dict