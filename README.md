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

