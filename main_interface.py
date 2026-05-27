import customtkinter as ctk
from tkinter import messagebox
from time import sleep
from funcoes_SQL import *
from validacoes import *

botao_turma = {}

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



def verificar_situacao(media):
    return "Aprovado" if media>=7 else ("Recuperação" if media>=5 else "Reprovado")


def menu_principal_admin():
    limpar_frame()
    ctk.CTkLabel(frame_principal, text="SISTEMA ESCOLAR", font=("Arial",35,"bold")).grid(row=0, column=1, pady=40)
    ctk.CTkButton(frame_principal, text="Cadastrar Aluno", width=300, height=50, command=tela_cadastrar_aluno).grid(row=1, column=1, pady=10)
    ctk.CTkButton(frame_principal, text="Listar Alunos", width=300, height=50, command=tela_listar_alunos).grid(row=2, column=1, pady=10)
    ctk.CTkButton(frame_principal, text="Atualizar Aluno", width=300, height=50, command=tela_atualizar_aluno).grid(row=3, column=1, pady=10)
    ctk.CTkButton(frame_principal, text="Desativar/Ativar Alunos", width=300, height=50, fg_color="red", command=tela_desativar_aluno).grid(row=4, column=1, pady=10)
    ctk.CTkButton(frame_principal, text="Buscar Aluno", width=300, height=50, command=tela_buscar_aluno).grid(row=5, column=1, pady=10)
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_login).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


def tela_cadastrar_aluno():
    def mudar_id(id):
        turma_aplicada = id


    def tela_turmas():
        global turma_aplicada
        limpar_frame()
        turma_aplicada = 0
        turmas = ler_turmas()
        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO ALUNO",width=300, font=("Arial",50,"bold")).grid(row=0, column=1, pady=40)

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(3)
            app.after(0, menu_principal_admin)

        else:
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=250, height=30, font=("Arial", 15), command=mudar_id(turma[0])).grid(row=turma[0], column=1, padx=100, pady=50, stick=...)
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=250, command=mudar_id(turma[0]))
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=250, command=mudar_id(turma[0]))
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=250, command=mudar_id(turma[0]))

        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=menu_principal_admin).grid(row=0, column=0, padx=20, pady=20, sticky="nw")

        botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=0, padx=20, pady=20, sticky="nw")


    tela_turmas()

    def cadastro_aluno():
        limpar_frame()
        global entrar_nome; global entrar_idade; global entrar_email; global entrar_nome_resp; global entrar_email_resp
        ctk.CTkLabel(frame_principal,text="CADASTRAR ALUNO",font=("Arial",30,"bold")).grid(row=0, column=1, pady=40)
        entrar_nome=ctk.CTkEntry(frame_principal,placeholder_text="Nome do aluno",width=300, height=30); entrar_nome.grid(row=1, column=1, pady=10)
        entrar_idade=ctk.CTkEntry(frame_principal,placeholder_text="Idade",width=300, height=30); entrar_idade.grid(row=2, column=1, pady=10)
        entrar_email=ctk.CTkEntry(frame_principal,placeholder_text="E-mail do aluno",width=300, height=30); entrar_email.grid(row=3, column=1, pady=10)
        entrar_nome_resp=ctk.CTkEntry(frame_principal,placeholder_text="Nome do responsável",width=300, height=30); entrar_nome_resp.grid(row=4, column=1, pady=10)
        entrar_email_resp=ctk.CTkEntry(frame_principal,placeholder_text="E-mail do responsável",width=300, height=30); entrar_email_resp.grid(row=5, column=1, pady=10)
        botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal,text="Cadastrar",width=250, height=50,command=...).grid(row=7, column=1, pady=10)
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_login).grid(row=0, column=0, padx=20, pady=20, sticky="nw")

    def cadastra_aluno():
        cadastro = cadastrar_alunos(entrar_nome.get(), entrar_idade.get(), entrar_email.get(), turma_aplicada, entrar_nome_resp.get(), entrar_email_resp.get())
        if not cadastro:
            ...


def tela_listar_alunos():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="LISTA DE ALUNOS",font=("Arial",30,"bold")).pack(pady=20)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=350); textbox.pack(pady=20)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)

    # for a in cursor.fetchall():
    #     textbox.insert("end",f"\nID:{a[0]}\nNome:{a[1]}\nIdade:{a[2]}\nTurma:{a[3]}\nNotas:{a[4]}\nMédia:{a[5]:.2f}\nSituação:{a[6]}\n----------------\n")

    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal_admin).pack(pady=10)

def tela_atualizar_aluno():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="ATUALIZAR ALUNO",font=("Arial",30,"bold")).pack(pady=20)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)

    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="ID",width=300); entrar_id.pack(pady=10)
    entrar_nome=ctk.CTkEntry(frame_principal,placeholder_text="Novo Nome",width=300); entrar_nome.pack(pady=10)
    entrar_idade=ctk.CTkEntry(frame_principal,placeholder_text="Nova Idade",width=300); entrar_idade.pack(pady=10)
    entrar_turma=ctk.CTkEntry(frame_principal,placeholder_text="Nova Turma",width=300); entrar_turma.pack(pady=10)
    entrar_notas=ctk.CTkEntry(frame_principal,placeholder_text="Novas Notas",width=300); entrar_notas.pack(pady=10)



    def atualizar():
        ...


    ctk.CTkButton(frame_principal,text="Atualizar Aluno",width=250,command=...).pack(pady=20)
    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal_admin).pack()

def tela_desativar_aluno():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="REMOVER ALUNO",font=("Arial",30,"bold")).pack(pady=20)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)

    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="ID do aluno",width=300); entrar_id.pack(pady=20)


    ctk.CTkButton(frame_principal,text="Remover Aluno",width=250,fg_color="red",command=...).pack(pady=20)
    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal_admin).pack()

def tela_buscar_aluno():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="BUSCAR ALUNO",font=("Arial",30,"bold")).pack(pady=20)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)

    entrar_busca=ctk.CTkEntry(frame_principal,placeholder_text="Digite o nome",width=300); entrar_busca.pack(pady=10)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=300); textbox.pack(pady=20)

    # def buscar():
    #     textbox.delete("0.0","end")
    #     cursor.execute("SELECT * FROM alunos WHERE nome LIKE %s",('%'+entrar_busca.get()+'%',))
    #     for a in cursor.fetchall():
    #         textbox.insert("end",f"\nID:{a[0]}\nNome:{a[1]}\nIdade:{a[2]}\nTurma:{a[3]}\nNotas:{a[4]}\nMédia:{a[5]}\nSituação:{a[6]}\n")

    # ctk.CTkButton(frame_principal,text="Buscar",width=250,command=buscar).pack(pady=10)
    # ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal_admin).pack()

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

    ctk.CTkButton(frame_principal,text="Entrar",width=450,command=fazer_login).pack(pady=20)

    



tela_login()
app.mainloop()
