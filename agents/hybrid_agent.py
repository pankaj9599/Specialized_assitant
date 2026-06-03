from agents.research_agent import research_agent
from agents.web_agent import web_agent


def hybrid_agent(state):
    print("Running hybrid")
    state=research_agent(state)
    state=web_agent(state)

    return state