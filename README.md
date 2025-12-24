# Mini-RAG: CPU-Friendly Retrieval-Augmented Generation System

A lightweight, modular **Retrieval-Augmented Generation (RAG)** system built for **CPU-only environments**.  
It uses **ChromaDB** for vector storage, **MiniLM embeddings** for semantic search, and a **local FLAN-T5 model** for answer generation.  

This project demonstrates a **full RAG pipeline** with **modular, maintainable code**, suitable for small to medium text knowledge bases.

---

## 🚀 Features

- **Semantic retrieval** using `all-MiniLM-L6-v2` embeddings
- **ChromaDB vector database** for scalable, persistent storage
- **CPU-friendly LLM generation** with `google/flan-t5-small`
- **Proper chunking with overlap** for improved retrieval quality
- Modular structure: easy to maintain, extend, or swap components
- CLI-based interactive Q&A loop

---

## 🗂 Project Structure

mini_rag/
│
├── data/
│ └── knowledge.txt # Knowledge base (text)
│
├── src/
│ ├── init.py
│ ├── loader.py # Loading + chunking text
│ ├── vector_store.py # ChromaDB init, add, query
│ ├── retrieval.py # Retrieval logic (optional thresholds)
│ ├── generator.py # LLM prompt + answer generation
│ └── main.py # Main interactive CLI
│
├── requirements.txt
└── README.md

Answers questions strictly from a local text file.

1. Load text
2. Split into chunks
3. Embed chunks
4. Store embeddings
5. Accept user query
6. Embed query
7. Retrieve relevant chunks
8. Ask LLM using retrieved text

Workflow

knowledge.txt
      ↓
Text Loader
      ↓
Text Chunking
      ↓
Embedding Model (MiniLM)
      ↓
Vector Store (in-memory)
      ↓
User Query
      ↓
Query Embedding
      ↓
Similarity Search (cosine)
      ↓
Top-K Relevant Chunks
      ↓
Displayed Answer (retrieved text)


## Architecture Overview

### File-Level Workflow
This project follows a modular RAG architecture where each component has a single responsibility.

![RAG File Workflow](docs/rag_file_level_workflow.png)
