# rag_pipeline.py
from retriever import retrieve_structured_context
from generator import call_ollama_model
from memory import ConversationMemory

def run_rag(query, memory, source_path):
    print("\n=== STEP 1: Full Chat History ===")
    print(memory.get_formatted_history())

    print("\n=== STEP 2: Retrieval (Structured + Embedding)")
    retrieved_docs = retrieve_structured_context(query, source_path, top_k=3)

    print("\n=== STEP 3: Prompt Augmentation ===")
    history = memory.get_formatted_history()
    context = "\n".join(
        f"- {doc['name']}: {doc.get('description', 'No description')} | Category: {doc.get('category', 'N/A')}."
        for doc in retrieved_docs
    )

    prompt_preview = f"""
You are a helpful assistant. Use the context below and conversation history to answer the user's latest question.

Chat History:
{history}

Context:
{context}

Question:
{query}

Answer:"""

    print(prompt_preview)
    print("\n=== STEP 4: Generating Answer via TinyLLaMA ===")
    answer = call_ollama_model(prompt_preview)

    print("\n=== FINAL ANSWER ===")
    print(answer)

    return answer, retrieved_docs
