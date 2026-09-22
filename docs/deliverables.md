# Evaluation Deliverables

This project is prepared for the **L2-13 Semantic Search Platform** assignment.

## Required deliverables covered

| Evaluation item | Project artifact |
|---|---|
| Vector DB | `app/vector_store.py`, generated `vector_db/index.faiss` after ingestion |
| Embeddings | `app/embeddings.py` |
| Ranking | `app/ranking.py`, `app/search.py` |
| REST API | `app/api.py` |
| Application | `frontend/streamlit_app.py` + backend |
| Architecture | `docs/architecture.md` |
| Examples | `EXAMPLES.md` + `data/documents/` |
| Documentation | `README.md`, `docs/` |
| Tests | `tests/` |

## Demonstration checklist

1. Start the FastAPI server.
2. Run document ingestion.
3. Start the Streamlit UI.
4. Search sample enterprise policies.
5. Open `/docs` to demonstrate the REST API.
6. Explain the embedding, vector search, and ranking flow.

## Expected evidence for an interview/demo

- Terminal output showing successful ingestion.
- Browser screenshot of the Streamlit results.
- FastAPI Swagger page at `/docs`.
- One or more example queries and returned chunks.
- Architecture explanation covering design trade-offs.
