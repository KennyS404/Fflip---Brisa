<div align="center">
  <img src="./assets/Logoflipp.png" alt="Logo UOL" width="120px" height="120px">
</div>

<div align="center">
  <h1>UOL ImigraLingo Assist</h1>
</div>

<div align="center">
  <h2>UOL ImigraLingo Assist - O desenvolvimento do chatbot destinado a servir como um Guia Multifuncional para Imigrantes Francófonos no Brasil</h2>
</div>

<div align="center">
  <p>Conheça a incrível equipe por trás deste projeto</p>
</div>

<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://github.com/angemydelson">
          <img src="https://avatars.githubusercontent.com/u/98717411?v=4" width="100px;" alt="Foto do Angemydelson Saint Bert"/><br>
          <sub><b>Angemydelson Saint Bert</b></sub>
        </a>
      </td>
      <td align="center">
        <a href="https://www.linkedin.com/in/kennildogoncalves/">
          <img src="https://avatars.githubusercontent.com/u/101444699?v=4s" width="100px;" alt="Foto do Kennildo Bastos"/><br>
          <sub><b>Kennildo Bastos</b></sub>
        </a>
      </td>
      <td align="center">
        <a href="https://www.linkedin.com/in/mariana-oliveira-cintra-b67918103/">
          <img src="https://avatars.githubusercontent.com/u/56887397?v=4" width="100px;" alt="Foto do Mariana Oliveira Cintra"/><br>
          <sub><b>Mariana Oliveira Cintra</b></sub>
        </a>
      </td>
      <td align="center">
        <a href="https://www.linkedin.com/in/sarah-oliveira-cintra-bastos-60343b176/">
          <img src="" width="100px;" alt="Foto do Sarah Oliveira Cintra"/><br>
          <sub><b>Sarah Oliveira Cintra</b></sub>
        </a>
      </td>
    </tr>
  </table>
</div>

---
---
## 📖 Sumário
- [1 - Objetivo](#ancora1)
  - [1.1 - Tecnologias Utilizadas](#ancora1-1)
- [2 - Funcionalidades](#ancora2)
- [3 - Desenvolvimento do Projeto](#ancora3)
- [4 - Estrutura de Pastas do Projeto](#ancora4)
- [5 - Configurações e Requisitos do projeto](#ancora5)
  - [5.1 - Instalação do Docker](#ancora1-1)
  - [5.2 - Instalação do Node.js](#ancora1-1)
  - [5.3 - Instalação do Python](#ancora1-1)
  - [5.4 - Clonar o Repositório Git](#ancora1-1)
  - [5.5 - Instalação de Dependências](#ancora1-1)
  - [5.6 - Configuração do MongoDB com Docker](#ancora1-1)
  - [5.7 - Configuração da Conexão MongoDB](#ancora1-1)
  - [5.8 - Principais Comandos do Git](#ancora1-1)
  - [5.9 - Execução do Projeto](#ancora1-1)
- [6 - Dificuldades conhecidas](#ancora6)
- [7 - Licença](#ancora7)

---

<a id="ancora1"></a>

## 1. Objetivo

  O chatbot------------

<a id="ancora1-1"></a>
### 1.1 Ferramentas Utilizadas

<div align="center">
  <img align="center" alt="Python" height="30" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" />
  <img align="center" alt="Git" height="28" width="42" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg">
  <img align="center" alt="Whatsapp" height="28"  src="https://www.pngkit.com/png/full/3-36604_whatsapp-png.png" />
  <img align="center" alt="Node JS" height="28"  src="assets/node.png" />
  <img align="center" alt="Docker" height="28"  src="assets/docker.png" />
</div>


---

<a id="ancora2"></a>

## 2. Funcionalidades
  
  **1.  📸🔍**

  

  **2.  🗣️📜**

  

  **3.  🌆📻**


  **4.  🚨🏥**


  **5.  📄🌐**

  
<a id="ancora3"></a>

## 3 - Desenvolvimento do Projeto
  

<a id="ancora4"></a>

## 4 - Estrutura de Pastas do Projeto

<a id="ancora5"></a>

## 5. Configurações e Requisitos do projeto

### Configuração em Ubuntu e Windows

#### 5.1 Instalação do Docker

**Ubuntu:**

- sudo apt-get update sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin


**Windows:**

Baixe e instale o Docker Desktop do [site oficial](https://www.docker.com/products/docker-desktop).

#### 5.2 Instalação do Node.js

**Ubuntu:**

- sh curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash 
- sudo apt-get install -y nodejs


**Windows:**

Baixe e instale o Node.js do [site oficial](https://nodejs.org/en/download/).

#### 5.3 Instalação do Python

**Ubuntu:**

- sudo apt-get update sudo apt-get install -y python3 python3-pip



**Windows:**

Baixe e instale o Python do [site oficial](https://www.python.org/downloads/). Durante a instalação, marque a opção para adicionar o Python ao PATH.

#### 5.4 Clonar o Repositório Git

- git clone <URL_DO_REPOSITORIO> cd <DIRETORIO_DO_REPOSITORIO>


Substitua `<URL_DO_REPOSITORIO>` pela URL do seu repositório e `<DIRETORIO_DO_REPOSITORIO>` pelo nome do diretório criado.

#### 5.5 Instalação de Dependências

**Python:**

pip3 ou pip install flask pymongo langchain_community


**Node.js:**

- npm install


#### 5.6 Configuração do MongoDB com Docker
Inicie o MongoDB com Docker:
- docker-compose up -d


#### 5.7 Configuração da Conexão MongoDB

Edite o arquivo principal do seu projeto Flask (por exemplo, `app.py`) para usar as credenciais definidas no Docker Compose:

python client = MongoClient('mongodb://root:example@localhost:27017/')


#### 5.8 Principais Comandos do Git

- Clonar um repositório: `git clone <URL_DO_REPOSITORIO>`
- Verificar o status: `git status`
- Adicionar arquivos: `git add .`
- Commitar mudanças: `git commit -m "Mensagem do commit"`
- Enviar para o repositório remoto: `git push`
- Atualizar o repositório local: `git pull`

#### 5.9 Execução do Projeto

**Flask (Backend Python):**

export FLASK_APP=model.py flask run ou python3 model.py


**Node.js (Frontend/Integração WhatsApp):**

- npm run dev

<a id="ancora6"></a>

## 6. Dificuldades conhecidas

  **1.** 

---

<a id="ancora7"></a>

## 7 - Licença

