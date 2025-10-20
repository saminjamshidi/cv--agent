import os
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings # Use the new, correct import

# --- Configuration ---
# These MUST match the settings in your 'vector.py' file
DB_LOCATION = "./cv_chroma_db"
EMBEDDING_MODEL = "mxbai-embed-large"
LLM_MODEL = "llama3.2" # Using "llama3" is standard. If it fails, try "llama3:latest"

# --- 1. Check if the database exists ---
if not os.path.exists(DB_LOCATION):
    print(f"Error: Vector database not found at '{DB_LOCATION}'")
    print("Please run your 'vector.py' script first to create it.")
    exit() # Exit the script if the database is missing

# --- 2. Load the Vector Database and Create the Retriever ---
print("--- Loading CV database... ---")
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
vector_store = Chroma(
    persist_directory=DB_LOCATION, 
    embedding_function=embeddings
)
retriever = vector_store.as_retriever(search_kwargs={"k": 6})
print("--- Database loaded. Chatbot is ready! ---")


# --- 3. Set up the LLM, Prompt, and Chain ---
model = OllamaLLM(model=LLM_MODEL)

# I've renamed 'reviews' to 'context' to be more accurate for a CV
template = """
You are an expert in answering questions about my CV.
Use the following relevant information from my CV to answer the question.
If you don't know the answer from the provided context, just say that you don't know.

Context from CV: 
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


# --- 4. Start the Chat Loop ---
while True:
    print("\n\n-------------------------------")
    question = input("Ask a question about the CV (q to quit): ")
    if question.lower() == "q":
        break
    
    # Use the retriever we created above to get relevant CV parts
    retrieved_docs = retriever.invoke(question)
    
    # Format the context for the prompt
    context_str = "\n\n---\n\n".join([doc.page_content for doc in retrieved_docs])
    
    # Send the context and question to the model
    result = chain.invoke({"context": context_str, "question": question})
    print("\nANSWER:")
    print(result)
