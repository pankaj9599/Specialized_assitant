import os

print(os.getcwd())
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


# Read all PDFs in the directory and load them as documents
def process_all_pdfs(directory):

    all_documents = []

    # Directory where PDF files are located
    pdf_dir = Path(directory)

    # Find all PDF files
    pdf_files = list(pdf_dir.glob("*.pdf"))
    print(f"Scanning directory: {directory}")
    print(f"the file is {pdf_files}")
    print(f"Found {len(pdf_files)} PDF files in directory: {directory}")

    for pdf in pdf_files:

        print(f"Processing file: {pdf.name}")

        try:
            # Load PDF
            loader = PyPDFLoader(str(pdf))

            documents = loader.load()

            # Add metadata
            for doc in documents:
                doc.metadata["source"] = pdf.name
                doc.metadata["file_type"] = "pdf"

            # Add documents to master list
            all_documents.extend(documents)

            print(f"Successfully processed: {pdf.name}")

        except Exception as e:
            print(f"Error processing {pdf.name}: {e}")

        print(f"Total documents loaded: {len(all_documents)}")
    return all_documents


# all_pdfs=process_all_pdfs("data/pdfs")