import mysql.connector
from mysql.connector import Error

def conectar():
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

def cadastrar_turma(nome):
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO turmas (nome_turma) VALUES (%s)'
        valor = (nome,)

        cursor.execute(sql, valor)
        conn.commit()
        print(f"{cursor.rowcount()} aluno(s) cadastrado(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Cadastro cancelado.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()

