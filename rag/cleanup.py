# reset_chroma.py

import chromadb

client = chromadb.PersistentClient(
    path="data/vector_db"
)

try:
    client.delete_collection("pdf_documents")
    print("Collection deleted")
except Exception as e:
    print(e)