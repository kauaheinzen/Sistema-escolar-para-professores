import customtkinter as ctk
from tkinter import messagebox
from funcoes_SQL import *
from validacoes import *


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("1920x1080")
app.title("Sistema Escolar")


frame_principal = ctk.CTkFrame(app)
frame_principal.pack(fill="both", expand=True)


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
    ctk.CTkLabel(frame_principal,text="SISTEMA ESCOLAR",font=("Arial",35,"bold")).pack(pady=40)
    ctk.CTkButton(frame_principal,text="Cadastrar Aluno",width=300,height=50,command=tela_cadastrar_aluno).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Listar Alunos",width=300,height=50,command=tela_listar_alunos).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Atualizar Aluno",width=300,height=50,command=tela_atualizar_aluno).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Desativar/Reativar Aluno",width=300,height=50,fg_color="red",command=tela_desativar_aluno).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Buscar Aluno",width=300,height=50,command=tela_buscar_aluno).pack(pady=10)
    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_login).place(x=50, y=50)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)
    


def tela_cadastrar_aluno():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="CADASTRAR ALUNO",font=("Arial",30,"bold")).pack(pady=20)
    entrar_nome=ctk.CTkEntry(frame_principal,placeholder_text="Nome do aluno",width=300); entrar_nome.pack(pady=10)
    entrar_idade=ctk.CTkEntry(frame_principal,placeholder_text="Idade",width=300); entrar_idade.pack(pady=10)
    entrar_turma=ctk.CTkEntry(frame_principal,placeholder_text="Turma",width=300); entrar_turma.pack(pady=10)
    entrar_email=ctk.CTkEntry(frame_principal,placeholder_text="E-mail do aluno",width=300); entrar_email.pack(pady=10)
    entrar_nome_resp=ctk.CTkEntry(frame_principal,placeholder_text="Nome do responsável",width=300); entrar_nome_resp.pack(pady=10)
    entrar_email_resp=ctk.CTkEntry(frame_principal,placeholder_text="E-mail do responsável",width=300); entrar_email_resp.pack(pady=10)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)

    def cadastra_aluno():
        ...

    ctk.CTkButton(frame_principal,text="Cadastrar",width=250,command=...).pack(pady=20)
    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal_admin).pack()

def tela_listar_alunos():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="LISTA DE ALUNOS",font=("Arial",30,"bold")).pack(pady=20)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=350); textbox.pack(pady=20)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)

    for a in cursor.fetchall():
        textbox.insert("end",f"\nID:{a[0]}\nNome:{a[1]}\nIdade:{a[2]}\nTurma:{a[3]}\nNotas:{a[4]}\nMédia:{a[5]:.2f}\nSituação:{a[6]}\n----------------\n")

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

    def buscar():
        textbox.delete("0.0","end")
        cursor.execute("SELECT * FROM alunos WHERE nome LIKE %s",('%'+entrar_busca.get()+'%',))
        for a in cursor.fetchall():
            textbox.insert("end",f"\nID:{a[0]}\nNome:{a[1]}\nIdade:{a[2]}\nTurma:{a[3]}\nNotas:{a[4]}\nMédia:{a[5]}\nSituação:{a[6]}\n")

    ctk.CTkButton(frame_principal,text="Buscar",width=250,command=buscar).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal_admin).pack()

def tela_login():
    limpar_frame()
    criar_admin_iniciar()
    ctk.CTkLabel(frame_principal,text="LOGIN",font=("Arial",35,"bold")).pack(pady=40)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)

    entrar_usuario=ctk.CTkEntry(frame_principal,placeholder_text="Usuário",width=300); entrar_usuario.pack(pady=10)
    
    frame_senha = ctk.CTkFrame(frame_principal)
    frame_senha.pack(pady=10)

    entrar_senha = ctk.CTkEntry(frame_senha, placeholder_text="Senha", show="*", width=250)
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
            ctk.CTkLabel(frame_principal,text="Erro, Usuário ou senha incorretos!",width=500,font=("Arial",35,"bold")).pack(pady=40)
        
        else:
            if usuario[1] == "admin":
                limpar_frame()
                tela_login()
                ctk.CTkLabel(frame_principal,text="Login realizado com sucesso",width=500,font=("Arial",35,"bold")).pack(pady=40); app.after(1000, menu_principal_admin)

    ctk.CTkButton(frame_principal,text="Entrar",width=250,command=fazer_login).pack(pady=20)

    



tela_login()
app.mainloop()
