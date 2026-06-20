from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from ingest import build_all_chunks

VECTOR_STORE_DIR = Path(__file__).resolve().parent.parent / "vector_store"
COLLECTION_NAME = "agilis_knowledge_base"
EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"

def build_vectordb():
    chunks = build_all_chunks()
    print(f"Embedding {len(chunks)} chunks with '{EMBEDDING_MODEL_NAME}'...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=str(VECTOR_STORE_DIR),
    )

    print(f"Vector store built and saved to: {VECTOR_STORE_DIR}")
    return vectordb

if __name__ == "__main__":
    build_vectordb()