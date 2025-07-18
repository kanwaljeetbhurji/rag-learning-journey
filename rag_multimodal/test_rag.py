from rag_pipeline import run_rag
from memory import ConversationMemory

def test_rag():
    memory = ConversationMemory()
    query = "What is ibuprofen used for?"
    memory.add_user_message(query)
    answer, retrieved = run_rag(query, memory)
    memory.add_assistant_message(answer)
    print(f"Test Query: {query}\nAnswer: {answer}\nRetrieved: {retrieved}")

if __name__ == "__main__":
    test_rag() 