from tool.llm_tool import llm
def review_agent(state):
    print("Running review")
    query=state["query"]
    research_output = state.get(
        "research_output",
        ""
    )

    web_output = state.get(
        "web_output",
        ""
    )
    # Example review
    review_prompt = f"""
    You are a review agent.

    User Query:
    {query}

    Research Information:
    {research_output}

    Web Information:
    {web_output}

    Tasks:

    1. Merge the research and web information.
    2. Remove duplicate information.
    3. Identify contradictions.
    4. Flag unsupported claims.
    5. Add missing context if necessary.
    6. Produce a single improved draft answer.

    Return only the improved draft.
    """
    review_output=llm.invoke(review_prompt)

    state["review_output"]=review_output.content
    # state["next_agent"]="summarizer_agent"
    return state
