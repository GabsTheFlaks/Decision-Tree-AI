# 🤖 CrewAI Chatbot
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Agent-orange?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3-black?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Este repositório contém um assistente virtual simples rodando diretamente no terminal, construído utilizando o framework **[CrewAI](https://www.crewai.com/)** e potencializado pelos modelos de linguagem super rápidos da **[Groq](https://groq.com/)** (especificamente o modelo `llama-3.3-70b-versatile`).

⚠️ **Aviso:** Este projeto foi criado e submetido ao GitHub estritamente como **conteúdo educacional** e serve como uma **prova de conceito (Proof of Concept - PoC)** de como orquestrar agentes IA autônomos com o CrewAI consumindo APIs externas.

## ✨ Recursos

- **Assistente Interativo**: Interface de chat direta no terminal limpa e rápida.
- **Processamento Ultra Rápido**: Integrado à Groq para inferência LLM quase instantânea.
- **Integração Segura**: Utiliza variáveis de ambiente (arquivo `.env`) protegendo chaves de acesso para que não vazem no código.
- **Correção Embutida**: Contém um *monkey-patch* no código que corrige bugs conhecidos (ex: envio de `cache_breakpoint` inválido) entre CrewAI/LiteLLM e a API da Groq.

## 🚀 Como começar

### Pré-requisitos
- Python 3.10 ou superior(não use python 3.14 ele quebra).
- Uma chave de API gratuita da Groq (Crie uma em [console.groq.com](https://console.groq.com)).

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/GabsTheFlaks/Decision-Tree-AI.git
   cd Decision-Tree-AI
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   
   # No Windows:
   .\.venv\Scripts\activate
   
   # No Linux/Mac:
   source .venv/bin/activate
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure sua chave de API:
   - Faça uma cópia do arquivo `.env.example` e renomeie para `.env`.
   - Adicione sua API Key da Groq dentro do arquivo `.env`:
     ```env
     GROQ_API_KEY=sua_chave_real_aqui
     ```

### Uso

Para iniciar o chat e começar a conversar com o agente, basta rodar o comando:
```bash
python main.py
```
