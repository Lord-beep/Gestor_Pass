# 🚀 GerePass

O **GerePass** é um gestor de palavras-passe portátil concebido para armazenar e gerir credenciais de forma segura num ficheiro local encriptado. A aplicação conta com uma interface gráfica moderna e garante que os dados sensíveis são apenas descifrados em memória RAM durante a utilização.

---

## ✨ Funcionalidades

- 🔑 **Autenticação Mestra:** Acesso protegido por uma palavra-passe mestra única.
- 🔐 **Encriptação Forte:** Armazenamento de credenciais num ficheiro local encriptado (`senhas.enc`).
- 💾 **Guardar Credenciais:** Registo seguro de serviço/site, nome de utilizador e palavra-passe.
- 👁️ **Visualização de Cofre:** Leitura e apresentação das credenciais descifradas diretamente em memória RAM.
- 🗑️ **Remoção de Registos:** Eliminação de credenciais específicas por nome de serviço sem deixar metadados.
- 🔄 **Gestão da Chave Mestra:** Alteração da palavra-passe mestra com reencriptação automática de todos os dados guardados.

---

## 🛠️ Tecnologias

| Tecnologia | Utilização |
|---|---|
| **Python** | Linguagem de programação principal |
| **CustomTkinter** | Interface gráfica moderna |
| **Tkinter** | Gestão de componentes gráficos e caixas de diálogo |
| **Cryptography** | Módulos `Fernet` e `PBKDF2HMAC` para segurança e cifragem |

---

## ⚙️ Instalação

### Pré-requisitos

Certifique-se de que tem o Python instalado no seu sistema.

### Dependências

Instale as dependências necessárias executando o seguinte comando no terminal:

```bash
pip install customtkinter cryptography
```

---

## ▶️ Execução

Para iniciar a aplicação, execute o ficheiro principal:

```bash
python gestor_portatil.py
```

---

## 📖 Como utilizar

1. **Acesso Inicial:**
   - Ao abrir a aplicação, introduza a sua **Palavra-passe Mestra**. 
   - Se for a primeira utilização, a palavra-passe introduzida será utilizada para inicializar o cofre encriptado.

2. **Guardar Password:**
   - Aceda à aba **Guardar Password**.
   - Preencha o nome do serviço/site, utilizador/e-mail e a palavra-passe associada.
   - Clique em **Gravar em Segurança**.

3. **Ver e Eliminar Guardadas:**
   - Na aba **Ver Guardadas**, visualize a lista de credenciais armazenadas no cofre.
   - Para remover um registo, introduza o nome exato do serviço no campo correspondente e clique em **Apagar**.

4. **Definições:**
   - Na aba **Definições**, introduza uma nova palavra-passe mestra e confirme em **Confirmar Nova Chave** para reencriptar a base de dados.

---

## 📁 Estrutura do projeto

```text
.
├── gestor_portatil.py
├── seguranca.py
└── style.py
```

---

## 🧠 Como funciona

O GerePass utiliza uma arquitetura simples focada na segurança e privacidade local:

```text
Utilizador (Palavra-passe Mestra)
            │
            ▼
   PBKDF2HMAC (SHA256)
            │
            ▼
    Chave AES-256 (Fernet)
            │
            ▼
Decifragem em Memória RAM ◄──► Ficheiro Local (senhas.enc)
```

1. A palavra-passe mestra é submetida ao algoritmo **PBKDF2HMAC** com **SHA256** (100.000 iterações) para derivar uma chave simétrica segura.
2. A biblioteca **Fernet** (baseada em AES-256 em modo CBC com HMAC) é utilizada para cifrar e descifrar o conteúdo.
3. Os dados descifrados residem unicamente na memória RAM enquanto a aplicação está em execução.

---

## 🔒 Segurança

- **Ficheiro Local:** Os dados são guardados exclusivamente no ficheiro `senhas.enc`.
- **Derivação de Chave:** Utiliza PBKDF2 com HMAC e SHA-256 para prevenir ataques de força bruta.
- **Proteção de Dados:** As credenciais nunca são gravadas em texto limpo no disco.

---

## ⭐ Projeto

Se este projeto lhe foi útil, considere dar uma estrela no repositório!
