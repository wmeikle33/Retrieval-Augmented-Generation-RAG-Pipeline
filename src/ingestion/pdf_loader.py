from pypdf import PdfReader

class PDFLoader:

    def load(self, path):
        reader = PdfReader(path)
        text = "\n".join(page.extract_text() for page in reader.pages)

        return {
            "text": text,
            "metadata": {"source": path, "type": "pdf"}
        }
