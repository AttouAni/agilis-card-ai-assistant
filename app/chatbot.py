""" from rag_pipeline import answer_question

if __name__ == "__main__":
    print("Assistant AGILIS — tape 'quit' pour sortir.\n")
    while True:
        question = input("Vous : ")
        if question.lower() in ("quit", "exit"):
            break
        answer = answer_question(question)
        print(f"\nAssistant : {answer}\n") """

import streamlit as st
from rag_pipeline import answer_question

st.set_page_config(page_title="Assistant AGILIS", page_icon="⛽")

st.title("⛽ Assistant AGILIS")
st.caption("Posez vos questions sur la carte pétrolière AGILIS — Agil Energy")

# Keep chat history across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Votre question...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Recherche en cours..."):
            answer = answer_question(question)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})