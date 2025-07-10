# run.py
from rag_pipeline import run_rag
from memory import ConversationMemory

if __name__ == "__main__":
    memory = ConversationMemory()

    while True:
        query = input("\n💬 Enter your query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break

        # Add user query to memory
        memory.add_user_message(query)

        # Run full conversational RAG pipeline
        answer = run_rag(query, memory)

        # Add assistant response to memory
        memory.add_assistant_message(answer)

        print(f"\n🧠 Memory Updated. Latest Answer:\n{answer}")
