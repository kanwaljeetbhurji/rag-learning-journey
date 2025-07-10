from rag_pipeline import run_rag
from tools.plotter import plot_bar_chart
import os

def agentic_rag(query, memory):
    print(f"\n[Agent] Received query: {query}")
    agent_log = ""

    # Step 1: Choose source
    if "fund" in query.lower() or "investment" in query.lower():
        source = "data/esg_funds.json"
        mode = "finance"
        agent_log = "Identified domain: Investment Funds (ESG)"
    elif "benefit" in query.lower() or "government" in query.lower() or "credit" in query.lower():
        source = "data/gov_benefits.json"
        mode = "benefits"
        agent_log = "Identified domain: UK Government Benefits"
    else:
        return "\u274c Agent: Sorry, I couldn't identify a valid domain (funds or benefits).", [], None, "No domain identified"

    # Step 2: Run RAG pipeline
    answer, retrieved_docs = run_rag(query, memory, source_path=source)

    # Step 3: Generate chart (only for finance mode)
    chart_path = None
    if mode == "finance":
        chart_path = plot_bar_chart(retrieved_docs, "name", "three_year_return", "Top ESG Funds", "Fund", "Return (%)")
        agent_log += "; Generated bar chart for fund returns."

    return answer, retrieved_docs, chart_path, agent_log