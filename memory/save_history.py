from memory.chat_history import chat_history
def save_history(state):
    print(state)
    chathistory_instance=chat_history()
    chathistory_instance.add_chat_history(
        session_id=state["session_id"],
        message=state["query"],
        role="user"
    )
    chathistory_instance.add_chat_history(
      session_id=state["session_id"],
        message=state["summarizer_output"],
        role="assistant"
    )

    return state