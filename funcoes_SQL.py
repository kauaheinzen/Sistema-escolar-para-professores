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


def cadastrar_alunos(nome, idade, email, turma, nome_responsavel = '', email_responvel = ''):
    '''Cadastra novos alunos'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO alunos (nome_alunos, idade_aluno, email_aluno, fk_id_turma, nome_responsavel,email_responsavel) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (nome, idade, email, turma, nome_responsavel, email_responvel)

        cursor.execute(sql, valores)
        conn.commit()
        print(f"{cursor.rowcount()} aluno(s) cadastrado(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Cadastro cancelado.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def registrar_avaliacao(data, aluno, nome_avaliacao, nota):
    '''Registra avaliações'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO avaliacoes (data_avaliacao, fk_id_alunos, nome_avaliacao, nota) VALUES (%s, %s, %s, %s)'
        valores = (data, aluno, nome_avaliacao, nota)

        cursor.execute(sql, valores)
        conn.commit()
        print("Avaliação registrada")

    except Error as e:
        print(f"Ocorreu um erro {e}. Registro da avaliação cancelado.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()

    
def atualizar_turma(id, nome, materias):
    '''atualiza o ano da turma, ex: do 1° pro 2° ano e muda matérias'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'UPDATE turmas SET nome_turma = %s, fk_id_materias = %s WHERE id_turma = %s'
        valores = (nome, materias, id)

        cursor.execute(sql, valores)
        conn.commit()
        print(f"{cursor.rowcount()} turma(s) atualizada(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Atualização cancelada.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def atualizar_professor(id, item_alterar, alteracao):
    '''atualiza o cadastro de um professor'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'UPDATE professores SET %s = %s WHERE id_professor = %s'
        valores = (item_alterar, alteracao, id)

        cursor.execute(sql, valores)
        conn.commit()
        print(f"{cursor.rowcount()} cadastro(s) de professor(es) alterado(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Alteração cancelada.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()