from .openai_embedder import OpenAIEmbedder
from .hf_embedder import HFEmbedder

def get_embedder(config):

    if config["provider"] == "openai":
        return OpenAIEmbedder(config)

    if config["provider"] == "huggingface":
        return HFEmbedder(config)

    raise ValueError("Unknown embedding provider")
