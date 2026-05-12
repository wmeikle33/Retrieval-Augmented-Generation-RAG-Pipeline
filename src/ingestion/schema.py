from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ChunkSchema(BaseModel):
    id: str
    text: str
    embedding: List[float]
    metadata: Dict[str, Any]  # Store source, page, author, etc.
    type: Optional[str] = "text" # e.g., text, table, chart
