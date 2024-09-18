import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Load environment variables from .env file
load_dotenv()

# Check if the OpenAI API key is set in the environment variables
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in .env file")

def load_pdfs(directory):
    # Load and split all PDF files from the specified directory.
    # Returns: list: A list of document chunks from all PDFs.
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load_and_split())
    return documents

def setup_qa_chain(pdf_directory):
    # Set up the question-answering chain with PDF documents.
    # Returns: ConversationalRetrievalChain: The set up QA chain.
    pages = load_pdfs(pdf_directory)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(pages, embeddings)
    
    memory = ConversationBufferMemory(memory_key="chat_history", output_key="answer", return_messages=True)
    llm = ChatOpenAI(temperature=1.0)
    
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=db.as_retriever(),
        memory=memory,
        return_source_documents=True
    )

def chat_loop(qa_chain):
    # Run the chat loop for interacting with the AI.
    # Args: qa_chain (ConversationalRetrievalChain): The QA chain to use for responses.
    print("Welcome! You can now chat with the AI assistant that uses information from the PDFs. Enter 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        response = qa_chain.invoke({"question": user_input})
        print("AI:", response['answer'])
        
        print("\nSources used:")
        for doc in response['source_documents']:
            print(f"- {doc.metadata['source']} (Page {doc.metadata['page']})")

def main():
    pdf_directory = "files"
    qa_chain = setup_qa_chain(pdf_directory)
    chat_loop(qa_chain)

if __name__ == "__main__":
    main()