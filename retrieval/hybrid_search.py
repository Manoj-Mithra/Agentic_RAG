from __future__ import annotations

from config import settings
from core.schemas import SearchResult
from retrieval.bm25_search import bm25_search
from retrieval.vector_store import query_chunks


def hybrid_search(query: str, use_bm25: bool = True) -> list[SearchResult]:
    combined: dict[str, SearchResult] = {}

    # Semantic search (inlined — was semantic_search.py)
    for result in query_chunks(query, top_k=settings.semantic_top_k):
        combined[result.chunk.id] = result

    if use_bm25:
        for result in bm25_search(query, top_k=settings.bm25_top_k):
            existing = combined.get(result.chunk.id)
            if existing:
                existing.score += result.score / 10.0
                existing.retriever = "hybrid"
            else:
                combined[result.chunk.id] = result

    return sorted(combined.values(), key=lambda result: result.score, reverse=True)
