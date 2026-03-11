from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Union


@dataclass
class DocumentRef:
    doc_id: str
    source_type: str
    updated_at: datetime


@dataclass
class SourceDocument:
    doc_id: str
    source_type: str
    raw_content: Union[str, bytes]
    mime_type: str
    metadata: Dict[str, Any]
    updated_at: datetime


@dataclass
class IngestionResult:
    processed: int
    skipped: int
    failed: int