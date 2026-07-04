from __future__ import annotations

import streamlit as st
from sentence_transformers import CrossEncoder

from config import settings
from core.schemas import SearchResult


@st.cache_resource(show_spinner="Loading reranker model…")
def get_reranker() -> CrossEncoder:
    """Load once, persist across all Streamlit reruns and sessions."""
    return CrossEncoder(settings.reranker_model)


def rerank(query: str, results: list[SearchResult], top_k: int | None = None) -> list[SearchResult]:
    if not results:
        return []
    try:
        model = get_reranker()
        pairs = [(query, result.chunk.text) for result in results]
        scores = model.predict(pairs)
        reranked = [
            SearchResult(chunk=result.chunk, score=float(score), retriever=f"{result.retriever}+rerank")
            for result, score in zip(results, scores)
        ]
        return sorted(reranked, key=lambda result: result.score, reverse=True)[: top_k or settings.rerank_top_k]
    except Exception:
        return results[: top_k or settings.rerank_top_k]
