from __future__ import annotations

from config import settings
from core.schemas import SearchResult
from retrieval.hybrid_search import hybrid_search
from models.reranker import rerank


def search_local_context(query: str, use_bm25: bool = True) -> list[SearchResult]:
    candidates = hybrid_search(query, use_bm25=use_bm25)
    return rerank(query, candidates, top_k=settings.rerank_top_k)
