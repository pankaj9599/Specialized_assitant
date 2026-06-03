from rag.loader import process_all_pdfs
from rag.chunk import split_documents
from rag.embedding import EmbeddingManager
from rag.vector_store import VectorStore
from rag.retrieve import RAGRetriever

import uuid


# =========================
# EMBEDDING MODEL
# =========================

embedding_manager = EmbeddingManager()





# =========================
# VECTOR STORE
# =========================

vectorStore = VectorStore()


# =========================
# BUILD VECTOR DB ONLY ONCE
# =========================

if vectorStore.collection.count() == 0:
    print("Collection empty. Building vector database...")
    all_pdfs=process_all_pdfs("data/pdfs")

    chunks = split_documents(
        all_pdfs,
        chunk_size=1000,
        chunk_overlap=200
    )

    print(f"Total chunks: {len(chunks)}")

    texts = [
        doc.page_content
        for doc in chunks
    ]

    embeddings = embedding_manager.generate_embeddings(
        texts
    )

    ids = []
    documents_text = []
    metadatas = []
    embeddings_list = []

    for i, doc in enumerate(chunks):

        ids.append(str(uuid.uuid4()))

        documents_text.append(
            doc.page_content
        )

        md = {
            "doc_index": i,
            "content_length": len(
                doc.page_content
            )
        }

        if isinstance(doc.metadata, dict):
            md.update(doc.metadata)

        metadatas.append(md)

        embeddings_list.append(
            embeddings[i].tolist()
        )

    vectorStore.collection.add(
        ids=ids,
        embeddings=embeddings_list,
        documents=documents_text,
        metadatas=metadatas
    )

    # print(
    #     f"Successfully added {len(ids)} docs"
    # )

else:

    print(
        f"Using existing collection with "
        f"{vectorStore.collection.count()} docs"
    )


# =========================
# CREATE RETRIEVER
# =========================

rag_retriever = RAGRetriever(
    vectorStore,
    embedding_manager
)