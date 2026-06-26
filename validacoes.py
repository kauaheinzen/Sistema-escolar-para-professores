from datetime import datetime, date
from funcoes_SQL import *
import re

def validar_nome(nome):
    '''Valida nomes de alunos, professores e de avaliações'''
    if not nome.strip():
        return False
    for n in nome:
        if n.isdigit():
            return False
    return True

def validar_idade(idade):
    '''Valida idade de alunos e professores'''
    try:
        idade = int(idade)
    except:
        return False
    if idade < 13 or idade > 150:
        return False
    return True

def validar_data(data, turma_abertura):
    '''Valida se a data é maior que a de hoje ou se é menor que a data de abertura da turma'''
    try:
        if isinstance(data, str):
            data = datetime.strptime(data.replace("-", "/"), "%Y/%m/%d").date()
        
        hoje = date.today()

        if isinstance(turma_abertura, datetime):
            abertura_objeto = turma_abertura.date()

        elif isinstance(turma_abertura, datetime.date):
            abertura_objeto = turma_abertura

        else:
            abertura_limpa = str(turma_abertura)[:10].replace("-", "/")
            abertura_objeto = datetime.strptime(abertura_limpa, "%Y/%m/%d").date()

        if data > hoje:
            return False

        if data < abertura_objeto:
            return False
        
        return data.strftime("%Y-%m-%d")
    except Exception as e:
        print (e)
        return False

def validar_adm(nome, senha):
    '''Verifica se o usuário e senha do admin estão corretos'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql_usuario = 'SELECT nome_usuario FROM admin_database'
        cursor.execute(sql_usuario,)
        nomes_adm = cursor.fetchall()

        for nomes in nomes_adm:
            for n in nomes:
                if n == nome:
                    sql_senha = 'SELECT senha FROM admin_database WHERE nome_usuario = %s'
                    valor = (n,)
                    cursor.execute(sql_senha, valor)
                    senha_admin = cursor.fetchone()

                    if senha == senha_admin[0]:
                        cursor.close()
                        conn.close()

                        return True
                
        cursor.close()
        conn.close()
        return False
    
    except Error as e:
        print(e)
        cursor.close()
        conn.close()    
        return False
    
def validar_professor(nome, senha):
    '''Verifica se o usuário e senha do professor estão corretos'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql_usuario = 'SELECT nome_usuario FROM professores'
        cursor.execute(sql_usuario,)
        nomes_professor = cursor.fetchall()

        for nomes in nomes_professor:
            for n in nomes:
                if n == nome:
                    sql_senha = 'SELECT senha FROM professores WHERE nome_usuario = %s'
                    valor = (n,)
                    cursor.execute(sql_senha, valor)
                    senha_admin = cursor.fetchone()

                    if senha == senha_admin[0]:
                        cursor.close()
                        conn.close()

                        return True
                
        cursor.close()
        conn.close()
        return False
    
    except Error as e:
        cursor.close()
        conn.close()
        return (False, f"Ocorreu um erro {e}. Login cancelado")
    
def validar_usuario(nome, senha):
    '''valida o login'''
    admin = validar_adm(nome, senha)
    if admin:
        return (True, "admin")
    professor = validar_professor(nome, senha)

    if professor:
        return (True, "professor")
    
    return (False, "Acesso negado")


def validar_id_aluno(id):
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'SELECT 1 FROM alunos WHERE id_aluno = %s'
        cursor.execute(sql, (id,))

        return cursor.fetchone() is not None


    finally:
        cursor.close()
        conn.close()


def validar_id_professor(id):
    '''valida id de alguma conta de professor'''
    conn = conectar()
    cursor = conn.cursor()
    sql = 'SELECT id_professor FROM professores'

    cursor.execute(sql,)
    resultado = cursor.fetchall()

    for professor in resultado:
        if id == professor:
            cursor.close()
            conn.close()
            return True
    
    cursor.close()
    conn.close()
    return False


def validar_nota(nota):
    '''valida a nota de uma avaliação'''
    
    nota_str = str(nota).strip()
    padrao = r"^(10(\.00?)?|[0-9](\.[0-9]{1,2})?)$"
    
    if re.match(padrao, nota_str):
        return True
    return False


def validar_materia_aluno(id):
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'SELECT 1 FROM aluno_materias WHERE fk_id_aluno = %s'
        cursor.execute(sql, (id,))

        return cursor.fetchone() is not None


    finally:
        cursor.close()
        conn.close()


def validar_turma_aluno_professor(id_aluno, id_professor):
    '''valida se o professor da aula para o aluno'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        turma_aluno = ler_turma_aluno(id_aluno)
        turma_professor = ler_turmas_professor(id_professor)

        for turma in turma_professor:
            if turma[0] == turma_aluno[0]:
                return True
            
        return False

    finally:
        cursor.close()
        conn.close()