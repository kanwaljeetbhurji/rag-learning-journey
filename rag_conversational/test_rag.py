from rag_pipeline import run_rag
from memory import ConversationMemory

def test_rag():
    memory = ConversationMemory()
    query = "What are the side effects of aspirin?"
    memory.add_user_message(query)
    answer = run_rag(query, memory)
    memory.add_assistant_message(answer)
    print(f"Test Query: {query}\nAnswer: {answer}")

if __name__ == "__main__":
    test_rag() 