from recursive_controller import recursive_agentic_rag
from memory import ConversationMemory

def test_rag():
    memory = ConversationMemory()
    query = "What are the eligibility criteria for Universal Credit?"
    memory.add_user_message(query)
    answer, sources, chart, agent_log = recursive_agentic_rag(query, memory)
    memory.add_assistant_message(answer)
    print(f"Test Query: {query}\nAnswer: {answer}\nSources: {sources}\nChart: {chart}\nAgent Log: {agent_log}")

if __name__ == "__main__":
    test_rag() 