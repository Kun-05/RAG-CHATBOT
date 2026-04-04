# RAG Chatbot for E-commerce Website

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG) chatbot** designed for an e-commerce website. The chatbot retrieves relevant product information from a custom-built vector database and generates accurate, context-aware responses using a local Large Language Model (LLM).

The system is fully self-contained, running locally without relying on external APIs, ensuring **privacy, low cost, and high customization**.

---

## 🎯 Features

* 🔍 Semantic search using vector embeddings
* 🧠 Context-aware responses using LLM
* ⚡ Fully local deployment (no external API required)
* 🛠️ Custom-built vector database (no frameworks like LangChain)
* 📦 Easy integration with existing e-commerce backend

---

## 🧱 System Architecture

```
User Query
   ↓
Embedding (Ollama)
   ↓
Vector Search (Cosine Similarity)
   ↓
Top-K Relevant Context
   ↓
LLM Generation
   ↓
Response
```

---

## 📁 Project Structure

```
rag-chatbot/
│── data/
│   ├── loader.py          # Load data from database
│   └── indexing.py        # Build vector database
│
│── core/
│   ├── embedding.py       # Generate embeddings
│   ├── vector_store.py    # Store and manage vectors
│   ├── retriever.py       # Search relevant data
│   ├── llm.py             # Call LLM
│   └── rag.py             # RAG pipeline
│
│── api/
│   └── main.py            # FastAPI server
│
│── db/
│   └── vector_db.json     # Stored embeddings
│
│── config.py              # Configuration
│── requirements.txt       # Dependencies
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd rag-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and run Ollama

Make sure Ollama is installed and running locally.

Pull required models:

```bash
ollama pull mistral
ollama pull nomic-embed-text
```

---

## 🚀 Usage

### Step 1: Build vector database

```bash
python data/indexing.py
```

### Step 2: Start the API server

```bash
uvicorn api.main:app --reload
```

### Step 3: Test the chatbot

Send a POST request:

```
POST http://localhost:8000/chat
```

Body:

```json
{
  "query": "What is the price of iPhone 15?"
}
```

---

## 🧠 How It Works

### 1. Data Processing

* Load product data from database
* Split into smaller chunks

### 2. Embedding

* Convert text into vectors using embedding model

### 3. Retrieval

* Compute cosine similarity between query and stored vectors
* Select top-K relevant chunks

### 4. Generation

* Combine retrieved context with user query
* Generate response using LLM

---

## ⚡ Configuration

Edit `config.py`:

```python
OLLAMA_URL = "http://localhost:11434"

EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "mistral"

CHUNK_SIZE = 300
TOP_K = 3
```

---

## 🔧 Customization

You can easily:

* Connect to real database (MySQL, MongoDB, etc.)
* Add product metadata (price, category, stock)
* Improve prompt design
* Add chat memory
* Implement recommendation logic

---

## ⚠️ Limitations

* Linear search (not optimized for large datasets)
* No advanced indexing (e.g., FAISS)
* Performance may degrade with large data

---

## 🚀 Future Improvements

* Implement Approximate Nearest Neighbor (ANN)
* Add reranking model
* Integrate recommendation system
* Support multi-turn conversations
* Deploy to production environment

---

## 👨‍💻 Author

Developed as a custom RAG chatbot system for learning and real-world application.

---

## 📜 License

This project is open-source and available for educational and development purposes.
