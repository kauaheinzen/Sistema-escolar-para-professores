# Sistema-escolar-para-professores
Trabalho de escola feito por 3 alunos do primeiro ano do ensino médio + técnico SENAC
## Autores
 
- Filipe Rocha
- Kauã Heinzen
- Pedro Soares
 
---



# Manual de Instalação e Execução do Sistema Escolar

Olá! Neste guia será mostrado como instalar e executar o Sistema Escolar.

## Passo a passo

**1.** Instale o Visual Studio Code (VS Code), caso ainda não tenha:
https://code.visualstudio.com/

**2.** Instale o Python:
https://www.python.org/downloads/

**3.** Abra o VS Code, vá até a aba **Extensões** e instale a extensão **Python**.

**4.** Abra o terminal do VS Code e execute os seguintes comandos:

```bash
pip install mysql-connector
pip install customtkinter
```

Caso ocorra algum erro, execute:

```bash
pip install --upgrade mysql-connector-python
python -m pip install --upgrade pip
```

**5.** Abra o MySQL Workbench e copie o código presente no arquivo **codigosql**, colando-o na área de consultas.

Caso ainda não tenha o MySQL Workbench instalado, faça o download em:
https://www.mysql.com/products/workbench/

**Importante:** defina a senha do usuário **root** como **Senac2026**. Caso prefira utilizar outra senha, altere o valor da variável **Password** no arquivo **funcoes_SQL.py** para a senha escolhida.

**6.** No MySQL Workbench, clique no botão de **Executar** (ícone de raio) para criar o banco de dados e as tabelas.

**7.** Para iniciar o sistema, execute no terminal do VS Code:

```bash
python main_interface.py
```

Ou simplesmente clique no botão **Run Python** do VS Code.

Pronto! O Sistema Escolar estará em funcionamento.
**8.** Login: admin.escola / Senha: 123:
