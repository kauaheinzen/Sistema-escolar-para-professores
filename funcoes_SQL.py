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
    resultado = bool(cursor.fetchone()[0])

    if not resultado:
        sql = 'INSERT INTO admin_database (nome_usuario, senha) VALUES (%s, %s)'
        valores = ('admin.escola', '123')
        cursor.execute(sql, valores)
        
        conn.commit()
    cursor.close()
    conn.close()


def cadastrar_materia(nome_materia):
    '''Cadastra novas matérias'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO materias (nome_materia) VALUES (%s)'
        valor = (nome_materia,)

        cursor.execute(sql, valor)
        conn.commit()

    except Error as e:
        conn.rollback()
        return f"Ocorreu um erro {e}. Cadastro cancelado."
    
    finally:
        cursor.close()
        conn.close()


def cadastrar_turma(nome):
    '''Cadastra novas turmas'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO turmas (nome_turma) VALUES (%s)'
        valor = (nome,)

        cursor.execute(sql, valor)
        conn.commit()

    except Error as e:
        conn.rollback()
        return f"Ocorreu um erro {e}. Cadastro cancelado."
    
    finally:
        cursor.close()
        conn.close()


def cadastrar_professores(nome, idade, email, usuario, senha, materia):
    '''Cadastra novos professores'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO professores (nome_professor, idade_professor, email_professor, nome_usuario, senha, fk_id_materia) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (nome, idade, email, usuario, senha, materia)

        cursor.execute(sql, valores)
        conn.commit()

    except Error as e:
        conn.rollback()
        return f"Ocorreu um erro {e}. Cadastro cancelado."
    
    finally:
        cursor.close()
        conn.close()


def cadastrar_alunos(nome, idade, email, turma, nome_responsavel = '', email_responvel = ''):
    '''Cadastra novos alunos'''
    conn = conectar()
    cursor = conn.cursor()

    try:
        sql = 'INSERT INTO alunos (nome_aluno, idade_aluno, email_aluno, fk_id_turma, nome_responsavel,email_responsavel) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (nome, idade, email, turma, nome_responsavel, email_responvel)

        cursor.execute(sql, valores)
        conn.commit()

    except Error as e:
        conn.rollback()
        return f"Ocorreu um erro {e}. Cadastro cancelado."
    
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

    except Error as e:
        conn.rollback()
        return f"Ocorreu um erro {e}. Registro da avaliação cancelado."
    
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

    except Error as e:
        conn.rollback()
        return f"Ocorreu um erro {e}. Alteração cancelada."
    
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

    except Error as e:
        conn.rollback()
        return f"Ocorreu um erro {e}. Atualização cancelada."
    
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

    except Error as e:
        conn.rollback()
        return f"Ocorreu um erro {e}. Alteração cancelada."
    
    finally:
        cursor.close()
        conn.close()


def desativar_reativar_materia(id, acao):
    '''desativa ou reativa uma matéria'''
    try:
        conn = conectar()
        cursor = conn.cursor()

        if acao == 0:
            valores = (0, id)

        else:
            valores = (1, id)
            
        sql = 'UPDATE materias SET ativo = %s WHERE id_materia = %s'
        cursor.execute(sql, valores)
        
        conn.commit()
    
    except:
        conn.rollbacl()
    
    finally:
        cursor.close()
        conn.close()


def desativar_reativar_turma_e_alunos(id, acao):
    '''desativa ou reativa uma turma e todos os seus alunos'''
    conn = conectar()
    cursor = conn.cursor()
    try:
        sql = 'UPDATE turmas SET ativo = %s WHERE id_turma = %s'
        valores = (acao, id[0])
        cursor.execute(sql, valores)

        sql_ver_alunos = 'SELECT id_aluno FROM alunos WHERE fk_id_turma = %s'
        valor = (id,)
        cursor.execute(sql_ver_alunos, valor)
        alunos = cursor.fetchall()

        for aluno in alunos:
            sql_aluno = 'UPDATE alunos SET ativo = %s WHERE id_aluno = %s'
            valores = (acao, aluno[0])
            cursor.execute(sql_aluno, valores)
    
        conn.commit()
        return False

    except Exception as e:
        conn.rollback()
        print(e)
        return e
    
    finally:
        cursor.close()
        conn.close()


def desativar_reativar_professor(id, acao):
    '''desativa ou reativa um professor'''
    try:
        conn = conectar()
        cursor = conn.cursor()

            
        sql = 'UPDATE professores SET ativo = %s WHERE id_professor = %s'
        valores = (acao, id)
        cursor.execute(sql, valores)
        
        conn.commit()
    
    except:
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def desativar_reativar_aluno(id, acao):
    '''desativa ou reativa um aluno'''
    try:
        conn = conectar()
        cursor = conn.cursor()

            
        sql = 'UPDATE alunos SET ativo = %s WHERE id_aluno = %s'
        valores = (acao, id)
        cursor.execute(sql, valores)
        
        conn.commit()
    
    except:
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()
    


def desativar_reativar_avaliacao(id, acao):
    '''desativa ou reativa uma avaliação'''
    try:
        conn = conectar()
        cursor = conn.cursor()

            
        sql = 'UPDATE avaliacoes SET ativo = %s WHERE id_avaliacao = %s'
        valores = (acao, id)
        cursor.execute(sql, valores)
        
        conn.commit()
    
    except:
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


def vincular_turma_materia(turma, materia):
    '''vincula uma turma em uma matéria'''
    conn = conectar()
    cursor = conn.cursor()

        
    sql = 'INSERT INTO turma_materias (fk_id_turma, fk_id_materia) VALUES (%s, %s)'
    valores = (turma, materia)
    cursor.execute(sql, valores)
    
    conn.commit()
    cursor.close()
    conn.close()


def vincular_professor_turma(professor, turma):
    '''vincula um professor em uma turma'''
    conn = conectar()
    cursor = conn.cursor()

        
    sql = 'INSERT INTO professor_turma (fk_id_professor, fk_id_turma) VALUES (%s, %s)'
    valores = (professor, turma)
    cursor.execute(sql, valores)
    
    conn.commit()
    cursor.close()
    conn.close()


def ler_turmas():
    '''mostra todos as turmas'''
    conn = conectar()
    cursor = conn.cursor()

    sql = 'SELECT * FROM turmas'
    cursor.execute(sql,)
    
    turmas = cursor.fetchall()

    cursor.close()
    conn.close()
    return turmas


def ler_materias():
    '''mostra todas as matérias'''
    conn = conectar()
    cursor = conn.cursor()

    sql = 'SELECT * FROM materias'
    cursor.execute(sql,)
    
    materias = cursor.fetchall()

    cursor.close()
    conn.close()
    return materias


def ler_professores():
    '''mostra todos os professores'''
    conn = conectar()
    cursor = conn.cursor()

    sql = 'SELECT * FROM professores'
    cursor.execute(sql,)
    
    professores = cursor.fetchall()

    cursor.close()
    conn.close()
    return professores


def ler_alunos():
    '''mostra todos os alunos'''
    conn = conectar()
    cursor = conn.cursor()

    sql = 'SELECT * FROM alunos'
    cursor.execute(sql,)
    
    alunos = cursor.fetchall()

    cursor.close()
    conn.close()
    return alunos


def buscar_alunos(nome):
    '''busca todos alunos'''
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT * FROM alunos WHERE nome_aluno LIKE %s"
    cursor.execute(sql, (nome,))
    
    alunos = cursor.fetchall()

    cursor.close()
    conn.close()
    return alunos


def ler_id_professor(nome):
    '''retorna o ID do professor'''
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT id_professor FROM professores WHERE nome_professor = %s"
    cursor.execute(sql, (nome,))
    
    professor = cursor.fetchone()

    cursor.close()
    conn.close()
    return professor


def ler_usuarios_professor(usuarios):
    '''retorna o ID do professor'''
    conn = conectar()
    cursor = conn.cursor()
 
    sql = "SELECT id_professor FROM professores WHERE nome_usuario = %s"
    cursor.execute(sql, (usuarios))
   
    professor = cursor.fetchone()
 
    cursor.close()
    conn.close()
    return professor
 
 

def ler_id_materia(nome):
    '''retorna o ID da matéria'''
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT id_materia FROM materias WHERE nome_materia = %s"
    cursor.execute(sql, (nome,))
    
    materia = cursor.fetchone()

    cursor.close()
    conn.close()
    return materia


def ler_id_turma(nome):
    '''retorna o ID da turma'''
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT id_turma FROM turmas WHERE nome_turma = %s"
    cursor.execute(sql, (nome,))
    
    turma = cursor.fetchone()

    cursor.close()
    conn.close()
    return turma


def ler_nome_materia(id):
    '''retorna o nome da matéria'''
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT nome_materia FROM materias WHERE id_materia = %s"
    cursor.execute(sql, (id,))
    
    materia = cursor.fetchone()

    cursor.close()
    conn.close()
    return materia


def ler_id_materia(nome):
    '''retorna o ID da materia'''
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT id_materia FROM materias WHERE nome_materia = %s"
    cursor.execute(sql, (nome,))
    
    materia = cursor.fetchone()

    cursor.close()
    conn.close()
    return materia





def ler_turmas_professor(id_professor):
    '''retorna as turmas vinculadas a um professor'''
    conn = conectar()
    cursor = conn.cursor()

    sql = '''SELECT t.id_turma, t.nome_turma 
              FROM turmas t
              INNER JOIN professor_turma pt ON t.id_turma = pt.fk_id_turma
              WHERE pt.fk_id_professor = %s'''
    cursor.execute(sql, (id_professor,))

    turmas = cursor.fetchall()

    cursor.close()
    conn.close()
    return turmas


def ler_alunos_turma(id_turma):
    '''retorna os alunos de uma turma específica'''
    conn = conectar()
    cursor = conn.cursor()

    sql = 'SELECT * FROM alunos WHERE fk_id_turma = %s'
    cursor.execute(sql, (id_turma,))

    alunos = cursor.fetchall()

    cursor.close()
    conn.close()
    return alunos