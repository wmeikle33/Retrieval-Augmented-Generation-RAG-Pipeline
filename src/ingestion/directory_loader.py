from pathlib import Path

def load_directory(path):
    docs = []
    for file in Path(path).glob("**/*.txt"):
        with open(file) as f:
            docs.append({
                "content": f.read(),
                "source": str(file)
            })
    return docs
