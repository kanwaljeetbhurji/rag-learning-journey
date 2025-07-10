# recursive_controller.py
from agent_controller import agentic_rag
from planner import needs_followup
from memory import ConversationMemory

def recursive_agentic_rag(query, memory, max_turns=2):
    print(f"\n🔁 Recursive Pass 1: {query}")
    all_sources = []
    all_logs = []
    final_chart = None

    # Pass 1
    answer, sources, chart, agent_log = agentic_rag(query, memory)
    memory.add_assistant_message(answer)

    all_sources.extend(sources)
    all_logs.append(f"[Agent Log: Pass 1] {agent_log}")
    if chart:
        final_chart = chart

    if not needs_followup(answer, query) or max_turns <= 1:
        return answer, all_sources, final_chart, "\n".join(all_logs)

    # Pass 2 (recursive follow-up)
    print("🔁 Agent triggered recursive follow-up")
    followup_query = "What more can you tell me about that?"
    memory.add_user_message(followup_query)

    followup_answer, sources2, chart2, agent_log2 = agentic_rag(followup_query, memory)
    memory.add_assistant_message(followup_answer)

    all_sources.extend(sources2)
    all_logs.append(f"[Agent Log: Pass 2] {agent_log2}")
    if chart2:
        final_chart = chart2  # Use updated chart if available

    combined_answer = f"{answer}\n\n---\n\n{followup_answer}"
    combined_log = "\n".join(all_logs)

    return combined_answer, all_sources, final_chart, combined_log
