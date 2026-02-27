# 🎬 IMDB Movie Reviews RAG Agent (Local, LangChain + Ollama)

Este projeto implementa um agente de IA local baseado em RAG (Retrieval-Augmented Generation) capaz de responder perguntas sobre filmes usando avaliações reais do dataset IMDB.

O sistema utiliza embeddings locais, vector database persistente e um LLM executado via Ollama, garantindo privacidade total e execução offline.

---

# 🚀 Arquitetura

Pipeline completo:

User Question  
↓  
Retriever (Chroma Vector Store)  
↓  
Relevant Reviews (Semantic Search)  
↓  
Prompt Template  
↓  
LLM (Llama 3.2 via Ollama)  
↓  
Final Answer  

---

# 🧠 Tecnologias utilizadas

- LangChain (orquestração do pipeline RAG)
- Ollama (LLM local e embeddings)
- ChromaDB (vector database persistente)
- Python
- IMDB Dataset (50.000 avaliações)

---

# 📂 Estrutura do projeto
