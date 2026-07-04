from __future__ import annotations

from typing import Iterable

import chromadb
import streamlit as st
from chromadb.api.models.Collection import Collection

from config import ensure_storage, settings
from models.embeddings import embed_query, embed_texts
from core.schemas import DocumentChunk, SearchResult, SourceType


@st.cache_resource(show_spinner=False)
def _get_chroma_client() -> chromadb.ClientAPI:
    """Persistent ChromaDB client — created once, reused across all reruns."""
    ensure_storage()
    return chromadb.PersistentClient(path=str(settings.chroma_path))


def get_collection() -> Collection:
    client = _get_chroma_client()
    return client.get_or_create_collection(
        name=settings.collection_name,
        metadata={"hnsw:space": "cosine"},
    )


def upsert_chunks(chunks: Iterable[DocumentChunk]) -> int:
    chunk_list = list(chunks)
    if not chunk_list:
        return 0

    collection = get_collection()
    embeddings = embed_texts([chunk.text for chunk in chunk_list])
    metadatas = []
    for chunk in chunk_list:
        metadata = dict(chunk.metadata)
        metadata.update({"source": chunk.source, "source_type": chunk.source_type.value})
        metadatas.append(metadata)

    collection.upsert(
        ids=[chunk.id for chunk in chunk_list],
        documents=[chunk.text for chunk in chunk_list],
        embeddings=embeddings,
        metadatas=metadatas,
    )

    # Invalidate the BM25 index cache since documents changed
    _invalidate_bm25_cache()
    return len(chunk_list)


def _invalidate_bm25_cache() -> None:
    """Clear the BM25 data cache so next search rebuilds the index."""
    try:
        from retrieval.bm25_search import _get_bm25_data
        _get_bm25_data.clear()
    except Exception:
        pass


def query_chunks(query: str, top_k: int | None = None) -> list[SearchResult]:
    collection = get_collection()
    if collection.count() == 0:
        return []

    results = collection.query(
        query_embeddings=[embed_query(query)],
        n_results=top_k or settings.semantic_top_k,
        include=["documents", "metadatas", "distances"],
    )
    output: list[SearchResult] = []
    ids = results.get("ids", [[]])[0]
    docs = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    for chunk_id, doc, metadata, distance in zip(ids, docs, metadatas, distances):
        source_type = SourceType(metadata.get("source_type", SourceType.LOCAL.value))
        chunk = DocumentChunk(
            id=chunk_id,
            text=doc,
            source=metadata.get("source", "unknown"),
            source_type=source_type,
            metadata=dict(metadata),
        )
        score = 1.0 - float(distance)
        output.append(SearchResult(chunk=chunk, score=score, retriever="semantic"))
    return output


def list_all_chunks(limit: int = 10_000) -> list[DocumentChunk]:
    collection = get_collection()
    if collection.count() == 0:
        return []
    data = collection.get(limit=limit, include=["documents", "metadatas"])
    chunks: list[DocumentChunk] = []
    for chunk_id, doc, metadata in zip(data["ids"], data["documents"], data["metadatas"]):
        source_type = SourceType(metadata.get("source_type", SourceType.LOCAL.value))
        chunks.append(
            DocumentChunk(
                id=chunk_id,
                text=doc,
                source=metadata.get("source", "unknown"),
                source_type=source_type,
                metadata=dict(metadata),
            )
        )
    return chunks


def collection_count() -> int:
    return get_collection().count()
