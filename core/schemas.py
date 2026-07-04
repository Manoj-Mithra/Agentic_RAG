from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class SourceType(str, Enum):
    LOCAL = "local"
    UPLOAD = "upload"
    URL = "url"
    WEB_SEARCH = "web_search"


class Intent(str, Enum):
    ANSWER = "answer"
    SUMMARIZE = "summarize"
    SEARCH_WEB = "search_web"
    CRAWL_URL = "crawl_url"
    INGEST = "ingest"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class DocumentChunk:
    id: str
    text: str
    source: str
    source_type: SourceType
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SearchResult:
    chunk: DocumentChunk
    score: float
    retriever: str


@dataclass(slots=True)
class Citation:
    label: str
    source: str
    chunk_id: str
    page: int | None = None
    url: str | None = None


@dataclass(slots=True)
class AgentDecision:
    intent: Intent
    needs_retrieval: bool
    allow_web_search: bool
    urls: list[str] = field(default_factory=list)
    reason: str = ""


@dataclass(slots=True)
class AgentAnswer:
    answer: str
    citations: list[Citation]
    context: list[SearchResult]
    self_check: dict[str, bool | str]
