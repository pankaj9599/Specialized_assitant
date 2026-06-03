import os
from dotenv import load_dotenv

from langgraph.graph import StateGraph,START,END
from agents.research_agent import research_agent
from agents.hybrid_agent import hybrid_agent
from agents.review_agent import review_agent
from agents.supervisor_agent import supervisor_agent
from agents.web_agent import web_agent
from agents.summarizer_agent import summarizer_agent # Placeholder for summarizer agent

from graph.state import AgentState;

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"] = "specialized_assitant"



print("LANGSMITH_API_KEY =", repr(os.getenv("LANGSMITH_API_KEY")))
print("LANGCHAIN_PROJECT =", repr(os.getenv("LANGCHAIN_PROJECT")))

def route_Agent(state):
     return state["next_agent"]

def build_graph():
    graph=StateGraph(AgentState)




    # NODES 
    graph.add_node("supervisor_agent",supervisor_agent)
    graph.add_node("research_agent",research_agent)
    graph.add_node("hybrid_agent",hybrid_agent)
    graph.add_node("review_agent",review_agent)
    graph.add_node("web_agent",web_agent)
    graph.add_node("summrizer_agent",summarizer_agent) 
    
    


    # EDGES
    graph.add_edge(START,"supervisor_agent")
    graph.add_conditional_edges("supervisor_agent",route_Agent,{
        "research_agent":"research_agent",
        "web_agent":"web_agent",
        "hybrid_agent":"hybrid_agent"
    })
    graph.add_edge("research_agent","review_agent")
    graph.add_edge("web_agent","review_agent")
    graph.add_edge("hybrid_agent", "review_agent")
    graph.add_edge("review_agent","summrizer_agent")
    graph.add_edge("summrizer_agent",END)

    app=graph.compile()

    return app



app = build_graph()

result = app.invoke({
    "query": "What are AI and recent mcp news ?"
})
print(result)