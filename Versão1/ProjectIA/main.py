from services.genai_service import configure_genai
from controllers.pdf_controller import ler_conteudo_arquivo

def main():
    model = configure_genai()

    # Aqui você pode usar tanto caminho para PDF quanto para TXT.
    caminho_do_arquivo = "documentos/data.txt"  # Pode ser .txt ou .pdf
    texto_arquivo = ler_conteudo_arquivo(caminho_do_arquivo)
    # print(texto_arquivo)

    while True:
        perguntas = input("Faça uma pergunta: ")
        if perguntas.lower() == "para":
            break

        prompt = f"""\nHuman:\n"
        Você é um assistente de suporte técnico.
        Considere os documentos de suporte como único contexto:

        <documentos_de_suporte>
        {texto_arquivo}
        </documentos_de_suporte>

        Por favor, responda à solicitação do usuário {perguntas}.

        Caso seja uma pergunta que esteja fora do escopo dos documentos de suporte ou a informação não conste neles, explique que a resposta não está disponível nos documentos de suporte.

        Se for uma pergunta relacionada aos documentos de suporte e a resposta puder ser encontrada neles, forneça a resposta de um jeito humanizada do documento que fundamenta a sua resposta.

        Caso alguma informação solicitada não esteja disponível nos documentos de suporte, indique claramente como "não informada".

        Quando mencionar procedimentos ou diretrizes específicas dos documentos de suporte, inclua a devida referência ao trecho correspondente.

        Seja sucinto e objetivo na resposta.

        O padrão de retorno deve seguir:

        - RESPOSTA
        > Referência da resposta
        "
        Assistant:
            """        

        response = model.generate_content(prompt)
        print(response.text)

if __name__ == "__main__":
    main()
