# generator.py
import subprocess

def call_ollama_model(prompt):
    """
    Sends the full augmented prompt to TinyLLaMA using Ollama.

    Args:
        prompt (str): The complete prompt (history + context + query).

    Returns:
        str: Model-generated answer or error message.
    """
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
