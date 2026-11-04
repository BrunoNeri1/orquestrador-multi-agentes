import os
from dotenv import load_dotenv

# Importa as funções da pasta Agentes
from Agentes.agente_olheiro import gerar_tendencias
from Agentes.agente_roteirista import criar_roteiro
from Agentes.agente_diretor import criar_prompts
from Agentes.agente_estrategista import criar_estrategia

# Configuração de ambiente
load_dotenv()
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")) # Para quando a API voltar

print("🎬 Iniciando a Fábrica de Conteúdo...\n")
print("-" * 50)

# 1. Olheiro gera os tópicos
topicos = gerar_tendencias()
print(topicos)
print("-" * 50)

# 2. Roteirista recebe os tópicos e cria o roteiro
roteiro = criar_roteiro(topicos)
print(roteiro)
print("-" * 50)

# 3. Diretor recebe o roteiro e cria os prompts de imagem
prompts = criar_prompts(roteiro)
print(prompts)
print("-" * 50)

# 4. Estrategista recebe o roteiro e cria a cópia social
estrategia = criar_estrategia(roteiro)
print(estrategia)
print("-" * 50)

print("✅ Processo finalizado com sucesso!")