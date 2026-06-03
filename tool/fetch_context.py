def fetch_context(query,retriever):
    """
    Retrieve relevant context
    from vector database.
    """

    docs=retriever.retrieve(
        query,
        top_k=4
    )

    # docs=retrieve_docs(query)
    context="\n".join(doc["document"] for doc in docs)

    return context,docs