from __future__ import annotations

from duckduckgo_search import DDGS

from core.schemas import SourceType
from tools.text_splitter import split_text
from retrieval.vector_store import upsert_chunks


def search_web_and_index(query: str, max_results: int = 5) -> int:
    documents = []
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
    except Exception as exc:
        raise RuntimeError(f"DuckDuckGo search failed: {exc}") from exc

    for result in results:
        url = result.get("href") or result.get("url") or ""
        title = result.get("title") or url or "DuckDuckGo result"
        body = result.get("body") or ""
        if body:
            documents.extend(
                split_text(
                    body,
                    source=url or title,
                    source_type=SourceType.WEB_SEARCH,
                    metadata={"url": url, "document_name": title},
                )
            )
    return upsert_chunks(documents)
