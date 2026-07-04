from __future__ import annotations

import trafilatura

from core.schemas import DocumentChunk, SourceType
from tools.text_splitter import split_text


def crawl_url(url: str) -> list[DocumentChunk]:
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            raise RuntimeError("empty response")
        text = trafilatura.extract(downloaded, include_comments=False, include_tables=True)
    except Exception as exc:
        raise RuntimeError(f"Could not crawl URL '{url}': {exc}") from exc

    if not text:
        raise RuntimeError(f"No readable text extracted from '{url}'")

    return split_text(
        text,
        source=url,
        source_type=SourceType.URL,
        metadata={"url": url, "document_name": url},
    )
