import os
from google import genai
from dotenv import load_dotenv

# 1. Configuração padrão (mantida para quando a API voltar)
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. O Prompt do Agente 1 (O Olheiro)
prompt_olheiro = """
Você é um pesquisador de tendências. Aja como o 'Olheiro' do meu time criativo.
Escreva 3 tópicos curtos e irônicos sobre os perrengues que desenvolvedores iniciantes passam ao tentar aprender Python, ou sobre a frustração de torcer para o São Paulo FC recentemente.
Não invente opiniões, apenas entregue os fatos brutos em formato de lista.
"""

print("🕵️ Acordando o Olheiro... Aguarde.\n")

# --- MODO SIMULADOR (MOCK) ATIVADO ---
# Quando o servidor voltar, apague a classe RespostaMock e descomente o bloco original
class RespostaMock:
    text = "1. O desespero de esquecer os dois pontos no final do 'if' e o Python julgar toda a sua linhagem.\n2. Assistir o São Paulo tomar gol de time da zona de rebaixamento nos acréscimos.\n3. Configurar ambiente virtual no Windows e descobrir que o pip sumiu."
resposta = RespostaMock()

# resposta = client.models.generate_content(
#     model='gemini-3.8-flash',
#     contents=prompt_olheiro
# )
# -------------------------------------

# 3. Imprime o resultado
print(resposta.text)
# ==========================================
# AGENTE 2: O ROTEIRISTA
# ==========================================
print("\n✍️ Passando a pauta para o Roteirista... Aguarde.\n")

# A mágica do multi-agente: passamos a "resposta.text" do Olheiro para dentro do novo prompt
prompt_roteirista = f"""
Você é um Roteirista especialista em vídeos virais curtos (YouTube Shorts e Instagram Reels).
O 'Olheiro' da nossa equipe te entregou a seguinte lista de tópicos em alta:

{resposta.text}

Sua tarefa:
1. Escolha apenas o tópico com maior potencial de engajamento (ou misture os dois universos: Python e São Paulo).
2. Escreva um roteiro narrado de 30 a 45 segundos.
3. Formate a saída com as tags [Visual] indicando o que aparece na tela e [Áudio] com o texto exato da narração.
Mantenha a pegada irônica e dinâmica!
"""

# --- MODO SIMULADOR (MOCK) DO ROTEIRISTA ---
class RespostaMockRoteirista:
    text = """[Visual]: Tela dividida. Em cima, um terminal VS Code cheio de erros vermelhos. Embaixo, o escudo do São Paulo FC com chuva caindo.
[Áudio] (Voz cansada e irônica): Sabe o que dói mais que esquecer os dois pontos no final do 'if' e ver o Python julgar toda a sua linhagem? 
[Visual]: Zoom rápido no rosto de um torcedor desesperado.
[Áudio]: É fechar o notebook achando que o dia não pode piorar, ligar a TV e assistir o São Paulo tomar gol de time da zona de rebaixamento nos acréscimos. 
[Visual]: Texto na tela piscando: "Vida de Dev Tricolor".
[Áudio]: Deixa o like aí, porque se depender do meu código ou do meu time, a alegria não vem hoje."""
resposta_roteirista = RespostaMockRoteirista()

# Quando a API estabilizar, descomentaremos o código real abaixo:
# resposta_roteirista = client.models.generate_content(
#     model='gemini-3.8-flash',
#     contents=prompt_roteirista
# )
# -------------------------------------------

# Imprime o roteiro final
print(resposta_roteirista.text)
# ==========================================
# AGENTE 3: O DIRETOR DE ARTE
# ==========================================
print("\n🎨 Passando o roteiro para o Diretor de Arte... Aguarde.\n")

# O input deste agente é o output do Roteirista
prompt_diretor = f"""
Você é um Diretor de Arte especialista em engenharia de prompts para Midjourney e DALL-E.
Analise o seguinte roteiro de vídeo:

{resposta_roteirista.text}

Sua tarefa:
1. Extraia apenas os momentos de imagem marcados com a tag [Visual].
2. Para cada cena, crie um prompt em INGLÊS, altamente detalhado, descrevendo o que deve ser gerado (inclua termos de iluminação, qualidade da câmera e clima da cena).
3. Entregue apenas os prompts finais numerados.
"""

# --- MODO SIMULADOR (MOCK) DO DIRETOR DE ARTE ---
class RespostaMockDiretor:
    text = "Scene 1: Split screen concept art. Top half: a glowing computer monitor showing a dark themed VS Code editor with glowing red syntax error highlights. Bottom half: the São Paulo FC soccer crest under heavy cinematic rain, dramatic dark lighting, 8k resolution, photorealistic.\n\nScene 2: Extreme close up of a young frustrated soccer fan's face in a dimly lit room, hands on head in despair, cinematic neon screen reflection on face, hyper-realistic, vivid emotions, cinematic color grading."
resposta_diretor = RespostaMockDiretor()

# resposta_diretor = client.models.generate_content(
#     model='gemini-3.8-flash',
#     contents=prompt_diretor
# )
# ------------------------------------------------

# Imprime os prompts de imagem gerados
print(resposta_diretor.text)
# ==========================================
# AGENTE 4: O ESTRATEGISTA DE REDES SOCIAIS
# ==========================================
print("\n🚀 Passando tudo para o Estrategista de Redes Sociais... Aguarde.\n")

prompt_social = f"""
Você é um Social Media especialista no algoritmo do YouTube Shorts e Instagram Reels.
Baseado no roteiro abaixo, crie:
1. Um título chamativo (com emojis).
2. Uma descrição curta e engajadora.
3. As 5 melhores hashtags para viralizar no nicho tech e de futebol.

Roteiro:
{resposta_roteirista.text}
"""

# --- MODO SIMULADOR (MOCK) DO ESTRATEGISTA ---
class RespostaMockSocial:
    text = "Título: Quando o Python e o São Paulo FC decidem acabar com o seu dia 🤡🐍⚽\n\nDescrição: Ser dev júnior já é difícil, mas ser dev e são-paulino ao mesmo tempo é teste de resistência! Quem mais aí sofre com o pip e com os acréscimos? Deixa nos comentários qual dos dois te dá mais dor de cabeça! 👇\n\nHashtags: #Python #ProgramadorIniciante #SaoPauloFC #VidaDeDev #HumorTech"
resposta_social = RespostaMockSocial()

# Quando a API voltar:
# resposta_social = client.models.generate_content(
#     model='gemini-3.8-flash',
#     contents=prompt_social
# )
# ---------------------------------------------

print(resposta_social.text)