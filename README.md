## Retrieval-Augmented-Generation-RAG-Pipeline

This is a Python-based Retrieval-Augmented Generation pipeline for ingesting documents, chunking text, creating embeddings, retrieving relevant context, and generating grounded answers with source citations.

## What This Project Does

```bash

1. Load documents from data/raw/ or data/sample_docs/
2. Parse and clean document text
3. Split documents into chunks
4. Generate embeddings
5. Store chunks in a vector index
6. Retrieve relevant chunks for a user query
7. Generate an answer using retrieved context
8. Return the answer with source references

```

## Repo Structure

``` bash

rag-repo/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env.example
├── configs/
│   ├── app.yaml
│   ├── retrieval.yaml
│   └── models.yaml
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample_docs/
├── src/
│   ├── ingestion/
│   ├── parsing/
│   ├── chunking/
│   ├── embeddings/
│   ├── indexing/
│   ├── retrieval/
│   ├── reranking/
│   ├── prompting/
│   ├── generation/
│   ├── evaluation/
│   ├── api/
│   └── utils/
├── scripts/
│   ├── ingest.py
│   ├── build_index.py
│   ├── query.py
│   └── evaluate.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── notebooks/
│   ├── exploration.ipynb
│   └── eval_analysis.ipynb
└── docs/
    ├── architecture.md
    ├── design_decisions.md
    └── troubleshooting.md

```

## Installation

```bash

git clone https://github.com/wmeikle33/Retrieval-Augmented-Generation-RAG-Pipeline.git
cd Retrieval-Augmented-Generation-RAG-Pipeline
python -m venv .venv source .venv/bin/activate
# macOS/Linux # .venv\Scripts\activate
# Windows pip install -r requirements.txt

```

## Environment_Setup

```bash

Environment setup
Create a .env file from the example:
cp .env.example .env
Then add your API keys:
OPENAI_API_KEY=your_api_key_here
VECTOR_DB_PATH=data/processed/vector_index
CHUNK_SIZE=800
CHUNK_OVERLAP=100
TOP_K=5

```
