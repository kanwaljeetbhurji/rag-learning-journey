# RAG: Hybrid (Sparse + Dense) Retrieval

## 🧠 Overview
This module showcases a Hybrid Retrieval-Augmented Generation (RAG) approach that combines both sparse (BM25) and dense (embedding-based) retrieval. It boosts the relevance of the retrieved context by leveraging the strengths of both methods before generating an answer using a local language model.

## ⚙️ Key Components
- `documents.py`: Loads and chunks input documents
- `embedder.py`: Generates dense vector embeddings
- `retriever.py`: Combines BM25 (sparse) and cosine similarity (dense) to fetch top results
- `generator.py`: Forms the prompt with top-k results and passes it to a local model
- `rag_pipeline.py`: Coordinates retrieval and generation
- `run.py`: CLI entry point

## 🧰 Tools and Libraries
- Python 3.10+
- `rank_bm25` (for sparse BM25 retrieval)
- `sentence-transformers` (dense embeddings)
- `transformers` (LLM inference)
- `scikit-learn`, `numpy`, `json`

## 🚀 How to Run
```bash
cd rag_hybrid
python run.py --query "What are the side effects of ibuprofen?"
