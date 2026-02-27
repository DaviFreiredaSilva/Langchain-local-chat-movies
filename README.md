# IMDB Movie Reviews RAG Agent (Local, LangChain + Ollama)

## Este projeto implementa um agente de IA local baseado em RAG (Retrieval-Augmented Generation) capaz de responder perguntas sobre filmes usando avaliações reais do dataset IMDB.

O sistema utiliza embeddings locais, vector database persistente e um LLM executado via Ollama, garantindo privacidade total e execução offline.

---

# Arquitetura

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

# Tecnologias utilizadas

- LangChain
- Ollama (LLM local e embeddings)
- ChromaDB (vector database persistente)
- Python
- IMDB Dataset (50.000 avaliações)

---

# Estrutura do projeto
project/
│
├── main.py # Agente principal
├── ingestion.py # Criação e persistência da vector store
├── chroma_db/ # Vector database persistente
├── IMDB-Dataset.csv # Dataset de avaliações
└── README.md


---

# Como funciona

## 1. Ingestão de dados

O arquivo `ingestion.py`:

- carrega o dataset CSV
- cria embeddings usando Ollama
- armazena os vetores no ChromaDB
- persiste o banco localmente

Executado automaticamente na primeira execução.

---

## 2. Retrieval (Busca semântica)

Quando uma pergunta é feita:

```python
docs = retriever.invoke(question)

3. Geração da resposta

O LLM recebe:

pergunta do usuário

reviews relevantes

e gera uma resposta contextualizada.

# Requisitos

Python 3.10+

Ollama instalado: https://ollama.com

# Executar o projeto
python main.py

Primeira execução:

cria vector store

pode levar 30–120 minutos dependendo do hardware

Execuções seguintes:

inicialização instantânea

# Exemplo de uso

Pergunta:

O Filme Dark Knight é um bom filme?

Resposta:

De acordo com as reviews este é um ótimo filme para quem gosta de filmes de ação.
