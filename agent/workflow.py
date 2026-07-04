from __future__ import annotations

from agent.query_rewriter import rewrite_query
from agent.response_generator import generate_answer
from agent.router import route
from core.schemas import AgentAnswer, Intent
from ingest.index_documents import index_url
from tools.web_search import search_web_and_index
from retrieval.search import search_local_context
from retrieval.vector_store import collection_count


def answer_question(question: str, allow_web_search: bool = False, use_bm25: bool = True) -> AgentAnswer:
    decision = route(question, allow_web_search=allow_web_search)

    for url in decision.urls:
        index_url(url)

    rewritten = rewrite_query(question)

    if decision.intent == Intent.SEARCH_WEB and allow_web_search:
        search_web_and_index(rewritten)

    if collection_count() == 0:
        return generate_answer(question, [])

    context = search_local_context(rewritten, use_bm25=use_bm25)
    return generate_answer(question, context)
