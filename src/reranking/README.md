## src/reranking

Purpose:
Loads preprocessed documents and parses them

Inputs:
- Already preprocessed documents

Outputs:
- Document objects

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