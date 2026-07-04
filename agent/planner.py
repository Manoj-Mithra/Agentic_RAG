from __future__ import annotations

from core.schemas import AgentDecision, Intent


def plan_retrieval(intent: Intent, allow_web_search: bool, urls: list[str]) -> list[str]:
    steps = ["rewrite query", "search local vector database", "optionally run BM25", "rerank context"]
    if urls:
        steps.insert(0, "crawl user-provided URL")
    if intent == Intent.SEARCH_WEB and allow_web_search:
        steps.insert(0, "run DuckDuckGo web search")
    return steps


def make_decision(intent: Intent, allow_web_search: bool, urls: list[str]) -> AgentDecision:
    return AgentDecision(
        intent=intent,
        needs_retrieval=True,
        allow_web_search=allow_web_search,
        urls=urls,
        reason=", ".join(plan_retrieval(intent, allow_web_search, urls)),
    )
