from __future__ import annotations

import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama

from config import settings


@st.cache_resource(show_spinner=False)
def _cached_llm(model: str, temperature: float, timeout: int) -> ChatOllama:
    """Cache the ChatOllama instance — avoids recreating it on every call."""
    return ChatOllama(
        model=model,
        temperature=temperature,
        timeout=timeout,
    )


def get_llm(temperature: float = 0.1) -> ChatOllama:
    return _cached_llm(
        model=settings.ollama_model,
        temperature=temperature,
        timeout=settings.request_timeout,
    )


def invoke_llm(system: str, user: str, temperature: float = 0.1) -> str:
    llm = get_llm(temperature=temperature)
    response = llm.invoke([SystemMessage(content=system), HumanMessage(content=user)])
    return str(response.content).strip()
