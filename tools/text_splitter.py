from __future__ import annotations

import hashlib
from typing import Iterable

from config import settings
from core.schemas import DocumentChunk, SourceType


def _stable_id(source: str, index: int, text: str) -> str:
    digest = hashlib.sha1(f"{source}:{index}:{text[:120]}".encode("utf-8")).hexdigest()
    return digest[:16]


def split_text(
    text: str,
    source: str,
    source_type: SourceType,
    metadata: dict | None = None,
    chunk_size: int | None = None,
    chunk_overlap: int | None = None,
) -> list[DocumentChunk]:
    clean = " ".join(text.split())
    if not clean:
        return []

    size = chunk_size or settings.chunk_size
    overlap = chunk_overlap or settings.chunk_overlap
    chunks: list[DocumentChunk] = []
    start = 0
    index = 0

    while start < len(clean):
        end = min(start + size, len(clean))
        if end < len(clean):
            boundary = clean.rfind(" ", start, end)
            if boundary > start + size // 2:
                end = boundary
        chunk_text = clean[start:end].strip()
        if chunk_text:
            base_metadata = dict(metadata or {})
            base_metadata["chunk_index"] = index
            chunk_id = _stable_id(source, index, chunk_text)
            chunks.append(
                DocumentChunk(
                    id=chunk_id,
                    text=chunk_text,
                    source=source,
                    source_type=source_type,
                    metadata=base_metadata,
                )
            )
        index += 1
        if end >= len(clean):
            break
        start = max(end - overlap, start + 1)

    return chunks


def split_pages(
    pages: Iterable[tuple[int | None, str]],
    source: str,
    source_type: SourceType,
    metadata: dict | None = None,
) -> list[DocumentChunk]:
    all_chunks: list[DocumentChunk] = []
    for page, text in pages:
        page_metadata = dict(metadata or {})
        if page is not None:
            page_metadata["page"] = page
        page_source = f"{source}#page={page}" if page else source
        all_chunks.extend(split_text(text, page_source, source_type, page_metadata))
    return all_chunks
