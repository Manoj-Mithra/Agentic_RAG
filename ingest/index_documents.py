from __future__ import annotations

from pathlib import Path

from core.schemas import SourceType
from tools.pdf_loader import load_pdf
from tools.text_splitter import split_text
from tools.web_crawler import crawl_url
from retrieval.vector_store import upsert_chunks


def index_pdf(path: str | Path) -> int:
    return upsert_chunks(load_pdf(path))


def index_text(text: str, source: str = "pasted text") -> int:
    chunks = split_text(text, source=source, source_type=SourceType.LOCAL, metadata={"document_name": source})
    return upsert_chunks(chunks)


def index_url(url: str) -> int:
    return upsert_chunks(crawl_url(url))
