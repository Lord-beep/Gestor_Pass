LARGURA_JANELA = 480
ALTURA_JANELA = 460

# Paleta de Cores Moderna (Estilo Clean/Tech)
COR_FUNDO = "#F3F4F6"         
COR_CARD = "#FFFFFF"          
COR_TEXTO = "#1F2937"         
COR_TEXTO_MUTED = "#6B7280"   
COR_SUCESSO = "#10B981"       
COR_ACAO = "#3B82F6"          
COR_BORDA = "#E5E7EB"         
COR_BRANCO = "#FFFFFF"       

FONTE_TITULO = ("Segoe UI", 15, "bold")
FONTE_TEXTO = ("Segoe UI", 10)
FONTE_TEXTO_BOLD = ("Segoe UI", 10, "bold")
FONTE_MONOSPACED = ("Consolas", 10)

def aplicar_estilos_globais():
    from tkinter import ttk
    estilo = ttk.Style()
    estilo.theme_use("clam") 
    
    estilo.configure("TNotebook", background=COR_FUNDO, borderwidth=0)
    estilo.configure("TNotebook.Tab", 
                     background=COR_FUNDO, 
                     foreground=COR_TEXTO_MUTED, 
                     font=("Segoe UI", 15, "bold"), 
                     padding=6,
                     borderwidth=0)
    
    estilo.map("TNotebook.Tab", 
               background=[("selected", COR_CARD)], 
               foreground=[("selected", COR_ACAO)])
