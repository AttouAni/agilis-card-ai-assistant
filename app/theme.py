"""
theme.py
--------
Custom CSS for the AGILIS chatbot.
"""

import streamlit as st

AGIL_YELLOW = "#FFD400"
AGIL_RED = "#E10600"

CUSTOM_CSS = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

:root {
    --agil-yellow: #FFD400;
    --agil-red: #E10600;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, sans-serif;
}

h1, h2, h3, .agil-header-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    letter-spacing: -0.01em;
}

#MainMenu, footer, header[data-testid="stHeader"] {
    visibility: hidden;
    height: 0;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 6rem !important;
    max-width: 760px;
}

.agil-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 0 1rem 0;
    border-bottom: 3px solid var(--agil-yellow);
    margin-bottom: 1.5rem;
}

.agil-logo-img {
    height: 38px;
    width: auto;
    display: block;
    border-radius: 6px;
}

.agil-header-title {
    font-size: 1.3rem;
    line-height: 1.1;
}

.agil-header-subtitle {
    font-size: 0.82rem;
    opacity: 0.65;
    font-weight: 400;
}

[data-testid="stChatMessage"] {
    border-radius: 14px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.6rem;
    border: none;
    box-shadow: 0 1px 2px rgba(0,0,0,0.06);
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background-color: var(--agil-yellow);
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) p {
    color: #161616 !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="chatAvatarIcon-user"] {
    display: none !important;
}

.agil-chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0.5rem 0 1.5rem 0;
}

div[data-testid="stButton"] button {
    border-radius: 20px;
    border: 1.5px solid var(--agil-yellow);
    background-color: transparent;
    font-size: 0.85rem;
    padding: 0.4rem 1rem;
    font-weight: 500;
    transition: background-color 0.15s ease;
}

div[data-testid="stButton"] button:hover {
    background-color: var(--agil-yellow);
    color: #161616;
    border-color: var(--agil-yellow);
}

.agil-empty-state {
    text-align: center;
    padding: 3rem 1rem 2rem 1rem;
}

.agil-empty-state-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    font-weight: 600;
    margin-bottom: 0.4rem;
}

.agil-empty-state-accent {
    width: 36px;
    height: 4px;
    background-color: var(--agil-red);
    border-radius: 2px;
    margin: 0.6rem auto 1rem auto;
}

.agil-empty-state-subtitle {
    font-size: 0.9rem;
    opacity: 0.6;
    max-width: 420px;
    margin: 0 auto;
}

[data-testid="stChatInput"] button {
    background-color: var(--agil-yellow) !important;
    border-radius: 10px !important;
}
[data-testid="stChatInput"] button svg {
    fill: #161616 !important;
    color: #161616 !important;
}

.agil-thinking {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    opacity: 0.65;
    font-size: 0.9rem;
    font-style: italic;
}

.agil-thinking-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: var(--agil-red);
    animation: agil-pulse 1.1s infinite ease-in-out;
}
.agil-thinking-dot:nth-child(2) { animation-delay: 0.15s; }
.agil-thinking-dot:nth-child(3) { animation-delay: 0.3s; }

@keyframes agil-pulse {
    0%, 80%, 100% { opacity: 0.25; transform: scale(0.85); }
    40% { opacity: 1; transform: scale(1); }
}

</style>
"""


def inject_custom_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)