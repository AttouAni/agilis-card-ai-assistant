import streamlit as st
from theme import inject_custom_css
from rag_pipeline import answer_question  # your real pipeline

st.set_page_config(
    page_title="Assistant AGILIS",
    page_icon="⛽",
    layout="centered",
)

inject_custom_css()

ASSISTANT_AVATAR = "./assets/agil_logo.jpg"

SUGGESTED_QUESTIONS = [
    "Frais de remplacement de carte ?",
    "Différence AGILIS Gold / Cash ?",
    "Stations disponibles à Sousse ?",
    "Comment renouveler ma carte ?",
]

# ---------- Header (normal flow, scrolls with the page like before) ----------
import base64
with open("./assets/agil_logo.jpg", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <div class="agil-header">
        <img src="data:image/jpeg;base64,{logo_b64}" class="agil-logo-img">
        <div>
            <div class="agil-header-title">Assistant AGILIS</div>
            <div class="agil-header-subtitle">Agil Energy — carte pétrolière privative</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


def queue_message(text: str):
    st.session_state.messages.append({"role": "user", "content": text})
    st.session_state.pending_question = text


if not st.session_state.messages:
    st.markdown(
        """
        <div class="agil-empty-state">
            <div class="agil-empty-state-title">Posez votre question sur la carte AGILIS</div>
            <div class="agil-empty-state-accent"></div>
            <div class="agil-empty-state-subtitle">
                Frais, sécurité, types de cartes, stations disponibles, conditions du contrat — je peux vous aider.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(len(SUGGESTED_QUESTIONS))
    for col, question in zip(cols, SUGGESTED_QUESTIONS):
        with col:
            if st.button(question, key=f"suggested_{question}", use_container_width=True):
                queue_message(question)
                st.rerun()

for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant", avatar=ASSISTANT_AVATAR):
            st.markdown(msg["content"])

if st.session_state.pending_question:
    with st.chat_message("assistant", avatar=ASSISTANT_AVATAR):
        st.markdown(
            """
            <div class="agil-thinking">
                <span>En train de réfléchir</span>
                <span class="agil-thinking-dot"></span>
                <span class="agil-thinking-dot"></span>
                <span class="agil-thinking-dot"></span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    question = st.session_state.pending_question
    answer = answer_question(question)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.pending_question = None
    st.rerun()

user_input = st.chat_input("Tapez votre question...")

if user_input:
    queue_message(user_input)
    st.rerun()