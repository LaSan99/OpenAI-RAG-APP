# RAG Application - Modular Structure

A Retrieval-Augmented Generation (RAG) application that supports multiple document formats (PDF, DOCX, TXT) with a clean, modular architecture.

## 📁 Project Structure

```
rag-app/
├── main.py              # Main entry point
├── config.py            # Configuration and environment variables
├── data_loader.py       # Document loading and processing
├── rag_system.py        # RAG system creation and management
├── utils.py             # Utility functions and helpers
├── .env                 # Environment variables (API keys)
├── data/                # Document storage directory
└── chroma_db/           # Vector database storage
```

## 🏗️ Module Overview

### `config.py`
- **Purpose**: Centralized configuration management
- **Contents**: 
  - Environment variable handling
  - Application constants (chunk sizes, model settings)
  - Configuration validation

### `data_loader.py`
- **Purpose**: Document loading and processing
- **Features**:
  - Support for multiple file formats (PDF, DOCX, TXT)
  - Batch document loading from directories
  - File listing and management
  - Sample data creation

### `rag_system.py`
- **Purpose**: Core RAG functionality
- **Features**:
  - Vector store creation and management
  - Text splitting and embedding
  - Question-answering chain creation
  - Document retrieval and formatting

### `utils.py`
- **Purpose**: Shared utility functions
- **Features**:
  - UI helpers (banners, formatting)
  - Input validation and handling
  - Interactive mode management
  - Test question management

### `main.py`
- **Purpose**: Application entry point
- **Features**:
  - Clean, readable main flow
  - Environment validation
  - System initialization
  - User interaction orchestration

## 🚀 Getting Started

1. **Install dependencies**:
   ```bash
   pip install langchain langchain-openai langchain-community langchain-text-splitters chromadb python-dotenv pypdf docx2txt
   ```

2. **Set up environment**:
   - Copy `.env.example` to `.env` (if exists)
   - Add your OpenAI API key to `.env`:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

3. **Add documents**:
   - Place PDF, DOCX, or TXT files in the `data/` directory
   - Or use the provided sample data

4. **Run the application**:
   ```bash
   python main.py
   ```

## 🎯 Features

- **Multi-format support**: PDF, DOCX, TXT files
- **Modular architecture**: Clean separation of concerns
- **Interactive mode**: Ask questions in real-time
- **Sample questions**: Built-in testing questions
- **File management**: List and manage loaded documents
- **Help system**: Built-in command help

## 🔧 Configuration

Key configuration options in `config.py`:

- `CHUNK_SIZE`: Document chunk size (default: 1000)
- `CHUNK_OVERLAP`: Chunk overlap (default: 100)
- `RETRIEVAL_K`: Number of documents to retrieve (default: 3)
- `OPENAI_MODEL`: OpenAI model (default: "gpt-3.5-turbo")

## 📝 Usage Examples

### Interactive Mode Commands:
- Type your question directly
- `files` - List all files in data directory
- `help` - Show available commands
- `quit`/`exit`/`q` - Exit application

### Programmatic Usage:

```python
from rag_system import RAGSystem
from data_loader import DataLoader

# Create and setup RAG system
rag_system = RAGSystem()
rag_system.setup_system()

# Ask a question
answer = rag_system.ask_question("What is RAG?")
```

## 🛠️ Benefits of Modular Structure

1. **Maintainability**: Each module has a single responsibility
2. **Reusability**: Components can be used independently
3. **Testability**: Individual modules can be unit tested
4. **Scalability**: Easy to add new features or modify existing ones
5. **Readability**: Clear organization and separation of concerns

## 🔍 Error Handling

The application includes comprehensive error handling for:
- Missing API keys
- Unsupported file formats
- Document loading errors
- Vector store issues
- User input validation

## 📊 Performance

- Efficient document chunking and embedding
- Persistent vector storage with ChromaDB
- Optimized retrieval with configurable parameters
- Memory-efficient processing of large documents
