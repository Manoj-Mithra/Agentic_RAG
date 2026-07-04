from __future__ import annotations

from agent.evaluator import INSUFFICIENT, enforce_grounding, self_check
from models.llm import invoke_llm
from core.prompts import ANSWER_TEMPLATE, SYSTEM_GROUNDING_RULES
from core.schemas import AgentAnswer, SearchResult
from retrieval.citation_builder import build_citations, format_context


def generate_answer(question: str, context: list[SearchResult]) -> AgentAnswer:
    citations = build_citations(context)
    if not context:
        return AgentAnswer(
            answer=INSUFFICIENT,
            citations=[],
            context=[],
            self_check=self_check(INSUFFICIENT, [], []),
        )

    prompt = ANSWER_TEMPLATE.format(question=question, context=format_context(context))
    try:
        raw_answer = invoke_llm(SYSTEM_GROUNDING_RULES, prompt, temperature=0.1)
    except Exception as exc:
        raw_answer = f"Answer generation failed locally: {exc}"

    answer = enforce_grounding(raw_answer, context, citations)
    return AgentAnswer(
        answer=answer,
        citations=citations,
        context=context,
        self_check=self_check(answer, context, citations),
    )
