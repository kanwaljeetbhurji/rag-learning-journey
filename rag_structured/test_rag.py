from rag_pipeline import run_rag

def test_rag():
    query = "What are the side effects of ibuprofen?"
    answer = run_rag(query)
    print(f"Test Query: {query}\nAnswer: {answer}")

if __name__ == "__main__":
    test_rag() 