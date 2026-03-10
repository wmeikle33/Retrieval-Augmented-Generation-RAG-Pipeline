import re


def clean_markdown(md_text: str) -> str:
    text = md_text

    # remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    # remove inline code
    text = re.sub(r"`([^`]*)`", r"\1", text)

    # remove markdown links
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # remove headings symbols
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)

    # remove emphasis
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)

    return text.strip()