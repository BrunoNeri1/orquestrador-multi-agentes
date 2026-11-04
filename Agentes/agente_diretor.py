import os
from google import genai

def criar_prompts(roteiro):
    print("🎨 Passando o roteiro para o Diretor de Arte... Aguarde.\n")
    
    prompt_diretor = f"""
    Você é um Diretor de Arte especialista em engenharia de prompts para Midjourney e DALL-E.
    Analise o seguinte roteiro de vídeo:

    {roteiro}

    Sua tarefa:
    1. Extraia apenas os momentos de imagem marcados com a tag [Visual].
    2. Para cada cena, crie um prompt em INGLÊS, altamente detalhado, descrevendo o que deve ser gerado (inclua termos de iluminação, qualidade da câmera e clima da cena).
    3. Entregue apenas os prompts finais numerados.
    """
    
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    resposta = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt_diretor
    )
    
    return resposta.text