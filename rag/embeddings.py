"""
Embedding helpers — supports both Anthropic (claude-3-haiku) and Ollama.
Chosen via EMBEDDING_MODEL env var: "claude" or "ollama".
"""

from __future__ import annotations

import os
from typing import Protocol

from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "claude")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "llama3.2")


class EmbeddingFunction(Protocol):
    def __call__(self, texts: list[str]) -> list[list[float]]: ...


def get_langchain_embeddings():
    """Return a LangChain-compatible embeddings object."""
    if EMBEDDING_MODEL == "ollama":
        from langchain_community.embeddings import OllamaEmbeddings
        return OllamaEmbeddings(
            base_url=OLLAMA_BASE_URL,
            model=OLLAMA_EMBED_MODEL,
        )
    else:
        # Use ChromaDB's default ONNX-based embeddings wrapped for LangChain.
        # This avoids PyTorch and sentence-transformers version conflicts.
        from langchain_chroma import Chroma
        from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

        class ChromaDefaultLangchainEmbeddings:
            """Thin wrapper so ChromaDB's default EF works as a LangChain embedder."""
            def __init__(self):
                self._ef = DefaultEmbeddingFunction()

            def embed_documents(self, texts: list[str]) -> list[list[float]]:
                return self._ef(texts)

            def embed_query(self, text: str) -> list[float]:
                return self._ef([text])[0]

        return ChromaDefaultLangchainEmbeddings()


def get_chroma_embeddings():
    """Return a ChromaDB-compatible embedding function (or None for default)."""
    if EMBEDDING_MODEL == "ollama":
        import chromadb.utils.embedding_functions as ef
        return ef.OllamaEmbeddingFunction(
            url=f"{OLLAMA_BASE_URL}/api/embeddings",
            model_name=OLLAMA_EMBED_MODEL,
        )
    else:
        # ChromaDB default = all-MiniLM-L6-v2 via onnxruntime (no torch needed)
        return None
