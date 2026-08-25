import os
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk

import seguranca
import style

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")



# ============================================================
# CONFIGURAÇÃO DA INTERFACE
# ============================================================

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class AplicacaoGestor:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "GerePass - Painel Seguro"
        )

        self.root.geometry(
            "600x680"
        )

        self.root.resizable(
            False,
            False
        )

        # Chave atualmente utilizada
        self.chave = None

        # Serviços cujas passwords estão visíveis
        self.passwords_visiveis = set()

        self.criar_ecra_login()

    # ========================================================
    # LOGIN
    # ========================================================

    def criar_ecra_login(self):

        self.limpar_ecra()

        titulo = ctk.CTkLabel(
            self.root,
            text="GerePass",
            font=(
                "Segoe UI",
                30,
                "bold"
            ),
            text_color="#3B82F6"
        )

        titulo.pack(
            pady=(50, 5)
        )

        subtitulo = ctk.CTkLabel(
            self.root,
            text="Gestor de Palavras-passe Portátil",
            font=(
                "Segoe UI",
                13
            ),
            text_color="gray"
        )

        subtitulo.pack(
            pady=(0, 30)
        )

        # ----------------------------------------------------
        # CARD LOGIN
        # ----------------------------------------------------

        card = ctk.CTkFrame(
            self.root,
            width=450,
            height=260,
            corner_radius=15
        )

        card.pack(
            padx=30,
            pady=10
        )

        card.pack_propagate(
            False
        )

        info = ctk.CTkLabel(
            card,
            text="Introduza a sua Password Mestra",
            font=(
                "Segoe UI",
                13
            )
        )

        info.pack(
            pady=(30, 10)
        )

        self.ent_master = ctk.CTkEntry(
            card,
            show="*",
            placeholder_text="Password Mestra",
            width=320,
            height=42,
            corner_radius=8
        )

        self.ent_master.pack(
            pady=10
        )

        self.ent_master.focus()

        botao_login = ctk.CTkButton(
            card,
            text="🔓 Desbloquear Painel",
            font=(
                "Segoe UI",
                12,
                "bold"
            ),
            width=320,
            height=42,
            corner_radius=8,
            fg_color="#10B981",
            hover_color="#059669",
            command=self.autenticar
        )

        botao_login.pack(
            pady=15
        )

        # Enter para desbloquear
        self.ent_master.bind(
            "<Return>",
            lambda event: self.autenticar()
        )

    # ========================================================
    # AUTENTICAÇÃO
    # ========================================================

    def autenticar(self):

        master = self.ent_master.get()

        if not master:

            messagebox.showwarning(
                "Aviso",
                "A Password Mestra não pode estar vazia."
            )

            return

        # ----------------------------------------------------
        # PRIMEIRA EXECUÇÃO
        # ----------------------------------------------------

        if not os.path.exists(
            seguranca.FICHEIRO_DADOS
        ):

            sucesso = (
                seguranca.inicializar_ficheiro(
                    master
                )
            )

            if not sucesso:

                messagebox.showerror(
                    "Erro",
                    "Não foi possível criar o cofre."
                )

                return

        # ----------------------------------------------------
        # TENTAR OBTER A CHAVE
        # ----------------------------------------------------

        self.chave = seguranca.autenticar(
            master
        )

        if self.chave is False:

            messagebox.showerror(
                "Acesso Negado",
                "Password Mestra incorreta!"
            )

            self.chave = None

            return

        # ----------------------------------------------------
        # CONFIRMAR QUE A CHAVE CONSEGUE DESENCRIPTAR
        # ----------------------------------------------------

        dados = seguranca.ler_dados(
            self.chave
        )

        if dados is False:

            messagebox.showerror(
                "Erro",
                "Não foi possível desencriptar o cofre."
            )

            self.chave = None

            return

        # Login efetuado
        self.criar_painel_principal()

    # ========================================================
    # PAINEL PRINCIPAL
    # ========================================================

    def criar_painel_principal(self):

        self.limpar_ecra()

        self.passwords_visiveis.clear()

        # ----------------------------------------------------
        # TABVIEW
        # ----------------------------------------------------

        self.tabview = ctk.CTkTabview(
            self.root,
            width=570,
            height=630,
            corner_radius=12
        )

        self.tabview.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

        aba_guardar = self.tabview.add(
            "Guardar"
        )

        aba_ver = self.tabview.add(
            "Ver Guardadas"
        )

        aba_definicoes = self.tabview.add(
            "Definições"
        )

        self.criar_aba_guardar(
            aba_guardar
        )

        self.criar_aba_ver(
            aba_ver
        )

        self.criar_aba_definicoes(
            aba_definicoes
        )

    # ========================================================
    # ABA GUARDAR
    # ========================================================

    def criar_aba_guardar(
        self,
        aba
    ):

        titulo = ctk.CTkLabel(
            aba,
            text="Proteger Nova Credencial",
            font=(
                "Segoe UI",
                18,
                "bold"
            )
        )

        titulo.pack(
            pady=(30, 25)
        )

        # ----------------------------------------------------
        # SERVIÇO
        # ----------------------------------------------------

        self.ent_servico = ctk.CTkEntry(
            aba,
            placeholder_text="🌐 Serviço ou Site",
            width=370,
            height=42,
            corner_radius=7
        )

        self.ent_servico.pack(
            pady=8
        )

        # ----------------------------------------------------
        # UTILIZADOR
        # ----------------------------------------------------

        self.ent_user = ctk.CTkEntry(
            aba,
            placeholder_text="👤 Utilizador ou E-mail",
            width=370,
            height=42,
            corner_radius=7
        )

        self.ent_user.pack(
            pady=8
        )

        # ----------------------------------------------------
        # PASSWORD
        # ----------------------------------------------------

        self.ent_pass = ctk.CTkEntry(
            aba,
            placeholder_text="🔑 Palavra-passe",
            width=370,
            height=42,
            corner_radius=7,
            show="*"
        )

        self.ent_pass.pack(
            pady=8
        )

        # ----------------------------------------------------
        # BOTÃO
        # ----------------------------------------------------

        botao = ctk.CTkButton(
            aba,
            text="🔐 Gravar em Segurança",
            width=370,
            height=45,
            corner_radius=7,
            font=(
                "Segoe UI",
                12,
                "bold"
            ),
            fg_color="#3B82F6",
            hover_color="#2563EB",
            command=self.gravar_senha
        )

        botao.pack(
            pady=(30, 10)
        )

        # Enter para gravar
        self.ent_pass.bind(
            "<Return>",
            lambda event: self.gravar_senha()
        )

    # ========================================================
    # GRAVAR PASSWORD
    # ========================================================

    def gravar_senha(self):

        servico = (
            self.ent_servico
            .get()
            .strip()
        )

        utilizador = (
            self.ent_user
            .get()
            .strip()
        )

        password = (
            self.ent_pass
            .get()
            .strip()
        )

        # ----------------------------------------------------
        # VALIDAÇÃO
        # ----------------------------------------------------

        if (
            not servico
            or not utilizador
            or not password
        ):

            messagebox.showwarning(
                "Aviso",
                "Preencha todos os campos."
            )

            return

        # ----------------------------------------------------
        # GUARDAR
        # ----------------------------------------------------

        sucesso = (
            seguranca.adicionar_credencial(
                self.chave,
                servico,
                utilizador,
                password
            )
        )

        if not sucesso:

            messagebox.showerror(
                "Erro",
                "Não foi possível guardar a credencial."
            )

            return

        messagebox.showinfo(
            "Sucesso",
            f"'{servico}' foi guardado com sucesso."
        )

        # Limpar campos
        self.ent_servico.delete(
            0,
            tk.END
        )

        self.ent_user.delete(
            0,
            tk.END
        )

        self.ent_pass.delete(
            0,
            tk.END
        )

        # Atualizar lista
        if hasattr(
            self,
            "lista_frame"
        ):

            self.atualizar_lista()

    # ========================================================
    # ABA VER GUARDADAS
    # ========================================================

    def criar_aba_ver(
        self,
        aba
    ):

        titulo = ctk.CTkLabel(
            aba,
            text="As Minhas Credenciais",
            font=(
                "Segoe UI",
                18,
                "bold"
            )
        )

        titulo.pack(
            pady=(10, 5)
        )

        # ----------------------------------------------------
        # PESQUISA
        # ----------------------------------------------------

        self.ent_pesquisa = ctk.CTkEntry(
            aba,
            placeholder_text="🔎 Pesquisar por site ou utilizador...",
            width=480,
            height=40,
            corner_radius=7
        )

        self.ent_pesquisa.pack(
            pady=(5, 10)
        )

        # Pesquisa enquanto escreve
        self.ent_pesquisa.bind(
            "<KeyRelease>",
            lambda event: self.pesquisar()
        )

        # ----------------------------------------------------
        # FILTROS
        # ----------------------------------------------------

        filtro_frame = ctk.CTkFrame(
            aba,
            fg_color="transparent"
        )

        filtro_frame.pack(
            pady=(0, 8)
        )

        ctk.CTkLabel(
            filtro_frame,
            text="Pesquisar em:",
            font=(
                "Segoe UI",
                11
            )
        ).pack(
            side="left",
            padx=5
        )

        self.filtro = tk.StringVar(
            value="Tudo"
        )

        ctk.CTkRadioButton(
            filtro_frame,
            text="Tudo",
            variable=self.filtro,
            value="Tudo",
            command=self.pesquisar
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkRadioButton(
            filtro_frame,
            text="Site",
            variable=self.filtro,
            value="Site",
            command=self.pesquisar
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkRadioButton(
            filtro_frame,
            text="Utilizador",
            variable=self.filtro,
            value="Utilizador",
            command=self.pesquisar
        ).pack(
            side="left",
            padx=5
        )

        # ----------------------------------------------------
        # LISTA SCROLLABLE
        # ----------------------------------------------------

        self.lista_frame = ctk.CTkScrollableFrame(
            aba,
            width=510,
            height=380,
            corner_radius=8
        )

        self.lista_frame.pack(
            padx=5,
            pady=5,
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # BOTÕES
        # ----------------------------------------------------

        botoes = ctk.CTkFrame(
            aba,
            fg_color="transparent"
        )

        botoes.pack(
            pady=8
        )

        ctk.CTkButton(
            botoes,
            text="↻ Atualizar",
            width=130,
            height=35,
            command=self.atualizar_lista
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            botoes,
            text="✕ Limpar Pesquisa",
            width=150,
            height=35,
            fg_color="#6B7280",
            hover_color="#4B5563",
            command=self.limpar_pesquisa
        ).pack(
            side="left",
            padx=5
        )

        # Mostrar inicialmente
        self.atualizar_lista()

    # ========================================================
    # CRIAR CARTÃO DE CREDENCIAL
    # ========================================================

    def criar_cartao(
        self,
        servico,
        utilizador,
        password
    ):

        cartao = ctk.CTkFrame(
            self.lista_frame,
            corner_radius=10,
            border_width=1
        )

        cartao.pack(
            fill="x",
            padx=5,
            pady=6
        )

        # ----------------------------------------------------
        # SITE
        # ----------------------------------------------------

        ctk.CTkLabel(
            cartao,
            text=f"🌐 {servico}",
            font=(
                "Segoe UI",
                14,
                "bold"
            ),
            anchor="w"
        ).pack(
            fill="x",
            padx=15,
            pady=(10, 3)
        )

        # ----------------------------------------------------
        # UTILIZADOR
        # ----------------------------------------------------

        ctk.CTkLabel(
            cartao,
            text=f"👤 {utilizador}",
            font=(
                "Segoe UI",
                11
            ),
            anchor="w"
        ).pack(
            fill="x",
            padx=15,
            pady=2
        )

        # ----------------------------------------------------
        # PASSWORD + BOTÕES
        # ----------------------------------------------------

        password_frame = ctk.CTkFrame(
            cartao,
            fg_color="transparent"
        )

        password_frame.pack(
            fill="x",
            padx=10,
            pady=(5, 10)
        )

        password_visivel = (
            servico in self.passwords_visiveis
        )

        if password_visivel:

            texto_password = password

        else:

            texto_password = "••••••••••••"

        label_password = ctk.CTkLabel(
            password_frame,
            text=f"🔑 {texto_password}",
            font=(
                "Consolas",
                11
            ),
            anchor="w"
        )

        label_password.pack(
            side="left",
            padx=5
        )

        # ----------------------------------------------------
        # MOSTRAR / OCULTAR
        # ----------------------------------------------------

        def alternar_password():

            if servico in self.passwords_visiveis:

                self.passwords_visiveis.remove(
                    servico
                )

            else:

                self.passwords_visiveis.add(
                    servico
                )

            self.pesquisar()

        ctk.CTkButton(
            password_frame,
            text="👁",
            width=38,
            height=30,
            command=alternar_password
        ).pack(
            side="right",
            padx=3
        )

        # ----------------------------------------------------
        # COPIAR
        # ----------------------------------------------------

        def copiar_password():

            self.root.clipboard_clear()

            self.root.clipboard_append(
                password
            )

            self.root.update()

            messagebox.showinfo(
                "Copiado",
                "Password copiada para a área de transferência."
            )

        ctk.CTkButton(
            password_frame,
            text="📋",
            width=38,
            height=30,
            fg_color="#10B981",
            hover_color="#059669",
            command=copiar_password
        ).pack(
            side="right",
            padx=3
        )

        # ----------------------------------------------------
        # APAGAR
        # ----------------------------------------------------

        def apagar():

            confirmar = messagebox.askyesno(
                "Confirmar eliminação",
                f"Tem a certeza que pretende apagar '{servico}'?"
            )

            if not confirmar:
                return

            resultado = (
                seguranca.eliminar_credencial(
                    self.chave,
                    servico
                )
            )

            if resultado is True:

                self.passwords_visiveis.discard(
                    servico
                )

                self.pesquisar()

                messagebox.showinfo(
                    "Sucesso",
                    f"'{servico}' foi eliminado."
                )

            elif resultado == "nao_encontrado":

                messagebox.showwarning(
                    "Aviso",
                    "A credencial já não existe."
                )

            else:

                messagebox.showerror(
                    "Erro",
                    "Não foi possível eliminar a credencial."
                )

        ctk.CTkButton(
            password_frame,
            text="🗑",
            width=38,
            height=30,
            fg_color="#EF4444",
            hover_color="#DC2626",
            command=apagar
        ).pack(
            side="right",
            padx=3
        )

    # ========================================================
    # PESQUISA
    # ========================================================

    def pesquisar(self):

        # ----------------------------------------------------
        # LER PESQUISA
        # ----------------------------------------------------

        pesquisa = (
            self.ent_pesquisa
            .get()
            .strip()
            .lower()
        )

        # ----------------------------------------------------
        # LER COFRE
        # ----------------------------------------------------

        dados = seguranca.ler_dados(
            self.chave
        )

        if dados is False:

            self.mostrar_mensagem_lista(
                "❌ Erro ao desencriptar o cofre."
            )

            return

        # ----------------------------------------------------
        # LIMPAR LISTA
        # ----------------------------------------------------

        for widget in (
            self.lista_frame.winfo_children()
        ):

            widget.destroy()

        # ----------------------------------------------------
        # COFRE VAZIO
        # ----------------------------------------------------

        if not dados.strip():

            self.mostrar_mensagem_lista(
                "🔐 Nenhuma credencial guardada."
            )

            return

        encontrou = False

        filtro = self.filtro.get()

        # ----------------------------------------------------
        # PERCORRER CREDENCIAIS
        # ----------------------------------------------------

        for linha in dados.strip().split("\n"):

            if "|" not in linha:
                continue

            try:

                servico, utilizador, password = (
                    linha.split("|", 2)
                )

            except ValueError:

                continue

            servico_lower = servico.lower()

            utilizador_lower = utilizador.lower()

            # ------------------------------------------------
            # FILTRO
            # ------------------------------------------------

            if filtro == "Site":

                corresponde = (
                    pesquisa in servico_lower
                )

            elif filtro == "Utilizador":

                corresponde = (
                    pesquisa in utilizador_lower
                )

            else:

                corresponde = (
                    pesquisa in servico_lower
                    or
                    pesquisa in utilizador_lower
                )

            if not corresponde:
                continue

            encontrou = True

            self.criar_cartao(
                servico,
                utilizador,
                password
            )

        # ----------------------------------------------------
        # SEM RESULTADOS
        # ----------------------------------------------------

        if not encontrou:

            if pesquisa:

                texto = (
                    f"🔍 Nenhum resultado para '{pesquisa}'."
                )

            else:

                texto = (
                    "🔐 Nenhuma credencial guardada."
                )

            self.mostrar_mensagem_lista(
                texto
            )

    # ========================================================
    # MENSAGEM NA LISTA
    # ========================================================

    def mostrar_mensagem_lista(
        self,
        texto
    ):

        for widget in (
            self.lista_frame.winfo_children()
        ):

            widget.destroy()

        mensagem = ctk.CTkLabel(
            self.lista_frame,
            text=texto,
            font=(
                "Segoe UI",
                12
            ),
            text_color="gray"
        )

        mensagem.pack(
            pady=50
        )

    # ========================================================
    # ATUALIZAR LISTA
    # ========================================================

    def atualizar_lista(self):

        if hasattr(
            self,
            "ent_pesquisa"
        ):

            self.ent_pesquisa.delete(
                0,
                tk.END
            )

        if hasattr(
            self,
            "filtro"
        ):

            self.filtro.set(
                "Tudo"
            )

        self.pesquisar()

    # ========================================================
    # LIMPAR PESQUISA
    # ========================================================

    def limpar_pesquisa(self):

        self.ent_pesquisa.delete(
            0,
            tk.END
        )

        self.filtro.set(
            "Tudo"
        )

        self.pesquisar()

    # ========================================================
    # ABA DEFINIÇÕES
    # ========================================================

    def criar_aba_definicoes(
        self,
        aba
    ):

        ctk.CTkLabel(
            aba,
            text="Segurança do Sistema",
            font=(
                "Segoe UI",
                18,
                "bold"
            )
        ).pack(
            pady=(35, 20)
        )

        ctk.CTkLabel(
            aba,
            text="Alterar Password Mestra",
            font=(
                "Segoe UI",
                12
            ),
            text_color="gray"
        ).pack(
            pady=5
        )

        self.ent_nova_master = ctk.CTkEntry(
            aba,
            show="*",
            placeholder_text="Nova Password Mestra",
            width=370,
            height=42,
            corner_radius=7
        )

        self.ent_nova_master.pack(
            pady=10
        )

        ctk.CTkButton(
            aba,
            text="🔐 Alterar Password Mestra",
            width=370,
            height=45,
            corner_radius=7,
            fg_color="#10B981",
            hover_color="#059669",
            font=(
                "Segoe UI",
                12,
                "bold"
            ),
            command=self.processar_mudanca_pass
        ).pack(
            pady=20
        )

        # ----------------------------------------------------
        # INFORMAÇÃO
        # ----------------------------------------------------

        info = ctk.CTkLabel(
            aba,
            text=(
                "Ao alterar a Password Mestra,\n"
                "o cofre será reencriptado e será\n"
                "gerado um novo salt aleatório."
            ),
            font=(
                "Segoe UI",
                11
            ),
            text_color="gray"
        )

        info.pack(
            pady=30
        )

    # ========================================================
    # ALTERAR PASSWORD MESTRA
    # ========================================================

    def processar_mudanca_pass(self):

        nova_pass = (
            self.ent_nova_master
            .get()
            .strip()
        )

        if not nova_pass:

            messagebox.showwarning(
                "Aviso",
                "A nova Password Mestra não pode estar vazia."
            )

            return

        # ----------------------------------------------------
        # CONFIRMAÇÃO
        # ----------------------------------------------------

        confirmar = messagebox.askyesno(
            "Confirmar alteração",
            (
                "Tem a certeza que pretende alterar "
                "a Password Mestra?\n\n"
                "O cofre será reencriptado com uma "
                "nova chave e um novo salt."
            )
        )

        if not confirmar:
            return

        # ----------------------------------------------------
        # ALTERAR
        # ----------------------------------------------------

        nova_chave = (
            seguranca.alterar_password_mestra(
                self.chave,
                nova_pass
            )
        )

        if nova_chave:

            self.chave = nova_chave

            self.ent_nova_master.delete(
                0,
                tk.END
            )

            self.passwords_visiveis.clear()

            messagebox.showinfo(
                "Sucesso",
                (
                    "Password Mestra alterada com sucesso.\n\n"
                    "O cofre foi reencriptado com um "
                    "novo salt aleatório."
                )
            )

            self.atualizar_lista()

        else:

            messagebox.showerror(
                "Erro",
                "Falha ao reencriptar o cofre."
            )

    # ========================================================
    # LIMPAR ECRÃ
    # ========================================================

    def limpar_ecra(self):

        for widget in (
            self.root.winfo_children()
        ):

            widget.destroy()


# ============================================================
# INICIAR PROGRAMA
# ============================================================

if __name__ == "__main__":

    style.aplicar_estilos_globais()

    root = ctk.CTk()

    app = AplicacaoGestor(root)

    root.mainloop()

