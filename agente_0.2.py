import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY") 

llm = ChatGroq(
    temperature=0, 
    model_name="llama-3.3-70b-versatile",
    api_key=api_key
)

system_instruction = """
Você é um especialista em levantamento de requisitos e documentação de aplicações. Seu papel é ajudar o usuário a definir claramente seu projeto, mesmo que ele não tenha domínio técnico.

Quando o usuário disser algo genérico como "quero fazer um site com Django", você deve:
- Propor uma stack adequada, caso ele não especifique.
- Fazer perguntas para entender o tipo de projeto, regras de negócio, público-alvo e funcionalidades desejadas.
- Avaliar o nível de conhecimento técnico do usuário. Se ele não tiver experiência, ofereça opções acessíveis e explique os prós e contras de cada uma.
- Só depois que o usuário tomar decisões claras, gere:
  - Os requisitos funcionais e não funcionais.
  - A documentação técnica básica.
  - Um exemplo de README para o projeto.

Mantenha um tom profissional, claro e acolhedor. Evite jargões técnicos sem explicação.
"""

def conversar_com_agente(pergunta):
    messages = [
        SystemMessage(content=system_instruction),
        HumanMessage(content=pergunta),
    ]

    resposta = llm.invoke(messages)
    return resposta.content


# --- TESTE ---
if __name__ == "__main__":
    print("--- Iniciando Agente (Especialista em Requisitos e Documentação) ---")
   

    # Pergunta de teste:
    pergunta_usuario = "Gostaria de criar um blog em html css e js.' "

    print(f"Pergunta: {pergunta_usuario}")
    print("Agente pensando...")

    resposta = conversar_com_agente(pergunta_usuario)

    print(f"Resposta: {resposta}")