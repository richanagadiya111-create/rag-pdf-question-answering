import os
import tempfile

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def process_pdf(uploaded_file):

    # Save the uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(uploaded_file.getvalue())
        pdf_path = temp_file.name

    try:
        # Step 1: Load the PDF
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        if not documents:
            raise ValueError("The PDF contains no readable pages.")

        # Step 2: Check whether the PDF contains readable text
        if not any(doc.page_content.strip() for doc in documents):
            raise ValueError(
                "No readable text found. "
                "The PDF may be scanned or image-based."
            )

        # Step 3: Split the PDF into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(documents)

        if not chunks:
            raise ValueError("No text chunks could be created.")

        # Step 4: Create a vector database
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings
        )

        # Return the database to the caller
        return vector_store

    finally:
        # Delete the temporary PDF file
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
