import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

# Inicializa LLM
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile",
    api_key=api_key
)

# Instrução inicial do sistema
system_instruction = """
Você é um especialista em levantamento de requisitos e documentação de aplicações. 
Seu papel é ajudar o usuário a definir claramente seu projeto, mesmo que ele não tenha domínio técnico.

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

# Função principal com suporte a memória
def conversar_com_agente(pergunta: str, contexto: list | None = None) -> str:
    """
    pergunta: texto atual do usuário
    contexto: lista de mensagens [{"role": "user"/"assistant", "content": "..."}]
    """
    contexto = contexto or []

    # Sempre começa com a instrução do sistema
    messages = [SystemMessage(content=system_instruction)]

    # Adiciona histórico ao prompt
    for m in contexto:
        if m["role"] == "user":
            messages.append(HumanMessage(content=m["content"]))
        else:
            # Para mensagens do agente, usamos SystemMessage como "resposta anterior"
            messages.append(SystemMessage(content=m["content"]))

    # Adiciona a nova pergunta
    messages.append(HumanMessage(content=pergunta))

    # Chama o modelo
    resposta = llm.invoke(messages)

    return resposta.content


# --- TESTE LOCAL ---
if __name__ == "__main__":
    print("--- Iniciando Agente (Especialista em Requisitos e Documentação) ---")

    # Histórico simulado
    contexto_teste = [
        {"role": "user", "content": "Quero criar um sistema de vendas online."},
        {"role": "assistant", "content": "Você gostaria de incluir controle de estoque e relatórios financeiros?"}
    ]

    # Pergunta de teste
    pergunta_usuario = "Sim, quero relatórios financeiros também."

    print(f"Pergunta: {pergunta_usuario}")
    print("Agente pensando...")

    resposta = conversar_com_agente(pergunta_usuario, contexto=contexto_teste)

    print(f"Resposta: {resposta}")