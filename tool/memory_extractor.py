from tool.llm_tool import llm

def memory_extractor(state):
    print("Extracting memory")
    old_memory = state.get("memory_summary", "")
    prompt = f"""
        Existing Memory:
        {old_memory}

        Current Conversation:

        User:
        {state["query"]}

        Assistant:
        {state["summarizer_output"]}

        Extract any NEW long-term facts.

        Merge them with existing memory.

        Remove duplicates.

        Keep only:
        - Projects
        - Interests
        - Goals
        - Preferences

        Return updated memory.
            """

    response = llm.invoke(prompt)

    state["memory_summary"] =response.content

    return state