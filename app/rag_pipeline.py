from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from utils import (
    GEMINI_API_KEY, GEMINI_MODEL_NAME,
    EMBEDDING_MODEL_NAME, TOP_K,
    VECTOR_STORE_DIR, COLLECTION_NAME,
)


if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found — check your .env file")
llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL_NAME,
    google_api_key=GEMINI_API_KEY,
    temperature=0.2,
)


embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
vectordb = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embeddings,
    persist_directory=VECTOR_STORE_DIR,
)

llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL_NAME,
    google_api_key=GEMINI_API_KEY,
    temperature=0.2,
)

def retrieve_context(question: str) -> str:
    results = vectordb.similarity_search(question, k=TOP_K)
    context_parts = []
    for doc in results:
        source = doc.metadata.get("source", "inconnu")
        context_parts.append(f"[Source: {source}]\n{doc.page_content}")
    return "\n\n---\n\n".join(context_parts)

def answer_question(question: str) -> str:
    context = retrieve_context(question)

    system_message = SYSTEM_PROMPT.format(context=context)
    user_message = USER_PROMPT_TEMPLATE.format(question=question)

    response = llm.invoke([
        ("system", system_message),
        ("human", user_message),
    ])

    return response.content
