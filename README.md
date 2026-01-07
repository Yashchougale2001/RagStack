RAG_Stack: CPU-Friendly Local Retrieval-Augmented Generation System

A lightweight, modular Retrieval-Augmented Generation (RAG) system designed for CPU-only, low-resource machines, using fully local models with zero paid APIs.

This project demonstrates how to build a production-style RAG pipeline that runs entirely on your machine using:

ChromaDB for persistent vector storage

BGE Small embeddings for accurate semantic retrieval

TinyLlama via Ollama for grounded answer generation

The system answers questions strictly from a local knowledge base, with explicit safeguards against hallucination.

🎯 Why This Project Exists

This project proves that:

RAG is an architecture, not a paid service

You can run a complete RAG pipeline locally, on CPU

Clean design and grounding rules matter more than model size

This is built for learning, interviews, and real-world constraints, not demo fluff.

🚀 Features

Semantic retrieval using BAAI/bge-small-en-v1.5

Persistent ChromaDB (no re-embedding on restart)

Local LLM inference using TinyLlama via Ollama

Overlapping text chunking for better recall

Strict context-grounded answering

Explicit “I don’t know” handling (no guessing)

Answer faithfulness evaluation

Clean, modular, interview-ready architecture

Interactive CLI-based Q&A

🗂 Project Structure
mini_rag/
│
├── data/
│   └── knowledge.txt              # Raw knowledge base
│
├── src/
│   ├── loader/
│   │   └── loader.py              # Text loading & chunking
│   │
│   ├── db/
│   │   └── vector_store.py        # ChromaDB creation & queries
│   │
│   ├── retrieval/
│   │   └── retriever.py           # Top-K retrieval logic
│   │
│   ├── generation/
│   │   ├── generator.py           # Ollama + TinyLlama inference
│   │   └── prompt_templates.py    # Strict grounding prompts
│   │
│   ├── eval/
│   │   └── evaluator.py           # Faithfulness checks
│   │
│   ├── ingest.py                  # One-time ingestion script
│   └── main.py                    # CLI entry point
│
├── chroma_db/                     # Persistent vector store
├── config.yaml                    # Models, chunking, retrieval params
├── requirements.txt
└── README.md

🔄 RAG Workflow (High-Level)

Load text from knowledge.txt

Split text into overlapping chunks

Generate embeddings using BGE Small

Store vectors in ChromaDB

Accept user query

Embed query

Retrieve top-K relevant chunks

Generate answer using TinyLlama

Validate answer grounding

🧠 Architecture Overview
knowledge.txt
      ↓
Text Loader
      ↓
Chunking (overlap)
      ↓
Embedding Model (BGE Small)
      ↓
ChromaDB (Persistent)
      ↓
User Query
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Top-K Context Chunks
      ↓
TinyLlama (Ollama)
      ↓
Grounded Answer

🧩 Modular Design (Single Responsibility)
Module	Responsibility
loader	Load & chunk raw text
vector_store	Vector DB creation & storage
retriever	Query orchestration
generator	Context-only answer generation
evaluator	Detect hallucinations
main	CLI application loop

Each module is replaceable without breaking the system.

⚙️ Tech Stack (Actual)
Component	Technology
Embeddings	BAAI/bge-small-en-v1.5
Vector DB	ChromaDB
LLM	TinyLlama (via Ollama)
Language	Python
Hardware	CPU-only

No cloud. No paid APIs. Fully local.

🧪 Limitations (Honest)

Designed for small–medium corpora

TinyLlama has limited reasoning depth

Single-turn Q&A (no memory)

No reranking or hybrid retrieval

Basic similarity filtering

These are engineering tradeoffs, not bugs.

▶️ How to Run
Prerequisites

Python 3.9+

Ollama installed

TinyLlama model pulled

ollama pull tinyllama

Setup
git clone https://github.com/<your-username>/mini_rag.git
cd mini_rag
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

Add Knowledge

Put your data in:

data/knowledge.txt

Ingest Data (One-Time)
python src/ingest.py

Start Q&A
python src/main.py


Ask questions related to knowledge.txt.
If the answer is not present, the system responds:

I don't know

Update Knowledge

If knowledge.txt changes:

rm -rf chroma_db
python src/ingest.py