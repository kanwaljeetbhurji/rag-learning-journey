# run.py
from rag_pipeline import run_rag

if __name__ == "__main__":
    while True:
        query = input("\n💬 Enter your query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        answer = run_rag(query)
        print(answer)
