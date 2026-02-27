import os
from langchain_community.document_loaders import CSVLoader
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

#Os dados do arquivo csv serão iniciamente transformados em um dataframe
file = "IMDB-Dataset.csv"
loader = CSVLoader(
    file_path=file,
    encoding="utf-8"
    )
docs= loader.load()

#Localização do db
db_location = "./chroma_db"

#Verificando se os processos já foram realizados:
add_documents = not os.path.exists(db_location)

# Embedding será realizado para uso na vectors store
embeddings = OllamaEmbeddings(
    model='nomic-embed-text'
    )

vectorstore = Chroma(
        collection_name="imdb",
        embedding_function=embeddings,
        persist_directory=db_location
    )

if add_documents:
    print(f"Total de documentos: {len(docs)}")

    batch_size = 100

    for i in range(0, len(docs), batch_size):

        batch = docs[i:i+batch_size]

        vectorstore.add_documents(batch)

        print(f"Processados {i+len(batch)} / {len(docs)}")

    print("Vector store criado!")

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 30}
)