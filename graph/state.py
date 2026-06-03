from typing import TypedDict,List
class AgentState(TypedDict):
    query:str
    retrieved_docs:List[str]
    web_results:List[str]
    web_output:str
    research_output:str
    review_output:str
    summarizer_output:str
    next_agent:str