"""
Configuration module for RAG application
Handles environment variables and constants
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the RAG application"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = "gpt-3.5-turbo"
    OPENAI_TEMPERATURE = 0
    
    # Vector Store Configuration
    PERSIST_DIRECTORY = "./chroma_db"
    EMBEDDING_MODEL = "text-embedding-ada-002"
    
    # Text Splitting Configuration
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 100
    
    # Retrieval Configuration
    RETRIEVAL_K = 3
    
    # Data Configuration
    DATA_DIRECTORY = "data"
    SUPPORTED_EXTENSIONS = {'.txt', '.pdf', '.docx'}
    
    @classmethod
    def validate_config(cls):
        """Validate required configuration"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        return True
