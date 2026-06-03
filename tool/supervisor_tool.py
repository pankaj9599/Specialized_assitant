from langchain.tools import tool


@tool
def research_tool(query: str):
    """Use for explanations, AI concepts, learning, and research."""
    return "research"

@tool
def web_tool(query: str):
    """Use for latest information, current events, and web search."""
    return "web"