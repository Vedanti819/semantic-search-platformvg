# Semantic Search Platform

A complete local **enterprise semantic search application** built with Python, Sentence Transformers, FAISS, FastAPI, and Streamlit.

## What this project does

- Ingests enterprise documents in PDF, DOCX, and TXT formats.
- Splits documents into overlapping chunks.
- Generates semantic embeddings.
- Stores embeddings in a FAISS vector index.
- Retrieves semantic candidates and applies hybrid re-ranking.
- Exposes search through a REST API.
- Provides a browser-based Streamlit interface.

## Project structure

```text
semantic-search-platform/
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── chunking.py
│   ├── config.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── models.py
│   ├── ranking.py
│   ├── search.py
│   └── vector_store.py
├── data/
│   └── documents/
│       ├── expense_policy.txt
│       ├── hr_policy.txt
│       ├── it_security.txt
│       └── leave_policy.txt
├── docs/
│   ├── architecture.md
│   ├── deliverables.md
│   └── skills.md
├── frontend/
│   └── streamlit_app.py
├── scripts/
│   └── ingest.py
├── tests/
│   ├── test_chunking.py
│   └── test_ranking.py
├── .env.example
├── EXAMPLES.md
├── README.md
└── requirements.txt
```

## Requirements

Recommended: **Python 3.12** on Windows. Current FAISS Windows wheels support CPython 3.12, and current Streamlit supports Python 3.12.

The project follows the evaluation workbook requirements for **L2-13 Semantic Search Platform**, which calls for a vector DB, embeddings, ranking, a REST API, an application, architecture documentation, and examples.

## Windows setup

Open PowerShell in the project folder.

### 1. Create and activate a virtual environment

```powershell
py -3.12 -m venv myaienv
.\myaienv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Create environment configuration

```powershell
Copy-Item .env.example .env
```

### 4. Add documents

Put your `.pdf`, `.docx`, or `.txt` files into:

```text
data\documents\
```

Sample documents are already included.

### 5. Build the vector index

Run this from the **project root**:

```powershell
python scripts\ingest.py
```

The first run may download the embedding model.

### 6. Start FastAPI

Open Terminal 1:

```powershell
cd C:\Users\hp\Downloads\semantic-search-platform
.\myaienv\Scripts\Activate.ps1
python -m uvicorn app.api:app --reload --host 127.0.0.1 --port 8000
```

Verify:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

### 7. Start Streamlit

Open Terminal 2:

```powershell
cd C:\Users\hp\Downloads\semantic-search-platform
.\myaienv\Scripts\Activate.ps1
python -m streamlit run frontend\streamlit_app.py
```

Open the URL shown by Streamlit, normally:

`http://localhost:8501`

## Fixing a broken Windows environment

If you see `Permission denied` for `myaienv\Scripts\python.exe`, broken `pip._internal`, `click.Choice`, or `google.protobuf` import errors, the virtual environment is corrupted or has incompatible packages. Follow `FIX_WINDOWS.md` to recreate it cleanly.

When your PowerShell prompt already ends with `C:\Users\hp\Downloads\semantic-search-platform>`, do **not** run `cd semantic-search-platform` again.

## Important Windows note

Do **not** launch the Streamlit app with:

```powershell
python frontend\streamlit_app.py
```

Use:

```powershell
python -m streamlit run frontend\streamlit_app.py
```

Also run commands from the project root so imports such as `app.api` work correctly.

## API

### GET `/health`

Returns backend status and vector-store counts.

### GET `/stats`

Returns the indexed vector count and distinct document count.

### POST `/search`

Request:

```json
{
  "query": "How many annual leave days do employees receive?",
  "top_k": 5
}
```

Response shape:

```json
{
  "query": "How many annual leave days do employees receive?",
  "count": 1,
  "results": [
    {
      "filename": "leave_policy.txt",
      "chunk_id": 0,
      "text": "...",
      "source_type": "txt",
      "score": 0.85,
      "semantic_score": 0.91,
      "metadata": {}
    }
  ]
}
```

## Architecture

See `docs/architecture.md`.

## Deliverables and skills

See:

- `docs/deliverables.md`
- `docs/skills.md`

## Testing

```powershell
pytest -q
```

## Troubleshooting

### `Could not connect to FastAPI`

Start FastAPI in a separate terminal and keep that terminal open.

### `Vector index not found`

Run:

```powershell
python scripts\ingest.py
```

### `ModuleNotFoundError: app`

Make sure the terminal is in:

```text
C:\Users\hp\Downloads\semantic-search-platform
```

and run:

```powershell
python -m uvicorn app.api:app --reload --host 127.0.0.1 --port 8000
```

## Interview explanation

A useful 60-second explanation is:

> Documents are loaded from PDF, DOCX, and TXT files, then split into overlapping chunks. Each chunk is converted into a normalized embedding using a Sentence Transformer and stored in FAISS. At query time, the same embedding model converts the user's query into a vector, FAISS retrieves semantically similar chunks, and a lightweight hybrid ranking step combines semantic similarity with lexical overlap. FastAPI exposes the search service, while Streamlit provides the web interface.

## Extension ideas

- Add OCR for scanned PDFs.
- Replace JSON metadata with PostgreSQL or a document database.
- Add a cross-encoder reranker.
- Add authentication and rate limiting.
- Add incremental indexing and document deletion.
- Add observability and evaluation metrics.
