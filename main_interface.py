import customtkinter as ctk
from tkinter import messagebox
from time import sleep
from funcoes_SQL import *
from validacoes import *
import validacoes as val_direto

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


app = ctk.CTk()
app.geometry("1920x1080")
app.title("Sistema Escolar")


frame_principal = ctk.CTkFrame(app)
frame_principal.pack(fill="both", expand=True)
frame_principal.grid_columnconfigure((0,1,2), weight=1)


def mudar_tema():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


def limpar_frame():
    for widget in frame_principal.winfo_children(): widget.destroy()



def tela_login():
    limpar_frame()
    criar_admin_iniciar()
    ctk.CTkLabel(frame_principal,text="LOGIN",font=("Arial",55,"bold")).pack(pady=40)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1840,y=20)

    entrar_usuario=ctk.CTkEntry(frame_principal,placeholder_text="Usuário",height=30,width=500); entrar_usuario.pack(pady=30)
    
    frame_senha = ctk.CTkFrame(frame_principal)
    frame_senha.pack(pady=30)

    entrar_senha = ctk.CTkEntry(frame_senha, placeholder_text="Senha", show="*", height=30, width=450)
    entrar_senha.pack(side="left", padx=5)

    
    def exibir_senha():
        nonlocal botao_mostrar
        if entrar_senha.cget("show") == "*":
            entrar_senha.configure(show="")
            botao_mostrar.configure(text="Ocultar")
        else:
            entrar_senha.configure(show="*")
            botao_mostrar.configure(text="👁")

    
    botao_mostrar = ctk.CTkButton(frame_senha, text="👁", width=50, command=exibir_senha)
    botao_mostrar.pack(side="left")
    
    entrar_usuario.bind("<Return>", lambda event: entrar_senha.focus())
    entrar_senha.bind("<Return>", lambda event: fazer_login())
        
    
    def fazer_login():
        usuario = validar_usuario(entrar_usuario.get(),entrar_senha.get())
        if not usuario[0]: 
            limpar_frame()
            tela_login()
            ctk.CTkLabel(frame_principal,text="Erro, Usuário ou senha incorretos!",width=250,font=("Arial",35,"bold")).pack(pady=40)
        
        else:
            if usuario[1] == "admin":
                limpar_frame()
                tela_login()
                ctk.CTkLabel(frame_principal,text="Login realizado com sucesso",width=250,font=("Arial",35,"bold")).pack(pady=40); app.after(1000, menu_principal_admin)
            elif usuario[1] == "professor":
                global id_login
                id_login = ler_usuarios_professor(entrar_usuario.get())
                limpar_frame()
                tela_login()
                ctk.CTkLabel(frame_principal,text="Login realizado com sucesso",width=250,font=("Arial",35,"bold")).pack(pady=40); app.after(1000, menu_principal_professor)

    btn_login = ctk.CTkButton(frame_principal,text="Entrar",width=450,command=fazer_login).pack(pady=20)


def menu_principal_admin():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text=" Sistema Escolar",font=("Arial",35,"bold")).place(x=810,y=40)

    ctk.CTkButton(frame_principal,text="Cadastrar Matéria",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_cadastrar_materia).place(x=280,y=180)
    ctk.CTkButton(frame_principal,text="Cadastrar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_cadastrar_aluno).place(x=810,y=180)
    ctk.CTkButton(frame_principal,text="Cadastrar Professor",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_cadastrar_professor).place(x=1340,y=180)

    ctk.CTkButton(frame_principal,text="Cadastrar Turma",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_cadastrar_turmas).place(x=280,y=270)
    ctk.CTkButton(frame_principal,text="Listar Alunos",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_listar_alunos).place(x=810,y=270)
    ctk.CTkButton(frame_principal,text="Listar Professores",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_listar_professores).place(x=1340,y=270)

    ctk.CTkButton(frame_principal,text="Listar Turmas",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_listar_turmas).place(x=280,y=360)
    ctk.CTkButton(frame_principal,text="Atualizar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_atualizar_aluno).place(x=810,y=360)
    ctk.CTkButton(frame_principal,text="Listar Materias",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_listar_materias).place(x=1340,y=360)

    ctk.CTkButton(frame_principal,text="Desativar/Ativar Matéria",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_desativar_materia).place(x=280,y=450)
    ctk.CTkButton(frame_principal,text="Desativar/Ativar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_desativar_aluno).place(x=810,y=450)
    ctk.CTkButton(frame_principal,text="Atualizar Professor",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_atualizar_professor).place(x=1340,y=450)

    ctk.CTkButton(frame_principal,text="Desativar/Ativar Turma",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_desativar_turma).place(x=280,y=540)
    ctk.CTkButton(frame_principal,text="Buscar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_buscar_aluno).place(x=810,y=540)
    ctk.CTkButton(frame_principal,text="Desativar/Ativar Professor",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_desativar_professor).place(x=1340,y=540)
    
    
    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_login).place(x=20,y=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)


# tela do admin

def tela_cadastrar_materia():
    def executar_cadastro(nome):
        nome = nome.strip()
        if nome == "":
            ctk.CTkLabel(frame_principal, text="DIGITE A MATÉRIA", font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)
            return
        
        executar = 1
        materias = ler_materias()
        for materia in materias:
            if materia == nome:
                executar = 0
                ctk.CTkLabel(frame_principal, text="MATÉRIA JÁ EXISTENTE", font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)
        
        valida_limite = validar_limite_materias()
        if not valida_limite:
            executar = 0
            ctk.CTkLabel(frame_principal, text="LIMITE DE MATÉRIAS ATINGIDO", font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)

        if executar == 1:

            cadastro=cadastrar_materia(nome)
            if not cadastro:
                ctk.CTkLabel(frame_principal, text="MATÉRIA CADASTRADA", font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)
            else:
                ctk.CTkLabel(frame_principal, text=cadastro, font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)
        
        app.after(1500, menu_principal_admin)

    
    def tela_cadastro_materia():
        limpar_frame()
        ctk.CTkLabel(frame_principal, text="CADASTRAR MATÉRIA", font=("Arial",45,"bold")).grid(row=0, column=1, pady=30)
        entrar_materia = ctk.CTkEntry(frame_principal,placeholder_text="Nome da matéria",width=300, height=30); entrar_materia.grid(row=1, column=1, pady=10)
        ctk.CTkButton(frame_principal,text="Cadastrar",width=250, height=50,command=lambda: executar_cadastro(entrar_materia.get())).grid(row=2, column=1, pady=10)
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


        entrar_materia.bind("<Return>", lambda event: executar_cadastro(entrar_materia.get()))
    
    tela_cadastro_materia()
        

def tela_cadastrar_aluno():
    def mudar_id(id):
        global turma_aplicada
        turma_aplicada = id

    def cadastra_aluno(nome, idade, email, nome_resp, email_resp):
        if nome.get() and idade.get() and email.get() and nome_resp.get() and email_resp.get():
            valida_nome = validar_nome(nome.get())
            valida_idade = validar_idade(idade.get())
            if valida_nome and valida_idade:
                valida_limite_alunos_turma = validar_limite_alunos_turma(turma_aplicada)
                if not valida_limite_alunos_turma:
                    ctk.CTkLabel(frame_principal, text="LIMITE DE ALUNOS DA TURMA ATINGIDO", font=("Arial",30,"bold")).grid(row=8, column=1, pady=30)
                    app.after(1500, menu_principal_admin)
                    return
                else:
                    cadastro = cadastrar_alunos(nome.get(), idade.get(), email.get(), turma_aplicada, nome_resp.get(), email_resp.get())
                    if not cadastro:
                        ctk.CTkLabel(frame_principal, text="ALUNO CADASTRADO", font=("Arial",30,"bold")).grid(row=8, column=1, pady=30)
                        id_aluno = ler_id_aluno(nome.get())
                        materias = ler_materias_turma(turma_aplicada)
                        for materia in materias:
                            vincular_aluno_materias(id_aluno[0], materia[0])
                    else:
                        ctk.CTkLabel(frame_principal, text=cadastro, text_color="red", font=("Arial",30,"bold")).grid(row=8, column=1, pady=30)
                        print(cadastro)
                
                app.after(1500, menu_principal_admin)
            
            else:
                ctk.CTkLabel(frame_principal, text="NOME E/OU IDADE NÃO VÁLIDOS", text_color="red", font=("Arial",30,"bold")).grid(row=8, column=1, pady=30)
                app.after(1500, cadastro_aluno)

        else:
            ctk.CTkLabel(frame_principal, text="HÁ ALGUM CAMPO NÃO PREENCHIDO", text_color="red", font=("Arial",30,"bold")).grid(row=8, column=1, pady=30)
            app.after(1500, cadastro_aluno)


    def cadastro_aluno():
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="CADASTRAR ALUNO",font=("Arial",45,"bold")).grid(row=0, column=1, pady=40)
        entrar_nome=ctk.CTkEntry(frame_principal,placeholder_text="Nome do aluno",width=300, height=30); entrar_nome.grid(row=1, column=1, pady=10)
        entrar_idade=ctk.CTkEntry(frame_principal,placeholder_text="Idade",width=300, height=30); entrar_idade.grid(row=2, column=1, pady=10)
        entrar_email=ctk.CTkEntry(frame_principal,placeholder_text="E-mail do aluno",width=300, height=30); entrar_email.grid(row=3, column=1, pady=10)
        entrar_nome_resp=ctk.CTkEntry(frame_principal,placeholder_text="Nome do responsável",width=300, height=30); entrar_nome_resp.grid(row=4, column=1, pady=10)
        entrar_email_resp=ctk.CTkEntry(frame_principal,placeholder_text="E-mail do responsável",width=300, height=30); entrar_email_resp.grid(row=5, column=1, pady=10)
        ctk.CTkButton(frame_principal,text="Cadastrar",width=250, height=50,command=lambda: cadastra_aluno(entrar_nome, entrar_idade, entrar_email, entrar_nome_resp, entrar_email_resp)).grid(row=7, column=1, pady=10)
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")
       
        entrar_nome.bind("<Return>", lambda event: entrar_idade.focus())       
        entrar_idade.bind("<Return>", lambda event: entrar_email.focus())       
        entrar_email.bind("<Return>", lambda event: entrar_nome_resp.focus())
        entrar_nome_resp.bind("<Return>", lambda event: entrar_email_resp.focus())
        entrar_email_resp.bind("<Return>", lambda event: cadastra_aluno(entrar_nome, entrar_idade, entrar_email, entrar_nome_resp, entrar_email_resp))
    
    
    
    def executar_cadastro(turma):
        mudar_id(turma)
        cadastro_aluno()


    def tela_turmas_cadastro():
        botao_turma = {}
        limpar_frame()
        turmas = ler_turmas_ativas()
        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO ALUNO",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, menu_principal_admin)

        else:
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda t=turma[0]: executar_cadastro(t)).grid(row=turma[0], column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda t=turma[0]: executar_cadastro(t)).grid(row=turma[0] - 5, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda t=turma[0]: executar_cadastro(t)).grid(row=turma[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda t=turma[0]: executar_cadastro(t)).grid(row=turma[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    tela_turmas_cadastro() 


def tela_cadastrar_professor():
    turmas_adicionadas = None
    turmas = []
    def executar_cadastro(nome, idade, email, usuario, senha, materia):
        if turmas:
            cadastro = cadastrar_professores(nome, idade, email, usuario, senha, materia)
            if not cadastro:
                ctk.CTkLabel(frame_principal, text="PROFESSOR CADASTRADO", font=("Arial",30,"bold")).grid(row=8, column=0, columnspan=3, pady=40, sticky="ew")
                id_professor_adicionado = ler_id_professor(nome)
                for turma in turmas:
                    id_turma = ler_id_turma(turma)
                    vincular_professor_turma(id_professor_adicionado[0], id_turma[0])
            else:
                ctk.CTkLabel(frame_principal, text=cadastro.upper(), text_color="red", font=("Arial",30,"bold")).grid(row=8, column=0, columnspan=3, pady=40, sticky="ew")
                print(cadastro)

            app.update()
            app.after(1500, menu_principal_admin)
        else:
            ctk.CTkLabel(frame_principal, text="NÃO FOI SELECIONADA NENHUMA TURMA", font=("Arial",30,"bold")).grid(row=8, column=0, columnspan=3, pady=40, sticky="ew")
            app.update()
            app.after(1500, tela_turmas_cadastro(nome, idade, email, usuario, senha, materia))
              
    
    def validar_cadastro(nome, idade, email, usuario, senha):
        valida_nome = validar_nome(nome)
        valida_idade = validar_idade_professor(idade)

        if valida_nome and valida_idade and email and usuario and senha:
            return True
        else:
            ctk.CTkLabel(frame_principal, text="NOME E/OU IDADE INVÁLIDA", text_color="red", font=("Arial",30,"bold")).grid(row=8, column=1, pady=(40, 20))
            return False

    def adicionar_turmas(turma):
        nonlocal turmas_adicionadas

        adicionar = 1
        for i, j in enumerate(turmas):
            if turma == j:
                adicionar = 0
                turmas.pop(i)
        if adicionar == 1:
            turmas.append(turma)

        if turmas_adicionadas is not None:
            try:
                turmas_adicionadas.destroy()
            except:
                None
        
        turmas_adicionadas = ctk.CTkLabel(frame_principal, text=f"Matérias adicionadas ao professor: {turmas}", font=("Arial",20))
        turmas_adicionadas.grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")

    def tela_escolher_materia(nome, idade, email, usuario, senha):
        botao_materia = {}
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="SELECIONE A MATÉRIA DO PROFESSOR",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=40, sticky="ew")
        materias = ler_materias_ativas()
        if not materias:
            ctk.CTkLabel(frame_principal, text="NÃO HÁ MATÉRIAS CADASTRADAS", fg_color="red", font=("Arial",30,"bold")).grid(row=1, column=1, pady=30)
        for materia in materias:
            if materia[0] < 6:
                botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda m=materia[0]: tela_turmas_cadastro(nome, idade, email, usuario, senha, m)).grid(row=materia[0], column=0, padx=100, pady=50, stick="nw")
            elif materia[0] < 11:
                botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda m=materia[0]: tela_turmas_cadastro(nome, idade, email, usuario, senha, m)).grid(row=materia[0] - 5, column=1, pady=50)
            elif materia[0] < 16:
                botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda m=materia[0]: tela_turmas_cadastro(nome, idade, email, usuario, senha, m)).grid(row=materia[0] - 10, column=2, padx=100, pady=50, stick="ne")
            else:
                botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda m=materia[0]: tela_turmas_cadastro(nome, idade, email, usuario, senha, m)).grid(row=materia[0] - 15, column=3, padx=100, pady=50, stick="ne")
        
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_cadastro).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    def validar_entradas(nome, idade, email, usuario, senha):
        nome_escrvido = nome.get().strip()
        idade_escrvida = idade.get().strip()
        email_escrvido = email.get().strip()
        usuario_escrvido = usuario.get().strip()
        senha_escrvida = senha.get().strip()
        if nome_escrvido and idade_escrvida and email_escrvido and usuario_escrvido and senha_escrvida:
            return True
        else:
            return False
    
    def enviar_dados(nome, idade, email, usuario, senha):
        validacao = validar_entradas(nome, idade, email, usuario, senha)
        if validacao:
            valida = validar_cadastro(nome.get(), idade.get(), email.get(), usuario.get(), senha.get())
            if not valida:
                app.update()
                app.after(1500, tela_cadastro)
            else:
                tela_escolher_materia(nome.get(), idade.get(), email.get(), usuario.get(), senha.get())

        else:
            ctk.CTkLabel(frame_principal, text="HÁ CAMPOS NÃO PREENCHIDOS", text_color="red", width=300, font=("Arial",50,"bold")).grid(row=7, column=1, pady=50)
            app.after(1500, tela_cadastro)


    def tela_cadastro():
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="CADASTRE O PROFESSOR",width=300, font=("Arial",50,"bold")).grid(row=0, column=1, pady=50)
        entrar_nome = ctk.CTkEntry(frame_principal, placeholder_text="Nome do Professor", height=30, width=300); entrar_nome.grid(row=1, column=1, pady=10)
        entrar_idade = ctk.CTkEntry(frame_principal, placeholder_text="Idade do Professor", height=30, width=300); entrar_idade.grid(row=2, column=1, pady=10)
        entrar_email = ctk.CTkEntry(frame_principal, placeholder_text="E-mail do Professor", height=30, width=300); entrar_email.grid(row=3, column=1, pady=10)
        entrar_usuario = ctk.CTkEntry(frame_principal, placeholder_text="Nome de Usuário do Professor", height=30, width=300); entrar_usuario.grid(row=4, column=1, pady=10)
        entrar_senha = ctk.CTkEntry(frame_principal, placeholder_text="Crie uma Senha", height=30, width=300); entrar_senha.grid(row=5, column=1, pady=10)
        ctk.CTkButton(frame_principal, text="CADASTRAR PROFESSOR", width=50, height=30, command=lambda: enviar_dados(entrar_nome, entrar_idade, entrar_email, entrar_usuario, entrar_senha)).grid(row=6, column=1, pady=50)
            
 
        entrar_nome.bind("<Return>", lambda event: entrar_idade.focus())       
        entrar_idade.bind("<Return>", lambda event: entrar_email.focus())       
        entrar_email.bind("<Return>", lambda event: entrar_usuario.focus())
        entrar_usuario.bind("<Return>", lambda event: entrar_senha.focus())
        entrar_senha.bind("<Return>", lambda event: enviar_dados(entrar_nome, entrar_idade, entrar_email, entrar_usuario, entrar_senha))


        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    def tela_turmas_cadastro(nome, idade, email, usuario, senha, materia):
        botao_turma = {}
        limpar_frame()
        turmas = ler_turmas_materias(materia)
        ctk.CTkLabel(frame_principal,text="SELECIONE AS TURMAS DO PROFESSOR",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=40, sticky="ew")

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, menu_principal_admin)

        else:
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda t=turma[1]: adicionar_turmas(t)).grid(row=turma[0], column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda t=turma[1]: adicionar_turmas(t)).grid(row=turma[0] - 5, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda t=turma[1]: adicionar_turmas(t)).grid(row=turma[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda t=turma[1]: adicionar_turmas(t)).grid(row=turma[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="ADICIONAR TURMAS E FINALIZAR", width=50, height=30, command=lambda: executar_cadastro(nome, idade, email, usuario, senha, materia)).grid(row=6, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_escolher_materia).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    tela_cadastro()

        
def tela_cadastrar_turmas():
    materias_adicionadas = None
    materias = []
    def executar_cadastro(nome):
        if materias:
            executar = 1
            turmas = ler_turmas()
            for turma in turmas:
                if turma[1] == nome:
                    executar = 0
                    ctk.CTkLabel(frame_principal, text="TURMA JÁ EXISTENTE", font=("Arial",30,"bold")).grid(row=8, column=0, columnspan=3, pady=(40,20), sticky="n")
                    app.update()
                    app.after(1500, menu_principal_admin)
            
            valida_limite_turmas = validar_limite_turma()
            if not valida_limite_turmas:
                executar = 0
                ctk.CTkLabel(frame_principal, text="LIMITE DE TURMAS ATINGIDO", font=("Arial",30,"bold")).grid(row=8, column=0, columnspan=3, pady=(40,20), sticky="n")
                app.update()
                app.after(1500, menu_principal_admin)
            
            if executar == 1:
                cadastro=cadastrar_turma(nome)
                if not cadastro:
                    ctk.CTkLabel(frame_principal, text="TURMA CADASTRADA", font=("Arial",30,"bold")).grid(row=8, column=0, columnspan=3, pady=(40,20), sticky="n")
                else:
                    ctk.CTkLabel(frame_principal, text=cadastro, font=("Arial",30,"bold")).grid(row=8, column=0, columnspan=3, pady=(40,20), sticky="n")

                id_turma_adicionada = ler_id_turma(nome)
                for materia in materias:
                    id_materia = ler_id_materia(materia)
                    vincular_turma_materia(id_turma_adicionada[0], id_materia[0])
                
                app.update()
                app.after(1500, menu_principal_admin)
        else:
            ctk.CTkLabel(frame_principal, text="NÃO FOI SELECIONADA NENHUMA MATÉRIA", font=("Arial",30,"bold")).grid(row=8, column=0, columnspan=3, pady=(40, 20), sticky="n")
            app.update()
            app.after(1500, tela_escolher_materias(nome))
              

    def adicionar_materia(materia):
        nonlocal materias_adicionadas

        adicionar = 1
        for i, j in enumerate(materias):
            if materia == j:
                adicionar = 0
                materias.pop(i)
        if adicionar == 1:
            materias.append(materia)

        if materias_adicionadas is not None:
            try:
                materias_adicionadas.destroy()
            except:
                None
        
        materias_adicionadas = ctk.CTkLabel(frame_principal, text=f"Matérias adicionadas ao professor: {materias}", font=("Arial",20))
        materias_adicionadas.grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")

    def tela_escolher_materias(nome):
        limpar_frame()
        botao_materia = {}
        materias = ler_materias_ativas()
        ctk.CTkLabel(frame_principal,text="SELECIONE AS MATÉRIAS DA TURMA",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not materias:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ MATÉRIAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, menu_principal_admin)

        else:
            for materia in materias:
                if materia[0] < 6:
                    botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda m=materia[1]: adicionar_materia(m)).grid(row=materia[0], column=0, padx=100, pady=50, stick="nw")
                elif materia[0] < 11:
                    botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda m=materia[1]: adicionar_materia(m)).grid(row=materia[0] - 5, column=1, pady=50)
                elif materia[0] < 16:
                    botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda m=materia[1]: adicionar_materia(m)).grid(row=materia[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda m=materia[1]: adicionar_materia(m)).grid(row=materia[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="ADICIONAR MATÉRIAS E FINALIZAR", width=50, height=30, command=lambda: executar_cadastro(nome)).grid(row=6, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")

    def tela_cadastro_materia():
        limpar_frame()
        ctk.CTkLabel(frame_principal, text="CADASTRAR TURMA", font=("Arial",45,"bold")).grid(row=0, column=1, pady=30)
        entrar_nome = ctk.CTkEntry(frame_principal,placeholder_text="Nome Da Turma",width=300, height=30); entrar_nome.grid(row=1, column=1, pady=50)
        ctk.CTkButton(frame_principal,text="Cadastrar",width=250, height=50,command=lambda: tela_escolher_materias(entrar_nome.get())).grid(row=2, column=1, pady=10)
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")
     
        entrar_nome.bind("<Return>", lambda event: tela_escolher_materias(entrar_nome.get()))

    tela_cadastro_materia()


def tela_listar_alunos():
    limpar_frame()
    ctk.CTkLabel(frame_principal, text="LISTA DE ALUNOS", font=("Arial", 45, "bold")).pack(pady=20)

    ctk.CTkButton(frame_principal, text="←", width=50, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1840, y=20)
    alunos = ler_alunos()
    
    textbox = None
    
    def mostrar_todos_alunos():
        textbox.delete("1.0", "end")
        alunos_atualizados = ler_alunos()
        if alunos_atualizados:
            for aluno in alunos_atualizados:
                textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]}\nIDADE: {aluno[2]}\nEMAIL: {aluno[3]}\nTURMA: {aluno[4]}\nRESPONSÁVEL: {aluno[5]}\nEMAIL DO RESPONSÁVEL: {aluno[6]}\nATIVO [1-SIM, 0-NÃO]: {aluno[7]}\n==========\n")
    
    def mostrar_alunos_ativos():
        textbox.delete("1.0", "end")
        alunos_ativos = ler_alunos_ativados_desativados(1)
        if alunos_ativos:
            for aluno in alunos_ativos:
                textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]}\nIDADE: {aluno[2]}\nEMAIL: {aluno[3]}\nTURMA: {aluno[4]}\nRESPONSÁVEL: {aluno[5]}\nEMAIL DO RESPONSÁVEL: {aluno[6]}\nATIVO [1-SIM, 0-NÃO]: {aluno[7]}\n==========\n")

    def mostrar_alunos_inativos():
        textbox.delete("1.0", "end")
        alunos_inativos = ler_alunos_ativados_desativados(0)
        if alunos_inativos:
            for aluno in alunos_inativos:
                textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]}\nIDADE: {aluno[2]}\nEMAIL: {aluno[3]}\nTURMA: {aluno[4]}\nRESPONSÁVEL: {aluno[5]}\nEMAIL DO RESPONSÁVEL: {aluno[6]}\nATIVO [1-SIM, 0-NÃO]: {aluno[7]}\n==========\n")

    if not alunos:
        ctk.CTkLabel(frame_principal, text="NÃO HÁ ALUNOS CADASTRADOS", width=250, text_color="red", font=("Arial", 45, "bold")).place(x=600, y=700) 
        app.after(1500, menu_principal_admin)
    else:
        botoes_frame = ctk.CTkFrame(frame_principal, fg_color="transparent")
        botoes_frame.pack(pady=10)
        
        ctk.CTkButton(botoes_frame, text="Todos os Alunos", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_todos_alunos).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Alunos Ativos", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_alunos_ativos).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Alunos Inativos", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_alunos_inativos).pack(side="left", padx=15)
        
        textbox = ctk.CTkTextbox(frame_principal, width=900, height=500)
        textbox.pack(pady=10)


def tela_listar_professores():
    limpar_frame()
    ctk.CTkLabel(frame_principal, text="LISTA DE PROFESSORES", font=("Arial", 45, "bold")).pack(pady=20)
    ctk.CTkButton(frame_principal, text="←", width=50, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1840, y=20)

    professores = ler_professores()
    textbox = None
    
    def mostrar_todos_professores():
        textbox.delete("1.0", "end")
        for professor in professores:
            materia = ler_nome_materia(professor[7])
            usuario = len(professor[4]) - 2
            textbox.insert("end", f"ID: {professor[0]} | NOME: {professor[1]}\nIDADE: {professor[2]}\nEMAIL: {professor[3]}\nUSUÁRIO: {professor[4][:2] + '*' * usuario}\nSENHA: {"*" * len(professor[5])}\nATIVO [1-SIM, 0-NÃO]: {professor[6]}\nMATÉRIA: {materia[0]}\n==========\n")

    def mostrar_professores_ativos():
        textbox.delete("1.0", "end")
        professores_ativos = ler_professores_ativados_desativados(1)
        for professor in professores_ativos:
            materia = ler_nome_materia(professor[7])
            usuario = len(professor[4]) - 2
            textbox.insert("end", f"ID: {professor[0]} | NOME: {professor[1]}\nIDADE: {professor[2]}\nEMAIL: {professor[3]}\nUSUÁRIO: {professor[4][:2] + '*' * usuario}\nSENHA: {"*" * len(professor[5])}\nATIVO [1-SIM, 0-NÃO]: {professor[6]}\nMATÉRIA: {materia[0]}\n==========\n")
    
    def mostrar_professores_inativos():
        textbox.delete("1.0", "end")
        professores_inativos = ler_professores_ativados_desativados(0)
        for professor in professores_inativos:
            materia = ler_nome_materia(professor[7])
            usuario = len(professor[4]) - 2
            textbox.insert("end", f"ID: {professor[0]} | NOME: {professor[1]}\nIDADE: {professor[2]}\nEMAIL: {professor[3]}\nUSUÁRIO: {professor[4][:2] + '*' * usuario}\nSENHA: {"*" * len(professor[5])}\nATIVO [1-SIM, 0-NÃO]: {professor[6]}\nMATÉRIA: {materia[0]}\n==========\n")
    
    if not professores:
        ctk.CTkLabel(frame_principal, text="NÃO HÁ PROFESSORES CADASTRADOS", width=250, text_color="red", font=("Arial", 45, "bold")).place(x=500, y=700) 
        app.after(1500, menu_principal_admin)
    else:
        botoes_frame = ctk.CTkFrame(frame_principal, fg_color="transparent")
        botoes_frame.pack(pady=10)
        
        ctk.CTkButton(botoes_frame, text="Todos os Professores", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_todos_professores).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Professores Ativos", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_professores_ativos).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Professores Inativos", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_professores_inativos).pack(side="left", padx=15)
        
        textbox = ctk.CTkTextbox(frame_principal, width=900, height=500)
        textbox.pack(pady=10)


def tela_listar_turmas():
    limpar_frame()
    ctk.CTkLabel(frame_principal, text="LISTA DE TURMAS", font=("Arial", 45, "bold")).pack(pady=20)
    ctk.CTkButton(frame_principal, text="←", width=50, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1840, y=20)

    turmas = ler_turmas()
    textbox = None

    def mostrar_todas_turmas():
        textbox.delete("1.0", "end")
        for turma in turmas:
            textbox.insert("end", f"ID: {turma[0]} | TURMA: {turma[1]} | DATA DE ABERTURA: {turma[2]} | ATIVO [1-SIM; 0-NÃO]: {turma[3]}\n=========\n")
    
    def mostrar_turmas_ativas():
        textbox.delete("1.0", "end")
        turmas_ativas = ler_turmas_ativadas_desativadas(1)
        for turma in turmas_ativas:
            textbox.insert("end", f"ID: {turma[0]} | TURMA: {turma[1]} | DATA DE ABERTURA: {turma[2]} | ATIVO [1-SIM; 0-NÃO]: {turma[3]}\n=========\n")
    
    def mostrar_turmas_inativas():
        textbox.delete("1.0", "end")
        turmas_inativas = ler_turmas_ativadas_desativadas(0)
        for turma in turmas_inativas:
            textbox.insert("end", f"ID: {turma[0]} | TURMA: {turma[1]} | DATA DE ABERTURA: {turma[2]} | ATIVO [1-SIM; 0-NÃO]: {turma[3]}\n=========\n")
    
    if not turmas:
        ctk.CTkLabel(frame_principal, text="NÃO HÁ TURMAS CADASTRADAS", text_color="red", font=("Arial", 45, "bold")).place(x=600, y=700)
        app.after(1500, menu_principal_admin)
    else:
        botoes_frame = ctk.CTkFrame(frame_principal, fg_color="transparent")
        botoes_frame.pack(pady=10)
        
        ctk.CTkButton(botoes_frame, text="Todos as Turmas", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_todas_turmas).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Turmas Ativas", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_turmas_ativas).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Turmas Inativas", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_turmas_inativas).pack(side="left", padx=15)
        
        textbox = ctk.CTkTextbox(frame_principal, width=700, height=350)
        textbox.pack(pady=10)


def tela_listar_materias():
    limpar_frame()
    ctk.CTkLabel(frame_principal, text="LISTA DE MATÉRIAS", font=("Arial", 45, "bold")).pack(pady=20)
    ctk.CTkButton(frame_principal, text="←", width=50, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1840, y=20)
    
    materias = ler_materias()
    textbox = None

    def mostrar_todas_materias():
        textbox.delete("1.0", "end")
        for materia in materias:
            textbox.insert("end", f"ID: {materia[0]} | MATÉRIA: {materia[1]} | ATIVO [1-SIM; 0-NÃO]: {materia[2]}\n=========\n")
    
    def mostrar_materias_ativas():
        textbox.delete("1.0", "end")
        materias_ativas = ler_materias_ativadas_desativadas(1)
        for materia in materias_ativas:
            textbox.insert("end", f"ID: {materia[0]} | MATÉRIA: {materia[1]} | ATIVO [1-SIM; 0-NÃO]: {materia[2]}\n=========\n")
    
    def mostrar_materias_inativas():
        textbox.delete("1.0", "end")
        materias_inativas = ler_materias_ativadas_desativadas(0)
        for materia in materias_inativas:
            textbox.insert("end", f"ID: {materia[0]} | MATÉRIA: {materia[1]} | ATIVO [1-SIM; 0-NÃO]: {materia[2]}\n=========\n")
    
    if not materias:
        ctk.CTkLabel(frame_principal, text="NÃO HÁ MATÉRIAS CADASTRADAS", text_color="red", font=("Arial", 45, "bold")).place(x=600, y=700)
        app.after(1500, menu_principal_admin)
    else:
        botoes_frame = ctk.CTkFrame(frame_principal, fg_color="transparent")
        botoes_frame.pack(pady=10)
        
        ctk.CTkButton(botoes_frame, text="Todos as Matérias", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_todas_materias).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Matérias Ativas", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_materias_ativas).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Matérias Inativas", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_materias_inativas).pack(side="left", padx=15)
        
        textbox = ctk.CTkTextbox(frame_principal, width=700, height=350)
        textbox.pack(pady=10)

def tela_desativar_materia():
    limpar_frame()
    global acao
    acao = 0
    def ativa():
        global acao
        acao = 1

    def desativa():
        global acao
        acao = 0

    def valida_dados(entrar_id_desativar, acao):
        if entrar_id_desativar.get():
            valida_id = validar_id_materia(entrar_id_desativar.get())
            if valida_id:
                if acao == 0 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="MATÉRIA DESATIVADA", font=("Arial",45,"bold")).place(x=750, y=420)
                elif acao == 1 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="MATÉRIA REATIVADA", font=("Arial",45,"bold")).place(x=750, y=420)
            else:
                ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)
        else:
            ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)

        app.after(1500, menu_principal_admin)


    ctk.CTkLabel(frame_principal, text="DESATIVAR/ATIVAR MATÉRIA", font=("Arial",45,"bold")).place(x=680, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Matéria", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Matéria", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID da matéria",width=300); entrar_id_desativar.place(x=820, y=280)

    ctk.CTkButton(frame_principal, text="Ativar/Desativar Matéria", width=250, fg_color='red', command=lambda: valida_dados(entrar_id_desativar, acao)).place(x=850, y=350)


def tela_atualizar_aluno():
    limpar_frame()
    global item
    item = ''
    global id_turma
    id_turma = 0

    def executar_atualizacao(id, turma):
        global id_turma
        id_turma = 0
        id_turma = (turma)
        atualizar(id)


    def muda_opcao(opcao):
        global item
        item = opcao


    def tela_muda_turma():
        botao_turma = {}
        limpar_frame()
        turmas = ler_turmas_ativas()
        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO ALUNO",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")
        entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="MATRÍCULA DO ALUNO",width=300); entrar_id.grid(row=1, column=0, columnspan=3, pady=10)

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=2, column=0, columnspan=3, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, tela_atualizar_aluno)

        else:
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda m=turma[0]: executar_atualizacao(entrar_id, m)).grid(row=turma[0] + 1, column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda m=turma[0]: executar_atualizacao(entrar_id, m)).grid(row=turma[0] - 4, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda m=turma[0]: executar_atualizacao(entrar_id,  m)).grid(row=turma[0] - 9, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda m=turma[0]: executar_atualizacao(entrar_id, m)).grid(row=turma[0] - 14, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_atualizar_aluno).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")

    def opcao_troca():
        ctk.CTkLabel(frame_principal,text="ESCOLHA O QUE DESEJA MUDAR",font=("Arial",45,"bold")).grid(row=2, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="Mudar Nome", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("nome")).grid(row=3, column=0, padx=100, pady=15, stick="ne")
        ctk.CTkButton(frame_principal, text="Mudar Idade", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("idade")).grid(row=4, column=0, padx=100, pady=15, stick="ne")
        ctk.CTkButton(frame_principal, text="Mudar e-mail", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("e-mail")).grid(row=3, column=1, pady=(10, 15), sticky="n")
        ctk.CTkButton(frame_principal, text="Mudar Turma", width=350, height=40, font=("Arial", 25), command=tela_muda_turma).grid(row=4, column=1, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="Mudar Nome do Responsável", width=350, height=40, font=("Arial", 20), command=lambda: muda_opcao("nome do responsável")).grid(row=3, column=2, padx=100, pady=15, stick="nw")
        ctk.CTkButton(frame_principal, text="Mudar e-mail do Responsável", width=350, height=40, font=("Arial", 20), command=lambda: muda_opcao("e-mail do responsável")).grid(row=4, column=2, padx=100, pady=15, stick="nw")

    opcao_troca()
    ctk.CTkLabel(frame_principal,text="ATUALIZAR ALUNO",font=("Arial",45,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")
    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="MATRÍCULA DO ALUNO",width=300); entrar_id.grid(row=1, column=0, columnspan=3, pady=(40, 20), sticky="n")
    entrar_item=ctk.CTkEntry(frame_principal,placeholder_text=f"Nova alteração", height=30, width=500); entrar_item.grid(row=5, column=0, columnspan=3, pady=(40, 20), sticky="n")
    
    entrar_id.bind("<Return>", lambda event: entrar_item.focus())
    entrar_item.bind("<Return>", lambda event: atualizar())

    def atualizar(id = ''):
        alunos = ler_alunos()
        valida_id = False

        if not alunos:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ ALUNOS CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
            app.update()
            sleep(1.5)
            app.after(0000, menu_principal_admin)
            return
        
        if not id == '':
            if id.get().strip():
                valida_id = validar_id_aluno(id.get())
                if valida_id and id_turma != 0:
                    atualizar_aluno(id.get(), "fk_id_turma", id_turma)
                    ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                    app.update()
                    sleep(1.5)
                    app.after(0000, menu_principal_admin)
                    return
            
        elif entrar_id.get().strip():
            valida_id = validar_id_aluno(entrar_id.get())
            if valida_id and id_turma != 0:
                atualizar_aluno(entrar_id.get(), "fk_id_turma", id_turma)
                ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                app.update()
                sleep(1.5)
                app.after(0000, menu_principal_admin)
                return
            
        if not valida_id:
            ctk.CTkLabel(frame_principal,text="MATRICULA DO ALUNO NÃO INSERIDA",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
            app.update()
            sleep(1.5)
            app.after(0000, tela_atualizar_aluno)
            return
        
        else:
            if not item:
                tela_atualizar_aluno()
                ctk.CTkLabel(frame_principal,text="OPÇÃO DE ALTERAÇÃO NÃO INSERIDA",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                app.update()
                sleep(1.5)
                app.after(0000, tela_atualizar_aluno)
                return 
            match item:
                case "nome":
                    valor = entrar_item.get().strip()
                    if not validar_nome(valor):
                        ctk.CTkLabel(frame_principal,text="Nome inválido",text_color="red",font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                        return
                    resultado = atualizar_aluno(entrar_id.get(), "nome_aluno", valor)
                    if resultado:
                        ctk.CTkLabel(frame_principal,text="Cadastro atualizado com sucesso",font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                    else:
                        ctk.CTkLabel(frame_principal,text="Erro ao atualizar no banco",text_color="red",font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")

                case "idade":
                    valida=validar_idade(entrar_item.get())
                    if valida:
                        atualiza=atualizar_aluno(entrar_id.get(), "idade_aluno", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                        else:
                            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                    else:
                        ctk.CTkLabel(frame_principal,text="Idade Inválida", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                        app.update()
                        sleep(1.5)
                        app.after(0000, tela_atualizar_aluno)


                case "e-mail":
                    atualiza=atualizar_aluno(entrar_id.get(), "email_aluno", entrar_item.get())
                    if atualiza:
                        ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                    else:
                        ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")


                case "nome do responsável":
                    valida=validar_nome(entrar_item.get())
                    if valida:
                        atualiza=atualizar_aluno(entrar_id.get(), "nome_responsavel", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                        else:
                            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO",width=250, font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                    else:
                        ctk.CTkLabel(frame_principal,text="Nome Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                        app.update()
                        sleep(1.5)
                        app.after(0000, tela_atualizar_aluno)

                
                case "e-mail do responsável":
                    atualiza=atualizar_aluno(entrar_id.get(), "email_responsavel", entrar_item.get())
                    if atualiza:
                        ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                    else:
                        ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO",width=250, font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
                

                case default:
                    ctk.CTkLabel(frame_principal,text="Erro ao Realizar Cadastro, por favor preencha os dados corretamente", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")
        

            app.after(1500, menu_principal_admin)
    ctk.CTkButton(frame_principal,text="Atualizar Aluno",height=50, width=450,command=atualizar).grid(row=6, column=0, columnspan=3, pady=(40, 20), sticky="n")


def tela_atualizar_professor():
    limpar_frame()
    global item
    item = ''
    global id_turma
    id_turma = 0
    
    id_professor_salvo = {"id": ""}

    def executar_vinculo_turma(id_da_turma):
        id_prof = id_professor_salvo["id"]
        if id_prof:
            try:
                vincular_professor_turma(id_prof, id_da_turma) 

                limpar_frame()
                ctk.CTkLabel(frame_principal, text="TURMA VINCULADA COM SUCESSO!", text_color="green", font=("Arial", 35, "bold")).pack(pady=100)
                app.update()
                sleep(1.5)
                menu_principal_admin()
            except Exception as e:
                limpar_frame()
                ctk.CTkLabel(frame_principal, text=f"Erro ao vincular turma: {e}", text_color="red", font=("Arial", 25, "bold")).pack(pady=100)
                app.update()
                sleep(2)
                tela_atualizar_professor()

    def muda_opcao(opcao):
        global item
        item = opcao

    def tela_adiciona_turma():
        id_prof = entrar_id.get().strip()

        if not id_prof or not id_prof.isdigit():
            ctk.CTkLabel(frame_principal,text="DIGITE UM ID DE PROFESSOR VÁLIDO ANTES",text_color="red",font=("Arial", 22, "bold")).grid(row=8, column=0, columnspan=3, pady=10)
            return

        valida_id = False

        try:
            conexao_teste = conectar()
            cursor_teste = conexao_teste.cursor()

            sql_teste = "SELECT id_professor FROM professores WHERE id_professor = %s"
            cursor_teste.execute(sql_teste, (int(id_prof),))

            if cursor_teste.fetchone():
                valida_id = True

            cursor_teste.close()
            conexao_teste.close()

        except Exception as erro:
            print(erro)

        if not valida_id:
            ctk.CTkLabel(frame_principal,text="ID DO PROFESSOR NÃO ENCONTRADO",text_color="red",font=("Arial", 22, "bold")).grid(row=8, column=0, columnspan=3, pady=10)
            return

        id_professor_salvo["id"] = id_prof

        limpar_frame()

        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO PROFESSOR",font=("Arial", 45, "bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20))
        ctk.CTkButton(frame_principal,text="←",width=50,command=tela_atualizar_professor).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).grid(row=0, column=2, padx=20, pady=20, sticky="ne")

        materia = ler_materia_professor(id_prof)
        turmas = ler_turmas_materias(materia[0])

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS PARA ESSA MATÉRIA",text_color="red",font=("Arial", 22, "bold")).grid(row=8, column=0, columnspan=3, pady=10)
            return

        botao_turma = {}

        for turma in ler_turmas_materias(materia[0]):
            if turma[0] < 6:
                botao_turma[turma[0]] = ctk.CTkButton(frame_principal,text=turma[1],width=350,height=40,font=("Arial", 25),command=lambda m=turma[0]: executar_vinculo_turma(m))
                botao_turma[turma[0]].grid(row=turma[0] + 1,column=0,padx=100,pady=50,sticky="nw")

            elif turma[0] < 11:
                botao_turma[turma[0]] = ctk.CTkButton(frame_principal,text=turma[1],width=350,height=40,font=("Arial", 25),command=lambda m=turma[0]: executar_vinculo_turma(m))
                botao_turma[turma[0]].grid(row=turma[0] - 4,column=1,pady=50)

            elif turma[0] < 16:
                botao_turma[turma[0]] = ctk.CTkButton(frame_principal,text=turma[1],width=350,height=40,font=("Arial", 25),command=lambda m=turma[0]: executar_vinculo_turma(m))
                botao_turma[turma[0]].grid(row=turma[0] - 9,column=2,padx=100,pady=50,sticky="ne")

            else:
                botao_turma[turma[0]] = ctk.CTkButton(frame_principal,text=turma[1],width=350,height=40,font=("Arial", 25),command=lambda m=turma[0]: executar_vinculo_turma(m))
                botao_turma[turma[0]].grid(row=turma[0] - 14,column=3,padx=100,pady=50,sticky="ne")
    
    def opcao_troca():

        ctk.CTkLabel(frame_principal,text="ESCOLHA O QUE DESEJA MUDAR",font=("Arial",45,"bold")).grid(row=2, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="Mudar Nome", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("nome")).grid(row=3, column=0, padx=100, pady=15, stick="ne")
        ctk.CTkButton(frame_principal, text="Mudar Idade", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("idade")).grid(row=4, column=0, padx=100, pady=15, stick="ne")
        ctk.CTkButton(frame_principal, text="Mudar e-mail", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("e-mail")).grid(row=3, column=1, pady=(10, 15), sticky="n")
        ctk.CTkButton(frame_principal, text="Adicionar Turma", width=350, height=40, font=("Arial", 25), command=tela_adiciona_turma).grid(row=4, column=1, pady=(40, 20), sticky="n")

    opcao_troca()
    ctk.CTkLabel(frame_principal,text="ATUALIZAR PROFESSOR",font=("Arial",45,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")
    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="ID DO PROFESSOR",width=300); entrar_id.grid(row=1, column=0, columnspan=3, pady=(40, 20), sticky="n")
    entrar_item=ctk.CTkEntry(frame_principal,placeholder_text=f"Nova alteração", height=30, width=500); entrar_item.grid(row=5, column=0, columnspan=3, pady=(40, 20), sticky="n")

    opcao_troca()

    def processar_atualizacao_professor():
        id_digitado = entrar_id.get().strip()
        
        if not id_digitado or not id_digitado.isdigit():
            ctk.CTkLabel(frame_principal, text="DIGITE UM ID VÁLIDO", text_color="red", font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)
            return

        if not item:
            ctk.CTkLabel(frame_principal, text="POR FAVOR, SELECIONE UMA OPÇÃO DE ALTERAÇÃO", width=250, text_color="red", font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)
            return 

        match item:
            case "nome":
                valor = entrar_item.get().strip()
                if not validar_nome(valor):
                    ctk.CTkLabel(frame_principal, text="Nome inválido", text_color="red", font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)
                    return
                resultado = atualizar_professor(id_digitado, "nome_professor", valor)
                if resultado:
                    ctk.CTkLabel(frame_principal, text="Cadastro atualizado com sucesso", font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)
                else:
                    ctk.CTkLabel(frame_principal, text="Erro ao atualizar no banco", text_color="red", font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)

            case "idade":
                valida = validar_idade_professor(entrar_item.get())
                if valida:
                    atualiza = atualizar_professor(id_digitado, "idade_professor", entrar_item.get())
                    if not atualiza:
                        ctk.CTkLabel(frame_principal, text="Erro ao Atualizar Idade no Banco", width=250, text_color="red", font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)
                    else:
                        ctk.CTkLabel(frame_principal, text="CADASTRO ATUALIZADO", width=250, font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)
                else:
                    ctk.CTkLabel(frame_principal, text="Idade Inválida para Professor", width=250, text_color="red", font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)

            case "e-mail":
                atualiza = atualizar_professor(id_digitado, "email_professor", entrar_item.get())  
                if not atualiza:
                    ctk.CTkLabel(frame_principal, text="Erro ao Atualizar E-mail no Banco", width=250, text_color="red", font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)
                else:
                    ctk.CTkLabel(frame_principal, text="CADASTRO ATUALIZADO", width=250, font=("Arial", 35, "bold")).grid(row=8, column=1, pady=20)
        
        app.after(1500, menu_principal_admin)
        
    ctk.CTkButton(frame_principal,text="Atualizar Professor",height=50, width=450,command=processar_atualizacao_professor).grid(row=6, column=0, columnspan=3, pady=(40, 20), sticky="n")


def tela_desativar_turma():
    limpar_frame()
    global acao
    acao = 0
    def ativa():
        global acao
        acao = 1

    def desativa():
        global acao
        acao = 0
    
    def valida_dados(entrar_id_desativar, acao):
        if entrar_id_desativar.get():
            valida_id = validar_id_turma(entrar_id_desativar.get())
            if valida_id:
                desativar_reativar_turma_e_alunos(entrar_id_desativar.get(), acao)
                if acao == 0 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="TURMA DESATIVADA", font=("Arial",45,"bold")).place(x=750, y=420)
                elif acao == 1 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="TURMA REATIVADA", font=("Arial",45,"bold")).place(x=750, y=420)
            else:
                ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)
        else:
            ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)

        app.after(1500, menu_principal_admin)

        
    ctk.CTkLabel(frame_principal, text="DESATIVAR/ATIVAR TURMA", font=("Arial",45,"bold")).place(x=685, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Turma", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Turma", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID Da Turma",width=300); entrar_id_desativar.place(x=820, y=280)

    ctk.CTkButton(frame_principal, text="Ativar/Desativar Turma", width=250, fg_color='red', command=lambda: valida_dados(entrar_id_desativar, acao)).place(x=850, y=350)


def tela_desativar_aluno():
    limpar_frame()
    global acao
    acao = 0
    def ativa():
        global acao
        acao = 1

    def desativa():
        global acao
        acao = 0

    def valida_dados(entrar_id_desativar, acao):
        if entrar_id_desativar.get():
            valida_id = validar_id_aluno(entrar_id_desativar.get())
            if valida_id:
                desativar_reativar_aluno(entrar_id_desativar.get(), acao)
                if acao == 0 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="ALUNO DESATIVADO", font=("Arial",45,"bold")).place(x=750, y=420)
                elif acao == 1 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="ALUNO REATIVADO", font=("Arial",45,"bold")).place(x=750, y=420)
            else:
                ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)
        else:
            ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)

        app.after(1500, menu_principal_admin)


    ctk.CTkLabel(frame_principal, text="Desativar ALUNO", font=("Arial",45,"bold")).place(x=780, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Aluno", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Aluno", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID do aluno",width=300); entrar_id_desativar.place(x=820, y=280)

    ctk.CTkButton(frame_principal, text="Ativar/Desativar Aluno", width=250, fg_color='red', command=lambda: valida_dados(entrar_id_desativar, acao)).place(x=850, y=350)


def tela_desativar_professor():
    limpar_frame()
    global acao
    acao = 0
    def ativa():
        global acao
        acao = 1

    def desativa():
        global acao
        acao = 0
    
    def valida_dados(entrar_id_desativar, acao):
        if entrar_id_desativar.get():
            valida_id = validar_id_professor(entrar_id_desativar.get())
            if valida_id:
                desativar_reativar_professor(entrar_id_desativar.get(), acao)
                if acao == 0 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="PROFESSOR DESATIVADO", font=("Arial",45,"bold")).place(x=750, y=420)
                elif acao == 1 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="PROFESSOR REATIVADO", font=("Arial",45,"bold")).place(x=750, y=420)
            else:
                ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)
        else:
            ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)

        app.after(1500, menu_principal_admin)


    ctk.CTkLabel(frame_principal, text="DESATIVAR/ATIVAR PROFESSOR", font=("Arial",45,"bold")).place(x=625, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Professor", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Professor", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID Do Professor",width=300); entrar_id_desativar.place(x=820, y=280)
    ctk.CTkButton(frame_principal, text="Ativar/Desativar Professor", width=250, fg_color='red', command=lambda: valida_dados(entrar_id_desativar, acao)).place(x=850, y=350)


def tela_buscar_aluno():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="BUSCAR ALUNO",font=("Arial",30,"bold")).grid(row=0,column=0,columnspan=3,pady=20)
    ctk.CTkButton(frame_principal,text="←",width=50,command=menu_principal_admin).grid(row=0,column=0,sticky="w",padx=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).grid(row=0,column=2,sticky="e",padx=20)

    entrar_busca=ctk.CTkEntry(frame_principal,placeholder_text="Digite o nome",width=300); entrar_busca.grid(row=1,column=0,columnspan=3,pady=10)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=300); textbox.grid(row=2,column=0,columnspan=3,pady=20)

    def buscar(nome):
        alunos = ler_alunos()
        if not alunos:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ ALUNOS CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=4,column=0,columnspan=3,pady=40) 
            app.after(1500, menu_principal_admin)    
        else:
            pesquisados = buscar_alunos(nome)
            textbox.delete("1.0", "end")
            for aluno in pesquisados:
                textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]}\nIDADE: {aluno[2]}\nEMAIL: {aluno[3]}\nTURMA: {aluno[4]}\nRESPONSÁVEL: {aluno[5]}\nEMAIL DO RESPONSÁVEL: {aluno[6]}\nATIVO [1-SIM, 0-NÃO]: {aluno[7]}\n==========\n")

    ctk.CTkButton(frame_principal,text="Buscar",width=250,command=lambda: buscar(entrar_busca.get())).grid(row=3,column=0,columnspan=3,pady=20)


def menu_principal_professor():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text=" Sistema Escolar",font=("Arial",35,"bold")).place(x=810,y=40)


    ctk.CTkButton(frame_principal,text="Adicionar Avaliação", font=("arial", 30),width=350,height=65, fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_adicionar_avaliacao).place(x=780,y=180)
 
    ctk.CTkButton(frame_principal,text="Listar Avaliações", font=("arial", 30),width=350,height=65, fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_listar_avaliacoes).place(x=780,y=270)

    ctk.CTkButton(frame_principal,text="Desativar/Ativar avaliação", font=("arial", 30),width=350,height=65, fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_desativar_avaliacao).place(x=780,y=360)
    
    ctk.CTkButton(frame_principal,text="Listar Aluno", font=("arial", 30),width=350,height=65, fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_ler_alunos_do_professor).place(x=780,y=450)
    
    
    ctk.CTkButton(frame_principal,text="Buscar Aluno", font=("arial", 30),width=350,height=65, fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_buscar_aluno_professor).place(x=780,y=540)
    

    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_login).place(x=20,y=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)


def tela_adicionar_avaliacao():
    def validar_dados(aluno, nome, data, nota):
        valida_aluno = ''
        valida_nome = ''
        valida_data = ''
        valida_nota = ''
        valida_data = ''
        valida_turma = ''

        if aluno.get():
            valida_aluno = validar_id_aluno(aluno.get())
            if valida_aluno:
                valida_turma = validar_turma_aluno_professor(aluno.get(), id_login)
                data_turma = ler_data_turma(aluno.get())
                if data.get():
                    valida_data = validar_data(data.get(), data_turma[0])
        if nome.get():
            valida_nome = validar_nome(nome.get())
        if nota.get():
            valida_nota = validar_nota(nota.get())
        
        if valida_aluno and valida_nome and valida_data and valida_nota and valida_turma:
            materia = ler_materia_professor(id_login)
            avaliacao = registrar_avaliacao(valida_data, aluno.get(), nome.get(), nota.get(), materia[0])
            if not avaliacao:
                ctk.CTkLabel(frame_principal, text="AVALIAÇÃO ADICIONADA", font=("Arial",45,"bold")).grid(row=6, column=1, pady=20)
            else:
                ctk.CTkLabel(frame_principal, text="OCORREU UM ERRO. TENTE NOVAMENTE MAIS TARDE", font=("Arial",45,"bold")).grid(row=6, column=1, pady=20)
        
        elif not valida_aluno:
            ctk.CTkLabel(frame_principal, text="MATRÍCULA DO ALUNO NÃO VÁLIDA", font=("Arial",45,"bold")).grid(row=6, column=1, pady=20)
            ctk.CTkLabel(frame_principal, text="VERIFIQUE SE VOCÊ INSERIU A MATRÍCULA DE UM ALUNO QUE É SEU CORRETAMENTE", font=("Arial",45,"bold")).grid(row=7, column=1, pady=20)

        elif not valida_turma:
            ctk.CTkLabel(frame_principal, text="VOCÊ NÃO DÁ AULA AO ALUNO ESCOLHIDO", font=("Arial",45,"bold")).grid(row=6, column=1, pady=20)

        else:
            print(valida_aluno, valida_nome, valida_data, valida_nota)
            ctk.CTkLabel(frame_principal, text="INFORMAÇÕES NÃO VÁLIDAS PREENCHIDAS", font=("Arial",45,"bold")).grid(row=6, column=1, pady=20)
        app.after(1500, menu_principal_professor)


    limpar_frame()
    ctk.CTkLabel(frame_principal,text="ADICIONAR AVALIAÇÃO",font=("Arial",40,"bold")).grid(row=0,column=1,pady=20)
    ctk.CTkButton(frame_principal,text="←",width=50,command=menu_principal_professor).grid(row=0,column=0,sticky="w",padx=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).grid(row=0,column=2,sticky="e",padx=20)

    entrar_aluno=ctk.CTkEntry(frame_principal,placeholder_text="Digite a matrícula do aluno",width=300); entrar_aluno.grid(row=1,column=1,pady=10)
    entrar_nome=ctk.CTkEntry(frame_principal,placeholder_text="Digite o nome da avaliação",width=300); entrar_nome.grid(row=2,column=1,pady=30)
    entrar_data=ctk.CTkEntry(frame_principal,placeholder_text="Digite a data da avaliação [AAAA/MM/DD]",width=300); entrar_data.grid(row=3,column=1,pady=10)
    entrar_nota=ctk.CTkEntry(frame_principal,placeholder_text="Digite a nota do aluno",width=300); entrar_nota.grid(row=4,column=1,pady=10)

    ctk.CTkButton(frame_principal,text="ADICIONAR AVALIAÇÃO",width=250,command=lambda: validar_dados(entrar_aluno, entrar_nome, entrar_data, entrar_nota)).grid(row=5, column=1, pady=20)
        
    entrar_aluno.bind("<Return>", lambda event: entrar_nome.focus())       
    entrar_nome.bind("<Return>", lambda event: entrar_data.focus())       
    entrar_data.bind("<Return>", lambda event: entrar_nota.focus())
    entrar_nota.bind("<Return>", lambda event: validar_dados(entrar_aluno, entrar_nome, entrar_data, entrar_nota))

def tela_listar_avaliacoes():
    limpar_frame()
    ctk.CTkLabel(frame_principal, text="LISTA DE AVALIAÇÕES", font=("Arial", 45, "bold")).pack(pady=20)
    ctk.CTkButton(frame_principal, text="←", width=50, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1840, y=20)

    materia = ler_materia_professor(id_login[0])
    avaliacoes = ler_avaliacoes(materia[0])
    
    textbox = None

    def mostrar_todas_avaliacoes():
        textbox.delete("1.0", "end")
        if avaliacoes:
            for avaliacao in avaliacoes:
                textbox.insert("end", f"ID: {avaliacao[0]} | NOME: {avaliacao[3]} | DATA: {avaliacao[1]} | MATRÍCULA DO ALUNO: {avaliacao[2]} | NOTA: {avaliacao[4]}\n=========\n")
    
    def mostrar_avaliacoes_ativas():
        textbox.delete("1.0", "end")
        avaliacoes_ativas = ler_avaliacoes_ativadas_desativadas(materia[0], 1)
        if avaliacoes_ativas:
            for avaliacao in avaliacoes_ativas:
                textbox.insert("end", f"ID: {avaliacao[0]} | NOME: {avaliacao[3]} | DATA: {avaliacao[1]} | MATRÍCULA DO ALUNO: {avaliacao[2]} | NOTA: {avaliacao[4]}\n=========\n")
    
    def mostrar_avaliacoes_inativas():
        textbox.delete("1.0", "end")
        avaliacoes_inativas = ler_avaliacoes_ativadas_desativadas(materia[0], 0)
        if avaliacoes_inativas:
            for avaliacao in avaliacoes_inativas:
                textbox.insert("end", f"ID: {avaliacao[0]} | NOME: {avaliacao[3]} | DATA: {avaliacao[1]} | MATRÍCULA DO ALUNO: {avaliacao[2]} | NOTA: {avaliacao[4]}\n=========\n")
    
    if not avaliacoes:
        ctk.CTkLabel(frame_principal, text="NÃO HÁ AVALIAÇÕES ADICIONADAS", text_color="red", font=("Arial", 45, "bold")).place(x=600, y=700)
        app.after(1500, menu_principal_professor)

    else:
        botoes_frame = ctk.CTkFrame(frame_principal, fg_color="transparent")
        botoes_frame.pack(pady=10)
        
        ctk.CTkButton(botoes_frame, text="Todas as Avaliações", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_todas_avaliacoes).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Avaliações Ativas", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_avaliacoes_ativas).pack(side="left", padx=15)
        ctk.CTkButton(botoes_frame, text="Avaliações Inativas", width=200, height=40, fg_color=("#2563EB", "#475569"), hover_color=("#1D4ED8", "#334155"), command=mostrar_avaliacoes_inativas).pack(side="left", padx=15)
        

        textbox = ctk.CTkTextbox(frame_principal, width=700, height=350)
        textbox.pack(pady=10)

def tela_desativar_avaliacao():
    limpar_frame()
    def ativa():
        global acao
        acao = 1

    def desativa():
        global acao
        acao = 0

    def valida_dados(entrar_id_desativar, acao):
        if entrar_id_desativar.get():
            valida_id = validar_id_avaliacao(entrar_id_desativar.get())
            if valida_id:
                if acao == 0 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="AVALIÇÃO DESATIVADA", font=("Arial",45,"bold")).place(x=750, y=420)
                elif acao == 1 and entrar_id_desativar.get():
                    ctk.CTkLabel(frame_principal, text="AVALIÇÃO REATIVADA", font=("Arial",45,"bold")).place(x=750, y=420)
            else:
                ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)
        else:
            ctk.CTkLabel(frame_principal, text="ID INVÁLIDO", font=("Arial",45,"bold")).place(x=800, y=420)

        app.after(1500, menu_principal_professor)


    ctk.CTkLabel(frame_principal, text="Desativar AVALIAÇÃO", font=("Arial",45,"bold")).place(x=780, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_professor).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Avaliação", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Avaliação", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID da avaliação",width=300); entrar_id_desativar.place(x=820, y=280)

    ctk.CTkButton(frame_principal, text="Ativar/Desativar Avaliação", width=250, fg_color='red', command=lambda: valida_dados(entrar_id_desativar, acao)).place(x=850, y=350)


def tela_ler_alunos_do_professor():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="ALUNOS DO PROFESSOR",font=("Arial",40,"bold")).grid(row=0, column=0, columnspan=3, pady=40, sticky="ew")
    ctk.CTkButton(frame_principal,text="←",width=50,command=menu_principal_professor).grid(row=0,column=0,sticky="w",padx=20)   
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0,column=2,sticky="e",padx=20)

    def mostrar_alunos_turma(id_turma, nome_turma):
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="ALUNOS DO PROFESSOR",font=("Arial",40,"bold")).pack(pady=20)
        ctk.CTkButton(frame_principal,text="←",width=50,command=tela_ler_alunos_do_professor).place(x=20, y=20)
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1840,y=20)
        textbox = ctk.CTkTextbox(frame_principal, width=900, height=500)
        textbox.pack(pady=20)
        textbox.delete("1.0", "end")
        alunos = ler_alunos_turma(id_turma)
        textbox.insert("end", f"--- TURMA: {nome_turma} ---\n\n")
        if not alunos:
            textbox.insert("end", "NÃO HÁ ALUNOS NESTA TURMA\n")
        else:
            for aluno in alunos:
                materia = ler_materia_professor(id_login)
                media = ler_media_aluno(aluno[0], materia[0])
                textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]}\nRESPONSÁVEL: {aluno[5]}\nEMAIL DO RESPONSÁVEL: {aluno[6]}\nMÉDIA: {media[0]}\n==========\n")

    def mostrar_todas_turmas():
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="ALUNOS DO PROFESSOR",font=("Arial",40,"bold")).pack(pady=20)
        ctk.CTkButton(frame_principal,text="←",width=50,command=tela_ler_alunos_do_professor).place(x=20, y=20)
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1840,y=20)
        textbox = ctk.CTkTextbox(frame_principal, width=900, height=500)
        textbox.pack(pady=20)
        textbox.delete("1.0", "end")
        turmas = ler_turmas_professor(id_login[0])
        if not turmas:
            textbox.insert("end", "NÃO HÁ TURMAS VINCULADAS A ESTE PROFESSOR\n")
            return
        for turma in turmas:
            alunos = ler_alunos_turma(turma[0])
            textbox.insert("end", f"--- TURMA: {turma[1]} ---\n\n")
            if not alunos:
                textbox.insert("end", "NÃO HÁ ALUNOS NESTA TURMA\n\n")
            else:
                for aluno in alunos:
                    materia = ler_materia_professor(id_login)
                    media = ler_media_aluno(aluno[0], materia[0])
                    textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]}\nRESPONSÁVEL: {aluno[5]}\nEMAIL DO RESPONSÁVEL: {aluno[6]}\nMÉDIA: {media[0]}\n==========\n")
            textbox.insert("end", "\n")

    turmas_professor = ler_turmas_professor(id_login[0])


    if not turmas_professor:
        ctk.CTkLabel(frame_principal, text="NÃO HÁ TURMAS VINCULADAS A ESTE PROFESSOR",text_color="red", font=("Arial",25,"bold")).pack(pady=10)
    else:
        ctk.CTkButton(frame_principal, text="Todas as Turmas", width=200, height=40,fg_color=("#2563EB","#475569"), hover_color=("#1D4ED8","#334155"),command=mostrar_todas_turmas).grid(row=1, column=0, columnspan=3, pady=40)
        for turma in turmas_professor:
            if turma[0] < 6:
                ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"), font=("Arial", 25),command=lambda t=turma[0], n=turma[1]: mostrar_alunos_turma(t, n)).grid(row=turma[0] + 1, column=0, pady=30)
            elif turma[0] < 11:
                ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"), font=("Arial", 25), command=lambda t=turma[0], n=turma[1]: mostrar_alunos_turma(t, n)   ).grid(row=turma[0] - 4, column=1, pady=30)
            elif turma[0] < 16:
                ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"), font=("Arial", 25), command=lambda t=turma[0], n=turma[1]: mostrar_alunos_turma(t, n)).grid(row=turma[0] - 9, column=2, padx=100, pady=30, stick="ne")
            else:
                ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, fg_color=("#475569","#2563EB"), hover_color=("#334155","#1D4ED8"), font=("Arial", 25), command=lambda t=turma[0], n=turma[1]: mostrar_alunos_turma(t, n)).grid(row=turma[0] - 14, column=3, padx=100, pady=30, stick="ne")


def tela_buscar_aluno_professor():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="BUSCAR ALUNO",font=("Arial",30,"bold")).grid(row=0,column=1,pady=20)
    ctk.CTkButton(frame_principal,text="←",width=50,command=menu_principal_professor).grid(row=0,column=0,sticky="w",padx=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).grid(row=0,column=2,sticky="e",padx=20)

    entrar_busca=ctk.CTkEntry(frame_principal,placeholder_text="Digite o nome",width=300); entrar_busca.grid(row=1,column=1,pady=10)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=300); textbox.grid(row=2,column=1,pady=20)

    def buscar(nome):
        pesquisados = []
        alunos = ler_alunos()
        if not alunos:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ ALUNOS CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=4,column=1,pady=40) 
            app.after(1500, menu_principal_professor)    
        else:
            turmas = ler_turmas_professor(id_login[0])
            for turma in turmas:
                if not turma[0]:
                    ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS VINCULADAS A ESTE PROFESSOR",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=4,column=1,pady=40) 
                    app.after(1500, menu_principal_admin)    
                    return
                pesquisados.append(buscar_alunos_professor(nome, turma[0]))
            textbox.delete("1.0", "end")
            for alunos in pesquisados:
                for aluno in alunos:
                    materia = ler_materia_professor(id_login[0])
                    media = ler_media_aluno(aluno[0], materia[0])
                    textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]}\nRESPONSÁVEL: {aluno[5]}\nEMAIL DO RESPONSÁVEL: {aluno[6]}\nMÉDIA: {media[0]}\n==========\n")

    ctk.CTkButton(frame_principal,text="Buscar",width=250,command=lambda: buscar(entrar_busca.get())).grid(row=3,column=1,pady=20)


tela_login()
app.mainloop()