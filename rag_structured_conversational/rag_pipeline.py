# rag_pipeline.py
from embedder import embed_texts
from retriever import retrieve_structured_context, load_medications
from generator import call_ollama_model

from memory import ConversationMemory
import os

def run_rag(query, memory):
    print("\n=== STEP 1: Full Chat History ===")
    print(memory.get_formatted_history())

    print("\n=== STEP 2: Load Structured Data ===")
    structured_docs = load_medications("data/medications.json")  # ✅ FIXED PATH

    print("\n=== STEP 3: Retrieval (Top-K Matching Records) ===")
    retrieved_docs = retrieve_structured_context(query, "data/medications.json", top_k=2)
    if not retrieved_docs:
        print("⚠️ No relevant documents found.")
    for i, r in enumerate(retrieved_docs, 1):
        print(f"{i}. {r['name']} ({r['category']})")

    print("\n=== STEP 4: Prompt Augmentation ===")
    history = memory.get_formatted_history()
    context = "\n".join(
        f"- {r['name']} ({r['category']}): used for {', '.join(r['used_for'])}; side effects include {', '.join(r['side_effects'])}"
        for r in retrieved_docs
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

    print("\n=== STEP 5: Generating Answer via TinyLLaMA ===")
    answer = call_ollama_model(prompt_preview)

    print("\n=== FINAL ANSWER ===")
    print(answer)

    print("\n=== SOURCES USED ===")
    for i, r in enumerate(retrieved_docs, 1):
        print(f"[{i}] {r['name']} ({r['category']}) — used for {', '.join(r['used_for'])}")

    return answer
