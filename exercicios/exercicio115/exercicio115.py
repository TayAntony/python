import inquirer
from funcoes import *

perguntas = [
    inquirer.List(
        'escolha',
        message = 'MENU',
        choices = ['Adicionar novo cadastro', 'Logar como ADM', 'Listar cadastros', 'Sair do programa']
    )
]

print('~'*40)
respostas = inquirer.prompt(perguntas)

if respostas['escolha'] == 'Adicionar novo cadastro':
    novo_cadastro()
    while True:
        confirmar = input('As informações estão corretas? [S/N] ').upper().strip()
        if confirmar == 'S':
            print('~~~~~~~~~~~~~ CADASTRO EFETUADO COM SUCESSO ~~~~~~~~~~~~~')
            break
        else:
            novo_cadastro()           
elif respostas['escolha'] == 'Logar como ADM':
    logar_adm()
elif respostas['escolha'] == 'Listar cadastros':
    print(3)
elif respostas['escolha'] == 'Sair do programa':
    sair()
