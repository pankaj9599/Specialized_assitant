from memory.chat_history import chat_history
from tool.llm_tool import llm

def context_builder(state):
    print("Building context")
    chathistory_instance=chat_history()
    session_id = state.get("session_id")

    if not session_id:
        query = state.get("query")
        state["rewritten_query"] = query
        state["memory_summary"] = ""
        state["recent_messages"] = ""
        return state

    query=state.get("query")

    memory_summary = chathistory_instance.get_memory_summary(
        session_id
    )
    recent_messages=chathistory_instance.get_recent_message(
        session_id
    )
    prompt = f"""
    Memory Summary:
    {memory_summary}

    Recent Chat:
    {recent_messages}

    Current Query:
    {query}

    Rewrite the query by resolving references.
    Return only the rewritten query.
    """
    response = llm.invoke(prompt)

    state["rewritten_query"]=response.content.strip()
    state["memory_summary"] = memory_summary
    state["recent_messages"] = recent_messages

    return state