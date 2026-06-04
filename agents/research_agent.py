from langchain.chat_models import init_chat_model
from tool.llm_tool import llm
from tool.fetch_context import fetch_context
from rag.rag_service import rag_retriever
def research_agent(state):
    print("Running research")
# python -m agents.research_agent
    query=state.get("rewritten_query", state["query"])

    # Example docs
    docs,context= fetch_context(query,rag_retriever)
    # history=context_builder(state)
    prompt = f"""
    You are a research assistant.

    Your task is to answer the user query using the provided context.

    conversation history:
    {state["memory_summary"]}

    Context:
    {context}

    Query:
    {query}
    """       

    # LLM call
    answer = llm.invoke(prompt)
    
    # Update state
    state["retrieved_docs"] = docs
    state["research_output"] = answer.content


    return state
