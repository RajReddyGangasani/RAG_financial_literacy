from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

import os 
from dotenv import load_dotenv

load_dotenv()
index_name = os.getenv("PINECONE_INDEX_NAME")

loader = PyPDFLoader("/Users/rajreddy/Desktop/PythonPractice/rag_project/data/financial_literacy_rag_dataset.pdf")
docs = loader.load()
print(f"document loaded", len(docs))


text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
chunks = text_splitter.split_documents(docs)
print(f"document split into chunks", len(chunks))


embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=512)
vector_store = PineconeVectorStore.from_documents(documents= chunks, embedding= embeddings, index_name=index_name)
print(f"document embedded and stored in pinecone index: {index_name}")

