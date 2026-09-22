from typing import List

from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1, description="Natural-language search query")
    top_k: int = Field(default=5, ge=1, le=50)


class SearchResult(BaseModel):
    filename: str
    chunk_id: int
    text: str
    source_type: str
    score: float
    semantic_score: float
    metadata: dict = Field(default_factory=dict)


class SearchResponse(BaseModel):
    query: str
    count: int
    results: List[SearchResult]
