from __future__ import annotations

from core.schemas import Citation, SearchResult


def build_citations(results: list[SearchResult]) -> list[Citation]:
    citations: list[Citation] = []
    for index, result in enumerate(results, start=1):
        metadata = result.chunk.metadata
        label = f"S{index}"
        citations.append(
            Citation(
                label=label,
                source=metadata.get("document_name") or result.chunk.source,
                page=metadata.get("page"),
                url=metadata.get("url"),
                chunk_id=result.chunk.id,
            )
        )
    return citations


def format_context(results: list[SearchResult]) -> str:
    lines: list[str] = []
    for index, result in enumerate(results, start=1):
        metadata = result.chunk.metadata
        source = metadata.get("document_name") or result.chunk.source
        page = f", page {metadata['page']}" if metadata.get("page") else ""
        url = f", url {metadata['url']}" if metadata.get("url") else ""
        lines.append(f"[S{index}] {source}{page}{url}, chunk {result.chunk.id}\n{result.chunk.text}")
    return "\n\n".join(lines)
