"""Premium dark-mode styling for the Agentic RAG UI.

Uses Söhne (with Inter fallback) for headings and
Tiempos Text (with Lora fallback) for body/subtitle text.
"""

from __future__ import annotations


def get_theme_css() -> str:
    """Return the full CSS block for the dark theme."""
    return """
<style>
/* ── Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap');

:root {
    --bg-primary:   #0a0e14;
    --bg-secondary: #131920;
    --bg-surface:   #1a2130;
    --bg-elevated:  #212b3a;
    --text-primary: #e8edf4;
    --text-secondary: #8b97a8;
    --text-muted:   #5a6577;
    --accent:       #0e9a82;
    --accent-dim:   rgba(14,154,130,.15);
    --border:       rgba(255,255,255,.06);
    --border-light: rgba(255,255,255,.10);
    --glass:        rgba(19,25,32,.85);
    --radius:       12px;
    --radius-sm:    8px;
    --font-heading: 'Söhne', 'Sohne', 'Inter', -apple-system, 'Segoe UI', sans-serif;
    --font-body:    'Tiempos Text', 'Lora', Georgia, 'Times New Roman', serif;
    --font-ui:      'Inter', -apple-system, 'Segoe UI', sans-serif;
}

/* ── Global Reset ── */
html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background-color: var(--bg-primary) !important;
    color: var(--text-primary) !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg-secondary) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * {
    font-family: var(--font-ui) !important;
}

/* ── App Title (Söhne) ── */
.app-title {
    font-family: var(--font-heading) !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: var(--text-primary) !important;
    margin: 0 0 2px 0 !important;
    letter-spacing: -0.02em;
}
.main-title {
    font-family: var(--font-heading) !important;
    font-size: 1.35rem !important;
    font-weight: 600 !important;
    color: var(--text-primary) !important;
    margin: 0 0 2px 0 !important;
    letter-spacing: -0.02em;
}

/* ── App Subtitle (Tiempos Text) ── */
.app-subtitle {
    font-family: var(--font-body) !important;
    font-size: 0.85rem !important;
    font-style: italic !important;
    color: var(--text-secondary) !important;
    margin: 0 0 16px 0 !important;
    line-height: 1.4;
}

/* ── Section Headers ── */
.section-header {
    font-family: var(--font-ui) !important;
    font-size: 0.7rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    color: var(--text-muted) !important;
    margin: 0 0 8px 0 !important;
}

/* ── Chat messages — dark backgrounds ── */
[data-testid="stChatMessage"] {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 14px 18px !important;
    margin-bottom: 10px !important;
}
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] span {
    color: var(--text-primary) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.92rem !important;
    line-height: 1.6 !important;
}

/* ── Chat container ── */
[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--bg-primary) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}

/* ── Chat input ── */
[data-testid="stChatInput"] {
    background: var(--bg-secondary) !important;
    border-top: 1px solid var(--border) !important;
}
[data-testid="stChatInput"] textarea {
    background: var(--bg-surface) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--radius) !important;
    font-family: var(--font-ui) !important;
}

/* ── Source Cards ── */
.source-card {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--radius-sm) !important;
    padding: 12px 14px !important;
    margin-bottom: 8px !important;
    transition: border-color 0.2s ease;
}
.source-card:hover {
    border-color: var(--accent) !important;
}
.source-card strong {
    color: var(--text-primary) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
}
.source-card small {
    color: var(--text-muted) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.72rem !important;
}

/* ── Self-check rows ── */
.check-row {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 4px 0;
    font-family: var(--font-ui) !important;
    font-size: 0.82rem !important;
}
.check-icon { font-size: 0.9rem; }
.check-label { color: var(--text-secondary); flex: 1; }
.check-value { font-weight: 600; }
.check-pass  { color: var(--accent); }
.check-fail  { color: #e85d5d; }
.check-note {
    margin-top: 8px;
    padding: 8px 12px;
    border-radius: var(--radius-sm);
    font-family: var(--font-ui);
    font-size: 0.8rem;
}
.check-note.grounded {
    background: var(--accent-dim);
    color: var(--accent);
    border: 1px solid rgba(14,154,130,.25);
}
.check-note.ungrounded {
    background: rgba(232,93,93,.1);
    color: #e85d5d;
    border: 1px solid rgba(232,93,93,.2);
}

/* ── Buttons ── */
.stButton > button {
    background: var(--bg-elevated) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--radius-sm) !important;
    font-family: var(--font-ui) !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: var(--accent-dim) !important;
    border-color: var(--accent) !important;
    color: var(--accent) !important;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    background: var(--bg-surface) !important;
    border: 1px dashed var(--border-light) !important;
    border-radius: var(--radius-sm) !important;
}

/* ── Text inputs & areas ── */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    background: var(--bg-surface) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--radius-sm) !important;
    font-family: var(--font-ui) !important;
}

/* ── Popover (Settings kebab menu) ── */
[data-testid="stPopover"] > div {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border-light) !important;
    border-radius: var(--radius) !important;
}

/* ── Toggle styling ── */
[data-testid="stToggle"] label span {
    font-family: var(--font-ui) !important;
    font-size: 0.82rem !important;
    color: var(--text-secondary) !important;
}

/* ── Dividers ── */
hr {
    border-color: var(--border) !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: var(--text-muted);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover { background: var(--text-secondary); }

/* ── Spinner ── */
[data-testid="stSpinner"] {
    color: var(--accent) !important;
}
[data-testid="stSpinner"] > div {
    font-family: var(--font-ui) !important;
    color: var(--text-secondary) !important;
}

/* ── Expander ── */
details {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
}
details summary {
    font-family: var(--font-ui) !important;
    font-size: 0.82rem !important;
    color: var(--text-secondary) !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden !important; height: 0 !important; }
</style>
"""
