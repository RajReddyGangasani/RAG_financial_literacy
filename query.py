import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser


load_dotenv()
index_name = os.getenv("PINECONE_INDEX_NAME")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=512)

vector_store = PineconeVectorStore(embedding=embeddings, index_name=index_name)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


prompt = ChatPromptTemplate.from_template("""
You are a financial literacy assistant.

Use only context below to answer the question.
If you don't know the answer, say you don't know.

Context: {context}
Question: {question}
Answer:
""")


# chain using LCEL
chain = prompt | llm | StrOutputParser()

while True:

    question = input("Ask a question about financial literacy: ")

    docs = vector_store.similarity_search(query=question, k=3)
    context = "\n\n".join([d.page_content for d in docs])
    answer = chain.invoke({"context": context, "question": question})
    print("\nAnswer:\n", answer)


    
    


