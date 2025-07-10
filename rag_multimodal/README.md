RAG: Multimodal Retrieval

🧠 Overview

This module demonstrates a Multimodal RAG system combining structured data and images. It retrieves both text and image context based on the query, augments the prompt, and displays answers alongside visual elements.

⚙️ Key Components

documents.py: Loads structured + image metadata

retriever.py: Retrieves structured records

generator.py: Generates answer using context

memory.py: Maintains chat history

static/: Stores visual charts/images

templates/result.html: Renders text + images in HTML

🧰 Tools and Libraries

Python 3.10+

flask, jinja2 for web interface

matplotlib or Pillow for image generation

Local LLM for answer generation

🚀 How to Run

cd rag_multimodal
python app.py  # then visit http://localhost:5000

🎯 What You Learn

Multimodal retrieval (text + image)

Web-based augmentation and rendering

Context formatting for LLMs