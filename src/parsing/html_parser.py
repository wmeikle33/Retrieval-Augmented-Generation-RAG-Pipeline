from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Dict


@dataclass
class ParsedDocument:
    doc_id: str
    text: str
    metadata: Dict


def parse_html(html: str, doc_id: str) -> ParsedDocument:
    soup = BeautifulSoup(html, "html.parser")

    # remove unwanted tags
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    metadata = {
        "title": soup.title.string if soup.title else None
    }

    return ParsedDocument(
        doc_id=doc_id,
        text=text.strip(),
        metadata=metadata
    )