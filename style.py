import customtkinter as ctk


# ============================================================
# DIMENSÕES
# ============================================================

LARGURA_JANELA = 600
ALTURA_JANELA = 680


# ============================================================
# PALETA DE CORES
# ============================================================

COR_FUNDO = "#F3F4F6"
COR_CARD = "#FFFFFF"

COR_TEXTO = "#1F2937"
COR_TEXTO_MUTED = "#6B7280"

COR_SUCESSO = "#10B981"
COR_SUCESSO_HOVER = "#059669"

COR_ACAO = "#3B82F6"
COR_ACAO_HOVER = "#2563EB"

COR_ERRO = "#EF4444"
COR_ERRO_HOVER = "#DC2626"

COR_BORDA = "#E5E7EB"

COR_BRANCO = "#FFFFFF"

COR_SECUNDARIA = "#6B7280"
COR_SECUNDARIA_HOVER = "#4B5563"


# ============================================================
# FONTES
# ============================================================

FONTE_TITULO = (
    "Segoe UI",
    18,
    "bold"
)

FONTE_TITULO_GRANDE = (
    "Segoe UI",
    30,
    "bold"
)

FONTE_SUBTITULO = (
    "Segoe UI",
    13
)

FONTE_TEXTO = (
    "Segoe UI",
    10
)

FONTE_TEXTO_BOLD = (
    "Segoe UI",
    10,
    "bold"
)

FONTE_MONOSPACED = (
    "Consolas",
    10
)


# ============================================================
# CONFIGURAÇÃO GLOBAL DO CUSTOMTKINTER
# ============================================================

def aplicar_estilos_globais():

    # Aparência
    ctk.set_appearance_mode(
        "System"
    )

    # Tema base
    ctk.set_default_color_theme(
        "blue"
    )


# ============================================================
# ESTILO DOS BOTÕES
# ============================================================

def estilo_botao_acao():

    return {
        "fg_color": COR_ACAO,
        "hover_color": COR_ACAO_HOVER,
        "text_color": COR_BRANCO,
        "font": FONTE_TEXTO_BOLD,
        "corner_radius": 7
    }


def estilo_botao_sucesso():

    return {
        "fg_color": COR_SUCESSO,
        "hover_color": COR_SUCESSO_HOVER,
        "text_color": COR_BRANCO,
        "font": FONTE_TEXTO_BOLD,
        "corner_radius": 7
    }


def estilo_botao_erro():

    return {
        "fg_color": COR_ERRO,
        "hover_color": COR_ERRO_HOVER,
        "text_color": COR_BRANCO,
        "font": FONTE_TEXTO_BOLD,
        "corner_radius": 7
    }


def estilo_botao_secundario():

    return {
        "fg_color": COR_SECUNDARIA,
        "hover_color": COR_SECUNDARIA_HOVER,
        "text_color": COR_BRANCO,
        "font": FONTE_TEXTO_BOLD,
        "corner_radius": 7
    }


# ============================================================
# ESTILO DOS CARDS
# ============================================================

def estilo_card():

    return {
        "fg_color": COR_CARD,
        "border_color": COR_BORDA,
        "border_width": 1,
        "corner_radius": 10
    }


# ============================================================
# ESTILO DOS CAMPOS
# ============================================================

def estilo_entry():

    return {
        "fg_color": COR_BRANCO,
        "border_color": COR_BORDA,
        "text_color": COR_TEXTO,
        "placeholder_text_color": COR_TEXTO_MUTED,
        "corner_radius": 7
    }
