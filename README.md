# Chat with Your PDF 📚

A Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF and ask questions about its content using Generative AI.

## Features

- Upload a PDF file.
- Extract and split PDF text into chunks.
- Generate embeddings using Hugging Face.
- Store and retrieve document chunks using ChromaDB.
- Ask questions about the uploaded PDF.
- Generate answers using the Groq LLM.
- Display chat history and source page numbers.
- Clear chat history.
- Download chat history.

## Technologies Used

- Python
- Streamlit
- LangChain
- Groq API
- Hugging Face Embeddings
- ChromaDB
- PyPDF

## Project Structure

- `app.py` — Streamlit user interface.
- `main.py` — Question-answering logic.
- `databse_file.py` — PDF processing, embeddings, and vector storage.
- `requirements.txt` — Python dependencies.
- `docloaders/` — PDF documents used for testing.

## Installation

1. Clone this repository and open its folder.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   `python -m pip install -r requirements.txt`

4. Create a `.env` file in the project root:

   `GROQ_API_KEY=your_groq_api_key_here`

5. Start the application:

   `streamlit run app.py`

## How It Works

1. Upload a PDF.
2. Extract and split its text into chunks.
3. Generate embeddings using Hugging Face.
4. Store and retrieve relevant chunks using ChromaDB.
5. Pass the retrieved context to the Groq language model.
6. Display the answer and relevant source pages.

## Purpose

This project demonstrates how Retrieval-Augmented Generation (RAG) can be used to build a PDF question-answering application.


