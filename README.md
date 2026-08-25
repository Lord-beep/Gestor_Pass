# 🔐 GerePass

O **GerePass** é uma aplicação desktop portátil concebida para a gestão e proteção de palavras-passe. Toda a informação é guardada num cofre local devidamente encriptado, garantindo a privacidade e a segurança dos dados do utilizador.

---

## ✨ Funcionalidades

- 🔐 **Cofre Encriptado**: Proteção de dados com encriptação simétrica Fernet e derivação de chave via PBKDF2HMAC.
- 🔑 **Gestão de Credenciais**: Adição, visualização e eliminação de credenciais (serviço, utilizador e palavra-passe).
- 🔎 **Pesquisa e Filtros**: Pesquisa rápida em tempo real por serviço, utilizador ou ambos.
- 👁️ **Visualização Alternável**: Opção para mostrar ou ocultar as palavras-passe salvas na interface.
- 📋 **Cópia Rápida**: Botão para copiar a palavra-passe diretamente para a área de transferência.
- 🔄 **Alteração de Password Mestra**: Possibilidade de reencriptar todo o cofre gerando um novo *salt* aleatório.

---

## 🛠️ Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python 3 | Linguagem principal do projeto |
| CustomTkinter | Interface gráfica moderna para o utilizador |
| Tkinter | Gestão da janela principal e janelas de diálogo |
| Cryptography | Encriptação de dados (Fernet, PBKDF2HMAC, SHA256) |

---

## ⚙️ Instalação

1. Certifique-se de que tem o Python 3 instalado no sistema.
2. Instale as dependências necessárias executando:

```bash
pip install customtkinter cryptography
```

---

## ▶️ Execução

Para iniciar a aplicação, execute o ficheiro principal no terminal:

```bash
python gestor_portatil.py
```

---

## 📖 Como utilizar

### 1. Primeiro Acesso / Autenticação
- Ao abrir a aplicação pela primeira vez, introduza uma **Password Mestra**. Esta chave será utilizada para criar e proteger o seu cofre de dados (`senhas.enc`).
- Nas utilizações subsequentes, introduza a mesma Password Mestra para desbloquear o painel.

### 2. Guardar Nova Credencial
1. Aceda ao separador **Guardar**.
2. Preencha os campos:
   - **Serviço ou Site**: Nome do serviço (ex: `GitHub`, `Gmail`).
   - **Utilizador ou E-mail**: Nome de utilizador ou e-mail de acesso.
   - **Palavra-passe**: A palavra-passe a proteger.
3. Clique em **Gravar em Segurança**.

### 3. Ver e Gerir Credenciais
1. Aceda ao separador **Ver Guardadas**.
2. Utilize a barra de pesquisa para filtrar os registos por site ou utilizador.
3. Utilize os botões de ação em cada cartão:
   - 👁️ **Mostrar/Ocultar**: Alterna a visibilidade da palavra-passe.
   - 📋 **Copiar**: Copia a palavra-passe para a área de transferência.
   - 🗑️ **Apagar**: Elimina a credencial do cofre.

### 4. Alterar Password Mestra
1. Aceda ao separador **Definições**.
2. Introduza a **Nova Password Mestra**.
3. Confirme a alteração. O cofre será reencriptado com uma nova chave e um novo *salt*.

---

## 📁 Estrutura do projeto

```text
GerePass/
├── gestor_portatil.py   # Aplicação principal e interface gráfica
├── seguranca.py         # Módulo de encriptação, gestão do cofre e autenticação
└── style.py             # Configuração de temas, cores e estilos visuais
```

---

## 🧠 Como funciona

A aplicação utiliza um modelo de encriptação local e autónomo:

```text
Utilizador (Password Mestra)
            │
            ▼
   PBKDF2HMAC (SHA256)
  + Salt (16 bytes aleatórios)
  + 600.000 iterações
            │
            ▼
       Chave Fernet
            │
            ▼
 Desencriptação / Encriptação
            │
            ▼
   Ficheiro senhas.enc
```

---

## 🔒 Segurança

- **Derivação de Chave**: Utiliza `PBKDF2HMAC` com algoritmo `SHA-256`, 600.000 iterações e um *salt* aleatório de 16 bytes.
- **Encriptação Simétrica**: As credenciais são encriptadas usando `Fernet` (AES-128 em modo CBC com HMAC).
- **Armazenamento do Salt**: O *salt* é gerado aleatoriamente e armazenado nos primeiros 16 bytes do ficheiro `senhas.enc`.
- **Reencriptação Total**: Ao alterar a Password Mestra, é gerado um novo *salt* aleatório e todos os dados são reencriptados com a nova chave.

---

## ⭐ Projeto

Se este projeto foi útil para si, considere dar uma estrela no repositório!
