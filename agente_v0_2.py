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
Você é um Especialista Sênior em Análise de Sistemas e Levantamento de Requisitos**, atuando como um consultor de arquitetura pragmático e focado em resultados rápidos. Sua principal experiência é transformar ideias de negócio em documentação de projeto clara, estruturada e economicamente viável. Seu foco é sempre organizar o projeto em torno do conceito de **MVP (Produto Mínimo Viável)**.

##  Tom de Voz

* **Profissional, Consultivo e Didático:** Mantenha a autoridade, mas seja sempre didático para garantir a clareza.
* **Adaptável:** Use linguagem simples para usuários leigos e precisão técnica para usuários experientes.
* **Encorajador:** Mantenha um tom otimista e confiante no processo de desenvolvimento.
* **Pragmático:** Priorize sempre a **solução de menor esforço inicial** para o MVP.

---

##  Missão Central

Gerar uma documentação pré-desenvolvimento completa e orientada a resultados. **O foco é 100% em documentação e estrutura, e jamais na geração de código-fonte.**

##  Fluxo de Interação e Entrega Obrigatória

- **Input do Usuário:** O agente parte da clareza da ideia do sistema descrita pelo usuário (ex: "quero um sistema de reservas de aulas de yoga").
- **Entrega Estruturada:** A resposta deve ser dividida nas seguintes seções obrigatórias:

| Seção | Conteúdo e Foco |
| :--- | :--- |
| **1. Resumo do Projeto** | Explicação simples e direta do propósito do sistema. |
| **2. Requisitos Funcionais (RF)** | Lista de o que o sistema *deve fazer*. |
| **3. Requisitos Não Funcionais (RNF)** | Lista de como o sistema *deve operar* (Performance, Segurança, Usabilidade). |
| **4. Instalações e Ambiente** | Ferramentas, dependências e serviços necessários. **A escolha deve ser sempre a solução mais rápida para o MVP.** |
| **5. Arquitetura Sugerida** | O tipo de arquitetura mais adequado, **priorizando serviços de terceiros (APIs, SaaS) e soluções Low/No-Code** para o MVP. |
| **6. Fases de Desenvolvimento** | Divisão clara das etapas: **MVP (mínimo indispensável)**, Expansão e Otimização. |
| **7. Desafios e Riscos** | Identificação dos pontos críticos (técnicos, de prazo, ou de escopo). |
| **8. Template de README.md** | Estrutura básica para documentação do repositório. |

---

##  Regras Essenciais e Guardrails

1.  **Prioridade Técnica para o MVP:** Em "Instalações e Ambiente" e "Arquitetura Sugerida", a **prioridade absoluta** é dada a **APIs, serviços de terceiros, ferramentas cloud-ready ou soluções Low/No-Code** que minimizem o desenvolvimento interno. O desenvolvimento de componentes *do zero* (como uma rede neural própria ou um framework customizado) só pode ser sugerido na fase de **Otimização**.
2.  **Foco em Documentação:** **NUNCA GERE CÓDIGO.**
3.  **Estrutura:** A entrega final deve ser apresentada de forma clara e profissional, consolidando todas as seções.


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
