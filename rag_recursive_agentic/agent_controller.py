# agent_controller.py
from rag_pipeline import run_rag
from tools.plotter import plot_bar_chart

def agentic_rag(query, memory, prior_domain=None, prior_source=None):
    print(f"\n[Agent] Received query: {query}")
    agent_log = ""
    domain, source = None, None

    lowered = query.lower()
    if "fund" in lowered or "investment" in lowered or "esg" in lowered:
        domain = "finance"
        source = "data/esg_funds.json"
        agent_log = "Identified domain: Investment Funds (ESG)"
    elif "benefit" in lowered or "government" in lowered or "credit" in lowered:
        domain = "benefits"
        source = "data/gov_benefits.json"
        agent_log = "Identified domain: UK Government Benefits"
    elif prior_domain and prior_source:
        domain = prior_domain
        source = prior_source
        agent_log = f"⏪ Reused prior domain: {domain}"
    elif memory.last_domain and memory.last_source:
        domain = memory.last_domain
        source = memory.last_source
        agent_log = f"⏪ Reused domain from memory: {domain}"
    else:
        return "❌ Agent: Sorry, I couldn't identify a valid domain (funds or benefits).", [], None, "No domain identified"

    # Save domain info to memory
    memory.last_domain = domain
    memory.last_source = source

    # Run RAG
    answer, retrieved_docs = run_rag(query, memory, source_path=source)

    # Chart (only for finance mode)
    chart_path = None
    if domain == "finance":
        chart_path = plot_bar_chart(
            retrieved_docs,
            x_field="name",
            y_field="three_year_return",
            title="Top ESG Funds",
            xlabel="Fund",
            ylabel="Return (%)"
        )
        agent_log += "; Chart generated."

    return answer, retrieved_docs, chart_path, agent_log
