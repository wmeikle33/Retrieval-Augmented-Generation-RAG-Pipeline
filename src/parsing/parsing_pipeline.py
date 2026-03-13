from pdf_parser import parse_pdf
from markdown_parser import parse_markdown
from html_parser import parse_html
from cleaners import clean_text
from metadata import attach_metadata


def parse_document(file_path):
    if file_path.endswith(".pdf"):
        doc = parse_pdf(file_path)

    elif file_path.endswith(".md"):
        doc = parse_markdown(file_path)

    elif file_path.endswith(".html"):
        doc = parse_html(file_path)

    else:
        raise ValueError("Unsupported file type")

    doc["text"] = clean_text(doc["text"])
    doc = attach_metadata(doc, file_path)

    return doc