import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk  
import seguranca  # Importa a lógica separada

# Configuração da UI Moderna
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

class AplicacaoGestor:
    def __init__(self, root):
        self.root = root
        self.root.title("GerePass - Painel Seguro")
        self.root.geometry("520x520")
        self.root.resizable(False, False)
        self.chave = None
        self.criar_ecra_login()

    def criar_ecra_login(self):
        self.limpar_ecra()
        
        lbl_titulo = ctk.CTkLabel(self.root, text="GerePass", font=("Segoe UI", 28, "bold"), text_color="#3B82F6")
        lbl_titulo.pack(pady=(40, 5))
        
        lbl_sub = ctk.CTkLabel(self.root, text="Gestor de Palavras-passe Portátil", font=("Segoe UI", 13), text_color="gray")
        lbl_sub.pack(pady=(0, 30))
        
        card = ctk.CTkFrame(self.root, width=400, height=220, corner_radius=15)
        card.pack(pady=10, padx=20, fill="both", expand=True)
        card.pack_propagate(False)
        
        lbl_info = ctk.CTkLabel(card, text="Introduza a sua Chave Mestra para cifrar os dados:", font=("Segoe UI", 12))
        lbl_info.pack(pady=(25, 10))
        
        self.ent_master = ctk.CTkEntry(card, show="*", placeholder_text="Palavra-passe Mestra", width=280, height=40, corner_radius=8)
        self.ent_master.pack(pady=10)
        self.ent_master.focus()
        
        btn_login = ctk.CTkButton(card, text="Desbloquear Painel", font=("Segoe UI", 12, "bold"), 
                                  height=40, width=280, corner_radius=8, fg_color="#10B981", hover_color="#059669",
                                  command=self.autenticar)
        btn_login.pack(pady=(15, 20))

    def autenticar(self):
        master = self.ent_master.get()
        if not master:
            messagebox.showwarning("Aviso", "A password mestra não pode estar vazia!")
            return
        self.chave = seguranca.gerar_chave(master)
        seguranca.inicializar_ficheiro(self.chave)
        if seguranca.ler_dados(self.chave) is False:
            messagebox.showerror("Erro", "Password Mestra incorreta! Acesso negado.")
            self.chave = None
        else:
            self.criar_painel_principal()

    def criar_painel_principal(self):
        self.limpar_ecra()
        
        tabview = ctk.CTkTabview(self.root, width=480, height=460, corner_radius=12)
        tabview.pack(pady=10, padx=10, fill="both", expand=True)
        
        aba1 = tabview.add("Guardar Password")
        aba2 = tabview.add("Ver Guardadas")
        aba3 = tabview.add("Definições")
        
        # --- Aba 1: Guardar ---
        ctk.CTkLabel(aba1, text="Proteger Nova Credencial", font=("Segoe UI", 16, "bold")).pack(pady=(15, 20))
        self.ent_servico = ctk.CTkEntry(aba1, placeholder_text="Serviço ou Site (ex: GitHub)", width=320, height=35, corner_radius=6)
        self.ent_servico.pack(pady=8)
        self.ent_user = ctk.CTkEntry(aba1, placeholder_text="Utilizador ou E-mail", width=320, height=35, corner_radius=6)
        self.ent_user.pack(pady=8)
        self.ent_pass = ctk.CTkEntry(aba1, placeholder_text="Palavra-passe do Serviço", width=320, height=35, corner_radius=6)
        self.ent_pass.pack(pady=8)
        btn_gravar = ctk.CTkButton(aba1, text="Gravar em Segurança", font=("Segoe UI", 12, "bold"), width=320, height=40, corner_radius=6, fg_color="#3B82F6", hover_color="#2563EB", command=self.gravar_senha)
        btn_gravar.pack(pady=(25, 10))
        
        # --- Aba 2: Visualizar e Eliminar ---
        ctk.CTkLabel(aba2, text="Credenciais Encriptadas em Disco", font=("Segoe UI", 16, "bold")).pack(pady=(10, 5))
        self.txt_lista = ctk.CTkTextbox(aba2, width=440, height=180, font=("Consolas", 11), corner_radius=8, border_width=1)
        self.txt_lista.pack(pady=5)
        
        frame_apagar = ctk.CTkFrame(aba2, fg_color="transparent")
        frame_apagar.pack(pady=10, fill="x", padx=10)
        
        self.ent_apagar_servico = ctk.CTkEntry(frame_apagar, placeholder_text="Nome do Serviço a APAGAR", width=240, height=35, corner_radius=6)
        self.ent_apagar_servico.pack(side="left", padx=(0, 10))
        
        btn_apagar = ctk.CTkButton(frame_apagar, text="Apagar", font=("Segoe UI", 11, "bold"), width=100, height=35, corner_radius=6, fg_color="#EF4444", hover_color="#DC2626", command=self.processar_eliminacao)
        btn_apagar.pack(side="left")
        
        btn_atualizar = ctk.CTkButton(aba2, text="Atualizar Lista", font=("Segoe UI", 11, "bold"), width=150, height=35, corner_radius=6, fg_color="gray", hover_color="#4B5563", command=self.atualizar_lista_ecra)
        btn_atualizar.pack(pady=(5, 0))
        self.atualizar_lista_ecra()

        # --- Aba 3: Definições ---
        ctk.CTkLabel(aba3, text="Segurança do Sistema", font=("Segoe UI", 16, "bold")).pack(pady=(15, 20))
        ctk.CTkLabel(aba3, text="Mudar a Password Mestra do Cofre:", font=("Segoe UI", 12), text_color="gray").pack(pady=5)
        self.ent_nova_master = ctk.CTkEntry(aba3, show="*", placeholder_text="Nova Password Mestra", width=320, height=35, corner_radius=6)
        self.ent_nova_master.pack(pady=10)
        btn_mudar = ctk.CTkButton(aba3, text="Confirmar Nova Chave", font=("Segoe UI", 12, "bold"), width=320, height=40, corner_radius=6, fg_color="#10B981", hover_color="#059669", command=self.processar_mudanca_pass)
        btn_mudar.pack(pady=20)

    def gravar_senha(self):
        servico = self.ent_servico.get().strip()
        user = self.ent_user.get().strip()
        senha = self.ent_pass.get().strip()
        if not servico or not user or not senha:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        dados_atuais = seguranca.ler_dados(self.chave)
        nova_linha = f"{servico}|{user}|{senha}\n"
        seguranca.gravar_dados(self.chave, dados_atuais + nova_linha)
        messagebox.showinfo("Sucesso", f"Dados para '{servico}' guardados com sucesso!")
        self.ent_servico.delete(0, tk.END)
        self.ent_user.delete(0, tk.END)
        self.ent_pass.delete(0, tk.END)
        self.atualizar_lista_ecra()

    def atualizar_lista_ecra(self):
        self.txt_lista.delete("1.0", tk.END)
        dados = seguranca.ler_dados(self.chave)
        if not dados or not dados.strip():
            self.txt_lista.insert(tk.END, "Nenhuma palavra-passe guardada no cofre encriptado.")
            return
        linhas = dados.strip().split("\n")
        for linha in linhas:
            if "|" in linha:
                srv, usr, psw = linha.split("|")
                self.txt_lista.insert(tk.END, f"📌 [SITE]: {srv}\n👤 [USER]: {usr}\n🔑 [PASS]: {psw}\n" + "—"*35 + "\n")

    def processar_eliminacao(self):
        target = self.ent_apagar_servico.get().strip()
        if not target:
            messagebox.showwarning("Aviso", "Digite o nome do serviço que pretende apagar!")
            return
        
        resultado = seguranca.eliminar_credencial(self.chave, target)
        if resultado is True:
            messagebox.showinfo("Sucesso", f"O serviço '{target}' foi completamente eliminado sem deixar metadados.")
            self.ent_apagar_servico.delete(0, tk.END)
            self.atualizar_lista_ecra()
        elif resultado == "nao_encontrado":
            messagebox.showwarning("Aviso", f"Não foi encontrado nenhum serviço com o nome '{target}'.")
        else:
            messagebox.showerror("Erro", "Falha de segurança ao aceder ao ficheiro.")

    def processar_mudanca_pass(self):
        nova_pass = self.ent_nova_master.get().strip()
        if not nova_pass:
            messagebox.showwarning("Aviso", "A nova password não pode estar vazia!")
            return
        nova_chave = seguranca.alterar_password_mestra(self.chave, nova_pass)
        if nova_chave:
            self.chave = nova_chave
            messagebox.showinfo("Sucesso", "Chave Mestra alterada!\nO ficheiro foi reencriptado com sucesso.")
            self.ent_nova_master.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Falha ao reencriptar os dados.")

    def limpar_ecra(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = AplicacaoGestor(root)
    root.mainloop()
