import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

import faiss
import numpy as np

from app.config import INDEX_PATH, METADATA_PATH, VECTOR_DB_DIR


def build_index(embeddings: np.ndarray, metadata: List[Dict[str, Any]]) -> None:
    if embeddings.ndim != 2 or embeddings.shape[0] == 0:
        raise ValueError("Embeddings must be a non-empty 2D matrix")
    if len(metadata) != embeddings.shape[0]:
        raise ValueError("Metadata count must match embedding count")

    VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings.astype("float32"))
    faiss.write_index(index, str(INDEX_PATH))
    METADATA_PATH.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")


def load_vector_store() -> Tuple[faiss.Index, List[Dict[str, Any]]]:
    if not INDEX_PATH.exists() or not METADATA_PATH.exists():
        raise FileNotFoundError(
            "Vector index not found. Run: python scripts\\ingest.py"
        )
    index = faiss.read_index(str(INDEX_PATH))
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    return index, metadata


def get_store_stats() -> Dict[str, int]:
    if not INDEX_PATH.exists() or not METADATA_PATH.exists():
        return {"vectors": 0, "documents": 0}
    index = faiss.read_index(str(INDEX_PATH))
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    filenames = {item.get("filename") for item in metadata}
    return {"vectors": int(index.ntotal), "documents": len(filenames)}
