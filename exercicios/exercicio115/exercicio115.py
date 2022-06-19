import inquirer
from funcoes import *

perguntas = [
    inquirer.List(
        'escolha',
        message = 'MENU',
        choices = ['Adicionar novo cadastro', 'Logar como ADM', 'Listar cadastros', 'Sair do programa']
    )
]

cabecalho('\33[1m\33[34mSISTEMA CADASTRAL    v1.0\33[m')
respostas = inquirer.prompt(perguntas)

if respostas['escolha'] == 'Adicionar novo cadastro':
    novo_cadastro()

elif respostas['escolha'] == 'Logar como ADM':
    logar_adm()

elif respostas['escolha'] == 'Listar cadastros':
    print(3)

elif respostas['escolha'] == 'Sair do programa':
    sair()

