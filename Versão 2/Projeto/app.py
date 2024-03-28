from flask import Flask, render_template, request, jsonify  # Import jsonify para tratar a resposta como JSON
from dotenv import load_dotenv
import os
import google.generativeai as genai
from time import sleep
from helpers import *

load_dotenv()

app = Flask(__name__)

api_key = os.getenv('GOOGLE_API_KEY')
if api_key is None:
    raise ValueError("The environment variable 'GOOGLE_API_KEY' is not defined.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

contexto = carrega("dados/ecomart.txt")

def bot(prompt):
    maximo_tentativas = 1
    repeticao = 0

    while True:
        try:
            prompt_do_sistema = f"""
            Você é um chatbot de atendimento a clientes de um e-commerce. 
            Você não deve responder perguntas que não sejam dados do ecommerce informado!
            Você deve gerar respostas utilizando o contexto abaixo.
            Pergunta: {prompt}
            # Contexto
            {contexto}
            """
            # Ajuste esta parte conforme a estrutura de resposta da API
            response = model.generate_content(prompt_do_sistema)
            texto_resposta = response.text  # Ajuste '.text' para o atributo correto que contém o texto da resposta
            return texto_resposta
        except Exception as erro:
                repeticao += 1
                if repeticao >= maximo_tentativas:
                        return f"Erro no GPT: {erro}"
                print('Erro de comunicação com OpenAI:', erro)
                sleep(1)

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["msg"]
    resposta = bot(prompt)
    # Supondo que `bot` retorne diretamente a string de resposta, apenas retorne ela.
    # Certifique-se de que a função bot esteja realmente retornando uma string diretamente.
    return resposta, 200, {'ContentType':'text/plain'} 

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
