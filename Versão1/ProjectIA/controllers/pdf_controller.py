import fitz  # PyMuPDF

def ler_conteudo_pdf(caminho_pdf):
    documento = fitz.open(caminho_pdf)
    texto_completo = ""
    for pagina in documento:
        texto_pagina = pagina.get_text()
        texto_completo += texto_pagina
    documento.close()
    return texto_completo

def ler_conteudo_txt(caminho_txt):
    with open(caminho_txt, 'r', encoding='utf-8') as arquivo:
        texto_completo = arquivo.read()
    return texto_completo

def ler_conteudo_arquivo(caminho_arquivo):
    if caminho_arquivo.lower().endswith('.pdf'):
        return ler_conteudo_pdf(caminho_arquivo)
    elif caminho_arquivo.lower().endswith('.txt'):
        return ler_conteudo_txt(caminho_arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado.")
