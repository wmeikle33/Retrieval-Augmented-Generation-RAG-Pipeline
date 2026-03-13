## src/ingestion

Purpose:
Loads raw documents from source systems and normalizes them.

Inputs:
- local files
- URLs
- API responses

Outputs:
- Document objects

Key files:
- directory_loader.py
- web_loader.py
- metadata_extractor.py
- deduplicator.py
- ingestion_pipeline.py

Depends on:
- src/utils/

Does not include:
- chunk splitting
- embeddings
- retrieval