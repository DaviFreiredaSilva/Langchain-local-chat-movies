from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from ingestion import retriever

#Criando um novo objeto OllamaLLM
model = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

template = """
Você é um expert em responder questões sobre filmes.

Seguem algumas avaliações relevantes de filmes: {reviews}

Esta é a questão a ser respondida: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain= prompt | model



def main():
    print("Agente de AI local. Avaliações de filmes do IMDB")
    print("Faça sua pergunta sobre filmes: (digite q ou sair para sair)")
    while True:
        question = input()
        if question == "q" or question == "sair":
            break

        docs = retriever.invoke(question)
    
        #Abaixo, as reviews do arquivo CSV que foram tratadas no arquivo vector.py serão usadas no RAG para responder à pergunta 
        reviews = "\n\n".join([doc.page_content for doc in docs])
           
        result =chain.invoke(
            {"reviews": reviews, 
             "question": question}
             )
        
        print(result.content)

if __name__ == "__main__":
    main()
