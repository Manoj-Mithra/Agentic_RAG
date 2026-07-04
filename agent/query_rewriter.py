from __future__ import annotations

from models.llm import invoke_llm
from core.prompts import QUERY_REWRITE_TEMPLATE


def rewrite_query(question: str) -> str:
    try:
        rewritten = invoke_llm(
            system="You rewrite user questions into retrieval queries. Return only the query.",
            user=QUERY_REWRITE_TEMPLATE.format(question=question),
            temperature=0.0,
        )
        return rewritten.strip() or question
    except Exception:
        return question
