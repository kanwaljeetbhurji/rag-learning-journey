# run.py
from rag_recursive_agentic.recursive_controller import recursive_agentic_rag
from memory import ConversationMemory

memory = ConversationMemory()

while True:
    query = input("\n💬 Enter your query (or 'exit'): ")
    if query.lower() == "exit":
        break

    memory.add_user_message(query)
    result = recursive_agentic_rag(query, memory)

    answer, sources, chart, agent_log = result
    memory.add_assistant_message(answer)

    print("\n🧠 Answer:\n", answer)
    if sources:
        print("\n📚 Sources:")
        for doc in sources:
            print(f"- {doc['name']}")
    if chart:
        print(f"\n📊 Chart saved at: {chart}")
    print(f"\n🤖 Agent Log:\n{agent_log}")
