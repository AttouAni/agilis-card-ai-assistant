from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = "gemini-2.5-flash"

EMBEDDING_MODEL_NAME = "paraphrase-multilingual-mpnet-base-v2"
TOP_K = 3
VECTOR_STORE_DIR = "vector_store"
COLLECTION_NAME = "agilis_knowledge_base"