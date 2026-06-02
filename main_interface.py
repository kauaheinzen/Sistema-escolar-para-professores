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
        global turma_aplicada
        turma_aplicada = id

    def cadastra_aluno():
        cadastro = cadastrar_alunos(entrar_nome.get(), entrar_idade.get(), entrar_email.get(), turma_aplicada, entrar_nome_resp.get(), entrar_email_resp.get())
        if not cadastro:
            ctk.CTkLabel(frame_principal, text="ALUNO CADASTRADO", font=("Arial",30,"bold")).grid(row=0, column=1, pady=30)
        else:
            ctk.CTkLabel(frame_principal, text=cadastro, font=("Arial",30,"bold")).grid(row=0, column=1, pady=30)
        
        app.after(1500, menu_principal_admin)



    def cadastro_aluno():
        limpar_frame()
        global entrar_nome; global entrar_idade; global entrar_email; global entrar_nome_resp; global entrar_email_resp
        ctk.CTkLabel(frame_principal,text="CADASTRAR ALUNO",font=("Arial",45,"bold")).grid(row=0, column=1, pady=40)
        entrar_nome=ctk.CTkEntry(frame_principal,placeholder_text="Nome do aluno",width=300, height=30); entrar_nome.grid(row=1, column=1, pady=10)
        entrar_idade=ctk.CTkEntry(frame_principal,placeholder_text="Idade",width=300, height=30); entrar_idade.grid(row=2, column=1, pady=10)
        entrar_email=ctk.CTkEntry(frame_principal,placeholder_text="E-mail do aluno",width=300, height=30); entrar_email.grid(row=3, column=1, pady=10)
        entrar_nome_resp=ctk.CTkEntry(frame_principal,placeholder_text="Nome do responsável",width=300, height=30); entrar_nome_resp.grid(row=4, column=1, pady=10)
        entrar_email_resp=ctk.CTkEntry(frame_principal,placeholder_text="E-mail do responsável",width=300, height=30); entrar_email_resp.grid(row=5, column=1, pady=10)
        ctk.CTkButton(frame_principal,text="Cadastrar",width=250, height=50,command=cadastra_aluno).grid(row=7, column=1, pady=10)
        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_login).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    def executar_cadastro():
        mudar_id(turma[0])
        cadastro_aluno()


    def tela_turmas_cadastro():
        limpar_frame()
        turmas = ler_turmas()
        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO ALUNO",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(3)
            app.after(0, menu_principal_admin)

        else:
            global turma
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=executar_cadastro).grid(row=turma[0], column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=executar_cadastro).grid(row=turma[0] - 5, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=executar_cadastro).grid(row=turma[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=executar_cadastro).grid(row=turma[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_login).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")


    tela_turmas_cadastro()
        

def tela_listar_alunos():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="LISTA DE ALUNOS",font=("Arial",45,"bold")).pack(pady=20)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=350); textbox.pack(pady=20)
    ctk.CTkButton(frame_principal,text="←",width=250,command=menu_principal_admin).place(x=50, y=50)
    botao_alterar = ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).place(x=1800,y=50)
    alunos = ler_alunos()
    if not alunos:
        ctk.CTkLabel(frame_principal,text="NÃO HÁ ALUNOS CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).place(x=600, y=700) 
        app.after(1500, menu_principal_admin)

    else:
        for aluno in alunos:
            textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]} | IDADE: {aluno[2]} | EMAIL: {aluno[3]} | TURMA: {aluno[4]} | RESPONSÁVEL: {aluno[5]} | EMAIL DO RESPONSÁVEL: {aluno[6]}")


def tela_atualizar_aluno():
    limpar_frame()


    def executar_atualizacao():
        global id_turma
        id_turma = 0
        id_turma = (turma[0])
        atualizar()


    def muda_opcao(opcao):
        global item
        global entrar_item

        item = opcao

        if not item:
            None
        else:
            entrar_item=ctk.CTkEntry(frame_principal,placeholder_text=f"Novo(a) {item}",width=300)

            try:
                entrar_item.destroy()
            except:
                None

            entrar_item.grid(row=5, column=1, pady=10)

    def tela_muda_turma():
        limpar_frame()
        turmas = ler_turmas()
        ctk.CTkLabel(frame_principal,text="SELECIONE A TURMA DO ALUNO",width=300, font=("Arial",50,"bold")).grid(row=0, column=0, columnspan=3, pady=(40, 20), sticky="n")

        if not turmas:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ TURMAS CADASTRADAS",width=250, text_color="red", font=("Arial",35,"bold")).grid(row=1, column=1, pady=200) 
            app.update()

            sleep(3)
            app.after(0, tela_atualizar_aluno)

        else:
            global turma
            for turma in turmas:
                if turma[0] < 6:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=executar_atualizacao).grid(row=turma[0], column=0, padx=100, pady=50, stick="nw")
                elif turma[0] < 11:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=executar_atualizacao).grid(row=turma[0] - 5, column=1, pady=50)
                elif turma[0] < 16:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=executar_atualizacao).grid(row=turma[0] - 10, column=2, padx=100, pady=50, stick="ne")
                else:
                    botao_turma[turma[0]] = ctk.CTkButton(frame_principal, text=turma[1], width=350, height=40, font=("Arial", 25), command=executar_atualizacao).grid(row=turma[0] - 15, column=3, padx=100, pady=50, stick="ne")


        ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_login).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
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
    ctk.CTkButton(frame_principal, text="←", width=50, height=30, command=tela_login).grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    ctk.CTkButton(frame_principal, text="☀️", width=50, command=mudar_tema).grid(row=0, column=5, padx=20, pady=20, sticky="nw")
    entrar_id=ctk.CTkEntry(frame_principal,placeholder_text="MATRÍCULA DO ALUNO",width=300); entrar_id.grid(row=1, column=1, pady=10)



    def atualizar():
        if id_turma != 0:
            atualizar_aluno(entrar_id.get(), "fk_id_turma", id_turma)
            ctk.CTkLabel(frame_principal,text="Cadastro Atualizado", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
        else:
            match item:
                case "nome":
                    valida=validar_nome(entrar_item.get())
                    if valida:
                        atualiza=atualizar_aluno(entrar_id.get(), "nome_aluno", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                        else:
                            ctk.CTkLabel(frame_principal,text="Cadastro Atualizado", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Nome Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case "idade":
                    valida=validar_idade(entrar_item.get())
                    if valida:
                        atualiza=atualizar_aluno(entrar_id.get(), "idade_aluno", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                        else:
                            ctk.CTkLabel(frame_principal,text="Cadastro Atualizado", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Idade Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case "e-mail":
                    atualiza=atualizar_aluno(entrar_id.get(), "email_aluno", entrar_item.get())
                    if atualiza:
                        ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Cadastro Atualizado", width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)


                case "nome do responsável":
                    valida=validar_nome(entrar_item.get())
                    if valida:
                        atualiza=atualizar_aluno(entrar_id.get(), "nome_responsavel", entrar_item.get())
                        if atualiza:
                            ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                        else:
                            ctk.CTkLabel(frame_principal,text="Cadastro Atualizado",width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Nome Inválido", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)

                
                case "e-mail do responsável":
                    atualiza=atualizar_aluno(entrar_id.get(), "email_responsavel", entrar_item.get())
                    if atualiza:
                        ctk.CTkLabel(frame_principal,text=valida[1], width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                    else:
                        ctk.CTkLabel(frame_principal,text="Cadastro Atualizado",width=250, font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
                

                case default:
                    ctk.CTkLabel(frame_principal,text="Erro ao Realizar Cadastro, por favor preencha os dados corretamente", width=250, text_color="red", font=("Arial",35,"bold")).grid(row=7, column=1, pady=50)
        

        app.after(1500, menu_principal_admin)

    ctk.CTkButton(frame_principal,text="Atualizar Aluno",width=450,command=atualizar).grid(row=6, column=1, pady=40)



def tela_desativar_aluno():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="Desativar ALUNO",font=("Arial",30,"bold")).grid(row=0,column=0,columnspan=3,pady=20)
    ctk.CTkButton(frame_principal,text="←",width=250,command=menu_principal_admin).grid(row=0,column=0,sticky="w",padx=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).grid(row=0,column=2,sticky="e",padx=20)

    entrar_id_desativar=ctk.CTkEntry(frame_principal,placeholder_text="ID do aluno",width=300); entrar_id_desativar.grid(row=1,column=0,columnspan=3,pady=20)

    ctk.CTkButton(frame_principal,text="Desativar Aluno",width=250,fg_color="red",command=lambda: desativar_reativar_aluno(entrar_id_desativar, 0)).grid(row=2,column=0,columnspan=3,pady=20)


def tela_reativar_aluno():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="Reativar ALUNO",font=("Arial",30,"bold")).grid(row=0,column=0,columnspan=3,pady=20)
    ctk.CTkButton(frame_principal,text="←",width=250,command=menu_principal_admin).grid(row=0,column=0,sticky="w",padx=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).grid(row=0,column=2,sticky="e",padx=20)

    entrar_id_ativar=ctk.CTkEntry(frame_principal,placeholder_text="ID do aluno",width=300); entrar_id_ativar.grid(row=1,column=0,columnspan=3,pady=20)

    ctk.CTkButton(frame_principal,text="Reativar Aluno",width=250,fg_color="red",command=lambda: desativar_reativar_aluno(entrar_id_ativar, 1)).grid(row=2,column=0,columnspan=3,pady=20)


def tela_buscar_aluno():
    limpar_frame()
    ctk.CTkLabel(frame_principal,text="BUSCAR ALUNO",font=("Arial",30,"bold")).grid(row=0,column=0,columnspan=3,pady=20)
    ctk.CTkButton(frame_principal,text="←",width=250,command=menu_principal_admin).grid(row=0,column=0,sticky="w",padx=20)
    ctk.CTkButton(frame_principal,text="☀️",width=50,command=mudar_tema).grid(row=0,column=2,sticky="e",padx=20)

    entrar_busca=ctk.CTkEntry(frame_principal,placeholder_text="Digite o nome",width=300); entrar_busca.grid(row=1,column=0,columnspan=3,pady=10)
    textbox=ctk.CTkTextbox(frame_principal,width=700,height=300); textbox.grid(row=2,column=0,columnspan=3,pady=20)

    def buscar():
        global alunos
        alunos = buscar_alunos(entrar_busca.get())

        if not alunos:
            ctk.CTkLabel(frame_principal,text="NÃO HÁ ALUNOS CADASTRADOS",width=250, text_color="red", font=("Arial",45,"bold")).place(x=600, y=700) 
            app.after(1500, menu_principal_admin)

        else:
            for aluno in alunos:
                textbox.insert("end", f"MATRÍCULA: {aluno[0]} | NOME: {aluno[1]} | IDADE: {aluno[2]} | EMAIL: {aluno[3]} | TURMA: {aluno[4]} | RESPONSÁVEL: {aluno[5]} | EMAIL DO RESPONSÁVEL: {aluno[6]}")

    ctk.CTkButton(frame_principal,text="Buscar",width=250,command=buscar).pack(pady=10)


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
