"""
Data loading module for RAG application
Handles document loading and processing from various file formats
"""
from pathlib import Path
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    Docx2txtLoader,
    DirectoryLoader
)
from config import Config


class DataLoader:
    """Handles loading documents from various file formats"""
    
    def __init__(self, directory=Config.DATA_DIRECTORY):
        self.directory = Path(directory)
        self.supported_extensions = Config.SUPPORTED_EXTENSIONS
    
    def load_single_file(self, file_path):
        """Load a single file based on its extension"""
        file_ext = file_path.suffix.lower()
        
        if file_ext == '.txt':
            loader = TextLoader(str(file_path), encoding='utf-8')
        elif file_ext == '.pdf':
            loader = PyPDFLoader(str(file_path))
        elif file_ext == '.docx':
            loader = Docx2txtLoader(str(file_path))
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")
        
        return loader.load()
    
    def load_documents_from_directory(self):
        """Load all supported documents from the directory"""
        documents = []
        
        if not self.directory.exists():
            print(f"❌ Directory '{self.directory}' not found!")
            return documents
        
        files = list(self.directory.glob("*"))
        supported_files = [f for f in files if f.suffix.lower() in self.supported_extensions]
        
        if not supported_files:
            print(f"⚠️  No supported files found in '{self.directory}'")
            print(f"   Supported formats: {', '.join(self.supported_extensions)}")
            return documents
        
        print(f"\n📚 Found {len(supported_files)} supported file(s):")
        
        for file_path in supported_files:
            try:
                file_ext = file_path.suffix.lower()
                
                if file_ext == '.txt':
                    print(f"   📄 Loading TXT: {file_path.name}")
                elif file_ext == '.pdf':
                    print(f"   📕 Loading PDF: {file_path.name}")
                elif file_ext == '.docx':
                    print(f"   📘 Loading DOCX: {file_path.name}")
                
                docs = self.load_single_file(file_path)
                documents.extend(docs)
                print(f"      ✓ Loaded {len(docs)} page(s)/chunk(s)")
                
            except Exception as e:
                print(f"      ❌ Error loading {file_path.name}: {str(e)}")
        
        return documents
    
    def list_files(self):
        """List all files in the data directory"""
        if not self.directory.exists():
            print(f"❌ Directory '{self.directory}' not found!")
            return
        
        files = list(self.directory.glob("*"))
        if not files:
            print(f"📁 Directory '{self.directory}' is empty")
            return
        
        print(f"\n📁 Files in '{self.directory}':")
        for file in files:
            size = file.stat().st_size / 1024  # Size in KB
            print(f"   • {file.name} ({size:.2f} KB)")


def setup_sample_data():
    """Create sample data files if they don't exist"""
    data_dir = Path(Config.DATA_DIRECTORY)
    data_dir.mkdir(exist_ok=True)
    
    # Create sample text file
    txt_file = data_dir / "sample_data.txt"
    if not txt_file.exists():
        with open(txt_file, "w") as f:
            f.write("""
Python is a high-level programming language known for its simplicity and readability.
It was created by Guido van Rossum and first released in 1991.
Python is widely used in web development, data science, AI, and automation.

RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval
with text generation. It helps AI models answer questions based on specific documents
rather than relying solely on their training data.

LangChain is a framework for developing applications powered by language models.
It provides tools for document loading, text splitting, embeddings, vector stores, and more.
LangChain makes it easier to build RAG applications.
            """)
        print(f"✓ Created sample text file at {txt_file}")
    
    print(f"\n📁 Data directory: {data_dir.absolute()}")
    print("   You can add your PDF, DOCX, and TXT files here!")
