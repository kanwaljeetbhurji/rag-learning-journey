from agent_controller import agentic_rag
from memory import ConversationMemory

memory = ConversationMemory()

while True:
    query = input("\n\ud83d\udcac Enter your query (or 'exit'): ")
    if query.lower() == "exit":
        break

    memory.add_user_message(query)
    answer, sources, chart_path, agent_log = agentic_rag(query, memory)
    memory.add_assistant_message(answer)

    print("\n\ud83e\udde0 Answer:\n", answer)
    if sources:
        print("\n\ud83d\udcda Sources:")
        for doc in sources:
            print(f"- {doc['name']}")
    if chart_path:
        print(f"\n\ud83d\udcca Chart saved at: {chart_path}")
    if agent_log:
        print(f"\n\ud83e\uddd0 Agent Log: {agent_log}")