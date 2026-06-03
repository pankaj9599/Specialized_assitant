from graph.graphbuilder import build_graph

app = build_graph()

response = app.invoke({
    "query": "Explain RAG architecture",
    "retrieved_docs": [],
    "web_results": [],
    "research_output": None,
    "review_output": None,
    "summarizer_output": None,
    "next_agent": None
})

print(response)