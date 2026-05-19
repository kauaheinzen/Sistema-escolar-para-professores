import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import time 

conexao = mysql.connector.connect(host="localhost", user="root", password="Senac2026", database="escola_db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, usuario VARCHAR(100) UNIQUE, senha VARCHAR(100))""")
cursor.execute("""CREATE TABLE IF NOT EXISTS alunos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), idade INT, turma VARCHAR(50), notas VARCHAR(200), media FLOAT, situacao VARCHAR(50))""")
conexao.commit()

try:
    cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)", ("admin", "123"))
    conexao.commit()
except:
    pass

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("900x600")
app.title("Sistema Escolar")

frame_principal = ctk.CTkFrame(app)
frame_principal.pack(fill="both", expand=True)

def limpar_frame():
    for widget in frame_principal.winfo_children(): widget.destroy()

def calcular_media(notas):
    lista=[float(n.strip()) for n in notas.split(",") if n.strip()!=""]
    return sum(lista)/len(lista) if lista else 0

def verificar_situacao(media):
    return "Aprovado" if media>=7 else ("Recuperação" if media>=5 else "Reprovado")

def menu_principal():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="SISTEMA ESCOLAR",font=("Arial",35,"bold")).pack(pady=40)
    ctk.CTkButton(frame_principal,text="Cadastrar Aluno",width=300,height=50,command=tela_cadastrar).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Listar Alunos",width=300,height=50,command=tela_listar).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Atualizar Aluno",width=300,height=50,command=tela_atualizar).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Remover Aluno",width=300,height=50,fg_color="red",command=tela_deletar).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Buscar Aluno",width=300,height=50,command=tela_buscar).pack(pady=10)
    ctk.CTkButton(frame_principal,text="←",width=50,height=30,command=tela_login).place(x=50, y=50)
def tela_cadastrar():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="CADASTRAR ALUNO",font=("Arial",30,"bold")).pack(pady=20)

    entrar_nome=ctk.CTkEntry(frame_principal,placeholder_text="Nome",width=300); entrar_nome.pack(pady=10)
    entrar_idade=ctk.CTkEntry(frame_principal,placeholder_text="Idade",width=300); entrar_idade.pack(pady=10)
    entrar_turma=ctk.CTkEntry(frame_principal,placeholder_text="Turma",width=300); entrar_turma.pack(pady=10)
    entrar_notas=ctk.CTkEntry(frame_principal,placeholder_text="Notas Ex: 7,8,10",width=300); entrar_notas.pack(pady=10)
    def salvar():
        nome, idade, turma, notas = entrar_nome.get(), entrar_idade.get(), entrar_turma.get(), entrar_notas.get()
        if nome=="" or idade=="" or turma=="": return messagebox.showerror("Erro","Preencha todos os campos!")
        media=calcular_media(notas); situacao=verificar_situacao(media)

        cursor.execute("""INSERT INTO alunos (nome,idade,turma,notas,media,situacao) VALUES (%s,%s,%s,%s,%s,%s)""",
                       (nome,idade,turma,notas,media,situacao))
        conexao.commit()
        messagebox.showinfo("Sucesso","Aluno cadastrado!")

    
    
    ctk.CTkButton(frame_principal,text="Salvar",width=250,command=salvar).pack(pady=20)
    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal).pack()

def tela_listar():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="LISTA DE ALUNOS",font=("Arial",30,"bold")).pack(pady=20)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=350); textbox.pack(pady=20)

    cursor.execute("SELECT * FROM alunos")
    for a in cursor.fetchall():
        textbox.insert("end",f"\nID:{a[0]}\nNome:{a[1]}\nIdade:{a[2]}\nTurma:{a[3]}\nNotas:{a[4]}\nMédia:{a[5]:.2f}\nSituação:{a[6]}\n----------------\n")

    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal).pack(pady=10)

def tela_atualizar():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="ATUALIZAR ALUNO",font=("Arial",30,"bold")).pack(pady=20)

    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="ID",width=300); entrar_id.pack(pady=10)
    entrar_nome=ctk.CTkEntry(frame_principal,placeholder_text="Novo Nome",width=300); entrar_nome.pack(pady=10)
    entrar_idade=ctk.CTkEntry(frame_principal,placeholder_text="Nova Idade",width=300); entrar_idade.pack(pady=10)
    entrar_turma=ctk.CTkEntry(frame_principal,placeholder_text="Nova Turma",width=300); entrar_turma.pack(pady=10)
    entrar_notas=ctk.CTkEntry(frame_principal,placeholder_text="Novas Notas",width=300); entrar_notas.pack(pady=10)

    
    
    
    
    def atualizar():
        media=calcular_media(entrar_notas.get()); situacao=verificar_situacao(media)
        cursor.execute("""UPDATE alunos SET nome=%s,idade=%s,turma=%s,notas=%s,media=%s,situacao=%s WHERE id=%s""",
                       (entrar_nome.get(),entrar_idade.get(),entrar_turma.get(),entrar_notas.get(),media,situacao,entrar_id.get()))
        conexao.commit()
        messagebox.showinfo("Sucesso","Aluno atualizado!")

    ctk.CTkButton(frame_principal,text="Atualizar",width=250,command=atualizar).pack(pady=20)
    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal).pack()

def tela_deletar():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="REMOVER ALUNO",font=("Arial",30,"bold")).pack(pady=20)

    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="ID do aluno",width=300); entrar_id.pack(pady=20)

    def remover():
        cursor.execute("DELETE FROM alunos WHERE id=%s",(entrar_id.get(),))
        conexao.commit()
        messagebox.showinfo("Sucesso","Aluno removido!")

    ctk.CTkButton(frame_principal,text="Remover",width=250,fg_color="red",command=remover).pack(pady=20)
    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal).pack()

def tela_buscar():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="BUSCAR ALUNO",font=("Arial",30,"bold")).pack(pady=20)

    entrar_busca=ctk.CTkEntry(frame_principal,placeholder_text="Digite o nome",width=300); entrar_busca.pack(pady=10)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=300); textbox.pack(pady=20)

    def buscar():
        textbox.delete("0.0","end")
        cursor.execute("SELECT * FROM alunos WHERE nome LIKE %s",('%'+entrar_busca.get()+'%',))
        for a in cursor.fetchall():
            textbox.insert("end",f"\nID:{a[0]}\nNome:{a[1]}\nIdade:{a[2]}\nTurma:{a[3]}\nNotas:{a[4]}\nMédia:{a[5]}\nSituação:{a[6]}\n")

    ctk.CTkButton(frame_principal,text="Buscar",width=250,command=buscar).pack(pady=10)
    ctk.CTkButton(frame_principal,text="Voltar",width=250,command=menu_principal).pack()

def tela_login():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="LOGIN",font=("Arial",35,"bold")).pack(pady=40)

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
        cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND senha=%s",(entrar_usuario.get(),entrar_senha.get()))
        if cursor.fetchone(): limpar_frame, tela_login(), ctk.CTkLabel(frame_principal,text="Login realizado com sucesso",width=500,font=("Arial",35,"bold")).pack(pady=40); app.after(1000, menu_principal)
        else: limpar_frame, tela_login(), ctk.CTkLabel(frame_principal,text="Erro, Usuário ou senha incorretos!",width=500,font=("Arial",35,"bold")).pack(pady=40);

    ctk.CTkButton(frame_principal,text="Entrar",width=250,command=fazer_login).pack(pady=20)
    ctk.CTkLabel(frame_principal,text="Usuário: admin | Senha: 123").pack()

    



tela_login()
app.mainloop()
