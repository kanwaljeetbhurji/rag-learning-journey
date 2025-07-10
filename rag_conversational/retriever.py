# retriever.py
import torch
from sentence_transformers.util import pytorch_cos_sim

def retrieve_top_k(query_embedding, doc_embeddings, docs, k=2):
    """
    Retrieve top-k documents based on cosine similarity between the query and documents.

    Args:
        query_embedding (tensor): Embedding for the input query.
        doc_embeddings (tensor): Embeddings for the documents.
        docs (list): Original document texts.
        k (int): Number of top documents to retrieve.

    Returns:
        list: Top-k most similar document texts.
    """
    scores = pytorch_cos_sim(query_embedding, doc_embeddings)[0]
    top_k = torch.topk(scores, k=k)
    return [docs[i] for i in top_k.indices]
