# Now split the documents into chunks using Recursive Character Text Splitter
# from rag.loader import all_pdfs
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents, chunk_size=1000, chunk_overlap=200):

    """Split documents into chunks using Recursive Character Text Splitter"""

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    split_docs = text_splitter.split_documents(documents)

    print(f"Split {len(documents)} documents into {len(split_docs)} chunks")

    if split_docs:
        print(f"First chunk: {split_docs[0].page_content[:200]}...")

    return split_docs



# chunk=split_documents(all_pdfs, chunk_size=1000, chunk_overlap=200)