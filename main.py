"""
Main entry point for the RAG application
Uses modular structure for better organization and maintainability
"""
from config import Config
from data_loader import DataLoader
from rag_system import RAGSystem
from utils import (
    print_banner, 
    print_section_banner, 
    validate_environment,
    run_test_questions,
    run_interactive_mode
)


def main():
    """Main function"""
    # Print application banner
    print_banner()
    
    # Validate environment
    if not validate_environment():
        return
    
    # List current files
    data_loader = DataLoader()
    data_loader.list_files()
    
    # Create and setup RAG system
    rag_system = RAGSystem()
    rag_system = rag_system.setup_system()
    
    if not rag_system:
        return
    
    # Run test questions
    run_test_questions(rag_system)
    
    # Run interactive mode
    run_interactive_mode(rag_system, data_loader)


if __name__ == "__main__":
    main()