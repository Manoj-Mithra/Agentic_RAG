from __future__ import annotations

from pathlib import Path

import streamlit as st

from agent.workflow import answer_question
from config import ensure_storage, settings
from core.schemas import AgentAnswer, Citation
from ingest.index_documents import index_pdf, index_text, index_url
from ui.styles import get_theme_css

# Emoji avatars — avoids broken Material Symbol ligatures ("face"/"smart_toy")
_USER_AVATAR = "👤"
_ASSISTANT_AVATAR = "🤖"


def _init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "last_answer" not in st.session_state:
        st.session_state.last_answer = None
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"


def _save_upload(uploaded_file) -> Path:
    target = settings.upload_path / uploaded_file.name
    target.write_bytes(uploaded_file.getbuffer())
    return target


def _render_citations(citations: list[Citation]) -> None:
    st.markdown("#### Sources")
    if not citations:
        st.caption("No citations for this turn.")
        return
    for citation in citations:
        page = f" · page {citation.page}" if citation.page else ""
        url_html = f'<br><small>{citation.url}</small>' if citation.url else ""
        st.markdown(
            f'<div class="source-card">'
            f'<strong>[{citation.label}] {citation.source}</strong>{page}<br>'
            f'<small>chunk {citation.chunk_id}</small>{url_html}'
            f'</div>',
            unsafe_allow_html=True,
        )


def _render_debug(answer: AgentAnswer | None) -> None:
    st.markdown("#### Self-check")
    if not answer:
        st.caption("No answer yet.")
        return

    check = answer.self_check
    grounded = check.get("grounded", False)

    items = [
        ("has_context", "Context retrieved"),
        ("has_citations", "Citations built"),
        ("has_citation_markers", "Markers in answer"),
        ("grounded", "Grounded"),
    ]

    for key, label in items:
        value = check.get(key)
        if isinstance(value, bool):
            icon = "✅" if value else "❌"
            css = "check-pass" if value else "check-fail"
            display = "Yes" if value else "No"
        else:
            icon = "ℹ️"
            css = "check-pass"
            display = str(value)

        st.markdown(
            f'<div class="check-row">'
            f'<span class="check-icon">{icon}</span>'
            f'<span class="check-label">{label}</span>'
            f'<span class="check-value {css}">{display}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

    note = check.get("note", "")
    if note:
        note_css = "grounded" if grounded else "ungrounded"
        st.markdown(
            f'<div class="check-note {note_css}">{note}</div>',
            unsafe_allow_html=True,
        )


def render_app() -> None:
    ensure_storage()
    st.set_page_config(page_title=settings.app_name, layout="wide")
    _init_state()
    st.markdown(get_theme_css(st.session_state.theme), unsafe_allow_html=True)

    # ── Sidebar ──
    with st.sidebar:
        st.markdown('<p class="app-title">Local Agentic RAG</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="app-subtitle">Grounded answers from uploaded, crawled, and indexed context.</p>',
            unsafe_allow_html=True,
        )

        # Theme toggle
        is_light = st.toggle(
            "☀️  Light mode" if st.session_state.theme == "dark" else "🌙  Dark mode",
            value=(st.session_state.theme == "light"),
            key="theme_toggle",
        )
        st.session_state.theme = "light" if is_light else "dark"

        allow_web_search = st.toggle("Allow web search for this query", value=False)
        use_bm25 = st.toggle("Use BM25 hybrid retrieval", value=True)
        use_reranker = st.toggle(
            "Use neural reranker (slower)",
            value=settings.use_reranker_by_default,
        )
        rewrite_queries = st.toggle(
            "Rewrite query with LLM (slower)",
            value=settings.rewrite_queries_by_default,
        )

        st.divider()
        st.markdown("#### Add Sources")

        uploaded = st.file_uploader("PDF upload", type=["pdf"])
        if uploaded and st.button("Index PDF", use_container_width=True):
            try:
                path = _save_upload(uploaded)
                count = index_pdf(path)
                st.success(f"Indexed {count} chunks from {uploaded.name}.")
            except Exception as exc:
                st.error(str(exc))

        url = st.text_input("Crawl URL")
        if url and st.button("Crawl and index URL", use_container_width=True):
            try:
                count = index_url(url)
                st.success(f"Indexed {count} chunks from URL.")
            except Exception as exc:
                st.error(str(exc))

        pasted = st.text_area("Paste local text", height=120)
        if pasted and st.button("Index pasted text", use_container_width=True):
            try:
                count = index_text(pasted, source="pasted text")
                st.success(f"Indexed {count} chunks.")
            except Exception as exc:
                st.error(str(exc))

    # ── Chat input at page level ──
    question = st.chat_input("Ask about your indexed sources")

    # ── Two-column layout ──
    main_col, source_col = st.columns([0.66, 0.34], gap="large")

    with main_col:
        st.markdown('<p class="app-title">Ask with receipts</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="app-subtitle">'
            'The model can plan and summarize, but final answers must come from retrieved context.'
            '</p>',
            unsafe_allow_html=True,
        )

        chat_area = st.container(height=460)
        with chat_area:
            for msg in st.session_state.messages:
                _avatar = _USER_AVATAR if msg["role"] == "user" else _ASSISTANT_AVATAR
                with st.chat_message(msg["role"], avatar=_avatar):
                    st.markdown(msg["content"])

            if question:
                st.session_state.messages.append({"role": "user", "content": question})
                with st.chat_message("user", avatar=_USER_AVATAR):
                    st.markdown(question)
                with st.chat_message("assistant", avatar=_ASSISTANT_AVATAR):
                    with st.spinner("Retrieving, reranking, and grounding..."):
                        try:
                            result = answer_question(
                                question,
                                allow_web_search=allow_web_search,
                                use_bm25=use_bm25,
                                use_reranker=use_reranker,
                                rewrite_queries=rewrite_queries,
                            )
                            st.markdown(result.answer)
                        except Exception as exc:
                            import traceback
                            traceback.print_exc()  # print full trace to terminal
                            result = None
                            st.error(f"⚠️ Workflow error: {type(exc).__name__}: {exc}")
                if result:
                    st.session_state.last_answer = result
                    st.session_state.messages.append(
                        {"role": "assistant", "content": result.answer}
                    )

    with source_col:
        _render_citations(
            st.session_state.last_answer.citations if st.session_state.last_answer else []
        )
        st.divider()
        _render_debug(st.session_state.last_answer)
