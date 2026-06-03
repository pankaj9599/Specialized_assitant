from tool.llm_tool import llm
from tool.supervisor_tool import research_tool, web_tool

def supervisor_agent(state):
    print("Running Supervisor")
    query = state["query"]

    prompt = f"""
    You are a routing agent.

    Available routes:

    research_agent
    - Use when information can be answered from internal AI documents.

    web_agent
    - Use when latest/current information is required.

    hybrid_agent
    - Use when both internal documents and current web information are needed.

    Return ONLY:
    research_agent
    web_agent
    hybrid_agent

    Query:
    {query}
    """

    response = llm.invoke(prompt)

    state["next_agent"] = response.content.strip()

    return state