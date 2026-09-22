from app.chunking import chunk_text


def test_chunking_creates_overlap_and_preserves_content():
    text = " ".join(f"word{i}" for i in range(20))
    chunks = chunk_text(text, chunk_size=8, overlap=2)
    assert len(chunks) == 3
    assert "word0" in chunks[0]
    assert "word7" in chunks[0]
    assert "word6" in chunks[1]


def test_empty_text():
    assert chunk_text("") == []
