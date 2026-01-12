"""
RAG system module for creating and managing the retrieval-augmented generation system
"""
import os
import shutil
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from config import Config
from data_loader import DataLoader, setup_sample_data


class RAGSystem:
    """Main RAG system class that handles document processing and question answering"""
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.llm = ChatOpenAI(
            model=Config.OPENAI_MODEL,
            temperature=Config.OPENAI_TEMPERATURE
        )
        self.vectorstore = None
        self.qa_chain = None
    
    def format_docs(self, docs):
        """Format documents for context"""
        return "\n\n".join(doc.page_content for doc in docs)
    
    def create_vector_store(self, documents):
        """Create and persist vector store from documents"""
        print("\n✂️  Splitting documents into chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP,
            length_function=len
        )
        texts = text_splitter.split_documents(documents)
        print(f"   Created {len(texts)} chunks")
        
        print("\n🔢 Creating embeddings and vector store...")
        print("   (This may take a moment...)")
        
        # Check if vector store already exists
        if os.path.exists(Config.PERSIST_DIRECTORY):
            print("   ℹ️  Removing old vector store...")
            shutil.rmtree(Config.PERSIST_DIRECTORY)
        
        self.vectorstore = Chroma.from_documents(
            documents=texts,
            embedding=self.embeddings,
            persist_directory=Config.PERSIST_DIRECTORY
        )
        print("   ✓ Vector store created")
        
        return self.vectorstore
    
    def create_qa_chain(self):
        """Create the question-answering chain"""
        if not self.vectorstore:
            raise ValueError("Vector store not created. Call create_vector_store first.")
        
        print("\n🔗 Creating QA chain...")
        
        # Create prompt template
        prompt = ChatPromptTemplate.from_template("""
        Answer the following question based only on the provided context:
        
        <context>
        {context}
        </context>
        
        Question: {input}
        
        Answer:
        """)
        
        # Create retriever
        retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": Config.RETRIEVAL_K}
        )
        
        # Create the chain using LCEL
        self.qa_chain = (
            RunnableParallel({
                "context": retriever | self.format_docs, 
                "input": RunnablePassthrough()
            })
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        print("✅ RAG system ready!\n")
        return self.qa_chain
    
    def ask_question(self, question):
        """Ask a question to the RAG system"""
        if not self.qa_chain:
            raise ValueError("QA chain not created. Call create_qa_chain first.")
        
        print(f"\n❓ Question: {question}")
        print("   🔍 Searching documents...")
        
        try:
            result = self.qa_chain.invoke(question)
            print(f"\n💡 Answer: {result}")
            return result
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def setup_system(self, data_directory=None):
        """Complete setup of the RAG system"""
        print("\n🚀 Setting up RAG system...")
        
        # Ensure sample data exists
        setup_sample_data()
        
        # Load documents
        print("\n📄 Loading documents from directory...")
        data_loader = DataLoader(data_directory or Config.DATA_DIRECTORY)
        documents = data_loader.load_documents_from_directory()
        
        if not documents:
            print("❌ No documents loaded. Please add files to the data directory.")
            return None
        
        print(f"\n✓ Total documents loaded: {len(documents)}")
        
        # Create vector store and QA chain
        self.create_vector_store(documents)
        self.create_qa_chain()
        
        return self
