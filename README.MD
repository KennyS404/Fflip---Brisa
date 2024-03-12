# Guia de Configuração do Projeto

Este projeto é uma aplicação combinando Flask (Python) e um projeto TypeScript com o Baileys (WhatsApp API). Ele utiliza o MongoDB como banco de dados e é executado em um ambiente Docker. Siga as instruções abaixo para configurar o ambiente e executar o projeto.

## Pré-requisitos

- Docker
- Node.js
- Python
- Git

### Configuração em Ubuntu e Windows

#### Instalação do Docker

**Ubuntu:**

- sudo apt-get update sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin


**Windows:**

Baixe e instale o Docker Desktop do [site oficial](https://www.docker.com/products/docker-desktop).

#### Instalação do Node.js

**Ubuntu:**

- sh curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash 
- sudo apt-get install -y nodejs


**Windows:**

Baixe e instale o Node.js do [site oficial](https://nodejs.org/en/download/).

#### Instalação do Python

**Ubuntu:**

- sudo apt-get update sudo apt-get install -y python3 python3-pip



**Windows:**

Baixe e instale o Python do [site oficial](https://www.python.org/downloads/). Durante a instalação, marque a opção para adicionar o Python ao PATH.

### Clonar o Repositório Git

- git clone <URL_DO_REPOSITORIO> cd <DIRETORIO_DO_REPOSITORIO>


Substitua `<URL_DO_REPOSITORIO>` pela URL do seu repositório e `<DIRETORIO_DO_REPOSITORIO>` pelo nome do diretório criado.

### Instalação de Dependências

**Python:**

pip3 ou pip install flask pymongo langchain_community


**Node.js:**

- npm install


### Configuração do MongoDB com Docker
Inicie o MongoDB com Docker:
- docker-compose up -d


### Configuração da Conexão MongoDB

Edite o arquivo principal do seu projeto Flask (por exemplo, `app.py`) para usar as credenciais definidas no Docker Compose:

python client = MongoClient('mongodb://root:example@localhost:27017/')


### Principais Comandos do Git

- Clonar um repositório: `git clone <URL_DO_REPOSITORIO>`
- Verificar o status: `git status`
- Adicionar arquivos: `git add .`
- Commitar mudanças: `git commit -m "Mensagem do commit"`
- Enviar para o repositório remoto: `git push`
- Atualizar o repositório local: `git pull`

### Execução do Projeto

**Flask (Backend Python):**

export FLASK_APP=model.py flask run ou python3 model.py


**Node.js (Frontend/Integração WhatsApp):**

- npm run dev
