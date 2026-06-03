from langchain_tavily import TavilySearch
import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
tavily_api=os.getenv("TAVILY_API_KEY")

@tool
def tavily_tool(query:str)->str:
    """Swearch the web for recent information"""
    # use tavily for search 
    tavily=TavilySearchResults(max_results=2)
    result=tavily.invoke(query)
    return str(result)