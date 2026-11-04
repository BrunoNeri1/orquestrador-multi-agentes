import os
from google import genai

def criar_estrategia(roteiro):
    print("🚀 Passando tudo para o Estrategista de Redes Sociais... Aguarde.\n")
    
    prompt_social = f"""
    Você é um Social Media especialista no algoritmo do YouTube Shorts e Instagram Reels.
    Baseado no roteiro abaixo, crie:
    1. Um título chamativo (com emojis).
    2. Uma descrição curta e engajadora.
    3. As 5 melhores hashtags para viralizar no nicho tech e de futebol.

    Roteiro:
    {roteiro}
    """
    
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    resposta = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt_social
    )
    
    return resposta.text