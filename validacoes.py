from datetime import datetime

def validar_nome(nome):
    '''Valida nomes de alunos, professores e de avaliações'''
    if not nome.strip():
        print("Nome inválido.")
        return False
    for n in nome:
        if n.isdigt():
            print("Nome inválido.")
            return False
    return True

def validar_idade(idade):
    '''Valida idade de alunos e professores'''
    try:
        idade = int(idade)
    except:
        print("Idade inválida.")
        return False
    if idade < 13 or idade > 150:
        print("Idade inválida.")
        return False
    return True

def validar_data(data, turma_abertura): 
    try:
        data = datetime.strptime(data, "%Y/%m/%d").date()
        hoje = datetime.now().date()

        if data > hoje:
            return False
        if data < turma_abertura:
            return False
        
        return True
    except:
        print("Data inválida.")
        return False