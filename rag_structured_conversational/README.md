RAG: Structured + Conversational

🧠 Overview

This module builds on structured RAG and adds memory-based conversation support. Useful for persistent multi-turn interactions over structured datasets.

⚙️ Key Components

memory.py: Maintains full chat history

documents.py, retriever.py: Structured data retrieval

rag_pipeline.py: Prompt composition with memory

run.py: Entry point for query loop

🧰 Tools and Libraries

Python 3.10+

json, termcolor

Local LLM (TinyLLaMA or similar)

🚀 How to Run

cd rag_structured_conversational
python run.py

🎯 What You Learn

Multi-turn memory with structured data

Dynamic query resolution over turns