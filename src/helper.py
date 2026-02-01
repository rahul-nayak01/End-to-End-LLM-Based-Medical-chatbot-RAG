"""from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document

#Extract Data From the PDF File
def load_pdf_file(data):
    loader= DirectoryLoader(data,
                            glob="*.pdf",
                            loader_cls=PyPDFLoader)

    documents=loader.load()

    return documents



def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    #Given a list of Document objects, return a new list of Document objects
    #containing only 'source' in metadata and the original page_content.
    """
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs



#Split the Data into Text Chunks
def text_split(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks



#Download the Embeddings from HuggingFace 
def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')  #this model return 384 dimensions
    return embeddings



from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import pinecone
import os

from src.prompt import *
from src.memory import get_conversation_memory


def load_llm():
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.3
    )
    return llm


def retrieval_qa_chain():
    pinecone.init(
        api_key=os.environ.get("PINECONE_API_KEY"),
        environment=os.environ.get("PINECONE_ENV")
    )

    embeddings = OpenAIEmbeddings()

    index_name = os.environ.get("PINECONE_INDEX_NAME")

    docsearch = Pinecone.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )

    retriever = docsearch.as_retriever(search_kwargs={"k": 3})

    memory = get_conversation_memory()

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=load_llm(),
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": PROMPT}
    )

    return qa_chain"""


import pinecone
import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

from src.agent import create_agent


def load_agent():
    pinecone.init(
        api_key=os.environ.get("PINECONE_API_KEY"),
        environment=os.environ.get("PINECONE_ENV")
    )

    embeddings = OpenAIEmbeddings()
    index_name = os.environ.get("PINECONE_INDEX_NAME")

    docsearch = Pinecone.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )

    retriever = docsearch.as_retriever(search_kwargs={"k": 3})

    agent = create_agent(retriever)

    return agent
