import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("STREAMLIT_API_URL", "http://127.0.0.1:8000").rstrip("/")

st.set_page_config(page_title="Semantic Search Platform", page_icon="🔎", layout="wide")

st.title("🔎 Enterprise Semantic Search")
st.caption("Search PDF, DOCX, and TXT documents using semantic embeddings + FAISS ranking.")

with st.sidebar:
    st.subheader("Search Settings")
    top_k = st.slider("Top results", min_value=1, max_value=20, value=5)
    st.code(API_URL, language="text")

try:
    health = requests.get(f"{API_URL}/health", timeout=5)
    health.raise_for_status()
    stats = health.json().get("vector_store", {})
    st.success(f"FastAPI connected · {stats.get('documents', 0)} documents · {stats.get('vectors', 0)} chunks")
except requests.RequestException as exc:
    st.error("FastAPI backend is not reachable.")
    st.code(str(exc))
    st.info("Start the backend with: python -m uvicorn app.api:app --reload --host 127.0.0.1 --port 8000")
    st.stop()

query = st.text_input("Search your enterprise knowledge", placeholder="Example: How many days of annual leave are allowed?")

if st.button("Search", type="primary") and query.strip():
    try:
        with st.spinner("Searching..."):
            response = requests.post(
                f"{API_URL}/search",
                json={"query": query, "top_k": top_k},
                timeout=60,
            )
            if not response.ok:
                st.error(response.text)
            else:
                payload = response.json()
                st.subheader(f"Results ({payload['count']})")
                if not payload["results"]:
                    st.info("No matching results found.")
                for i, result in enumerate(payload["results"], start=1):
                    with st.container(border=True):
                        st.markdown(f"**{i}. {result['filename']}** · chunk {result['chunk_id']}")
                        st.caption(
                            f"Hybrid score: {result['score']:.4f} · Semantic score: {result['semantic_score']:.4f}"
                        )
                        st.write(result["text"])
    except requests.RequestException as exc:
        st.error("Search request failed.")
        st.code(str(exc))
elif not query.strip():
    st.info("Enter a question or phrase to search the indexed documents.")
