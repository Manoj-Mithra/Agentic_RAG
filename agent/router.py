from __future__ import annotations

import re

from core.schemas import AgentDecision, Intent


# ── Intent classification (pattern-based) ──

WEB_PATTERNS = (
    "search the web",
    "browse",
    "look up",
    "check latest",
    "online sources",
    "internet",
)


def classify_intent(question: str) -> Intent:
    query = question.lower()
    if re.search(r"https?://", question):
        return Intent.CRAWL_URL
    if any(pattern in query for pattern in WEB_PATTERNS):
        return Intent.SEARCH_WEB
    if any(word in query for word in ("summarize", "summary", "tl;dr")):
        return Intent.SUMMARIZE
    if any(word in query for word in ("upload", "index this", "add this document")):
        return Intent.INGEST
    return Intent.ANSWER


# ── Routing ──

def extract_urls(text: str) -> list[str]:
    return re.findall(r"https?://[^\s)>\]]+", text)


def route(question: str, allow_web_search: bool = False) -> AgentDecision:
    from agent.planner import make_decision

    intent = classify_intent(question)
    urls = extract_urls(question)
    if intent == Intent.CRAWL_URL:
        allow_web_search = False
    return make_decision(intent, allow_web_search, urls)
