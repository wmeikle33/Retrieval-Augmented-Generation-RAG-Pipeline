import re
import unicodedata


def normalize_text(text: str) -> str:
    # normalize unicode
    text = unicodedata.normalize("NFKC", text)

    # remove weird whitespace
    text = re.sub(r"\s+", " ", text)

    # normalize quotes
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("’", "'")

    # normalize line breaks
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()