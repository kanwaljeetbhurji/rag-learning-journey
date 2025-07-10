def needs_followup(answer, query):
    print("[Planner] Checking if recursion is needed...")
    print("Answer content (truncated):", answer[:200])
    print("User query:", query)
    return any(
        phrase in answer.lower()
        for phrase in [
            "i'm unable to",
            "i can't",
            "not sure",
            "not enough info",
            "insufficient",
            "couldn't find",
            "sorry",
            "couldn't identify",
            "domain not found"
        ]
    )
