# rag_pipeline.py
import os
from retriever import retrieve_structured_context
from generator import call_ollama_model

DATA_PATH = os.path.join("data", "medications.json")

def run_rag(query):
    print("\n=== STEP 1: Original Query ===")
    print(query)

    print("\n=== STEP 2: Retrieving Structured Context ===")
    structured_records = retrieve_structured_context(query, DATA_PATH, top_k=4)

    if not structured_records:
        print("⚠️ No relevant records found.")
        return "No matching medication found."

    for i, record in enumerate(structured_records, 1):
        print(f"{i}. {record['name']} - {record['used_for']}")

    print("\n=== STEP 3: Prompt Augmentation ===")
    context = "\n".join([f"- {record}" for record in structured_records])
    prompt = f"""You are a helpful assistant. Use the structured medication records below to answer the user's question.

Context:
{context}

Question:
{query}

Answer:"""
    print(prompt)

    print("\n=== STEP 4: Generating Answer via TinyLLaMA ===")
    answer = call_ollama_model(query, [context])
    print("\n=== FINAL ANSWER ===")
    print(answer)
    return answer
