# Repository Intelligence Assistant

An AI-powered Repository Analysis Platform that enables users to upload software repositories and interact with them using natural language. The system leverages Retrieval-Augmented Generation (RAG), Vector Databases, Embeddings, and Large Language Models to provide repository-aware insights, code explanations, architecture understanding, and semantic search capabilities.

## Features

* Repository Upload and Indexing
* Semantic Code Search
* Repository Question Answering
* Context-Aware Retrieval using RAG
* Vector Storage with ChromaDB
* Embedding Generation using Sentence Transformers
* LLM-Powered Responses using Gemini
* FastAPI Backend
* Interactive Streamlit Frontend
* File-Level Traceability and Context Retrieval

## Tech Stack

### Backend

* FastAPI
* Python

### Retrieval Layer

* ChromaDB
* Sentence Transformers
* Vector Embeddings

### LLM Layer

* Google Gemini API

### Frontend

* Streamlit

### Utilities

* Git
* GitHub

## Architecture

Repository ZIP
↓
File Loader
↓
Chunking Engine
↓
Embedding Generator
↓
ChromaDB Vector Store
↓
Retriever
↓
Gemini LLM
↓
Answer Generation
↓
Streamlit Interface

## Workflow

1. Upload a repository ZIP file.
2. Extract and process repository files.
3. Generate semantic chunks from source code and documentation.
4. Create embeddings using Sentence Transformers.
5. Store embeddings in ChromaDB.
6. Convert user questions into embeddings.
7. Retrieve relevant repository context.
8. Generate grounded responses using Gemini.
9. Return repository-specific answers to the user.

## Example Questions

* Explain this repository.
* What is the architecture of this project?
* Which file contains authentication logic?
* Explain the execution flow.
* What technologies are used?
* How does the API work?
* What improvements would you suggest?

## Project Structure

repository-intelligence-assistant/

├── backend/

│   ├── main.py

│   ├── rag_pipeline.py

│   ├── file_loader.py

│   ├── chunker.py

│   ├── embeddings.py

│   ├── vector_store.py

│   ├── llm_handler.py

│   └── config.py

│

├── frontend/

│   └── app.py

│

├── uploads/

├── chroma_db/

├── requirements.txt

└── README.md

## Future Enhancements

* Multi-Repository Support
* GitHub URL Direct Analysis
* Code Dependency Graph Visualization
* Repository Summarization Reports
* Multi-LLM Support
* Agentic Repository Exploration
* Automated Documentation Generation

