# retriever.py (Hybrid with source tagging for debug)
import torch
from sentence_transformers.util import pytorch_cos_sim
from keyword_search import KeywordIndex

def retrieve_top_k(query_embedding, doc_embeddings, docs, query, k=2):
    # --- Vector Similarity Retrieval ---
    scores = pytorch_cos_sim(query_embedding, doc_embeddings)[0]
    top_k_vector = torch.topk(scores, k=k)
    vector_results = [docs[i] for i in top_k_vector.indices]

    print("\n--- 🔍 Vector Retrieval ---")
    for i, doc in enumerate(vector_results, 1):
        print(f"{i}. {doc}")

    # --- Keyword Search Retrieval ---
    keyword_index = KeywordIndex(docs)
    keyword_results = keyword_index.search(query, top_k=k)

    print("\n--- 🔤 Keyword Retrieval ---")
    for i, doc in enumerate(keyword_results, 1):
        print(f"{i}. {doc}")

    # --- Merge and Deduplicate ---
    combined = list(dict.fromkeys(vector_results + keyword_results))

    return combined[:k*2]
