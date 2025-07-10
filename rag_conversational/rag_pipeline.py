# rag_pipeline.py
from embedder import embed_texts
from retriever import retrieve_top_k
from generator import call_ollama_model
from documents import docs  # Can later be swapped with structured source
from memory import ConversationMemory

def run_rag(query, memory):
    print("\n=== STEP 1: Full Chat History ===")
    print(memory.get_formatted_history())

    print("\n=== STEP 2: Embedding Query & Documents ===")
    doc_embeddings = embed_texts(docs)
    query_embedding = embed_texts([query])[0]

    print("\n=== STEP 3: Retrieval (Top-K Matching Docs) ===")
    retrieved_docs = retrieve_top_k(query_embedding, doc_embeddings, docs, k=2)
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"{i}. {doc}")

    print("\n=== STEP 4: Prompt Augmentation ===")
    history = memory.get_formatted_history()
    context = "\n".join(f"- {doc}" for doc in retrieved_docs)

    prompt_preview = f"""
You are a helpful assistant. Use the context below to answer the user's question.

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
    return answer
