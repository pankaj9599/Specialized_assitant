import numpy as np
from sentence_transformers import SentenceTransformer
# import chromadb
# from chromadb.config import Settings
import uuid
from typing import List,Any,Dict,Tuple
# from sklearn.metrics.pairwise import cosine_similarity



class EmbeddingManager:
    """handle embedding generation using huggingface sentence transformers """
    def __init__(self,model_name:str="all-MiniLM-L6-v2"):
        """
        Initialize the embeding manager with a specified model name
        """
        self.model_name=model_name
        self.model=None
        self.load_model()
    
    def load_model(self):
        """load the sentence transformer model"""
        try:
            print(f"{self.model_name}model loading...")
            self.model=SentenceTransformer(self.model_name)
        except Exception as e:
            print(f"error loading model {self.model_name}:{e}")
     
            raise

    def generate_embeddings(self,texts:List[str])->np.ndarray:
        """
        generate embeddings for a list of texts

        args:
        text:list of text to embed

        returns:
        numpy array of embeddings with shape (len(texts),embedding_dim)
        """   
        if not self.model:
            raise ValueError("model not loader") 
        
        print(f"generating embeddings for {len(texts)} texts...")
        embeddings=self.model.encode(texts,show_progress_bar=True)
        print(f"generated embeddings with shape {embeddings.shape}")
        return embeddings
    
# embeddingmanager=EmbeddingManager();
# embeddingmanager