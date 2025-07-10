# retriever.py
import torch
from sentence_transformers.util import pytorch_cos_sim

def retrieve_top_k(query_embedding, doc_embeddings, docs, k=2):
    scores = pytorch_cos_sim(query_embedding, doc_embeddings)[0]
    top_k = torch.topk(scores, k=k)
    return [docs[i] for i in top_k.indices]
