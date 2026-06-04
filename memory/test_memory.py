
from memory.chat_history import chat_history

chat_history=chat_history()

session_id="test_session"

chat_history.add_chat_history(session_id,"AI stands for Artificial Intelligence.",role="assistant")
chat_history.add_chat_history(session_id,"What is AI?",role="user")

recent_chats=chat_history.get_recent_chat(session_id)

print(recent_chats)