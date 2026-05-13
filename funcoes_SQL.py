import mysql.connector
from mysql.connector import Error

def conectar():
    '''Faz a conexão entre o Python e o MySQL'''
    try:
        conexao = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'Senac2026',
            database = 'escola'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


def cadastrar_materias(nome_materia):
    '''Cadastra novas matérias'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO materias (nome_materia) VALUES (%s)'
        valor = (nome_materia,)

        cursor.execute(sql, valor)
        conn.commit()
        print(f"{cursor.rowcount()} matéria(s) cadastrada(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Cadastro cancelado.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def cadastrar_turma(nome, materias):
    '''Cadastra novas turmas'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO turmas (nome_turma, fk_id_materias) VALUES (%s, %s)'
        valor = (nome, materias)

        cursor.execute(sql, valor)
        conn.commit()
        print(f"{cursor.rowcount()} aluno(s) cadastrado(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Cadastro cancelado.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def cadastrar_professores(nome, idade, email, usuario, senha, materia, turmas):
    '''Cadastra novos professores'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO professores (nome_professor, idade_professor, email_professor nome_usuario, senha, fk_id_materia, fk_id_turmas) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        valores = (nome, idade, email, usuario, senha, materia, turmas)

        cursor.execute(sql, valores)
        conn.commit()
        print(f"{cursor.rowcount()} professor(s) cadastrado(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Cadastro cancelado.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()