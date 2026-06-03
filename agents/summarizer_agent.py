from tool.llm_tool import llm

def summarizer_agent(state):
    print("Running summarizer")
    review_output = state["review_output"]

    summarize_prompt = f"""
    You are an AI Summarizer Agent specialized in:

    - AI
    - LLMs
    - RAG
    - Prompt Engineering
    - AI Agents
    - Agentic Systems

    Your task:

    - Create a concise final answer
    - Remove repetition
    - Improve readability
    - Preserve technical accuracy
    - Use headings and bullet points when useful
    - Focus on practical insights

    Draft Answer:
    {review_output}
    """

    response = llm.invoke(summarize_prompt)

    state["summarizer_output"] = response.content

    return state