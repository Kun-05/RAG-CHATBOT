# RAG Chatbot — Local Knowledge Assistant

## 📌 Overview

A fully local **Retrieval-Augmented Generation (RAG) chatbot** built from scratch, designed to answer product-related questions from an e-commerce catalog. The system retrieves relevant context from a custom-built JSON vector database and generates accurate, grounded responses using a local LLM — zero external API calls, all data stays on-device.

Key engineering decisions:
- **No LangChain, no ChromaDB** — vector storage and cosine similarity implemented in pure Python
- **Multi-format ingestion** — parses structured `.js` product arrays (via Regex) and unstructured `.pdf` documents (via `pypdf`)
- **Sliding window chunking** for PDF text; product-aware chunking for structured data

---

## 🎯 Features

- 🔍 **Custom Cosine Similarity Search** — implemented from scratch using only Python's `math` module, no vector DB framework
- 🧠 **Structured Prompt Engineering** — prompt template separates role instruction, answer constraints, and context injection
- ⚡ **Fully Local Deployment** — Ollama runs both the embedding model and LLM locally; no internet required after setup
- 🛠️ **Custom JSON Vector Store** — embeddings persisted in `db/vector_db.json`, managed by `CustomVectorDB` class
- 📄 **Multi-format Ingestion** — supports `.js`, `.pdf`, `.txt`, `.md`, `.csv`, `.json`, `.docx`
- 📦 **FastAPI Backend** — exposes `/chat` and `/health` endpoints; Swagger UI at `/docs`

---

## 🧱 System Architecture

```text
User Query
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
Response
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
│   └── rag.py             # ask() — full pipeline: retrieve → build prompt → call Mistral
│
│── api/
│   └── main.py            # FastAPI: POST /chat, GET /health
│
│── db/
│   └── vector_db.json     # Persisted vector embeddings
│
│── storage/               # Drop product .js files or .pdf documents here before indexing
│── config.py              # OLLAMA_URL, EMBED_MODEL, LLM_MODEL, CHUNK_SIZE, TOP_K, VECTOR_DB_PATH
│── requirement.txt        # Python dependencies
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kun-05/RAG-CHATBOT.git
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

Place product `.js` files or `.pdf` documents into the `storage/` folder.

### Step 2: Build the vector database

```bash
python -m data.indexing
```

This will embed all documents and save vectors to `db/vector_db.json`.

### Step 3: Start the API server

```bash
uvicorn api.main:app --reload
```

### Step 4: Query the chatbot

```
POST http://localhost:8000/chat
```

```json
{
  "query": "What is the price of this ring and is it in stock?"
}
```

Or open `http://localhost:8000/docs` for the interactive Swagger UI.

---

## 🧠 How It Works

### 1. Ingestion & Chunking

`data/loader.py` handles multi-format parsing:
- **`.js` product arrays** — extracts the JSON array using `rfind`, strips comments and trailing commas via Regex, then parses to Python list
- **`.pdf` documents** — extracts text page-by-page using `pypdf`
- **`.txt`, `.md`, `.csv`, `.json`, `.docx`** — also supported

`data/chunking.py` applies two strategies:
- `chunk_products()` — one chunk per product, preserving all fields (title, price, discount, stock, description)
- `chunk_text()` — sliding window with configurable `chunk_size` and `overlap` for free-form text

### 2. Embedding

`core/embedding.py` calls Ollama's local API (`nomic-embed-text`) to convert each text chunk into a float vector. No cloud API involved.

### 3. Custom Vector Store

`core/vector_store.py` — `CustomVectorDB` class:
- Stores and loads embeddings as a JSON list (`db/vector_db.json`)
- Implements `cosine_similarity(v1, v2)` from scratch using only `math.sqrt` and list comprehensions
- `search(query_vector, top_k)` — linear scan over all entries, returns top-K by similarity score

### 4. Prompt Engineering

`core/rag.py` — `ask()` constructs a structured prompt with three explicit sections:
- **Role instruction** — defines the assistant's persona and task scope
- **Answer constraints** — explicitly forbids hallucination ("only answer from provided context")
- **Context injection** — inserts the top-K retrieved chunks under a labeled section header

### 5. Generation

The assembled prompt is sent to the local Mistral model via Ollama. Response is returned as plain text through the FastAPI `/chat` endpoint.

---

## ⚡ Configuration

Edit `config.py`:

```python
OLLAMA_URL = "http://localhost:11434"

EMBED_MODEL = "nomic-embed-text"
LLM_MODEL   = "mistral"

CHUNK_SIZE      = 300   # words per chunk (sliding window)
TOP_K           = 3     # number of retrieved chunks
VECTOR_DB_PATH  = "db/vector_db.json"
```

---

## ⚠️ Limitations

- **O(N) linear search** — `CustomVectorDB.search()` scores every entry on each query. Intentionally simple; not optimized for large-scale datasets.
- **No advanced indexing** — does not use FAISS, HNSW, or any approximate nearest-neighbor structure.
- **No upload endpoint** — documents must be placed manually in `storage/` before running `data.indexing`.
- **Single-turn only** — no conversation memory across queries.

---

## 🚀 Future Improvements

- Add `/upload` endpoint for runtime document ingestion
- Implement Approximate Nearest Neighbor (ANN) search
- Add a Cross-Encoder reranking step after retrieval
- Support multi-turn conversation via session state
- Hybrid search: BM25 sparse + dense vector retrieval

---

## 👨‍💻 Author

Built as a foundational AI engineering project — custom vector math, multi-format document ingestion, and structured prompt engineering — with no reliance on high-level RAG frameworks.

---

## 📜 License

Open-source, available for educational and development purposes.