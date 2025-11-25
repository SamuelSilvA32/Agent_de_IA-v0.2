## 🔑 Configuração da API Groq

Este projeto utiliza a **API da Groq** para processamento de IA.  
Para rodar o sistema corretamente, é necessário configurar uma chave de API.

### 1. Obter a chave
- Crie uma conta ou faça login no [Groq Console](https://console.groq.com/keys).
- Gere uma nova chave de API no painel de **API Keys**.

### 2. Criar o arquivo `.env`
Na raiz do projeto, crie um arquivo chamado `.env` e adicione a seguinte linha: 

GROQ_API_KEY="coloque_sua_chave_aqui"

### 3. Usar a chave no projeto
Certifique-se de que o código ou framework utilizado esteja configurado para ler variáveis de ambiente.  
Exemplo em Python (com `python-dotenv`):

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
