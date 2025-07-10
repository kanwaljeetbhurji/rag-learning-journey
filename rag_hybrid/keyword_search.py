# keyword_search.py
import re
from collections import defaultdict

class KeywordIndex:
    def __init__(self, documents):
        self.keyword_map = defaultdict(set)
        self.documents = documents

        for i, doc in enumerate(documents):
            words = re.findall(r'\w+', doc.lower())
            for w in words:
                self.keyword_map[w].add(i)

    def search(self, query, top_k=5):
        query_words = re.findall(r'\w+', query.lower())
        matched_doc_ids = set()

        for w in query_words:
            if w in self.keyword_map:
                matched_doc_ids.update(self.keyword_map[w])

        doc_scores = []
        for doc_id in matched_doc_ids:
            doc_text = self.documents[doc_id].lower()
            score = sum(1 for w in query_words if w in doc_text)
            doc_scores.append((score, doc_id))

        doc_scores.sort(key=lambda x: x[0], reverse=True)

        return [self.documents[doc_id] for _, doc_id in doc_scores[:top_k]]
