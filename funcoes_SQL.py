import mysql.connector
from mysql.connector import Error

# faça com que o def (criar_admin_iniciar) execute ao iniciar o programa

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


def criar_admin_iniciar():
    '''verifica se existe algum admin, caso não exista, cria um automaticamente'''
    conn = conectar()
    cursor = conn.cursor()

    sql_verificacao = 'SELECT EXISTS (SELECT 1 FROM admin_database)'
    cursor.execute(sql_verificacao,)
    resultado = bool(cursor.fetchone[0])

    if not resultado:
        sql = 'INSERT INTO admin_database (nome_usuario, senha) VALUES (%s, %s)'
        valores = ('admin.escola', '123')
        cursor.execute(sql, valores)
        
        conn.commit()
    cursor.close()
    conn.close()


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


def atualizar_professor(id, item_alterar, alteracao):
    '''atualiza o cadastro de um professor'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'UPDATE professores SET %s = %s WHERE id_professor = %s'
        valores = (item_alterar, alteracao, id)

        cursor.execute(sql, valores)
        conn.commit()
        print(f"{cursor.rowcount()} cadastro(s) alterado(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Alteração cancelada.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def atualizar_aluno(id, item_alterar, alteracao):
    '''atualiza o cadastro de um aluno ou para mudar sua turma'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'UPDATE alunos SET %s = %s WHERE id_aluno = %s'
        valores = (item_alterar, alteracao, id)

        cursor.execute(sql, valores)
        conn.commit()
        print(f"{cursor.rowcount()} cadastro(s) alterado(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Alteração cancelada.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def atualizar_avaliacao(id, item_alterar, alteracao):
    '''atualiza alguma avaliação, como aluno que fez ou nota'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'UPDATE avaliacoes SET %s = %s WHERE id_avaliacao = %s'
        valores = (item_alterar, alteracao, id)

        cursor.execute(sql, valores)
        conn.commit()
        print(f"{cursor.rowcount()} avaliações(s) alterado(s).")

    except Error as e:
        print(f"Ocorreu um erro {e}. Alteração cancelada.")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def desativar_reativar_materia(id, acao):
    '''desativa uma matéria'''
    conn = conectar()
    cursor = conn.cursor()

    if acao == 0:
        sql = 'UPDATE materias SET ativo = %s WHERE id_materia = %s'
        valores = (0, id)
        cursor.execute(sql, valores)

    else:
        sql = 'UPDATE materias SET ativo = %s WHERE id_materia = %s'
        valores = (1, id)
        cursor.execute(sql, valores)
    
    conn.commit()
    cursor.close()
    conn.close()