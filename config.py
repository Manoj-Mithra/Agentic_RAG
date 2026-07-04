from __future__ import annotations

import os
from pathlib import Path

from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parent
STORAGE_DIR = BASE_DIR / "storage"
CHROMA_DIR = STORAGE_DIR / "chroma"
CACHE_DIR = STORAGE_DIR / "cache"
MODEL_CACHE_DIR = CACHE_DIR / "models"
UPLOAD_DIR = STORAGE_DIR / "uploads"

os.environ.setdefault("HF_HOME", str(MODEL_CACHE_DIR / "huggingface"))
os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", str(MODEL_CACHE_DIR / "sentence-transformers"))
os.environ.setdefault("TRANSFORMERS_CACHE", str(MODEL_CACHE_DIR / "transformers"))
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


class Settings(BaseModel):
    app_name: str = "Local Agentic RAG"
    ollama_model: str = "qwen3:8b"
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    reranker_model: str = "BAAI/bge-reranker-base"
    collection_name: str = "agentic_rag"
    chunk_size: int = 1400
    chunk_overlap: int = 200
    semantic_top_k: int = 15
    bm25_top_k: int = 8
    rerank_top_k: int = 6
    request_timeout: int = 180
    require_citations: bool = True
    use_reranker_by_default: bool = False
    rewrite_queries_by_default: bool = False
    web_search_default: bool = False
    chroma_path: Path = Field(default=CHROMA_DIR)
    model_cache_path: Path = Field(default=MODEL_CACHE_DIR)
    upload_path: Path = Field(default=UPLOAD_DIR)


settings = Settings()


def ensure_storage() -> None:
    for directory in (STORAGE_DIR, CHROMA_DIR, CACHE_DIR, MODEL_CACHE_DIR, UPLOAD_DIR):
        directory.mkdir(parents=True, exist_ok=True)
