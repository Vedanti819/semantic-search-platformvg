# Evaluation Mapping

## Assignment

**L2-13 — Semantic Search Platform**

## Mapping

- **Vector DB** → `app/vector_store.py` using FAISS.
- **Embeddings** → `app/embeddings.py` using Sentence Transformers.
- **Ranking** → `app/ranking.py` and `app/search.py` using hybrid ranking.
- **REST API** → `app/api.py` with `/health`, `/stats`, and `/search`.
- **Application** → `frontend/streamlit_app.py`.
- **Architecture** → `docs/architecture.md`.
- **Examples** → `EXAMPLES.md` and `data/documents/`.

## Demonstration evidence

The evaluator can inspect the source code, run ingestion, open the FastAPI Swagger UI, and perform searches in the Streamlit application.
