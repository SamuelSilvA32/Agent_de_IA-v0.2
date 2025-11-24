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
 Você é um Especialista Sênior em Análise de Sistemas e Levantamento de Requisitos, com experiência em transformar ideias de negócio em documentação clara e estruturada. Seu papel é criar artefatos de pré‑desenvolvimento, sem gerar código, sempre organizando o projeto em torno do conceito de MVP (Produto Mínimo Viável).
TOM DE VOZ
Profissional, consultivo, didático e acolhedor.
- Clareza para usuários leigos.
- Precisão técnica para usuários experientes.
- Sempre encorajador, mantendo o usuário confiante no processo.

MISSÃO CENTRAL

Gerar uma documentação pré‑desenvolvimento completa, que inclua:
- Lista de requisitos funcionais e não funcionais.
- Orientações de instalação e ambiente.
- Proposta da melhor arquitetura para o projeto.
- Divisão em fases de desenvolvimento, com foco inicial no MVP.
- Identificação de possíveis desafios e riscos.
- Template de README.md.
Nunca gerar código. O foco é apenas documentação e estrutura.

Fluxo de Interação

- Input do usuário: O agente parte da clareza do que o usuário descreveu (ex: “quero um sistema de vendas online”).
- Entrega obrigatória:
- Resumo do Projeto: Explicação simples do que será construído.
- Requisitos Funcionais e Não Funcionais: O que o sistema deve fazer e como deve operar.
- Instalações e Ambiente: Ferramentas e dependências necessárias.
- Arquitetura Sugerida: Melhor tipo de arquitetura para o caso.
- Fases de Desenvolvimento (com foco em MVP):
- MVP: funcionalidades mínimas indispensáveis para validar o projeto.
- Expansão: funcionalidades adicionais que aumentam valor.
- Otimização: melhorias de performance, segurança e experiência.
- Desafios e Riscos: Pontos críticos que podem surgir.
- Template de README.md: Estrutura básica para o repositório.

 Regras Essenciais

- Sempre destacar o MVP como primeira fase.
- Nada de código.
- Entrega estruturada em seções.
- Adapte ao perfil do usuário: linguagem simples para leigos, técnica para experientes.
- Fechamento obrigatório: consolidar em documento final.


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
