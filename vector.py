import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---
PDF_PATH = "cv.pdf"  # IMPORTANT: Place your CV PDF in the same directory and name it this, or change the path.
DB_LOCATION = "./cv_chroma_db"
EMBEDDING_MODEL = "mxbai-embed-large" # A good default embedding model

def create_vector_db():
    """Creates a Chroma vector database from a PDF document."""

    if not os.path.exists(PDF_PATH):
        print(f"Error: PDF file not found at '{PDF_PATH}'")
        return

    if os.path.exists(DB_LOCATION):
        print(f"Database already exists at '{DB_LOCATION}'. Skipping creation.")
        return

    print("--- 1. Loading PDF document ---")
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    if not docs:
        print("Error: Could not load any content from the PDF.")
        return

    print(f"--- 2. Splitting {len(docs)} document(s) into chunks ---")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    if not splits:
        print("Error: Failed to split the document into chunks.")
        return
        
    print(f"--- 3. Created {len(splits)} text chunks ---")

    print(f"--- 4. Initializing embedding model: {EMBEDDING_MODEL} ---")
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

    print(f"--- 5. Creating and persisting vector store at '{DB_LOCATION}' ---")
    # This single command creates the embeddings and stores them in the database.
    vector_store = Chroma.from_documents(
        documents=splits, 
        embedding=embeddings, 
        persist_directory=DB_LOCATION
    )
    
    print("--- Vector database created successfully! ---")


if __name__ == "__main__":
    create_vector_db()
