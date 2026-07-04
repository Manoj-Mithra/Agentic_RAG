from __future__ import annotations

from pathlib import Path

import streamlit as st

from agent.workflow import answer_question
from config import ensure_storage, settings
from core.schemas import AgentAnswer, Citation
from ingest.index_documents import index_pdf, index_text, index_url
from ui.styles import get_theme_css

# Emoji avatars
_USER_AVATAR = "👤"
_ASSISTANT_AVATAR = "🤖"


def _init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "last_answer" not in st.session_state:
        st.session_state.last_answer = None


def _save_upload(uploaded_file) -> Path:
    target = settings.upload_path / uploaded_file.name
    target.write_bytes(uploaded_file.getbuffer())
    return target


def _render_citations(citations: list[Citation]) -> None:
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
    st.markdown(get_theme_css(), unsafe_allow_html=True)

    # ── Sidebar — clean: title + sources only ──
    with st.sidebar:
        st.markdown(
            '<p class="app-title">Local Agentic RAG</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="app-subtitle">'
            'Grounded answers from uploaded, crawled, and indexed context.'
            '</p>',
            unsafe_allow_html=True,
        )

        st.markdown('<p class="section-header">Add Sources</p>', unsafe_allow_html=True)

        uploaded = st.file_uploader("PDF upload", type=["pdf"], label_visibility="collapsed")
        if uploaded and st.button("Index PDF", use_container_width=True):
            try:
                path = _save_upload(uploaded)
                count = index_pdf(path)
                st.success(f"Indexed {count} chunks from {uploaded.name}.")
            except Exception as exc:
                st.error(str(exc))

        url = st.text_input("Crawl URL", placeholder="https://example.com/article")
        if url and st.button("Crawl & index", use_container_width=True):
            try:
                count = index_url(url)
                st.success(f"Indexed {count} chunks from URL.")
            except Exception as exc:
                st.error(str(exc))

        pasted = st.text_area("Paste text", height=100, placeholder="Paste content to index…")
        if pasted and st.button("Index text", use_container_width=True):
            try:
                count = index_text(pasted, source="pasted text")
                st.success(f"Indexed {count} chunks.")
            except Exception as exc:
                st.error(str(exc))

    # ── Chat input (page-level, always at bottom) ──
    question = st.chat_input("Ask about your indexed sources…")

    # ── Two-column layout: chat | sources ──
    main_col, source_col = st.columns([0.64, 0.36], gap="large")

    with main_col:
        # Header row with title + settings popover
        title_col, settings_col = st.columns([0.85, 0.15])
        with title_col:
            st.markdown(
                '<p class="main-title">Ask with receipts</p>',
                unsafe_allow_html=True,
            )
        with settings_col:
            with st.popover("⚙️", use_container_width=True):
                st.markdown('<p class="section-header">Settings</p>', unsafe_allow_html=True)
                allow_web_search = st.toggle("Allow web search", value=False)
                use_reranker = st.toggle("Neural reranker", value=False)
                rewrite_queries = st.toggle("LLM query rewrite", value=False)

        # Chat area
        chat_area = st.container(height=480)
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
                    with st.spinner("Retrieving, reranking, and grounding…"):
                        try:
                            result = answer_question(
                                question,
                                allow_web_search=allow_web_search,
                                use_bm25=True,
                                use_reranker=use_reranker,
                                rewrite_queries=rewrite_queries,
                            )
                            st.markdown(result.answer)
                        except Exception as exc:
                            import traceback
                            traceback.print_exc()
                            result = None
                            st.error(f"⚠️ {type(exc).__name__}: {exc}")
                if result:
                    st.session_state.last_answer = result
                    st.session_state.messages.append(
                        {"role": "assistant", "content": result.answer}
                    )

    # ── Right panel: scrollable sources + self-check ──
    with source_col:
        st.markdown('<p class="section-header">Sources</p>', unsafe_allow_html=True)
        sources_box = st.container(height=280)
        with sources_box:
            _render_citations(
                st.session_state.last_answer.citations if st.session_state.last_answer else []
            )

        st.markdown('<p class="section-header">Self-check</p>', unsafe_allow_html=True)
        check_box = st.container(height=180)
        with check_box:
            _render_debug(st.session_state.last_answer)
