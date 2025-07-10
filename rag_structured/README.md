RAG: Structured Retrieval

🧠 Overview

This module focuses on RAG using structured data such as JSON records. Retrieval is done based on field matching and embedding proximity.

⚙️ Key Components

documents.py: Loads structured records

retriever.py: Filters + retrieves relevant entries

generator.py: Formats and generates answer

rag_pipeline.py: Core logic

🧰 Tools and Libraries

Python 3.10+

json, numpy

Local LLM (TinyLLaMA or similar)

🚀 How to Run

cd rag_structured
python run.py --query "What are some benefits for pensioners?"

🎯 What You Learn

Working with structured JSON sources

Field-based filtering

Structured-to-text prompt formatting