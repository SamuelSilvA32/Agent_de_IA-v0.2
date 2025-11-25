

# 🧠 agenteV0.2

## 📌 Visão Geral

O `agenteV0.2` é um assistente inteligente para levantamento de requisitos e documentação de aplicações. Desenvolvido com a biblioteca `langchain_groq` e o modelo `llama-3.3-70b-versatile`, ele ajuda usuários — mesmo sem conhecimento técnico — a definir projetos de software com clareza, propondo stacks, levantando requisitos e gerando documentação.

---

## 🚀 Funcionalidades

- Interação natural com o usuário para entender ideias de projeto
- Sugestão de tecnologias adequadas (frontend, backend, banco de dados)
- Geração automática de requisitos funcionais e não funcionais
- Criação de documentação técnica em linguagem acessível
- Interface web com Streamlit para uso direto no navegador

---

## 🛠️ Tecnologias Utilizadas

- `Python 3.11+`
- `langchain_groq`
- `llama-3.3-70b-versatile`
- `Streamlit` para interface web
- `python-dotenv` para gerenciamento de variáveis de ambiente

---

## 📦 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/SamuelSilvA32/Agente_demo_0.2.git
cd Agente_demo_0.2
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua chave da API

Crie um arquivo `.env` com:

```env
GROQ_API_KEY=sua_chave_aqui
```

---

## 🖥️ Interface Web com Streamlit

### Executar a interface:

```bash
streamlit run app.py
```

O navegador abrirá automaticamente com a interface do agente.

---

## 📁 Estrutura do Projeto

```
Agente_demo_0.2/
├── agente.py
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env  # não versionado
```

---
  “Este projeto utiliza uma chave de API. Configure um arquivo .env com sua chave. Para mais detalhes, veja a seção de Configuração.”


## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes 
