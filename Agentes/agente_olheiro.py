import os
from google import genai

def gerar_tendencias():
    print("🕵️ Acordando o Olheiro... Aguarde.\n")
    
    prompt_olheiro = """
    Você é um pesquisador de tendências. Aja como o 'Olheiro' do meu time criativo.
    Escreva 3 tópicos curtos e irônicos sobre os perrengues que desenvolvedores iniciantes passam ao tentar aprender Python, ou sobre a frustração de torcer para o São Paulo FC recentemente.
    Não invente opiniões, apenas entregue os fatos brutos em formato de lista.
    """
    
    # Chama a API real do Google
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    resposta = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt_olheiro
    )
    
    return resposta.text