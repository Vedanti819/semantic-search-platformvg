from pathlib import Path
import os
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "400"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "80"))
VECTOR_DB_DIR = ROOT_DIR / os.getenv("VECTOR_DB_DIR", "vector_db")
DOCUMENTS_DIR = ROOT_DIR / os.getenv("DOCUMENTS_DIR", "data/documents")
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8000"))
TOP_K_DEFAULT = int(os.getenv("TOP_K_DEFAULT", "5"))
CORS_ORIGINS = [x.strip() for x in os.getenv(
    "CORS_ORIGINS", "http://localhost:8501,http://127.0.0.1:8501"
).split(",") if x.strip()]

INDEX_PATH = VECTOR_DB_DIR / "index.faiss"
METADATA_PATH = VECTOR_DB_DIR / "metadata.json"
