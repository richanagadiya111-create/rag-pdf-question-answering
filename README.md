# RAG-Based PDF Question Answering System

## About the Project

This project is a Retrieval-Augmented Generation (RAG) application that allows users to ask questions about information contained in PDF documents.

It uses Python and LangChain to process documents, Hugging Face embeddings to represent text as vectors, Chroma as a vector store, and a Groq-hosted language model to generate answers using retrieved document context.

The project also includes a Streamlit interface for interacting with the question-answering system.

## Features

* Load and process PDF documents.
* Split document text into smaller chunks.
* Generate embeddings using Hugging Face.
* Store document embeddings in Chroma.
* Retrieve relevant text chunks using a retriever.
* Generate answers using a language model through Groq.
* Provide a Streamlit interface for asking questions about document content.

## Technologies Used

* Python
* LangChain
* Streamlit
* PyPDF
* Hugging Face Embeddings
* Chroma Vector Database
* Groq API
* Sentence Transformers

## How It Works

The application follows a Retrieval-Augmented Generation workflow:

1. **Document Loading:** Extract text from a PDF document.
2. **Text Splitting:** Divide the extracted text into smaller chunks using `RecursiveCharacterTextSplitter`.
3. **Embedding Generation:** Convert text chunks into vector representations using Hugging Face embeddings.
4. **Vector Storage:** Store the embeddings in Chroma.
5. **Retrieval:** Find relevant document chunks for a user's question.
6. **Answer Generation:** Send the question and retrieved context to a language model through Groq.
7. **Response Display:** Display the generated answer through the application interface.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/rag-pdf-question-answering.git
cd rag-pdf-question-answering
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the packages required by the project. For example:

```bash
pip install streamlit langchain langchain-community langchain-text-splitters langchain-huggingface langchain-chroma langchain-groq pypdf sentence-transformers python-dotenv
```

### 4. Configure the API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your actual API key.

**Security:** Never upload your `.env` file or expose your API key on GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local address displayed in the terminal to use the application.

## Concepts Practised

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Document loading and text chunking
* Text embeddings
* Vector databases
* Information retrieval
* Prompt templates and context-based answering
* LangChain integration
* Streamlit application development

## Future Improvements

* Support multiple PDF documents.
* Display relevant source passages alongside answers.
* Improve retrieval accuracy.
* Add chat history.
* Deploy the application online.
