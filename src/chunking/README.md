## Chunking

Purpose:
Loads parsed documents and chunks them

Inputs:
- Already passed documents

Outputs:
- Chunk objects

Key files:
- docx_parser.py
- html_parser.py
- markdown_cleaner.py
- pdf_parser.py
- text_normalizer.py

Depends on:
- src/utils/

Does not include:
- chunk splitting
- embeddings
- retrieval
