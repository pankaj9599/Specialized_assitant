from typing import TypedDict,List
class AgentState(TypedDict):
    query:str
    rewritten_query:str

    memory_summary: str          # long-term summary
    recent_messages: str     # last few messages
    session_id: str

    retrieved_docs:List[str]
    web_results:List[str]
    web_output:str
    research_output:str
    review_output:str
    summarizer_output:str
    next_agent:str