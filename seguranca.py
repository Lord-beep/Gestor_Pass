import os
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


FICHEIRO_DADOS = "senhas.enc"

# Salt com 16 bytes aleatórios
TAMANHO_SALT = 16

# Número de iterações do PBKDF2
ITERACOES = 600_000


def gerar_salt():
    """
    Gera um salt criptograficamente seguro e aleatório.
    """
    return os.urandom(TAMANHO_SALT)


def gerar_chave(master_password, salt):
    """
    Deriva uma chave Fernet a partir da Password Mestra
    e do salt.
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERACOES
    )

    chave = kdf.derive(
        master_password.encode("utf-8")
    )

    return base64.urlsafe_b64encode(chave)


def inicializar_ficheiro(master_password):
    """
    Cria o cofre caso ainda não exista.

    O salt é gerado aleatoriamente apenas uma vez
    e fica guardado no início do ficheiro.
    """

    if os.path.exists(FICHEIRO_DADOS):
        return True

    salt = gerar_salt()

    chave = gerar_chave(
        master_password,
        salt
    )

    f = Fernet(chave)

    dados_vazios = f.encrypt(
        b""
    )

    try:

        with open(
            FICHEIRO_DADOS,
            "wb"
        ) as ficheiro:

            # Primeiro guardamos o salt
            ficheiro.write(
                salt
            )

            # Depois os dados encriptados
            ficheiro.write(
                dados_vazios
            )

        return True

    except Exception:

        return False


def obter_salt():
    """
    Lê o salt guardado no ficheiro.
    """

    try:

        with open(
            FICHEIRO_DADOS,
            "rb"
        ) as ficheiro:

            salt = ficheiro.read(
                TAMANHO_SALT
            )

        if len(salt) != TAMANHO_SALT:
            return False

        return salt

    except Exception:

        return False


def autenticar(master_password):
    """
    Obtém o salt existente e deriva a chave
    correspondente à Password Mestra.
    """

    salt = obter_salt()

    if salt is False:
        return False

    return gerar_chave(
        master_password,
        salt
    )


def ler_dados(chave):
    """
    Desencripta os dados do cofre.
    """

    try:

        with open(
            FICHEIRO_DADOS,
            "rb"
        ) as ficheiro:

            # Ignorar os primeiros 16 bytes,
            # que correspondem ao salt
            ficheiro.seek(
                TAMANHO_SALT
            )

            dados_encriptados = (
                ficheiro.read()
            )

        f = Fernet(chave)

        return f.decrypt(
            dados_encriptados
        ).decode("utf-8")

    except Exception:

        return False


def gravar_dados(chave, dados_texto):
    """
    Encripta os dados e mantém o salt existente.
    """

    try:

        salt = obter_salt()

        if salt is False:
            return False

        f = Fernet(chave)

        dados_encriptados = f.encrypt(
            dados_texto.encode("utf-8")
        )

        with open(
            FICHEIRO_DADOS,
            "wb"
        ) as ficheiro:

            # Manter o mesmo salt
            ficheiro.write(
                salt
            )

            # Escrever os novos dados
            ficheiro.write(
                dados_encriptados
            )

        return True

    except Exception:

        return False


def adicionar_credencial(
    chave,
    servico,
    utilizador,
    password
):
    """
    Adiciona uma credencial ao cofre.
    """

    dados_atuais = ler_dados(
        chave
    )

    if dados_atuais is False:
        return False

    nova_linha = (
        f"{servico}|{utilizador}|{password}\n"
    )

    return gravar_dados(
        chave,
        dados_atuais + nova_linha
    )


def eliminar_credencial(
    chave,
    servico_apagar
):
    """
    Remove todas as credenciais do serviço indicado.
    """

    dados_atuais = ler_dados(
        chave
    )

    if dados_atuais is False:
        return False

    linhas = dados_atuais.strip().split(
        "\n"
    )

    novas_linhas = []
    encontrado = False

    for linha in linhas:

        if "|" not in linha:
            continue

        try:

            servico, utilizador, password = (
                linha.split("|", 2)
            )

        except ValueError:

            continue

        if (
            servico.lower()
            == servico_apagar.lower()
        ):

            encontrado = True

        else:

            novas_linhas.append(
                linha
            )

    if not encontrado:
        return "nao_encontrado"

    if novas_linhas:

        texto_final = (
            "\n".join(
                novas_linhas
            ) + "\n"
        )

    else:

        texto_final = ""

    return gravar_dados(
        chave,
        texto_final
    )


def alterar_password_mestra(
    chave_antiga,
    password_nova
):
    """
    Cria um NOVO salt aleatório e reencripta
    todo o cofre com a nova Password Mestra.

    Isto é uma vantagem adicional:
    ao mudar a Password Mestra, o salt também muda.
    """

    dados_atuais = ler_dados(
        chave_antiga
    )

    if dados_atuais is False:
        return False

    # Novo salt aleatório
    novo_salt = gerar_salt()

    nova_chave = gerar_chave(
        password_nova,
        novo_salt
    )

    f = Fernet(
        nova_chave
    )

    dados_encriptados = f.encrypt(
        dados_atuais.encode("utf-8")
    )

    try:

        with open(
            FICHEIRO_DADOS,
            "wb"
        ) as ficheiro:

            ficheiro.write(
                novo_salt
            )

            ficheiro.write(
                dados_encriptados
            )

        return nova_chave

    except Exception:

        return False
