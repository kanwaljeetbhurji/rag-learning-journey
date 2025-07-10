# retriever.py
import json
import re

def load_medications(json_path="medications.json"):
    with open(json_path, "r") as f:
        return json.load(f)

def preprocess(text):
    return re.findall(r"\w+", text.lower())

def retrieve_structured_context(query, json_path="medications.json", top_k=4):
    query_tokens = preprocess(query)
    query_tokens_set = set([token.rstrip('s') for token in query_tokens])

    all_records = load_medications(json_path)
    matched = []

    for record in all_records:
        searchable_parts = [
            record.get("name", ""),
            record.get("category", ""),
            " ".join(record.get("used_for", [])),
            " ".join(record.get("side_effects", [])),
            str(record.get("child_safe", "")).lower()
        ]
        searchable_text = " ".join(searchable_parts).lower()
        searchable_tokens = set([token.rstrip('s') for token in preprocess(searchable_text)])

        if query_tokens_set & searchable_tokens:
            matched.append(record)

    return matched[:top_k]
