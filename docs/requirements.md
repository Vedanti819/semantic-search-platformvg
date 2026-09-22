# Project Requirements

## Functional requirements

1. Accept PDF, DOCX, and TXT enterprise documents.
2. Extract text and split documents into overlapping chunks.
3. Generate dense semantic embeddings for indexed chunks.
4. Persist vectors in a local vector database/index.
5. Retrieve relevant chunks for natural-language queries.
6. Re-rank results using semantic similarity plus lexical overlap.
7. Expose search through a REST API.
8. Provide a browser-based search application.
9. Return structured search results with document name, chunk, scores, and metadata.
10. Provide health/status endpoints and useful error handling.

## Non-functional requirements

- Modular Python codebase.
- Environment-based configuration.
- Windows-friendly startup commands.
- Documentation for setup, architecture, and examples.
- Unit tests for core retrieval utilities.
- No database server required for the local demo.

## Technical stack

Python, FastAPI, Sentence Transformers, FAISS, Streamlit, pypdf, python-docx, Pydantic, pytest.
