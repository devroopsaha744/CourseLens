import os
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

#Configuring API Keys
load_dotenv()
hf_token = os.getenv('HF_TOKEN')
pinecone_api_key = os.getenv('PINECONE_API_KEY')
pinecone_url = os.getenv("PINECONE_URL")

file_path = "data/extracted_content.csv"
loader = CSVLoader(file_path= file_path, encoding="utf-8")
docs = loader.load()

#initializing the text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=500)

# Prepare the documents for vectorization by splitting them if needed
split_docs = []

for doc in docs:  # Assuming `docs` is a list of Document objects
    split_text = text_splitter.split_text(doc.page_content)
    # Create a new Document for each chunk while preserving metadata
    for text_chunk in split_text:
        split_docs.append(Document(page_content=text_chunk, metadata=doc.metadata))

#Embedding Model 
embedding = HuggingFaceInferenceAPIEmbeddings(api_key= hf_token)

#Indexing the documents in on vectorDB
index_name = "courselens"
docsearch = PineconeVectorStore.from_documents(split_docs, embedding, index_name=index_name)


print("Indexing done!")