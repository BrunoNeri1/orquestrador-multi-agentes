# 📽️ Orquestrador Multi-Agentes para Criação de Conteúdo (Shorts/Reels)
**Foco:** Narrativas de Ação, Sobrevivência e Lifestyle.

## 📌 Visão Geral do Projeto
Este projeto implementa um ecossistema de Inteligência Artificial baseado em múltiplos agentes autônomos utilizando a biblioteca `google-genai`. O objetivo é automatizar a esteira de pré-produção, roteirização, direção de arte e estratégia de SEO para vídeos curtos verticais (YouTube Shorts, Instagram Reels, TikTok), otimizando o tempo de criação de conteúdo.

Projeto desenvolvido como parte do bootcamp de IA e Engenharia de Prompts da DIO.

## 🏗️ Arquitetura do Sistema

O framework foi desenhado para operar em duas fases de maturidade: o estado atual (Pré-produção Automatizada) e o estado futuro (Edição Autônoma).

### Fase 1: O "Cérebro" Criativo (MVP - Concluído)
Um pipeline em Python utilizando a API do Google Gemini, onde a saída (`output`) de um agente se torna a entrada (`input`) do próximo.

1.  **Agente 1 - O Olheiro (Pesquisador):** Busca tópicos e tendências no nicho de sobrevivência e lifestyle.
2.  **Agente 2 - O Roteirista:** Transforma o tópico em um roteiro de 30-60 segundos, com ganchos de retenção e marcações de cena `[Visual]` e `[Áudio]`.
3.  **Agente 3 - Diretor de Arte:** Lê as marcações visuais e gera *prompts* técnicos em inglês para IAs geradoras de imagem/vídeo.
4.  **Agente 4 - Estrategista de Redes (SEO):** Gera o título viral, a legenda persuasiva e as hashtags estratégicas.

---

## ⚙️ Fluxo de Trabalho (Como o projeto funciona na prática)

Para garantir a publicação imediata de vídeos enquanto o Agente de Edição está em desenvolvimento, o ecossistema opera no formato híbrido (Human-in-the-loop). 

### Workflow Atual (V1.0)
1.  **Geração:** O script Python roda a cadeia de agentes e entrega o documento completo (Roteiro + Prompts + SEO) no terminal.
2.  **Captação Humana:** O criador grava a locução ou o vídeo base lendo o texto gerado pelo *Agente Roteirista*.
3.  **Montagem Assistida (Edição):** 
    *   *Opção A (IA de Edição):* O roteiro gerado é colado em uma plataforma de IA "Prompt-to-Video" (como InVideo AI ou Fliki), que gera e edita o vídeo automaticamente com base no texto.
    *   *Opção B (Edição Manual Rápida):* As imagens são geradas no Midjourney/Leonardo.ai usando os prompts do *Diretor de Arte*, e a montagem final é feita no CapCut juntando a gravação real com as imagens geradas.
4.  **Publicação:** O vídeo é postado usando o título e as hashtags do *Agente Estrategista*.

### Roadmap Futuro: A "Fábrica" (V2.0)
O objetivo final da arquitetura é eliminar a necessidade de softwares de edição externos. A esteira ganhará novos módulos:

*   **Agente Integrador de Mídia:** Scripts Python que farão requisições via API para o Leonardo.ai (imagens) e OpenAI (legendas dinâmicas).
*   **Agente Montador (Editor Automático):** Uma automação utilizando a biblioteca `MoviePy`. Após gravar o vídeo bruto no celular e jogar em uma pasta, o Agente Montador irá:
    1. Ler o vídeo bruto e cortar os silêncios.
    2. Inserir as imagens de fundo geradas pela IA nos tempos certos.
    3. Queimar as legendas na tela.
    4. Exportar o `.mp4` final no formato 9:16, pronto para upload.