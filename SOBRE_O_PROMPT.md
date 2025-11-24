
---

# SOBREOPROMPT.md

## 🎯 Objetivo
Este documento explica as técnicas utilizadas na construção do **prompt do agente de análise de sistemas e levantamento de requisitos**, destacando como ele foi projetado para gerar **documentação pré‑desenvolvimento clara, estruturada e orientada ao conceito de MVP (Produto Mínimo Viável)**.

---

## 🧩 Contexto
O agente foi desenhado para atuar como um **consultor de arquitetura pragmático**, focado em resultados rápidos e economicamente viáveis.  
Ele **não gera código**, mas entrega documentação que pode ser usada como briefing, proposta ou base de projeto.

---

## ⚙️ Técnicas de Prompt Engineering Aplicadas

### 1. **Role Definition (Definição de Persona)**
- O agente é definido como **Especialista Sênior em Análise de Sistemas**.  
- Técnica: delimitar claramente o papel garante consistência e autoridade.  
- Benefício: evita que o agente se desvie para tarefas fora do escopo (ex: programação).

---

### 2. **Adaptive Tone Control (Controle Adaptativo de Tom)**
- O tom é **profissional, consultivo e didático**, mas adaptável:  
  - Linguagem simples para usuários leigos.  
  - Precisão técnica para usuários experientes.  
- Técnica: instruções explícitas sobre tom de voz.  
- Benefício: aumenta acessibilidade e engajamento.

---

### 3. **Scope Guardrail (Restrição de Escopo)**
- O prompt define que o foco é **100% em documentação**, com proibição explícita de código.  
- Técnica: uso de guardrails para limitar escopo.  
- Benefício: garante que o agente não se perca em geração de código ou design.

---

### 4. **Structured Output Enforcement (Saída Estruturada Obrigatória)**
- A resposta deve seguir seções fixas:  
  1. Resumo do Projeto  
  2. Requisitos Funcionais  
  3. Requisitos Não Funcionais  
  4. Instalações e Ambiente  
  5. Arquitetura Sugerida  
  6. Fases de Desenvolvimento  
  7. Desafios e Riscos  
  8. Template de README.md  
- Técnica: obrigatoriedade de estrutura.  
- Benefício: consistência e comparabilidade entre projetos.

---

### 5. **Incremental Roadmapping (Planejamento Incremental via MVP)**
- O projeto é sempre dividido em fases:  
  - **MVP:** mínimo indispensável.  
  - **Expansão:** funcionalidades adicionais.  
  - **Otimização:** melhorias de performance e segurança.  
- Técnica: roadmap incremental.  
- Benefício: ajuda o usuário a visualizar evolução do sistema sem escopo inflado.

---

### 6. **Constraint Engineering (Engenharia de Restrições)**
- Prioridade absoluta para **APIs, SaaS, soluções Low/No‑Code** no MVP.  
- Desenvolvimento customizado só pode ser sugerido em fases avançadas.  
- Técnica: restrições explícitas para escolhas técnicas.  
- Benefício: garante viabilidade econômica e rapidez.

---

### 7. **Document Standardization (Padronização de Documentos)**
- Entrega final sempre consolidada em formato claro e profissional.  
- Técnica: padronização de saída.  
- Benefício: facilita uso como briefing, proposta ou base de projeto.

---

## 📌 Estratégia
- **Evitar loops de perguntas infinitas.**  
- **Sempre entregar documento final consolidado.**  
- **Ensinar MVP como eixo central.**  
- **Antecipar desafios e riscos.**  
- **Manter pragmatismo:** solução de menor esforço inicial.  

---
