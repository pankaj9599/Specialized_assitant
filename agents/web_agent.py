from tool.tavily_tool import tavily_tool
from tool.llm_tool import llm
def web_agent(state):
    print("Running web")
    query = state["query"]
    
    # Simulate web search results
    web_results = tavily_tool.invoke(query)

    prompt = f"""
    You are an expert research analyst and editor.

    Your task:
    1. Read the raw web research provided below.
    2. Extract the most relevant, accurate, and useful information.
    3. Remove duplicate, low-quality, promotional, or irrelevant content.
    4. Verify consistency between sources when possible.
    5. Organize the information into a clean, structured response.
    6. Improve clarity, grammar, readability, and logical flow.
    7. Add concise explanations where needed.
    8. Keep the response factual and professional.
    9. If the web data contains conflicting claims, mention the conflict clearly.
    10. Return the final answer in markdown format.

    Web Research Data:
    -------------------
    {web_results}
    -------------------

    Output Requirements:
    - Well-structured markdown
    - Use headings and bullet points where appropriate
    - Include a short summary at the top
    - Keep only high-signal information
    - Do not invent facts not present in the source data
    - Make the final response concise but complete
    """

    ans = llm.invoke(prompt)

    state["web_results"] = ans.content
    # state["web_output"]=ans.content
    # state["next_agent"] = "review_agent"

    return state