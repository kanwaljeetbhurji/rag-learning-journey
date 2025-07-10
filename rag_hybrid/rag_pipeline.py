# rag_pipeline.py
from embedder import embed_texts
from retriever import retrieve_top_k
from generator import call_ollama_model
from documents import docs

def run_rag(query):
    print("\n=== STEP 1: Original Query ===")
    print(query)

    print("\n=== STEP 2: Embedding Query & Documents ===")
    doc_embeddings = embed_texts(docs)
    query_embedding = embed_texts([query])[0]

    print("\n=== STEP 3: Retrieval (Hybrid: Vector + Keyword) ===")
    retrieved_docs = retrieve_top_k(query_embedding, doc_embeddings, docs, query, k=2)
    for i, doc in enumerate(retrieved_docs, 1):
        print(f"{i}. {doc}")

    print("\n=== STEP 4: Prompt Augmentation ===")
    prompt_preview = f"""You are an expert assistant. Use the following context to answer the user's question.

Context:
{chr(10).join(f'- {doc}' for doc in retrieved_docs)}

Question:
{query}

Answer:"""
    print(prompt_preview)

    print("\n=== STEP 5: Generating Answer via TinyLLaMA ===")
    answer = call_ollama_model(query, retrieved_docs)
    print("\n=== FINAL ANSWER ===")
    print(answer)
    return answer
