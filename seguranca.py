import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

FICHEIRO_DADOS = "senhas.enc"

def gerar_chave(master_password):
    """Deriva uma chave criptográfica AES-256 a partir da password mestra."""
    salt = b'salt_seguro_1234'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

def inicializar_ficheiro(chave):
    """Cria a base de dados portátil encriptada se não existir."""
    if not os.path.exists(FICHEIRO_DADOS):
        f = Fernet(chave)
        with open(FICHEIRO_DADOS, "wb") as ficheiro:
            ficheiro.write(f.encrypt("".encode()))

def ler_dados(chave):
    """Decripta os dados locais diretamente na memória RAM."""
    try:
        f = Fernet(chave)
        with open(FICHEIRO_DADOS, "rb") as ficheiro:
            dados_enc = ficheiro.read()
        return f.decrypt(dados_enc).decode()
    except Exception:
        return False

def gravar_dados(chave, dados_texto):
    """Cifra os dados e grava-os por cima do ficheiro portátil."""
    f = Fernet(chave)
    with open(FICHEIRO_DADOS, "wb") as ficheiro:
        ficheiro.write(f.encrypt(dados_texto.encode()))

def alterar_password_mestra(chave_antiga, password_nova):
    """Reencripta todos os dados guardados com uma nova password mestra."""
    dados_atuais = ler_dados(chave_antiga)
    if dados_atuais is False:
        return False
    nova_chave = gerar_chave(password_nova)
    gravar_dados(nova_chave, dados_atuais)
    return nova_chave

def eliminar_credencial(chave, servico_apagar):
    """Filtra os dados na RAM e remove o serviço sem deixar rastos ou metadados."""
    dados_atuais = ler_dados(chave)
    if dados_atuais is False:
        return False
    
    linhas = dados_atuais.strip().split("\n")
    novas_linhas = []
    encontrado = False
    
    for linha in linhas:
        if "|" in linha:
            srv, usr, psw = linha.split("|")
            if srv.lower() == servico_apagar.lower():
                encontrado = True  
            else:
                novas_linhas.append(linha)
                
    if not encontrado:
        return "nao_encontrado"
        
    texto_final = "\n".join(novas_linhas) + ("\n" if novas_linhas else "")
    gravar_dados(chave, texto_final)
    return True
