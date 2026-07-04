from __future__ import annotations

import streamlit as st
from sentence_transformers import SentenceTransformer

from config import settings


@st.cache_resource(show_spinner="Loading embedding model…")
def get_embedding_model() -> SentenceTransformer:
    """Load once, persist across all Streamlit reruns and sessions."""
    return SentenceTransformer(settings.embedding_model)


def embed_texts(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []
    model = get_embedding_model()
    vectors = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
    return vectors.tolist()


def embed_query(text: str) -> list[float]:
    return embed_texts([text])[0]
