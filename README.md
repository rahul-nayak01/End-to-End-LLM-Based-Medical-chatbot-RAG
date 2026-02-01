# End-to-End-LLM-Based-Medical-chatbot-RAG
This is End to End Rag project


# 🩺 End-to-End LLM-Based Medical Chatbot using RAG

This project is an end-to-end Medical Question Answering Chatbot built using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).  
The system generates accurate and context-aware medical responses by grounding LLM outputs with information retrieved from a medical knowledge base.

---

## 📌 Project Motivation

Large Language Models can generate fluent responses, but in sensitive domains like healthcare they may hallucinate or provide unreliable information.  
To address this, I implemented a Retrieval-Augmented Generation (RAG) architecture where relevant medical documents are retrieved first and then passed as context to the LLM for response generation.

This approach improves:
- Factual accuracy  
- Domain relevance  
- Trustworthiness of responses  

---

## 🧠 Architecture Overview

User Query  
→ Flask API  
→ LangChain RAG Pipeline  
→ Query Embedding  
→ Semantic Search using Pinecone  
→ Context Injection into LLM  
→ Final Medical Response  

---

## 🛠️ Tech Stack

- Language Model: OpenAI GPT  
- RAG Framework: LangChain  
- Vector Database: Pinecone  
- Backend API: Flask  
- Embeddings: Sentence Transformers  
- Document Processing: PyPDF  
- Deployment: AWS EC2  
- Secrets Management: Environment Variables (.env)

---

## ✨ Key Features

- Semantic search over medical documents using vector embeddings  
- Retrieval-Augmented Generation to reduce hallucinations  
- Domain-specific medical knowledge base  
- Secure API key and credential management  
- Deployable both locally and on AWS  

---

## 🔁 Conversational RAG with Memory

This project has been extended from a basic knowledge-based RAG system
to a conversational RAG architecture using LangChain's
ConversationBufferMemory.

### Key Features
- Maintains full chat history across turns
- Supports follow-up medical questions
- Uses ConversationalRetrievalChain
- Non-agentic, deterministic control flow

### Architecture
User → Flask API → Conversational Retrieval Chain
→ (Conversation Buffer Memory + Pinecone Retriever + LLM)
→ Context-aware medical response

-----------
## 🤖 Agentic RAG Architecture

This project has been upgraded from a conversational RAG system to an
Agentic RAG architecture using LangChain agents.

### Key Enhancements
- ReAct-style reasoning loop
- LLM-driven decision making
- Retriever exposed as a tool
- Conversation memory preserved
- Conditional medical knowledge retrieval

### Architecture
User → Flask API → LLM Agent
→ (Conversation Memory + Pinecone Retriever Tool)
→ Grounded Medical Response



┌──────────────────────┐
│        User          │
│ (Medical Question)   │
└──────────┬───────────┘
           │
           ▼
┌─────────────────────────────┐
│        Flask API             │
│  (Inference Endpoint)        │
└──────────┬──────────────────┘
           │
           ▼
┌──────────────────────────────────────────┐
│        LLM Agent (LangChain Agent)         │
│------------------------------------------│
│  • ReAct Reasoning Loop                   │
│  • LLM-driven decision making             │
│  • Decides whether to:                    │
│      - Retrieve medical knowledge         │
│      - Refine the query                   │
│      - Answer directly                    │
└───────┬───────────────┬──────────────────┘
        │               │
        │               │
        ▼               ▼
┌─────────────────┐   ┌────────────────────────┐
│ Conversation     │   │   Retriever Tool        │
│ Memory           │   │ (Pinecone Vector DB)    │
│-----------------│   │------------------------│
│ • Buffer Memory  │   │ • Medical embeddings   │
│ • Chat history   │   │ • Semantic similarity  │
└────────┬────────┘   └──────────┬─────────────┘
         │                         │
         └──────────────┬──────────┘
                        ▼
              ┌──────────────────────────┐
              │ Retrieved Medical Context │
              └──────────┬───────────────┘
                         ▼
              ┌──────────────────────────┐
              │      LLM Generation       │
              │ (Grounded Medical Answer) │
              └──────────┬───────────────┘
                         ▼
                   Final Response

