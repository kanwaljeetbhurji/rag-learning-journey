RAG: Conversational Memory

🧠 Overview

This module implements memory-aware RAG with free-form documents. User inputs and assistant responses are remembered and used for better context.

⚙️ Key Components

memory.py: Tracks conversation turns

retriever.py: Uses recent history to influence retrieval

generator.py: Uses memory + docs to respond

🧰 Tools and Libraries

Python 3.10+

sentence-transformers, json, transformers

🚀 How to Run

cd rag_conversational
python run.py

🎯 What You Learn

Long context usage

Memory injection into RAG

Dialogue coherence via history