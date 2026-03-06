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
