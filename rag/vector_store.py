from rag.embedding import EmbeddingManager
import chromadb
from chromadb.config import Settings
import os
import uuid
from typing import List,Any,Dict,Tuple
import numpy as np

class VectorStore:
    """manage vector storage and retrieval using chromadb
    """
    def __init__(self,collection_name:str="pdf_documents",persist_directory:str="data/vector_db"):
        """initialize the vector store with collection name and persist directory"""
        self.collection_name=collection_name
        self.persist_directory=persist_directory
        self.client=None
        self.collection=None
        self._initialize_store()

    def _initialize_store(self):
        """intialize the chromadb client and collection"""   
        try:
            os.makedirs(self.persist_directory,exist_ok=True)
            self.client=chromadb.PersistentClient(path=self.persist_directory)
            
            # get or create collection 
            self.collection=self.client.get_or_create_collection(name=self.collection_name,
                                 metadata={"description":"collection of pdf document chunks and emgbeddings "})
            print(
                os.path.abspath(self.persist_directory)
            )
            
            print(f"chromadb client initialized with collection: {self.collection_name} at {self.collection.count()}")


        except Exception as e:
            print(f"error initializing chromadb client:{e}")
            raise   

    def add_documents(self,documents:List[str],embeddings:np.ndarray):
        """add documents and their corrresponding embeddings to the vector store
        ards:
        documents:list of langchain document chunks to add
        corresponding embeddings for arrays
        """
        if(len(documents)!=embeddings.shape[0]):
            raise ValueError("number of documents and embeddings must match")
        
        print(f"adding {len(documents)} documents to vector store...")
        ids=[]
        doc_metadata=[]
        documents_text=[]
        embeddings_list=[]

        for i,doc in enumerate(documents):
            doc_id=str(uuid.uuid4())
            ids.append(doc_id)
        metadata = {
        "doc_index": i,
        "content_length": len(doc.page_content)
    }
        metadata.append(doc_metadata)

        documents_text.append(doc.page_content)
        embeddings_list.append(embeddings[i].tolist())

        try:
            self.collection.add(
                ids=ids,
                embeddings=embeddings_list,
                documents=documents_text,
                metadatas=metadata
            )
            print(f"successfully added {len(documents)} documents to vector store")
            print(f"current collection size: {self.collection.count()}")
        except Exception as e:
            print(f"error adding documents to vector store:{e}")
            raise
    


