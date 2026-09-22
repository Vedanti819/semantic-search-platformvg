import sys
from pathlib import Path

# Allow `python scripts\\ingest.py` from the project root.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.chunking import chunk_text
from app.document_loader import load_documents
from app.embeddings import embed_texts
from app.config import CHUNK_OVERLAP, CHUNK_SIZE, DOCUMENTS_DIR
from app.vector_store import build_index


def main() -> None:
    documents = load_documents(DOCUMENTS_DIR)
    if not documents:
        raise SystemExit(f"No supported documents found in {DOCUMENTS_DIR}")

    chunks = []
    for doc in documents:
        for chunk_id, chunk in enumerate(chunk_text(doc.text, CHUNK_SIZE, CHUNK_OVERLAP)):
            metadata = {
                "filename": doc.filename,
                "chunk_id": chunk_id,
                "text": chunk,
                "source_type": doc.source_type,
                "metadata": doc.metadata,
            }
            chunks.append(metadata)

    texts = [item["text"] for item in chunks]
    embeddings = embed_texts(texts)
    build_index(embeddings, chunks)

    print(f"Indexed documents: {len({d.filename for d in documents})}")
    print(f"Indexed chunks: {len(chunks)}")
    print("Vector index written to vector_db/")


if __name__ == "__main__":
    main()
