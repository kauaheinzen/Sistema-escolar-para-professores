def validar_nome(nome):
    '''Valida nomes de alunos, professores e de avaliações'''
    if not nome.strip():
        return False
    for n in nome:
        if n.isdigt():
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