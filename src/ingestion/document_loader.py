class TextFolderLoader:
    def __init__(self, docuemnt: str, encoding: str = "utf-8", pattern: str = "*.txt") -> None:
        loader = PyPDFLoader(file_path)
        return loader.load() 
