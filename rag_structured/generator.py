# generator.py
import subprocess

def call_ollama_model(query, context_docs):
    """
    Call the local tinyllama model via Ollama with a prompt augmented by retrieved docs.

    Args:
        query (str): User question.
        context_docs (list of str): Retrieved context documents.

    Returns:
        str: Generated answer or error message.
    """
    context = "\n".join(f"- {doc}" for doc in context_docs)
    prompt = f"""You are an expert assistant. Use the following context to answer the user's question.

Context:
{context}

Question:
{query}

Answer:"""

    try:
        process = subprocess.Popen(
            ["ollama", "run", "tinyllama"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=prompt, timeout=90)

        if process.returncode != 0:
            print("⚠️ Ollama error:", stderr)
            return "⚠️ Model execution failed."

        if not stdout.strip():
            return "⚠️ No output received from model."

        return stdout.strip()

    except subprocess.TimeoutExpired:
        return "⏳ Model timed out. Try again or simplify the query."
