import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, LLM
import crewai.llms.cache as _crewai_cache

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Monkey-patch para contornar um bug na CrewAI com a Groq e o cache_breakpoint
_crewai_cache.mark_cache_breakpoint = lambda msg: msg

def main():
    # Verifica se a API Key foi configurada
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "sua_chave_da_groq_aqui":
        print("❌ Erro: GROQ_API_KEY não encontrada. Verifique se você criou o arquivo .env corretamente.")
        return

    # Instanciando o LLM corretamente usando a classe da própria CrewAI
    llm_groq = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=api_key
    )

    # Criando o Agente Especialista
    assistente = Agent(
        role="Assistente Inteligente",
        goal="Responder de forma clara e precisa às dúvidas do usuário.",
        backstory="Você é um assistente virtual prestativo e muito inteligente.",
        llm=llm_groq, 
        verbose=False  # Desativado para o terminal ficar limpo como um chat
    )

    print("🤖 Chat iniciado! Digite sua pergunta (ou 'sair' para encerrar):")

    while True:
        try:
            pergunta_usuario = input("\nVocê: ")
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\n🤖 Assistente: Até logo!")
            break

        if pergunta_usuario.strip().lower() == 'sair':
            print("🤖 Assistente: Até logo!")
            break

        if not pergunta_usuario.strip():
            continue

        # Criando a tarefa dinamicamente com a sua pergunta
        tarefa = Task(
            description=pergunta_usuario,
            expected_output="Uma resposta direta e natural para o usuário.",
            agent=assistente
        )

        # Executando a resposta do agente
        crew = Crew(
            agents=[assistente],
            tasks=[tarefa]
        )
        
        resultado = crew.kickoff()
        print(f"\n🤖 Assistente: {resultado}")

if __name__ == "__main__":
    main()
