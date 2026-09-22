from typing import Any, Dict, List

from app.embeddings import embed_query
from app.ranking import hybrid_score
from app.vector_store import load_vector_store


def semantic_search(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    index, metadata = load_vector_store()
    if index.ntotal == 0:
        return []

    query_embedding = embed_query(query)
    candidate_k = min(max(top_k * 4, top_k), index.ntotal)
    scores, indices = index.search(query_embedding.astype("float32"), candidate_k)

    candidates = []
    for semantic, index_id in zip(scores[0], indices[0]):
        if index_id < 0:
            continue
        item = metadata[int(index_id)].copy()
        item["semantic_score"] = round(float(semantic), 4)
        item["score"] = round(hybrid_score(query, item["text"], float(semantic)), 4)
        candidates.append(item)

    candidates.sort(key=lambda x: x["score"], reverse=True)
    return candidates[:top_k]
