# tools/answer_evaluator.py

def is_answer_sufficient(answer):
    """
    Checks if the generated answer is detailed enough.
    Very basic for now; we can plug in LLM or keyword-based scorer later.
    """
    return len(answer.split()) > 50  # Example: >50 words is "sufficient"

def generate_followup_query(original_query, previous_answer):
    """
    Generates a new query to dig deeper based on prior answer.
    """
    return f"Can you give more specifics about: {original_query}?"
