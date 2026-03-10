class MarkdownLoader:

    def load(self, path):
        with open(path) as f:
            text = f.read()

        return {
            "text": text,
            "metadata": {"source": path, "type": "markdown"}
        }