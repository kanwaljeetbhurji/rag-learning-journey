# RAG Learning Journey 🚀

This repository documents a hands-on, free, and local-only exploration of **Retrieval-Augmented Generation (RAG)** systems. Each subfolder contains a working example of a different RAG type, progressing from traditional to agentic and multimodal forms.

## 🎯 Purpose
This repo is designed to **train yourself** to become an AI Engineer capable of building real-world RAG systems end-to-end.

No APIs. No cloud dependencies. Everything runs **locally**.

---

## 📂 RAG Types & Folders
- [`rag_vector_basic`](rag_vector_basic/): 🔹 Basic vector-store-based RAG using local embeddings and retrieval.
- [`rag_hybrid`](rag_hybrid/): 🔸 Combines sparse keyword search with dense embedding retrieval for better coverage.
- [`rag_structured`](rag_structured/): 📊 Retrieves answers from structured JSON (e.g. tables) instead of plain text.
- [`rag_conversational`](rag_conversational/): 🗣️ Adds memory to enable follow-up queries and multi-turn dialogue.
- [`rag_structured_conversational`](rag_structured_conversational/): 💬 Combines structured retrieval with conversational memory for domain-focused Q&A.
- [`rag_multimodal`](rag_multimodal/): 🖼️ Retrieves both text and images (e.g. pill diagrams), augments prompts and displays outputs with charts.
- [`rag_recursive_agentic`](rag_recursive_agentic/): ♻️ Combines agent-style planning with recursive refinement and follow-up generation.
- [`rag_recursive_and_agentic`](rag_recursive_and_agentic/): 🔁 Includes **recursive** RAG and **agentic** RAG separately for comparison.

---
## 🧰 Tools & Libraries Used
- Python 3.10+
- Flask (for web interface)
- `faiss`, `scikit-learn`, or local vector store libraries
- `matplotlib` for charts
- `spacy` for NLP parsing
- `tinyllama` or other small LLMs run locally

---
## 🖼️ Architecture Diagram (Text Version)
```
[User Query] --> [Memory] --> [Retriever (Structured + Vector)] --> [Prompt Augmentor]
    --> [Local LLM (e.g. TinyLLaMA)] --> [Response]
                                ⤷ [Planner/Agent (optional)] ⤶
                                ⤷ [Recursive Follow-up (optional)] ⤶
```

---
## 💻 Setup Instructions
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/rag-learning-journey.git
cd rag-learning-journey

# Set up virtualenv (Mac & Windows)
python3 -m venv ragvirtualenv
source ragvirtualenv/bin/activate  # or ragvirtualenv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---
## ✅ How to Test
Each subfolder has its own `run.py`. For example:
```bash
cd rag_structured
python run.py
```
Then open `http://localhost:5000` to test in the browser.

---
## 📄 License
MIT (free to learn, adapt, and share)