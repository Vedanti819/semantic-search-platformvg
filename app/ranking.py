import re
from typing import Iterable

_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how",
    "i", "in", "is", "it", "me", "of", "on", "or", "the", "to", "what",
    "when", "where", "which", "who", "with", "you", "your"
}


def _tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-zA-Z0-9]+", text.lower())
        if token not in _STOPWORDS
    }


def lexical_score(query: str, text: str) -> float:
    q = _tokens(query)
    d = _tokens(text)
    if not q or not d:
        return 0.0
    return len(q & d) / len(q)


def hybrid_score(query: str, text: str, semantic_score: float) -> float:
    # Blend semantic similarity with lightweight lexical overlap for ranking.
    # Semantic: 85%, lexical: 15%.
    lex = lexical_score(query, text)
    return max(0.0, min(1.0, 0.85 * semantic_score + 0.15 * lex))
