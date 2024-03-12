from flask import Flask, request, jsonify
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_community.vectorstores import faiss
from langchain_community.llms import huggingface_hub
import os
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['nome_do_seu_banco_de_dados']
collection = db['nome_da_sua_colecao']
from langchain.chains.question_answering import load_qa_chain
app = Flask(__name__)

historico_perguntas_respostas = []

# Configuração do ambiente e variáveis necessárias
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "token_da_huggingface"
caminho_correto_do_arquivo = '/home/kenny/brisa/Fflip---Brisa/python-model/data.csv'

# Configuração inicial do modelo e documentação
loader = CSVLoader(caminho_correto_do_arquivo)
document = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(document)
embeddings = HuggingFaceEmbeddings()
llm = huggingface_hub.HuggingFaceHub(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", model_kwargs={"temperature": 0.9, "maxlength": 512})
chain = load_qa_chain(llm, chain_type="stuff")
db = faiss.FAISS.from_documents(docs, embeddings)

# Definição da rota de API para receber perguntas e retornar respostas
@app.route('/pergunta', methods=['POST'])
def responder_pergunta():
    # Obter a pergunta do corpo da requisição
    dados = request.json
    pergunta = dados.get('pergunta')
    
    # Verificação de segurança básica
    if not pergunta:
        return jsonify({"erro": "Nenhuma pergunta fornecida"}), 400
    
    # Armazenar a pergunta no MongoDB
    collection.insert_one({"pergunta": pergunta})
    
    # Recuperar todas as perguntas do MongoDB para gerar a memória da IA
    perguntas_historico = list(collection.find({}, {"_id": 0, "pergunta": 1}))
    perguntas_historico = [item['pergunta'] for item in perguntas_historico]
    print(perguntas_historico)
    # Criação do banco de dados de vetores e busca por similaridade
    docsResult = db.similarity_search(pergunta)
    
    # Executar a cadeia de QA para obter a resposta
    resposta = chain.run(input_documents=docsResult, question=pergunta)
    
    # Armazenar no histórico
    historico_perguntas_respostas.append((pergunta, resposta))
    
    # Retornar a resposta
    return jsonify({"pergunta": pergunta, "resposta": resposta})

if __name__ == "__main__":
    app.run(port=6000)  # Rodar a aplicação na porta X
