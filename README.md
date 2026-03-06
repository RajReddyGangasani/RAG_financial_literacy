# Financial Literacy RAG Assistant

This project implements a Retrieval-Augmented Generation (RAG) pipeline using:

- OpenAI GPT models
- OpenAI embeddings
- Pinecone vector database
- LangChain document loaders and retrievers

The system answers financial literacy questions based on a PDF knowledge base.


---

## Installation

pip install -r requirements.txt

---

## Setup

Create a `.env` file with:

OPENAI_API_KEY=your_key
PINECONE_API_KEY=your_key
PINECONE_INDEX_NAME= index_name

---

## Run config.py
set up config file with all environment variables.

---

## Ask Questions

python query.py



### Challenges_Faced #####
python dependencies issues because of python version mismatch with langchain version and vertual environment.

python interpreter version vs dependencies (all the dependencies must be installed in same version and kernal of project, 
else error occers)


### Project architecure ####

                         ┌─────────────────────┐
                         │  Financial PDF Data │
                         └──────────┬──────────┘
                                    │
                                    ▼
                             Document Loader
                                    │
                                    ▼
                                Chunking
                                    │
                                    ▼
                               Embeddings
                                    │
                                    ▼
                             Pinecone Index
                                    │
────────────────────────────────────────────────────────
                                    │
                                    ▼
                              User Question
                                    │
                                    ▼
                                Retriever
                                    │
                                    ▼
                             Retrieved Chunks
                                    │
                                    ▼
                           Context Construction
                                    │
                                    ▼
                               Prompt Template
                                    │
                                    ▼
                                 ChatGPT
                                    │
                                    ▼
                                Final Answer




### Project structure ###
rag_project/

data/
   financial_literacy_rag_dataset.pdf

ingest.py
   PDF → Loader → Chunking → Embeddings → Pinecone

query.py
   Question → Retriever → Context → prompt | llm | parser

config.py
   loads environment variables

.env
   OPENAI_API_KEY
   PINECONE_API_KEY
   PINECONE_INDEX_NAME
   PINECONE_ENVIRONMENT

requirements.txt
   all dependencies

README.md
   project documentation




### Query Pipeline  ###

                 DATA PIPELINE
┌───────────────────────────────────────┐
│                                       │
│  PDF → Loader → Chunking → Embedding  │
│                      │                │
│                      ▼                │
│               Pinecone Index          │
│                                       │
└───────────────────────────────────────┘


                 QUERY PIPELINE

User Question
      │
      ▼
Retriever (Pinecone)
      │
      ▼
Retrieved Chunks
      │
      ▼
Context Assembly
      │
      ▼
Prompt Template
      │
      ▼
LCEL Chain
(prompt | llm | parser)
      │
      ▼
Final Answer