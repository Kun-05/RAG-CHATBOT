# RAG Chatbot — Local Knowledge Assistant

## 📌 Overview

A fully local Retrieval-Augmented Generation (RAG) chatbot built from scratch, designed to answer domain-specific questions from custom datasets. The system retrieves relevant context from a custom-built JSON vector database and generates accurate, grounded responses using a local LLM. It operates with zero external API calls, ensuring all data stays on-device.

Key engineering decisions:
- **No LangChain, no ChromaDB** — vector storage and cosine similarity are implemented in pure Python.
- **Interactive Web UI** — features a Streamlit-based frontend with real-time token streaming (Server-Sent Events) for a smooth, ChatGPT-like user experience.
- **Multi-format ingestion** — parses structured `.js` data arrays (via Regex) and unstructured `.pdf` documents (via `pypdf`).
- **Sliding window chunking** is used for PDF text, while schema-aware chunking is applied to structured data.

---

## 🎯 Features

- 🎨 **Streamlit Frontend** — a clean, interactive chat interface decoupled from the backend, supporting real-time text streaming.
- 🔍 **Custom Cosine Similarity Search** — implemented from scratch using only Python's `math` module, without relying on any vector DB framework.
- 🧠 **Structured Prompt Engineering** — the prompt template explicitly separates role instruction, answer constraints, and context injection.
- ⚡ **Fully Local Deployment** — Ollama runs both the embedding model and LLM locally, requiring no internet after setup.
- 🛠️ **Custom JSON Vector Store** — embeddings are persisted in `db/vector_db.json` and managed by the `CustomVectorDB` class.
- 📦 **FastAPI Backend** — exposes `/chat` and `/health` endpoints, with Swagger UI available at `/docs`.

---

## 🧱 System Architecture

```text
User Query (Streamlit UI)
   ↓
FastAPI Backend (/chat)
   ↓
Embedding (Ollama: nomic-embed-text)
   ↓
CustomVectorDB.search() — Cosine Similarity in pure Python
   ↓
Top-K Relevant Chunks (from vector_db.json)
   ↓
build_prompt() — role + constraints + context injection
   ↓
LLM Generation (Ollama: mistral)
   ↓
Response Streaming (Yielding tokens back to UI)

```

---

## 📁 Project Structure

```text
rag-chatbot/
│── data/
│   ├── loader.py          # Multi-format file parser (.js via Regex, .pdf via pypdf, etc.)
│   ├── chunking.py        # chunk_products() for .js data; chunk_text() sliding window for PDFs
│   └── indexing.py        # Orchestrates ingestion → embedding → save to CustomVectorDB
│
│── core/
│   ├── embedding.py       # embed_text() / embed_many() — calls Ollama nomic-embed-text
│   ├── vector_store.py    # CustomVectorDB class: JSON persistence + cosine_similarity() from scratch
│   ├── retriever.py       # retrieve() — embeds query, calls CustomVectorDB.search()
│   ├── llm.py             # (reserved for LLM abstraction layer)
│   └── rag.py             # ask() and ask_stream() — pipeline: retrieve → build prompt → call LLM
│
│── api/
│   └── main.py            # FastAPI: POST /chat (with StreamingResponse support), GET /health
│
│── ui.py                  # Streamlit frontend for interactive chat and streaming
│
│── db/
│   └── vector_db.json     # Persisted vector embeddings
│
│── storage/               # Drop structured .js files or .pdf documents here before indexing
│── config.py              # OLLAMA_URL, EMBED_MODEL, LLM_MODEL, CHUNK_SIZE, TOP_K
│── requirement.txt        # Python dependencies (including fastapi, streamlit, requests)

```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone [https://github.com/Kun-05/RAG-CHATBOT.git](https://github.com/Kun-05/RAG-CHATBOT.git)
cd RAG-CHATBOT

```

### 2. Install dependencies

```bash
pip install -r requirement.txt

```

### 3. Install and run Ollama

Install [Ollama](https://ollama.com/), then pull the required models:

```bash
ollama pull mistral
ollama pull nomic-embed-text

```

---

## 🚀 Usage

### Step 1: Add your data

Place target `.js` files or `.pdf` documents into the `storage/` folder.

### Step 2: Build the vector database

```bash
python -m data.indexing

```

This process will embed all documents and save the vectors to `db/vector_db.json`.

### Step 3: Start the Backend API (Terminal 1)

Run the FastAPI server to handle retrieval and LLM generation:

```bash
uvicorn api.main:app --reload

```

### Step 4: Start the Chat UI (Terminal 2)

Open a new terminal window and launch the Streamlit frontend:

```bash
streamlit run ui.py

```

The application will automatically open in your browser at `http://localhost:8501`.

### Step 5: Direct API Query (Optional)

You can still bypass the UI and query the API directly or use the Swagger UI at `http://localhost:8000/docs`.

```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"query": "What are the specifications of this item?", "stream": true}'

```

---

## 🧠 How It Works

### 1. Ingestion & Chunking

`data/loader.py` handles multi-format parsing. Formats including `.txt`, `.md`, `.csv`, `.json`, and `.docx` are also supported.
`data/chunking.py` applies two distinct strategies: `chunk_products()` for structured data and `chunk_text()` for free-form text.

### 2. Custom Vector Store

The `CustomVectorDB` class acts as the persistence layer, implementing `cosine_similarity(v1, v2)` from scratch utilizing only `math.sqrt` and list comprehensions.

### 3. Prompt Engineering & Generation

In `core/rag.py`, the system constructs a structured prompt explicitly forbidding hallucination. The assembled prompt is sent to the local Mistral model via Ollama. The `ask_stream()` function utilizes Python generators (`yield`) to stream tokens back to the FastAPI `/chat` endpoint, which are then consumed and rendered dynamically by the Streamlit UI.

---

## ⚠️ Limitations

* **O(N) linear search** — `CustomVectorDB.search()` scores every entry on each query. It is intentionally simple and not optimized for large-scale datasets.
* **No advanced indexing** — the system does not use FAISS, HNSW, or any approximate nearest-neighbor structures.
* **Single-turn only** — there is no conversation memory maintained across queries in the current implementation.

---

## 🚀 Future Improvements

* Add an `/upload` endpoint for runtime document ingestion via the UI.
* Implement Approximate Nearest Neighbor (ANN) search for better scaling.
* Add a Cross-Encoder reranking step following the initial retrieval.
* Support multi-turn conversation via Streamlit session state management.
* Implement Hybrid search combining BM25 sparse and dense vector retrieval.

---

## 👨‍💻 Author

Built as a foundational AI engineering project — showcasing custom vector math, real-time streaming, and structured prompt engineering — with no reliance on high-level RAG frameworks.

```

```