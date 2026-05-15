
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Senac2026",
    database="escola_db"
)

cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100) UNIQUE,
    senha VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    turma VARCHAR(50),
    notas VARCHAR(200),
    media FLOAT,
    situacao VARCHAR(50)
)
""")

conexao.commit()


try:
    cursor.execute("""
    INSERT INTO usuarios (usuario, senha)
    VALUES (%s, %s)
    """, ("admin", "123"))

    conexao.commit()

except:
    pass


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
# APP


app = ctk.CTk()
app.geometry("900x600")
app.title("Sistema Escolar")

# ==========================================
# FRAME PRINCIPAL
# ==========================================

frame_principal = ctk.CTkFrame(app)
frame_principal.pack(fill="both", expand=True)

# ==========================================
# FUNÇÕES
# ==========================================

def limpar_frame():

    for widget in frame_principal.winfo_children():
        widget.destroy()

# ==========================================
# MÉDIA
# ==========================================

def calcular_media(notas):

    lista = []

    for nota in notas.split(","):

        nota = nota.strip()

        if nota != "":
            lista.append(float(nota))

    if len(lista) == 0:
        return 0

    return sum(lista) / len(lista)

# ==========================================
# SITUAÇÃO
# ==========================================

def verificar_situacao(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperação"

    else:
        return "Reprovado"

# ==========================================
# MENU
# ==========================================

def menu_principal():

    limpar_frame()

    titulo = ctk.CTkLabel(
        frame_principal,
        text="SISTEMA ESCOLAR",
        font=("Arial", 35, "bold")
    )

    titulo.pack(pady=40)

    btn_cadastrar = ctk.CTkButton(
        frame_principal,
        text="Cadastrar Aluno",
        width=300,
        height=50,
        command=tela_cadastrar
    )

    btn_cadastrar.pack(pady=10)

    btn_listar = ctk.CTkButton(
        frame_principal,
        text="Listar Alunos",
        width=300,
        height=50,
        command=tela_listar
    )

    btn_listar.pack(pady=10)

    btn_atualizar = ctk.CTkButton(
        frame_principal,
        text="Atualizar Aluno",
        width=300,
        height=50,
        command=tela_atualizar
    )

    btn_atualizar.pack(pady=10)

    btn_deletar = ctk.CTkButton(
        frame_principal,
        text="Remover Aluno",
        width=300,
        height=50,
        fg_color="red",
        command=tela_deletar
    )

    btn_deletar.pack(pady=10)

    btn_buscar = ctk.CTkButton(
        frame_principal,
        text="Buscar Aluno",
        width=300,
        height=50,
        command=tela_buscar
    )

    btn_buscar.pack(pady=10)

# ==========================================
# CADASTRAR
# ==========================================

def tela_cadastrar():

    limpar_frame()

    titulo = ctk.CTkLabel(
        frame_principal,
        text="CADASTRAR ALUNO",
        font=("Arial", 30, "bold")
    )

    titulo.pack(pady=20)

    entry_nome = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Nome",
        width=300
    )

    entry_nome.pack(pady=10)

    entry_idade = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Idade",
        width=300
    )

    entry_idade.pack(pady=10)

    entry_turma = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Turma",
        width=300
    )

    entry_turma.pack(pady=10)

    entry_notas = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Notas Ex: 7,8,10",
        width=300
    )

    entry_notas.pack(pady=10)

    def salvar():

        nome = entry_nome.get()
        idade = entry_idade.get()
        turma = entry_turma.get()
        notas = entry_notas.get()

        if nome == "" or idade == "" or turma == "":

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )

            return

        media = calcular_media(notas)
        situacao = verificar_situacao(media)

        cursor.execute("""
        INSERT INTO alunos
        (nome, idade, turma, notas, media, situacao)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nome,
            idade,
            turma,
            notas,
            media,
            situacao
        ))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Aluno cadastrado!"
        )

    btn_salvar = ctk.CTkButton(
        frame_principal,
        text="Salvar",
        width=250,
        command=salvar
    )

    btn_salvar.pack(pady=20)

    btn_voltar = ctk.CTkButton(
        frame_principal,
        text="Voltar",
        width=250,
        command=menu_principal
    )

    btn_voltar.pack()

# ==========================================
# LISTAR
# ==========================================

def tela_listar():

    limpar_frame()

    titulo = ctk.CTkLabel(
        frame_principal,
        text="LISTA DE ALUNOS",
        font=("Arial", 30, "bold")
    )

    titulo.pack(pady=20)

    textbox = ctk.CTkTextbox(
        frame_principal,
        width=700,
        height=350
    )

    textbox.pack(pady=20)

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    for aluno in alunos:

        texto = f"""
ID: {aluno[0]}
Nome: {aluno[1]}
Idade: {aluno[2]}
Turma: {aluno[3]}
Notas: {aluno[4]}
Média: {aluno[5]:.2f}
Situação: {aluno[6]}
----------------------------------------
"""

        textbox.insert("end", texto)

    btn_voltar = ctk.CTkButton(
        frame_principal,
        text="Voltar",
        width=250,
        command=menu_principal
    )

    btn_voltar.pack(pady=10)

# ==========================================
# ATUALIZAR
# ==========================================

def tela_atualizar():

    limpar_frame()

    titulo = ctk.CTkLabel(
        frame_principal,
        text="ATUALIZAR ALUNO",
        font=("Arial", 30, "bold")
    )

    titulo.pack(pady=20)

    entry_id = ctk.CTkEntry(
        frame_principal,
        placeholder_text="ID",
        width=300
    )

    entry_id.pack(pady=10)

    entry_nome = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Novo Nome",
        width=300
    )

    entry_nome.pack(pady=10)

    entry_idade = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Nova Idade",
        width=300
    )

    entry_idade.pack(pady=10)

    entry_turma = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Nova Turma",
        width=300
    )

    entry_turma.pack(pady=10)

    entry_notas = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Novas Notas",
        width=300
    )

    entry_notas.pack(pady=10)

    def atualizar():

        media = calcular_media(entry_notas.get())
        situacao = verificar_situacao(media)

        cursor.execute("""
        UPDATE alunos
        SET nome=%s,
            idade=%s,
            turma=%s,
            notas=%s,
            media=%s,
            situacao=%s
        WHERE id=%s
        """, (
            entry_nome.get(),
            entry_idade.get(),
            entry_turma.get(),
            entry_notas.get(),
            media,
            situacao,
            entry_id.get()
        ))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Aluno atualizado!"
        )

    btn_atualizar = ctk.CTkButton(
        frame_principal,
        text="Atualizar",
        width=250,
        command=atualizar
    )

    btn_atualizar.pack(pady=20)

    btn_voltar = ctk.CTkButton(
        frame_principal,
        text="Voltar",
        width=250,
        command=menu_principal
    )

    btn_voltar.pack()

# ==========================================
# DELETAR
# ==========================================

def tela_deletar():

    limpar_frame()

    titulo = ctk.CTkLabel(
        frame_principal,
        text="REMOVER ALUNO",
        font=("Arial", 30, "bold")
    )

    titulo.pack(pady=20)

    entry_id = ctk.CTkEntry(
        frame_principal,
        placeholder_text="ID do aluno",
        width=300
    )

    entry_id.pack(pady=20)

    def remover():

        cursor.execute("""
        DELETE FROM alunos
        WHERE id=%s
        """, (entry_id.get(),))

        conexao.commit()

        messagebox.showinfo(
            "Sucesso",
            "Aluno removido!"
        )

    btn_remover = ctk.CTkButton(
        frame_principal,
        text="Remover",
        width=250,
        fg_color="red",
        command=remover
    )

    btn_remover.pack(pady=20)

    btn_voltar = ctk.CTkButton(
        frame_principal,
        text="Voltar",
        width=250,
        command=menu_principal
    )

    btn_voltar.pack()

# ==========================================
# BUSCAR
# ==========================================

def tela_buscar():

    limpar_frame()

    titulo = ctk.CTkLabel(
        frame_principal,
        text="BUSCAR ALUNO",
        font=("Arial", 30, "bold")
    )

    titulo.pack(pady=20)

    entry_busca = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Digite o nome",
        width=300
    )

    entry_busca.pack(pady=10)

    textbox = ctk.CTkTextbox(
        frame_principal,
        width=700,
        height=300
    )

    textbox.pack(pady=20)

    def buscar():

        textbox.delete("0.0", "end")

        cursor.execute("""
        SELECT * FROM alunos
        WHERE nome LIKE %s
        """, ('%' + entry_busca.get() + '%',))

        alunos = cursor.fetchall()

        for aluno in alunos:

            texto = f"""
ID: {aluno[0]}
Nome: {aluno[1]}
Idade: {aluno[2]}
Turma: {aluno[3]}
Notas: {aluno[4]}
Média: {aluno[5]:.2f}
Situação: {aluno[6]}
----------------------------------------
"""

            textbox.insert("end", texto)

    btn_buscar = ctk.CTkButton(
        frame_principal,
        text="Buscar",
        width=250,
        command=buscar
    )

    btn_buscar.pack(pady=10)

    btn_voltar = ctk.CTkButton(
        frame_principal,
        text="Voltar",
        width=250,
        command=menu_principal
    )

    btn_voltar.pack()

def tela_login():

    limpar_frame()

    titulo = ctk.CTkLabel(
        frame_principal,
        text="LOGIN",
        font=("Arial", 35, "bold")
    )

    titulo.pack(pady=40)

    entry_usuario = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Usuário",
        width=300
    )

    entry_usuario.pack(pady=10)

    entry_senha = ctk.CTkEntry(
        frame_principal,
        placeholder_text="Senha",
        show="*",
        width=300
    )

    entry_senha.pack(pady=10)

    def fazer_login():

        cursor.execute("""
        SELECT * FROM usuarios
        WHERE usuario=%s AND senha=%s
        """, (
            entry_usuario.get(),
            entry_senha.get()
        ))

        resultado = cursor.fetchone()

        if resultado:

            messagebox.showinfo(
                "Sucesso",
                "Login realizado!"
            )

            menu_principal()

        else:

            messagebox.showerror(
                "Erro",
                "Usuário ou senha incorretos!"
            )

    btn_login = ctk.CTkButton(
        frame_principal,
        text="Entrar",
        width=250,
        command=fazer_login
    )

    btn_login.pack(pady=20)

    info = ctk.CTkLabel(
        frame_principal,
        text="Usuário: admin | Senha: 123"
    )

    info.pack()

# ==========================================
# INICIAR
# ==========================================

tela_login()

app.mainloop()