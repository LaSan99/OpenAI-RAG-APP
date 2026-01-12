"""
Utility functions for the RAG application
"""
from pathlib import Path
from config import Config


def print_banner():
    """Print the application banner"""
    print("=" * 70)
    print("       Welcome to Your Multi-Format RAG Application!")
    print("       Supports: PDF, DOCX, TXT files")
    print("=" * 70)


def print_section_banner(title):
    """Print a section banner"""
    print("\n" + "=" * 70)
    print(f"       {title}")
    print("=" * 70)


def validate_environment():
    """Validate that the environment is properly set up"""
    try:
        Config.validate_config()
        return True
    except ValueError as e:
        print(f"❌ Error: {str(e)}")
        return False


def get_sample_questions():
    """Return a list of sample questions for testing"""
    return [
        "What is RAG?",
        "What programming languages or technologies are mentioned?",
        "Summarize the main topics in the documents"
    ]


def handle_user_input(user_input, rag_system, data_loader):
    """Handle user input in interactive mode"""
    user_input = user_input.strip()
    
    if user_input.lower() in ['quit', 'exit', 'q']:
        print("\n👋 Goodbye!")
        return False
    elif user_input.lower() == 'files':
        data_loader.list_files()
    elif user_input.lower() == 'help':
        print("\n📖 Available commands:")
        print("   • Type your question to ask the RAG system")
        print("   • 'files' - List all files in the data directory")
        print("   • 'help' - Show this help message")
        print("   • 'quit' or 'exit' or 'q' - Exit the application")
    elif user_input:
        rag_system.ask_question(user_input)
    else:
        print("   Please enter a question or command")
    
    return True


def run_interactive_mode(rag_system, data_loader):
    """Run the interactive mode"""
    print_section_banner("Interactive Mode")
    print("       Commands: 'quit' to exit, 'files' to list files, 'help' for commands")
    print("=" * 70)
    
    while True:
        try:
            user_input = input("\n🔍 Your question: ")
            if not handle_user_input(user_input, rag_system, data_loader):
                break
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")


def run_test_questions(rag_system):
    """Run sample test questions"""
    print_section_banner("Testing with Sample Questions")
    
    questions = get_sample_questions()
    for question in questions:
        rag_system.ask_question(question)
