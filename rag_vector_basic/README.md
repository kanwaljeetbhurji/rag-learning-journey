# RAG: Vector-Based Basic Retrieval

## 🧠 Overview

This module demonstrates a traditional Retrieval-Augmented Generation (RAG) system using simple vector-based retrieval. It loads a small document set, converts them into embeddings, retrieves the most relevant ones for a given query, and then generates an answer using a local LLM.

## ⚙️ Key Components

* `documents.py`: Loads and prepares document chunks
* `embedder.py`: Converts documents into vector embeddings
* `retriever.py`: Finds top-k relevant chunks using cosine similarity
* `generator.py`: Generates answer using prompt + retrieved context
* `rag_pipeline.py`: Orchestrates all steps of the RAG pipeline
* `run.py`: Entry point to test the RAG pipeline

## 🧰 Tools and Libraries

* Python 3.10+
* `sentence-transformers` (for embeddings)
* `transformers` (for generation)
* `numpy`, `scikit-learn`, `json`

## 🚀 How to Run

```bash
cd rag_vector_basic
python run.py --query "What are the effects of ibuprofen?"
```

## 🧪 Sample Output

```bash
Query: What are the effects of ibuprofen?
Answer: Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) used for pain relief, reducing fever, and inflammation.
```

## 🎯 What You Learn

* Basics of embedding documents
* Cosine similarity retrieval
* Prompt augmentation
* Integration with a local small language model (SLM)

---

✅ Start here if you're new to RAG and want a clean, working baseline implementation.
