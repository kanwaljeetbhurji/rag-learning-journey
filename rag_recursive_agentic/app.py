# app.py
from flask import Flask, render_template, request
from recursive_controller import recursive_agentic_rag
from memory import ConversationMemory

app = Flask(__name__)
memory = ConversationMemory()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    query = request.form["query"]
    memory.add_user_message(query)

    answer, retrieved, chart, agent_log = recursive_agentic_rag(query, memory)
    memory.add_assistant_message(answer)

    return render_template("result.html", query=query, answer=answer,
                           retrieved=retrieved, chart=chart, agent_log=agent_log)

if __name__ == "__main__":
    app.run(debug=True)
