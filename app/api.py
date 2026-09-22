from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import CORS_ORIGINS
from app.models import SearchRequest, SearchResponse
from app.search import semantic_search
from app.vector_store import get_store_stats

app = FastAPI(
    title="Semantic Search Platform",
    description="Enterprise semantic document search API using embeddings and FAISS.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Semantic Search Platform API",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    stats = get_store_stats()
    return {"status": "healthy", "vector_store": stats}


@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Search query cannot be empty")
    try:
        results = semantic_search(request.query.strip(), request.top_k)
        return SearchResponse(query=request.query.strip(), count=len(results), results=results)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Search failed: {exc}") from exc


@app.get("/stats")
def stats():
    return get_store_stats()
