# rag_pipeline.py
from embedder import embed_texts
from retriever import retrieve_structured_context
from generator import call_ollama_model
from memory import ConversationMemory

def run_rag(query, memory):
    print("\n=== STEP 1: Full Chat History ===")
    print(memory.get_formatted_history())

    print("\n=== STEP 2: Retrieval (Structured + Embedding)")  # only structured now
    retrieved_docs = retrieve_structured_context(query, "data/medications.json", top_k=3)

    print("\n=== STEP 3: Prompt Augmentation ===")
    history = memory.get_formatted_history()
    context = "\n".join(
        f"- {doc['name']}: used for {', '.join(doc['used_for'])}. Side effects: {', '.join(doc['side_effects'])}."
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
    
    print("\n=== SOURCES USED ===")
    for i, doc in enumerate(retrieved_docs, 1):
        name = doc.get("name", "Unknown")
        category = doc.get("category", "N/A")
        used_for = ", ".join(doc.get("used_for", []))
        print(f"[{i}] {name} ({category}) - Used for: {used_for}")


    return answer, retrieved_docs  # full doc dicts for frontend
