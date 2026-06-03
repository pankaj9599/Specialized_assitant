import os 
from rag.vector_store import VectorStore
from rag.embedding import EmbeddingManager
from typing import List,Any,Dict,Tuple
class RAGRetriever:
    """Retriever for retrieving relevant documents from the vector store based on query embeddings.
    
    Args:
        vector_store: Instance of the vector store to retrieve from.
        embedding_manager: Instance of the embedding manager to generate query embeddings.
    """
    def __init__(self, vector_store: VectorStore, embedding_manager: EmbeddingManager):
        self.vector_store = vector_store
        self.embedding_manager = embedding_manager

    def retrieve(self, query: str, top_k: int = 5, score_threshold: float = 0.0) -> List[Dict[str, Any]]:
        """Retrieve relevant documents based on query.
        
        Args:
            query: Input query string to search for relevant documents.
            top_k: Number of top relevant documents to retrieve.
            score_threshold: Minimum similarity score threshold for filtering results.
            
        Returns:
            List of dicts containing document text, metadata, scores, and rank.
        """
        print(f"Retrieving relevant documents for query: {query}")
        print(f"{top_k} relevant docs will be retrieved, score {score_threshold} will be applied if specified")

        # Generate query embeddings
        query_embedding = self.embedding_manager.generate_embeddings([query])

        # Search in vector DB
        try:
            result = self.vector_store.collection.query(
                query_embeddings=[query_embedding[0].tolist()],
                n_results=top_k,
            )

            retrieve_doc = []
            if result['documents'] and result['documents'][0]:
                documents = result['documents'][0]
                metadatas = result['metadatas'][0]
                distances = result['distances'][0]
                ids = result['ids'][0]

                for i, (doc, md, distance, doc_id) in enumerate(zip(documents, metadatas, distances, ids)):
                    # Convert distance to similarity score using cosine similarity
                    similarity_score = 1 - distance
                    if similarity_score >= score_threshold:
                        retrieve_doc.append({
                            "id": doc_id,
                            "document": doc,       
                            "metadata": md,        
                            "similarity_score": similarity_score,
                            "distance": distance,  
                            "rank": i + 1          
                        })

                if retrieve_doc:
                    print(f"Retrieved {len(retrieve_doc)} relevant documents for query: {query}")
                else:
                    print(f"No relevant documents found for query: {query} with score above {score_threshold}")

            return retrieve_doc

        except Exception as e:
            print(f"Error retrieving documents from vector store: {e}")
            raise  


# RAGRetriever = RAGRetriever(vectorStore, embeddingmanager)