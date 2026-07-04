from __future__ import annotations

from core.schemas import Citation, SearchResult


INSUFFICIENT = "I do not have enough retrieved information to answer that."


def self_check(answer: str, context: list[SearchResult], citations: list[Citation]) -> dict[str, bool | str]:
    has_context = bool(context)
    has_citations = bool(citations)
    insufficient = INSUFFICIENT.lower() in answer.lower()
    has_citation_markers = any(f"[{citation.label}]" in answer for citation in citations)
    grounded = insufficient or (has_context and has_citations and has_citation_markers)
    return {
        "has_context": has_context,
        "has_citations": has_citations,
        "has_citation_markers": has_citation_markers,
        "grounded": grounded,
        "note": "Answer passed citation check." if grounded else "Answer lacked citation grounding.",
    }


def enforce_grounding(answer: str, context: list[SearchResult], citations: list[Citation]) -> str:
    check = self_check(answer, context, citations)
    if not check["grounded"]:
        return INSUFFICIENT
    return answer
