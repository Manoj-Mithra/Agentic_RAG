from __future__ import annotations


def dark_theme_css() -> str:
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0&display=swap');

/* ── Dark palette ── */
:root {
  --bg: #0a0e14;
  --bg-subtle: #0d1118;
  --surface: #131920;
  --surface-hover: #1a2130;
  --surface-elevated: #1e2636;
  --border: rgba(255,255,255,.08);
  --border-light: rgba(255,255,255,.05);
  --border-accent: rgba(15,190,160,.25);
  --text: #e8edf4;
  --text-secondary: #b0b8c4;
  --text-muted: #8b949e;
  --text-dim: #5a6370;
  --accent: #0fbea0;
  --accent-soft: rgba(15,190,160,.12);
  --accent-glow: rgba(15,190,160,.25);
  --accent-hover: #12d4b2;
  --accent-gradient: linear-gradient(135deg, #0fbea0, #0ea5e9);
  --danger: #f85149;
  --success: #3fb950;
  --warning: #d29922;
  --info: #58a6ff;
  --radius: 12px;
  --radius-sm: 8px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 2px rgba(0,0,0,.3);
  --shadow: 0 2px 8px rgba(0,0,0,.25), 0 8px 24px rgba(0,0,0,.15);
  --shadow-lg: 0 4px 16px rgba(0,0,0,.3), 0 12px 40px rgba(0,0,0,.2);
  --shadow-glow: 0 0 20px rgba(15,190,160,.15);
  --glass: rgba(19,25,32,.75);
  --glass-border: rgba(255,255,255,.06);
  --transition: all .25s cubic-bezier(.4,0,.2,1);
  --transition-fast: all .15s cubic-bezier(.4,0,.2,1);
}

/* ── Global app ── */
.stApp {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  background: var(--bg) !important;
  color: var(--text) !important;
}

/* ── Header — translucent glass bar (VISIBLE, restores nav + sidebar toggle) ── */
header[data-testid="stHeader"] {
  background: rgba(10,14,20,.80) !important;
  backdrop-filter: blur(16px) saturate(1.4);
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
  border-bottom: 1px solid var(--border) !important;
  height: auto !important;
  min-height: auto !important;
  visibility: visible !important;
  z-index: 999;
}

/* ── Ensure sidebar collapse button is visible and styled ── */
button[data-testid="stSidebarCollapseButton"],
button[data-testid="baseButton-headerNoPadding"] {
  color: var(--text-muted) !important;
  opacity: 1 !important;
  visibility: visible !important;
  transition: var(--transition-fast);
}

button[data-testid="stSidebarCollapseButton"]:hover,
button[data-testid="baseButton-headerNoPadding"]:hover {
  color: var(--accent) !important;
}

.block-container {
  max-width: 1380px;
  padding-top: 1.5rem;
  padding-bottom: .5rem;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
  background: var(--surface) !important;
  border-right: 1px solid var(--border) !important;
  min-width: 280px !important;
  visibility: visible !important;
}

[data-testid="stSidebar"] > div:first-child {
  background: var(--surface) !important;
  padding-top: .8rem;
}

[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  gap: .35rem;
}

/* Sidebar logo / brand area accent line */
[data-testid="stSidebar"]::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: var(--accent-gradient);
  z-index: 10;
}

/* ── Typography hierarchy ── */

/* H1 — App title */
.app-title,
[data-testid="stSidebar"] .app-title,
[data-testid="stColumn"] .app-title,
.stMarkdown .app-title {
  font-family: 'Inter', sans-serif !important;
  font-size: 1.45rem !important;
  font-weight: 700 !important;
  color: #f0f4f8 !important;
  margin: 0 0 .15rem !important;
  letter-spacing: -.025em;
  line-height: 1.3;
  display: block !important;
  background: linear-gradient(135deg, #f0f4f8 40%, var(--accent)) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
}

/* Sidebar title — no gradient, just clean white */
[data-testid="stSidebar"] .app-title {
  background: none !important;
  -webkit-text-fill-color: #f0f4f8 !important;
  font-size: 1.3rem !important;
}

/* H2 — Subtitle */
.app-subtitle,
[data-testid="stSidebar"] .app-subtitle,
[data-testid="stColumn"] .app-subtitle,
.stMarkdown .app-subtitle {
  font-family: 'Inter', sans-serif !important;
  font-size: .88rem !important;
  font-weight: 400 !important;
  color: var(--text-muted) !important;
  margin: 0 0 1rem !important;
  line-height: 1.6;
  display: block !important;
}

/* H4 — Section headers */
h4,
[data-testid="stSidebar"] h4,
[data-testid="stColumn"] h4,
.main h4,
.stMarkdown h4 {
  font-family: 'Inter', sans-serif !important;
  font-weight: 600 !important;
  font-size: .78rem !important;
  letter-spacing: .1em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
  margin-top: .8rem !important;
  margin-bottom: .5rem !important;
  padding-bottom: .3rem;
  border-bottom: 1px solid var(--border);
}

/* All markdown text — force light color */
.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown code,
[data-testid="stColumn"] p,
[data-testid="stColumn"] li {
  color: var(--text) !important;
  font-family: 'Inter', sans-serif !important;
}

/* Body text */
p, label, li {
  font-family: 'Inter', sans-serif !important;
}

/* Captions */
[data-testid="stCaptionContainer"],
.stCaption {
  font-family: 'Inter', sans-serif !important;
  color: var(--text-dim) !important;
  font-size: .8rem;
}

/* ── Main columns panel ── */
[data-testid="stColumn"] > [data-testid="stVerticalBlockBorderWrapper"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
}

/* ── Chat messages — glassmorphism ── */
[data-testid="stChatMessage"] {
  background: var(--glass) !important;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid var(--glass-border) !important;
  border-radius: var(--radius);
  transition: var(--transition);
  animation: messageSlideIn .35s cubic-bezier(.4,0,.2,1);
}

[data-testid="stChatMessage"]:hover {
  border-color: var(--border-accent) !important;
  box-shadow: var(--shadow-glow);
}

/* Chat avatar icon — ensure Material Symbols font renders */
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-user"],
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-assistant"] {
  font-family: 'Material Symbols Rounded', sans-serif !important;
  font-size: 22px !important;
  font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}

/* User avatar background */
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-user"] {
  background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
  color: #fff !important;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Assistant avatar background */
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-assistant"] {
  background: var(--accent-gradient) !important;
  color: #fff !important;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

@keyframes messageSlideIn {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Chat message text */
[data-testid="stChatMessage"] p {
  color: var(--text) !important;
  font-size: .9rem;
  line-height: 1.7;
}

/* ── Chat input ── */
[data-testid="stChatInput"] {
  background: transparent !important;
  border-top: none !important;
}

[data-testid="stChatInput"] textarea {
  background: var(--surface) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius);
  font-family: 'Inter', sans-serif !important;
  font-size: .88rem;
  transition: var(--transition);
}

[data-testid="stChatInput"] textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px var(--accent-soft), var(--shadow-glow) !important;
}

[data-testid="stChatInput"] button {
  color: var(--accent) !important;
  transition: var(--transition-fast);
}

[data-testid="stChatInput"] button:hover {
  color: var(--accent-hover) !important;
  transform: scale(1.08);
}

/* ── Scrollable containers ── */
[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] > div {
  scrollbar-width: thin;
  scrollbar-color: rgba(255,255,255,.1) transparent;
}

::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: rgba(255,255,255,.1);
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(255,255,255,.18);
}

/* ── Source cards — glass effect ── */
.source-card {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: .7rem .85rem;
  margin-bottom: .5rem;
  background: var(--glass);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  transition: var(--transition);
  animation: cardFadeIn .4s cubic-bezier(.4,0,.2,1);
}

.source-card:hover {
  border-color: var(--accent);
  background: rgba(15,190,160,.06);
  box-shadow: var(--shadow-glow);
  transform: translateY(-1px);
}

.source-card strong {
  color: var(--text) !important;
  font-weight: 600;
  font-size: .88rem;
}

.source-card small {
  color: var(--text-dim) !important;
  font-size: .78rem;
}

@keyframes cardFadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Self-check rows ── */
.check-row {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: .42rem .65rem;
  margin-bottom: .35rem;
  border-radius: var(--radius-sm);
  background: var(--surface-hover);
  border: 1px solid var(--border-light);
  font-size: .84rem;
  font-family: 'Inter', sans-serif !important;
  transition: var(--transition);
}

.check-row:hover {
  background: var(--surface-elevated);
  border-color: var(--border);
}

.check-icon { font-size: .95rem; flex-shrink: 0; }
.check-label { color: var(--text-secondary) !important; font-weight: 500; }
.check-value { margin-left: auto; font-weight: 600; }
.check-pass { color: var(--success) !important; }
.check-fail { color: var(--danger) !important; }

.check-note {
  padding: .5rem .7rem;
  margin-top: .35rem;
  border-radius: var(--radius-sm);
  font-size: .8rem;
  line-height: 1.5;
  font-family: 'Inter', sans-serif !important;
}

.check-note.grounded {
  background: rgba(63,185,80,.07);
  color: var(--success) !important;
  border: 1px solid rgba(63,185,80,.15);
}

.check-note.ungrounded {
  background: rgba(248,81,73,.07);
  color: var(--danger) !important;
  border: 1px solid rgba(248,81,73,.15);
}

/* ── Buttons ── */
.stButton > button {
  border-radius: var(--radius-sm) !important;
  border: 1px solid var(--border) !important;
  background: var(--surface-hover) !important;
  color: var(--text) !important;
  font-family: 'Inter', sans-serif !important;
  font-weight: 500;
  font-size: .84rem;
  padding: .45rem 1rem;
  transition: var(--transition);
  position: relative;
  overflow: hidden;
}

.stButton > button:hover {
  border-color: var(--accent) !important;
  color: var(--accent) !important;
  background: var(--accent-soft) !important;
  box-shadow: 0 0 16px rgba(15,190,160,.12);
}

.stButton > button:active {
  transform: scale(.97);
}

/* ── Toggle / Switch ── */
[data-testid="stToggle"] label span {
  font-family: 'Inter', sans-serif !important;
  font-size: .85rem !important;
  color: var(--text-secondary) !important;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
  font-family: 'Inter', sans-serif !important;
}

[data-testid="stFileUploader"] section {
  background: var(--surface-hover) !important;
  border: 1px dashed var(--border) !important;
  border-radius: var(--radius) !important;
  transition: var(--transition);
}

[data-testid="stFileUploader"] section:hover {
  border-color: var(--accent) !important;
  background: var(--accent-soft) !important;
}

[data-testid="stFileUploader"] button {
  background: var(--surface-hover) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
  border-radius: var(--radius-sm) !important;
}

/* ── Text input / Text area ── */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
  background: var(--surface-hover) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: .88rem;
  transition: var(--transition);
}

[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px var(--accent-soft) !important;
}

[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label,
[data-testid="stFileUploader"] label {
  color: var(--text-muted) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: .84rem !important;
  font-weight: 500 !important;
}

/* ── Dividers ── */
hr {
  border-color: var(--border) !important;
  margin: .6rem 0;
  opacity: .5;
}

/* ── Spinner — pulsing accent ── */
.stSpinner > div {
  border-top-color: var(--accent) !important;
}

.stSpinner {
  animation: spinnerPulse 1.5s ease-in-out infinite;
}

@keyframes spinnerPulse {
  0%, 100% { opacity: .7; }
  50% { opacity: 1; }
}

/* ── Alerts (success, error) ── */
[data-testid="stAlert"] {
  border-radius: var(--radius-sm) !important;
  font-family: 'Inter', sans-serif !important;
  animation: alertSlideIn .3s cubic-bezier(.4,0,.2,1);
  backdrop-filter: blur(6px);
}

@keyframes alertSlideIn {
  from { opacity: 0; transform: translateY(-6px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Toolbar — subtle until hovered ── */
[data-testid="stToolbar"] {
  opacity: .3;
  transition: opacity .3s ease;
}
[data-testid="stToolbar"]:hover {
  opacity: 1;
}

/* ── Bottom pinned chat input area ── */
[data-testid="stBottom"] {
  background: rgba(10,14,20,.85) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-top: 1px solid var(--border);
}

/* ── Expander styling ── */
[data-testid="stExpander"] {
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  background: var(--surface) !important;
}

[data-testid="stExpander"] summary {
  color: var(--text-secondary) !important;
  font-family: 'Inter', sans-serif !important;
}

/* ── Select box ── */
[data-testid="stSelectbox"] > div > div {
  background: var(--surface-hover) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text) !important;
}

/* ── Chat container inner styling ── */
[data-testid="stVerticalBlockBorderWrapper"] > div[style*="overflow"] {
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-lg) !important;
  background: var(--bg-subtle) !important;
}

</style>
"""


def light_theme_css() -> str:
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0&display=swap');

/* ── Light palette ── */
:root {
  --bg: #f8f9fc;
  --bg-subtle: #f0f2f6;
  --surface: #ffffff;
  --surface-hover: #f4f5f8;
  --surface-elevated: #ebedf2;
  --border: rgba(0,0,0,.1);
  --border-light: rgba(0,0,0,.06);
  --border-accent: rgba(15,143,122,.3);
  --text: #1a1f2e;
  --text-secondary: #4a5568;
  --text-muted: #6b7280;
  --text-dim: #9ca3af;
  --accent: #0e9a82;
  --accent-soft: rgba(14,154,130,.1);
  --accent-glow: rgba(14,154,130,.2);
  --accent-hover: #0bb89a;
  --accent-gradient: linear-gradient(135deg, #0e9a82, #0d8ecf);
  --danger: #e53e3e;
  --success: #38a169;
  --warning: #d69e2e;
  --info: #3182ce;
  --radius: 12px;
  --radius-sm: 8px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 2px rgba(0,0,0,.06);
  --shadow: 0 2px 8px rgba(0,0,0,.08), 0 4px 16px rgba(0,0,0,.04);
  --shadow-lg: 0 4px 16px rgba(0,0,0,.1), 0 8px 32px rgba(0,0,0,.06);
  --shadow-glow: 0 0 20px rgba(14,154,130,.1);
  --glass: rgba(255,255,255,.85);
  --glass-border: rgba(0,0,0,.08);
  --transition: all .25s cubic-bezier(.4,0,.2,1);
  --transition-fast: all .15s cubic-bezier(.4,0,.2,1);
}

/* ── Global app ── */
.stApp {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  background: var(--bg) !important;
  color: var(--text) !important;
}

/* ── Header — translucent glass bar ── */
header[data-testid="stHeader"] {
  background: rgba(248,249,252,.85) !important;
  backdrop-filter: blur(16px) saturate(1.4);
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
  border-bottom: 1px solid var(--border) !important;
  height: auto !important;
  min-height: auto !important;
  visibility: visible !important;
  z-index: 999;
}

/* ── Sidebar collapse button ── */
button[data-testid="stSidebarCollapseButton"],
button[data-testid="baseButton-headerNoPadding"] {
  color: var(--text-muted) !important;
  opacity: 1 !important;
  visibility: visible !important;
  transition: var(--transition-fast);
}

button[data-testid="stSidebarCollapseButton"]:hover,
button[data-testid="baseButton-headerNoPadding"]:hover {
  color: var(--accent) !important;
}

.block-container {
  max-width: 1380px;
  padding-top: 1.5rem;
  padding-bottom: .5rem;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
  background: var(--surface) !important;
  border-right: 1px solid var(--border) !important;
  min-width: 280px !important;
  visibility: visible !important;
}

[data-testid="stSidebar"] > div:first-child {
  background: var(--surface) !important;
  padding-top: .8rem;
}

[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  gap: .35rem;
}

[data-testid="stSidebar"]::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: var(--accent-gradient);
  z-index: 10;
}

/* ── Typography hierarchy ── */

.app-title,
[data-testid="stSidebar"] .app-title,
[data-testid="stColumn"] .app-title,
.stMarkdown .app-title {
  font-family: 'Inter', sans-serif !important;
  font-size: 1.45rem !important;
  font-weight: 700 !important;
  color: var(--text) !important;
  margin: 0 0 .15rem !important;
  letter-spacing: -.025em;
  line-height: 1.3;
  display: block !important;
  background: linear-gradient(135deg, #1a1f2e 40%, var(--accent)) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
}

[data-testid="stSidebar"] .app-title {
  background: none !important;
  -webkit-text-fill-color: var(--text) !important;
  font-size: 1.3rem !important;
}

.app-subtitle,
[data-testid="stSidebar"] .app-subtitle,
[data-testid="stColumn"] .app-subtitle,
.stMarkdown .app-subtitle {
  font-family: 'Inter', sans-serif !important;
  font-size: .88rem !important;
  font-weight: 400 !important;
  color: var(--text-muted) !important;
  margin: 0 0 1rem !important;
  line-height: 1.6;
  display: block !important;
}

h4,
[data-testid="stSidebar"] h4,
[data-testid="stColumn"] h4,
.main h4,
.stMarkdown h4 {
  font-family: 'Inter', sans-serif !important;
  font-weight: 600 !important;
  font-size: .78rem !important;
  letter-spacing: .1em !important;
  text-transform: uppercase !important;
  color: var(--text-muted) !important;
  margin-top: .8rem !important;
  margin-bottom: .5rem !important;
  padding-bottom: .3rem;
  border-bottom: 1px solid var(--border);
}

.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown code,
[data-testid="stColumn"] p,
[data-testid="stColumn"] li {
  color: var(--text) !important;
  font-family: 'Inter', sans-serif !important;
}

p, label, li {
  font-family: 'Inter', sans-serif !important;
}

[data-testid="stCaptionContainer"],
.stCaption {
  font-family: 'Inter', sans-serif !important;
  color: var(--text-dim) !important;
  font-size: .8rem;
}

/* ── Main columns panel ── */
[data-testid="stColumn"] > [data-testid="stVerticalBlockBorderWrapper"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
}

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
  background: var(--glass) !important;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid var(--glass-border) !important;
  border-radius: var(--radius);
  transition: var(--transition);
  animation: messageSlideIn .35s cubic-bezier(.4,0,.2,1);
}

[data-testid="stChatMessage"]:hover {
  border-color: var(--border-accent) !important;
  box-shadow: var(--shadow-glow);
}

[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-user"],
[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-assistant"] {
  font-family: 'Material Symbols Rounded', sans-serif !important;
  font-size: 22px !important;
  font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 24;
}

[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-user"] {
  background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
  color: #fff !important;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

[data-testid="stChatMessage"] [data-testid="chatAvatarIcon-assistant"] {
  background: var(--accent-gradient) !important;
  color: #fff !important;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

@keyframes messageSlideIn {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

[data-testid="stChatMessage"] p {
  color: var(--text) !important;
  font-size: .9rem;
  line-height: 1.7;
}

/* ── Chat input ── */
[data-testid="stChatInput"] {
  background: transparent !important;
  border-top: none !important;
}

[data-testid="stChatInput"] textarea {
  background: var(--surface) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius);
  font-family: 'Inter', sans-serif !important;
  font-size: .88rem;
  transition: var(--transition);
}

[data-testid="stChatInput"] textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px var(--accent-soft), var(--shadow-glow) !important;
}

[data-testid="stChatInput"] button {
  color: var(--accent) !important;
  transition: var(--transition-fast);
}

[data-testid="stChatInput"] button:hover {
  color: var(--accent-hover) !important;
  transform: scale(1.08);
}

/* ── Scrollable containers ── */
[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] > div {
  scrollbar-width: thin;
  scrollbar-color: rgba(0,0,0,.12) transparent;
}

::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: rgba(0,0,0,.12);
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(0,0,0,.2);
}

/* ── Source cards ── */
.source-card {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: .7rem .85rem;
  margin-bottom: .5rem;
  background: var(--glass);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  transition: var(--transition);
  animation: cardFadeIn .4s cubic-bezier(.4,0,.2,1);
}

.source-card:hover {
  border-color: var(--accent);
  background: rgba(14,154,130,.05);
  box-shadow: var(--shadow-glow);
  transform: translateY(-1px);
}

.source-card strong {
  color: var(--text) !important;
  font-weight: 600;
  font-size: .88rem;
}

.source-card small {
  color: var(--text-dim) !important;
  font-size: .78rem;
}

@keyframes cardFadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Self-check rows ── */
.check-row {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: .42rem .65rem;
  margin-bottom: .35rem;
  border-radius: var(--radius-sm);
  background: var(--surface-hover);
  border: 1px solid var(--border-light);
  font-size: .84rem;
  font-family: 'Inter', sans-serif !important;
  transition: var(--transition);
}

.check-row:hover {
  background: var(--surface-elevated);
  border-color: var(--border);
}

.check-icon { font-size: .95rem; flex-shrink: 0; }
.check-label { color: var(--text-secondary) !important; font-weight: 500; }
.check-value { margin-left: auto; font-weight: 600; }
.check-pass { color: var(--success) !important; }
.check-fail { color: var(--danger) !important; }

.check-note {
  padding: .5rem .7rem;
  margin-top: .35rem;
  border-radius: var(--radius-sm);
  font-size: .8rem;
  line-height: 1.5;
  font-family: 'Inter', sans-serif !important;
}

.check-note.grounded {
  background: rgba(56,161,105,.07);
  color: var(--success) !important;
  border: 1px solid rgba(56,161,105,.15);
}

.check-note.ungrounded {
  background: rgba(229,62,62,.07);
  color: var(--danger) !important;
  border: 1px solid rgba(229,62,62,.15);
}

/* ── Buttons ── */
.stButton > button {
  border-radius: var(--radius-sm) !important;
  border: 1px solid var(--border) !important;
  background: var(--surface) !important;
  color: var(--text) !important;
  font-family: 'Inter', sans-serif !important;
  font-weight: 500;
  font-size: .84rem;
  padding: .45rem 1rem;
  transition: var(--transition);
}

.stButton > button:hover {
  border-color: var(--accent) !important;
  color: var(--accent) !important;
  background: var(--accent-soft) !important;
  box-shadow: 0 0 16px rgba(14,154,130,.08);
}

.stButton > button:active {
  transform: scale(.97);
}

/* ── Toggle / Switch ── */
[data-testid="stToggle"] label span {
  font-family: 'Inter', sans-serif !important;
  font-size: .85rem !important;
  color: var(--text-secondary) !important;
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
  font-family: 'Inter', sans-serif !important;
}

[data-testid="stFileUploader"] section {
  background: var(--surface-hover) !important;
  border: 1px dashed var(--border) !important;
  border-radius: var(--radius) !important;
  transition: var(--transition);
}

[data-testid="stFileUploader"] section:hover {
  border-color: var(--accent) !important;
  background: var(--accent-soft) !important;
}

[data-testid="stFileUploader"] button {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
  border-radius: var(--radius-sm) !important;
}

/* ── Text input / Text area ── */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
  background: var(--surface) !important;
  color: var(--text) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: .88rem;
  transition: var(--transition);
}

[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px var(--accent-soft) !important;
}

[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label,
[data-testid="stFileUploader"] label {
  color: var(--text-muted) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: .84rem !important;
  font-weight: 500 !important;
}

/* ── Dividers ── */
hr {
  border-color: var(--border) !important;
  margin: .6rem 0;
  opacity: .5;
}

/* ── Spinner ── */
.stSpinner > div {
  border-top-color: var(--accent) !important;
}

.stSpinner {
  animation: spinnerPulse 1.5s ease-in-out infinite;
}

@keyframes spinnerPulse {
  0%, 100% { opacity: .7; }
  50% { opacity: 1; }
}

/* ── Alerts ── */
[data-testid="stAlert"] {
  border-radius: var(--radius-sm) !important;
  font-family: 'Inter', sans-serif !important;
  animation: alertSlideIn .3s cubic-bezier(.4,0,.2,1);
}

@keyframes alertSlideIn {
  from { opacity: 0; transform: translateY(-6px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Toolbar ── */
[data-testid="stToolbar"] {
  opacity: .3;
  transition: opacity .3s ease;
}
[data-testid="stToolbar"]:hover {
  opacity: 1;
}

/* ── Bottom pinned chat input ── */
[data-testid="stBottom"] {
  background: rgba(248,249,252,.9) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-top: 1px solid var(--border);
}

/* ── Expander ── */
[data-testid="stExpander"] {
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  background: var(--surface) !important;
}

[data-testid="stExpander"] summary {
  color: var(--text-secondary) !important;
  font-family: 'Inter', sans-serif !important;
}

/* ── Select box ── */
[data-testid="stSelectbox"] > div > div {
  background: var(--surface) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text) !important;
}

/* ── Chat container ── */
[data-testid="stVerticalBlockBorderWrapper"] > div[style*="overflow"] {
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-lg) !important;
  background: var(--bg-subtle) !important;
}

</style>
"""


def get_theme_css(theme: str = "dark") -> str:
    """Return CSS for the given theme name."""
    if theme == "light":
        return light_theme_css()
    return dark_theme_css()
