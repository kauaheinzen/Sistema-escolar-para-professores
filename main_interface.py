import customtkinter as ctk
from tkinter import messagebox
from time import sleep
from funcoes_SQL import *
from validacoes import *

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
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)

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
            elif usuario[2] == "professor":
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

    ctk.CTkButton(frame_principal,text="Desativar/Ativar Matéria",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_desativar_materia).place(x=280,y=360)
    ctk.CTkButton(frame_principal,text="Atualizar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_atualizar_aluno).place(x=810,y=360)
    ctk.CTkButton(frame_principal,text="Atualizar Professor",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_atualizar_professor).place(x=1340,y=360)

    ctk.CTkButton(frame_principal,text="Desativar/Ativar Turma",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_desativar_turma).place(x=280,y=450)
    ctk.CTkButton(frame_principal,text="Desativar/Ativar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_desativar_aluno).place(x=810,y=450)
    ctk.CTkButton(frame_principal,text="Desativar/Ativar Professor",width=300,height=50,fg_color=("#475569","#2563EB"),hover_color=("#334155","#1D4ED8"),command=tela_desativar_professor).place(x=1340,y=450)

    ctk.CTkButton(frame_principal,text="Buscar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_buscar_aluno).place(x=810,y=540)

    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_login).place(x=20,y=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)



def menu_principal_professor():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text=" Sistema Escolar",font=("Arial",35,"bold")).place(x=810,y=40)


    ctk.CTkButton(frame_principal,text="Cadastrar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_cadastrar_aluno).place(x=810,y=180)
 
    ctk.CTkButton(frame_principal,text="Listar Alunos",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_listar_alunos).place(x=810,y=270)

    
    ctk.CTkButton(frame_principal,text="Atualizar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_atualizar_aluno).place(x=810,y=360)
    
    
    ctk.CTkButton(frame_principal,text="Desativar/Ativar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_desativar_aluno).place(x=810,y=450)
    

    ctk.CTkButton(frame_principal,text="Buscar Aluno",width=300,height=50,fg_color=("#2563EB","#475569"),hover_color=("#1D4ED8","#334155"),command=tela_buscar_aluno).place(x=810,y=540)

    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_login).place(x=20,y=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).place(x=1840,y=20)

def tela_cadastrar_materia():
    def executar_cadastro(nome):
        executar = 1
        materias = ler_materias()
        for materia in materias:
            if materia == nome:
                executar = 0
                ctk.CTkLabel(frame_principal, text="MATÉRIA JÁ EXISTENTE", font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)
        
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

    
    tela_cadastro_materia()
        

def tela_cadastrar_aluno():
    def mudar_id(id):
        global turma_aplicada
        turma_aplicada = id

    def cadastra_aluno(nome, idade, email, nome_resp, email_resp):
        cadastro = cadastrar_alunos(nome.get(), idade.get(), email.get(), turma_aplicada, nome_resp.get(), email_resp.get())
        if not cadastro:
            ctk.CTkLabel(frame_principal, text="ALUNO CADASTRADO", font=("Arial",30,"bold")).grid(row=0, column=1, pady=30)
        else:
            ctk.CTkLabel(frame_principal, text=cadastro, font=("Arial",30,"bold")).grid(row=0, column=1, pady=30)
        
        app.after(1500, menu_principal_admin)



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


    def executar_cadastro(turma):
        mudar_id()
        cadastro_aluno()


    def tela_turmas_cadastro():
        botao_turma = {}
        limpar_frame()
        turmas = ler_turmas()
        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO ALUNO",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, menu_principal_admin)

        else:
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_cadastro(turma[0])).grid(row=turma[0], column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_cadastro(turma[0])).grid(row=turma[0] - 5, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_cadastro(turma[0])).grid(row=turma[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_cadastro(turma[0])).grid(row=turma[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    tela_turmas_cadastro() 

def tela_cadastrar_professor():
    turmas = []
    def executar_cadastro(nome, idade, email, usuario, senha, materia):
        if not turmas:
            ctk.CTkLabel(frame_principal, text="NÃO HÁ TURMAS ESCOLHIDAS", fg_color="red", font=("Arial",30,"bold")).grid(row=7, column=1, pady=30)
            app.update()
            app.after(1500, tela_turmas_cadastro(nome, idade, email, usuario, senha, materia))
        else:
            valida_nome = validar_nome(nome)
            valida_idade = validar_idade(idade)

            if valida_nome and valida_idade:
                cadastro = cadastrar_professores(nome.get(), idade.get(), email.get(), usuario.get(), senha.get(), materia.get())
                if not cadastro:
                    ctk.CTkLabel(frame_principal, text="PROFESSOR CADASTRADO", font=("Arial",30,"bold")).grid(row=7, column=1, pady=30)
                else:
                    ctk.CTkLabel(frame_principal, text=cadastro.upper(), fg_color="red", font=("Arial",30,"bold")).grid(row=7, column=1, pady=30)
            else:
                ctk.CTkLabel(frame_principal, text="NOME E/OU IDADE INVÁLIDA", fg_color="red", font=("Arial",30,"bold")).grid(row=7, column=1, pady=30)


        professor = ler_id_professor(nome)
        for turma in turmas:
            vincular_professor_turma(professor[0], turma)
        
        app.update()
        app.after(1500, menu_principal_admin)

    def adicionar_turmas(turma):
        for i, j in enumerate(turmas):
            adicionar = 1
            if turma == j:
                adicionar = 0
                turmas.pop(i)
            if adicionar == 1:
                turmas.append(turma)
     
        turmas_adicionadas = ctk.CTkLabel(frame_principal, text=f"Turmas adicionadas ao professor: {turmas}", font=("Arial",20))
        try:
            turmas_adicionadas.destroy()
        except:
            None
        
        turmas_adicionadas.grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")

    def tela_escolher_materia(nome, idade, email, usuario, senha):
        botao_materia = {}
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="SELECIONE A MATÉRIA DO PROFESSOR",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")
        materias = ler_materias()
        if not materias:
            ctk.CTkLabel(frame_principal, text="NÃO HÁ MATÉRIAS CADASTRADAS", fg_color="red", font=("Arial",30,"bold")).grid(row=1, column=1, pady=30)
        for materia in materia:
            if materia[0] < 6:
                botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda: tela_turmas_cadastro(nome, idade, email, usuario, senha, materia[1])).get().grid(row=materia[0], column=0, padx=100, pady=50, stick="nw")
            elif materia[0] < 11:
                botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda: tela_turmas_cadastro(nome, idade, email, usuario, senha, materia[1])).grid(row=materia[0] - 5, column=1, pady=50)
            elif materia[0] < 16:
                botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda: tela_turmas_cadastro(nome, idade, email, usuario, senha, materia[1])).grid(row=materia[0] - 10, column=2, padx=100, pady=50, stick="ne")
            else:
                botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda: tela_turmas_cadastro(nome, idade, email, usuario, senha, materia[1])).grid(row=materia[0] - 15, column=3, padx=100, pady=50, stick="ne")
        
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_cadastro).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    def tela_cadastro():
        limpar_frame()
        ctk.CTkLabel(frame_principal,text="CADASTRE O PROFESSOR",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")
        entrar_nome = ctk.CTkEntry(frame_principal, placeholder_text="Nome do Professor", height=30, width=300); entrar_nome.grid(row=1, column=1, pady=50)
        entrar_idade = ctk.CTkEntry(frame_principal, placeholder_text="Idade do Professor", height=30, width=300); entrar_idade.grid(row=2, column=1, pady=10)
        entrar_email = ctk.CTkEntry(frame_principal, placeholder_text="E-mail do Professor", height=30, width=300); entrar_email.grid(row=3, column=1, pady=10)
        entrar_usuario = ctk.CTkEntry(frame_principal, placeholder_text="Nome de Usuário do Professor", height=30, width=300); entrar_usuario.grid(row=4, column=1, pady=10)
        entrar_senha = ctk.CTkEntry(frame_principal, placeholder_text="Crie uma Senha", height=30, width=300); entrar_senha.grid(row=5, column=1, pady=10)
        ctk.CTkButton(frame_principal, text="CADASTRAR PROFESSOR", width=50, height=30, command=lambda: tela_escolher_materia(entrar_nome, entrar_idade, entrar_email, entrar_usuario, entrar_senha)).grid(row=6, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    def tela_turmas_cadastro(nome, idade, email, usuario, senha, materia):
        botao_turma = {}
        limpar_frame()
        turmas = ler_turmas()
        ctk.CTkLabel(frame_principal,text="SELECIONE AS TURMAS DO PROFESSOR",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, menu_principal_admin)

        else:
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: adicionar_turmas(turma[1])).grid(row=turma[0], column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: adicionar_turmas(turma[1])).grid(row=turma[0] - 5, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: adicionar_turmas(turma[1])).grid(row=turma[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: adicionar_turmas(turma[1])).grid(row=turma[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="ADICIONAR TURMAS E FINALIZAR", width=50, height=30, command=lambda: executar_cadastro(nome, idade, email, usuario, senha, materia)).grid(row=6, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    tela_cadastro()
        
def tela_cadastrar_turmas():
    materias = []
    def executar_cadastro(nome):
        executar = 1
        turmas = ler_turmas()
        for turma in turmas:
            if turma == nome:
                executar = 0
                ctk.CTkLabel(frame_principal, text="TURMA JÁ EXISTENTE", font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)
        
        if executar == 1:
            cadastro=cadastrar_turma(nome.get())
            if not cadastro:
                ctk.CTkLabel(frame_principal, text="TURMA CADASTRADA", font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)
            else:
                ctk.CTkLabel(frame_principal, text=cadastro, font=("Arial",30,"bold")).grid(row=3, column=1, pady=30)
        
        materias = ler_id_materia(nome)
        for materia in materias:
            vincular_turma_materia(turma, materia[0])
        
        app.update()
        app.after(1500, menu_principal_admin)

    def adicionar_materia(materia):
        for i, j in enumerate(materias):
            adicionar = 1
            if materia == j:
                adicionar = 0
                materias.pop(i)
            if adicionar == 1:
                materias.append(materia)
     
        materias_adicionadas = ctk.CTkLabel(frame_principal, text=f"Matérias adicionadas ao professor: {materias}", font=("Arial",20))
        try:
            materias_adicionadas.destroy()
        except:
            None
        
        materias_adicionadas.grid(row=7, column=0, columnspan=3, pady=(40, 20), sticky="n")

    def tela_escolher_materias(nome):
        botao_materia = {}
        limpar_frame()
        materias = ler_materias()
        ctk.CTkLabel(frame_principal,text="SELECIONE AS MATÉRIAS DA TURMA",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not materias:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ MATÉRIAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, menu_principal_admin)

        else:
            for materia in materias:
                if materia[0] < 6:
                    botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda: adicionar_materia(materia[1])).grid(row=materia[0], column=0, padx=100, pady=50, stick="nw")
                elif materia[0] < 11:
                    botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda: adicionar_materia(materia[1])).grid(row=materia[0] - 5, column=1, pady=50)
                elif materia[0] < 16:
                    botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda: adicionar_materia(materia[1])).grid(row=materia[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_materia[materia[0]] = ctk.CTkButton(frame_principal, text=materia[1], width=350, height=40, font=("Arial", 25), command=lambda: adicionar_materia(materia[1])).grid(row=materia[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="ADICIONAR MATÉRIAS E FINALIZAR", width=50, height=30, command=lambda: executar_cadastro(nome.get())).grid(row=6, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")

    def tela_cadastro_materia():
        limpar_frame()
        ctk.CTkLabel(frame_principal, text="CADASTRAR TURMA", font=("Arial",45,"bold")).grid(row=0, column=1, pady=30)
        entrar_nome = ctk.CTkEntry(frame_principal,placeholder_text="Nome Da Turma",width=300, height=30); entrar_nome.grid(row=1, column=1, pady=50)
        ctk.CTkButton(frame_principal,text="Cadastrar",width=250, height=50,command=lambda: tela_escolher_materias(entrar_nome.get())).grid(row=2, column=1, pady=10)
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")

    
    tela_cadastro_materia()


def tela_listar_alunos():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="LISTA DE ALUNOS",font=("Arial",45,"bold")).pack(pady=20)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=350); textbox.pack(pady=20)
    ctk.CTkButton(frame_principal,text="←",width=250,command=menu_principal_admin).place(x=50, y=50)
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)
    alunos = ler_alunos()
    if not alunos:
        ctk.CTkLabel(frame_principal,text="NÃO HÁ ALUNOS CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).place(x=600, y=700) 
        app.after(1500, menu_principal_admin)

    else:
        for aluno in alunos:
            textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]} | IDADE: {aluno[2]} | EMAIL: {aluno[3]} | TURMA: {aluno[4]} | ATIVO [1-SIM, 0-NÃO]: {aluno[5]} | RESPONSÁVEL: {aluno[6]} | EMAIL DO RESPONSÁVEL: {aluno[7]}")


def tela_listar_professores():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="LISTA DE PROFESSORES",font=("Arial",45,"bold")).pack(pady=20)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=350); textbox.pack(pady=20)
    ctk.CTkButton(frame_principal,text="←",width=250,command=menu_principal_admin).place(x=50, y=50)
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)
    professores = ler_professores()
    if not professores:
        ctk.CTkLabel(frame_principal,text="NÃO HÁ PROFESSORES CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).place(x=600, y=700) 
        app.after(1500, menu_principal_admin)

    else:
        for professor in professores:
            materia = ler_nome_materia(professor[7])
            usuario = len(professor[4]) - 4
            textbox.insert("end", f"ID: {professor[0]} | NOME: {professor[1]} | IDADE: {professor[2]} | EMAIL: {professor[3]} | USUÁRIO: {professor[4][:4] + "*" * usuario} | SENHA: {"*" * len(professor[5])} | ATIVO [1-SIM, 0-NÃO]: {professor[6]} | MATÉRIA: {materia}")


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
        
    ctk.CTkLabel(frame_principal, text="DESATIVAR/ATIVAR MATÉRIA", font=("Arial",45,"bold")).place(x=780, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Matéria", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Matéria", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID da matéria",width=300); entrar_id_desativar.place(x=820, y=280)

    ctk.CTkButton(frame_principal, text="Ativar/Desativar Matéria", width=250, fg_color='red', command=lambda: desativar_reativar_materia(entrar_id_desativar.get(), acao)).place(x=850, y=350)


def tela_atualizar_aluno():
    limpar_frame()
    global item
    item = ''
    global id_turma
    id_turma = 0

    def executar_atualizacao(turma):
        global id_turma
        id_turma = 0
        id_turma = (turma)
        atualizar()


    def muda_opcao(opcao):
        global item
        item = opcao


    def tela_muda_turma():
        botao_turma = {}
        limpar_frame()
        turmas = ler_turmas()
        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO ALUNO",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, tela_atualizar_aluno)

        else:
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_atualizacao(turma[0])).grid(row=turma[0], column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_atualizacao(turma[0])).grid(row=turma[0] - 5, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_atualizacao(turma[0])).grid(row=turma[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_atualizacao(turma[0])).grid(row=turma[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_atualizar_aluno).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")

    def opcao_troca():
        ctk.CTkLabel(frame_principal,text="ESCOLHA O QUE DESEJA MUDAR",font=("Arial",45,"bold")).grid(row=2, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="Mudar Nome", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("nome")).grid(row=3, column=0, padx=100, pady=15, stick="ne")
        ctk.CTkButton(frame_principal, text="Mudar Idade", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("idade")).grid(row=4, column=0, padx=100, pady=15, stick="ne")
        ctk.CTkButton(frame_principal, text="Mudar e-mail", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("e-mail")).grid(row=3, column=1, pady=(10, 15), sticky="n")
        ctk.CTkButton(frame_principal, text="Mudar Turma", width=350, height=40, font=("Arial", 25), command=tela_muda_turma).grid(row=4, column=1, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="Mudar Nome do Responsável", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("nome do responsável")).grid(row=3, column=2, padx=100, pady=15, stick="nw")
        ctk.CTkButton(frame_principal, text="Mudar e-mail do Responsável", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("e-mail do responsável")).grid(row=4, column=2, padx=100, pady=15, stick="nw")

    opcao_troca()
    ctk.CTkLabel(frame_principal,text="ATUALIZAR ALUNO",font=("Arial",45,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")
    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="MATRÍCULA DO ALUNO",width=300); entrar_id.grid(row=1, column=1, pady=10)
    entrar_item=ctk.CTkEntry(frame_principal,placeholder_text=f"Nova alteração", height=30, width=500); entrar_item.grid(row=5, column=1, pady=30)



    def atualizar():
        alunos = ler_alunos()
        valida_id = validar_id_aluno(entrar_id.get())
        if not alunos:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ ALUNOS CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=1, pady=50)
            app.update()
            sleep(1.5)
            app.after(0000, menu_principal_admin)

        if id_turma != 0:
            atualizar_aluno(entrar_id.get(), "fk_id_turma", id_turma)
            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)

        elif not valida_id:
            tela_atualizar_aluno()
            ctk.CTkLabel(frame_principal,text="MATRICULA DO ALUNO NÃO INSERIDA",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=1, pady=50)

        else:
            if not item:
                tela_atualizar_aluno()
                ctk.CTkLabel(frame_principal,text="OPÇÃO DE ALTERAÇÃO NÃO INSERIDA",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=1, pady=50)

            match item:
                case "nome":
                    valida=validar_nome(entrar_item.get())
                    if valida:
                        atualiza=atualizar_aluno(entrar_id.get(), "nome_aluno", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                        else:
                            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Nome Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case "idade":
                    valida=validar_idade(entrar_item.get())
                    if valida:
                        atualiza=atualizar_aluno(entrar_id.get(), "idade_aluno", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                        else:
                            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Idade Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case "e-mail":
                    atualiza=atualizar_aluno(entrar_id.get(), "email_aluno", entrar_item.get())
                    if atualiza:
                        ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case "nome do responsável":
                    valida=validar_nome(entrar_item.get())
                    if valida:
                        atualiza=atualizar_aluno(entrar_id.get(), "nome_responsavel", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                        else:
                            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO",width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Nome Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)

                
                case "e-mail do responsável":
                    atualiza=atualizar_aluno(entrar_id.get(), "email_responsavel", entrar_item.get())
                    if atualiza:
                        ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO",width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                

                case default:
                    ctk.CTkLabel(frame_principal,text="Erro ao Realizar Cadastro, por favor preencha os dados corretamente", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
        

        app.after(1500, menu_principal_admin)

    ctk.CTkButton(frame_principal,text="Atualizar Aluno",height=50, width=450,command=atualizar).grid(row=6, column=1, pady=40)


def tela_atualizar_professor():
    limpar_frame()
    global item
    item = ''
    global id_turma
    id_turma = 0

    def executar_atualizacao(id, turma):
        global id_turma
        global id_professor

        id_professor = id
        id_turma = turma
        atualizar()


    def muda_opcao(opcao):
        global item
        item = opcao


    def tela_adiciona_turma():
        botao_turma = {}
        limpar_frame()
        turmas = ler_turmas()
        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO ALUNO",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(1.5)
            app.after(0, tela_atualizar_aluno)

        else:
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_atualizacao(turma[0])).grid(row=turma[0], column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_atualizacao(turma[0])).grid(row=turma[0] - 5, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_atualizacao(turma[0])).grid(row=turma[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=lambda: executar_atualizacao(turma[0])).grid(row=turma[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_atualizar_aluno).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")

    def opcao_troca():
        ctk.CTkLabel(frame_principal,text="ESCOLHA O QUE DESEJA MUDAR",font=("Arial",45,"bold")).grid(row=2, column=0, columnspan=3, pady=(40, 20), sticky="n")
        ctk.CTkButton(frame_principal, text="Mudar Nome", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("nome")).grid(row=3, column=0, padx=100, pady=15, stick="ne")
        ctk.CTkButton(frame_principal, text="Mudar Idade", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("idade")).grid(row=4, column=0, padx=100, pady=15, stick="ne")
        ctk.CTkButton(frame_principal, text="Mudar e-mail", width=350, height=40, font=("Arial", 25), command=lambda: muda_opcao("e-mail")).grid(row=3, column=1, pady=(10, 15), sticky="n")
        ctk.CTkButton(frame_principal, text="Adicionar Turma Ao Professor", width=350, height=40, font=("Arial", 25), command=tela_adiciona_turma).grid(row=4, column=1, pady=(40, 20), sticky="n")
        
    opcao_troca()
    ctk.CTkLabel(frame_principal,text="ATUALIZAR ALUNO",font=("Arial",45,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")
    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="ID do Professor",width=300); entrar_id.grid(row=1, column=1, pady=10)
    entrar_item=ctk.CTkEntry(frame_principal,placeholder_text=f"Nova alteração", height=30, width=500); entrar_item.grid(row=5, column=1, pady=30)



    def atualizar():
        professores = ler_professores()
        valida_id = validar_id_professor(entrar_id.get())
        if not professores:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ PROFESSORES CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=1, pady=50)
            app.update()
            sleep(1.5)
            app.after(0000, menu_principal_admin)

        if id_turma != 0:
            vincular_professor_turma(entrar_id.get(), "fk_id_turma")
            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)

        elif not valida_id:
            tela_atualizar_aluno()
            ctk.CTkLabel(frame_principal,text="ID DO PROFESSOR NÃO INSERIDO",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=1, pady=50)

        else:
            if not item:
                tela_atualizar_aluno()
                ctk.CTkLabel(frame_principal,text="OPÇÃO DE ALTERAÇÃO NÃO INSERIDA",width=250, text_color="red", font=("Arial",45,"bold")).grid(row=7, column=1, pady=50)

            match item:
                case "nome":
                    valida=validar_nome(entrar_item.get())
                    if valida:
                        atualiza=atualizar_professor(entrar_id.get(), "nome_professor", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                        else:
                            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Nome Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case "idade":
                    valida=validar_idade(entrar_item.get())
                    if valida:
                        atualiza=atualizar_professor(entrar_id.get(), "idade_professor", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                        else:
                            ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Idade Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case "e-mail":
                    atualiza=atualizar_professor(entrar_id.get(), "email_professor", entrar_item.get())
                    if atualiza:
                        ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="CADASTRO ATUALIZADO", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case default:
                    ctk.CTkLabel(frame_principal,text="Erro ao Realizar Cadastro, por favor preencha os dados corretamente", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
        

        app.after(1500, menu_principal_admin)

    ctk.CTkButton(frame_principal,text="Atualizar Professor",height=50, width=450,command=atualizar).grid(row=6, column=1, pady=40)


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
        
    ctk.CTkLabel(frame_principal, text="DESATIVAR/ATIVAR TURMA", font=("Arial",45,"bold")).place(x=780, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Turma", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Turma", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID Da Turma",width=300); entrar_id_desativar.place(x=820, y=280)

    ctk.CTkButton(frame_principal, text="Ativar/Desativar Turma", width=250, fg_color='red', command=lambda: desativar_reativar_turma_e_alunos(entrar_id_desativar.get(), acao)).place(x=850, y=350)


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
        
    ctk.CTkLabel(frame_principal, text="Desativar ALUNO", font=("Arial",45,"bold")).place(x=780, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Aluno", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Aluno", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID do aluno",width=300); entrar_id_desativar.place(x=820, y=280)

    ctk.CTkButton(frame_principal, text="Ativar/Desativar Aluno", width=250, fg_color='red', command=lambda: desativar_reativar_aluno(entrar_id_desativar.get(), acao)).place(x=850, y=350)


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
        
    ctk.CTkLabel(frame_principal, text="DESATIVAR/ATIVAR PROFESSOR", font=("Arial",45,"bold")).place(x=780, y=40)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).place(x=20, y=20)
    ctk.CTkButton(frame_principal, text="☀️", width=50, height=30, command=mudar_tema).place(x=1850, y=20)
    ctk.CTkButton(frame_principal, text="Ativar Professor", height=50, width=200, command=ativa).place(x=760, y=180)
    ctk.CTkButton(frame_principal, text="Desativar Professor", height=50, width=200, command=desativa).place(x=980, y=180)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID Do Professor",width=300); entrar_id_desativar.place(x=820, y=280)

    ctk.CTkButton(frame_principal, text="Ativar/Desativar Professor", width=250, fg_color='red', command=lambda: desativar_reativar_professor(entrar_id_desativar.get(), acao)).place(x=850, y=350)


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
            for aluno in pesquisados:
                textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]} | IDADE: {aluno[2]} | EMAIL: {aluno[3]} | TURMA: {aluno[4]} | ATIVO [1-SIM, 0-NÃO]: {aluno[5]} | RESPONSÁVEL: {aluno[6]} | EMAIL DO RESPONSÁVEL: {aluno[7]}")

    ctk.CTkButton(frame_principal,text="Buscar",width=250,command=lambda: buscar(entrar_busca.get())).grid(row=3,column=0,columnspan=3,pady=20)



    



tela_login()
app.mainloop()
