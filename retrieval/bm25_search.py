from __future__ import annotations

import streamlit as st
from rank_bm25 import BM25Okapi

from core.schemas import DocumentChunk, SearchResult
from retrieval.vector_store import list_all_chunks


def _tokenize(text: str) -> list[str]:
    return [token.lower() for token in text.split() if token.strip()]


@st.cache_resource(show_spinner=False)
def _get_bm25_data() -> tuple[list[DocumentChunk], BM25Okapi | None]:
    """Cache the full chunk list + BM25 index in memory.
    Rebuilt only when explicitly cleared (by upsert_chunks) or on restart."""
    chunks = list_all_chunks()
    if not chunks:
        return [], None
    corpus = [_tokenize(chunk.text) for chunk in chunks]
    return chunks, BM25Okapi(corpus)


def bm25_search(query: str, top_k: int) -> list[SearchResult]:
    chunks, bm25 = _get_bm25_data()
    if not chunks or bm25 is None:
        return []

    scores = bm25.get_scores(_tokenize(query))
    ranked = sorted(enumerate(scores), key=lambda item: item[1], reverse=True)[:top_k]
    return [
        SearchResult(chunk=chunks[index], score=float(score), retriever="bm25")
        for index, score in ranked
        if score > 0
    ]
