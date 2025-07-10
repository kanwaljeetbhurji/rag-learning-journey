# recursive_controller.py

from rag_pipeline import run_rag
from tools.answer_evaluator import is_answer_sufficient, generate_followup_query

def recursive_rag(query, memory, max_depth=2):
    """
    Orchestrates recursive refinement of answers using RAG.
    """
    all_contexts = []
    full_answer = ""

    for depth in range(max_depth):
        print(f"\n🔁 Recursive Pass {depth + 1}: {query}")
        answer, retrieved_docs = run_rag(query, memory)

        all_contexts.extend(retrieved_docs)
        memory.add_assistant_message(answer)
        full_answer += f"\nPASS {depth + 1}:\n{answer}\n"

        if is_answer_sufficient(answer):
            print("✅ Answer is sufficient. Stopping recursion.")
            break

        # Generate refined query
        query = generate_followup_query(query, answer)
        memory.add_user_message(query)

    return full_answer.strip(), all_contexts
