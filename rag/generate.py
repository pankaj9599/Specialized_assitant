# from langchain_google_genai import GoogleGenerativeAI
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from rag.retrieve import RAGRetriever
load_dotenv()
key = os.environ.get("YOUR_GROQ_API_KEY")
print(repr(key))  # repr() shows hidden spaces, None, empty string
# llm =GoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.7,gemini_api_key=os.getenv("GOOGLE_API_KEY"))

llm = ChatGroq(
    model="llama-3.1-8b-instant",  # free & fast
    api_key=os.environ.get("YOUR_GROQ_API_KEY")    # free at console.groq.com
)

# retrieve context + generate response using the llm 
def generate_response(query:str,retriever:RAGRetriever,llm:ChatGroq,top_k:int=4,score_threshold:float=0.5)->str:
    """Generate response for a query using retrieved context and LLM
      
    args:
    input query string
    retriever: instance of RAGRetriever to retrieve relevant documents
    llm: instance of GoogleGenerativeAI to generate response
    top_k: number of relevant documents to retrieve
    score_threshold: minimum similarity score threshold for filtering retrieved documents
    returns:
    
    """
    response_from_retriever=retriever.retrieve(query,top_k=top_k,score_threshold=score_threshold)
    context="\n\n".join([doc["document"] for doc in response_from_retriever]) if response_from_retriever else "" 
    if not response_from_retriever:
        print("no relevant documents found,generating response without context")
        response=llm.invoke(query)
        return response.content
    
    # generate the answer using the llm +context  from retriever 
    prompt=f"""use the following context to answer the question:\n\n{context}\n\nQuestion:{query}\nAnswer:"""

    # response=llm.invoke([prompt.format(context=context,query=query)])
    response=llm.invoke(prompt)
    return response.content 

# answer=generate_response("what is ai agents?",RAGRetriever,llm)
# answer
