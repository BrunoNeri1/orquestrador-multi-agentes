import os
from google import genai

def criar_roteiro(topicos_do_olheiro):
    print("✍️ Passando a pauta para o Roteirista... Aguarde.\n")
    
    prompt_roteirista = f"""
    Você é um Roteirista especialista em vídeos virais curtos (YouTube Shorts e Instagram Reels).
    O 'Olheiro' da nossa equipe te entregou a seguinte lista de tópicos em alta:

    {topicos_do_olheiro}

    Sua tarefa:
    1. Escolha apenas o tópico com maior potencial de engajamento.
    2. Escreva um roteiro narrado de 30 a 45 segundos.
    3. Formate a saída com as tags [Visual] indicando o que aparece na tela e [Áudio] com o texto exato da narração.
    Mantenha a pegada irônica e dinâmica!
    """
    
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    resposta = client.models.generate_content(
        model='gemini-1.5-pro',
        contents=prompt_roteirista
    )
    
    return resposta.text