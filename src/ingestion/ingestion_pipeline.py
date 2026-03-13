from pathlib import Path
from typing import List, Optional
import logging

from src.ingestion.schema import Document
from src.ingestion.directory_loader import load_directory
from src.ingestion.web_loader import load_urls
from src.ingestion.document_loader import TextFolderLoader
from src.ingestion.metadata_extractor import enrich_metadata
from src.ingestion.deduplicator import deduplicate_documents

logger = logging.getLogger(__name__)


class IngestionPipeline:
    def __init__(
        self,
        input_dir: Optional[str] = None,
        urls: Optional[list[str]] = None,
        output_dir: Optional[str] = None,
        deduplicate: bool = True,
    ):
        self.input_dir = input_dir
        self.urls = urls or []
        self.output_dir = output_dir
        self.deduplicate = deduplicate

    def load(self) -> List[Document]:
        documents = []

        if self.input_dir:
            logger.info("Loading documents from directory: %s", self.input_dir)
            documents.extend(load_directory(self.input_dir))

        if self.urls:
            logger.info("Loading documents from URLs")
            documents.extend(load_urls(self.urls))

        return documents

    def attach_metadata(self, documents: List[Document]) -> List[Document]:
        logger.info("Extracting metadata for %d documents", len(documents))
        return [enrich_metadata(doc) for doc in documents]

    def validate(self, documents: List[Document]) -> List[Document]:
        logger.info("Validating documents")
        valid_docs = []

        for doc in documents:
            if doc.content and doc.content.strip():
                valid_docs.append(doc)

        return valid_docs

    def dedup(self, documents: List[Document]) -> List[Document]:
        if not self.deduplicate:
            return documents

        logger.info("Deduplicating %d documents", len(documents))
        return deduplicate_documents(documents)

    def save(self, documents: List[Document]) -> None:
        if not self.output_dir:
            return

        output_path = Path(self.output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        for i, doc in enumerate(documents):
            file_path = output_path / f"doc_{i}.txt"
            file_path.write_text(doc.content, encoding="utf-8")

    def run(self) -> List[Document]:
        logger.info("Starting ingestion pipeline")

        documents = self.load()
        documents = self.attach_metadata(documents)
        documents = self.validate(documents)
        documents = self.dedup(documents)
        self.save(documents)

        logger.info("Finished ingestion pipeline with %d documents", len(documents))
        return documents
