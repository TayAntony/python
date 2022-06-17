import inquirer

perguntas = [
    inquirer.List(
        'escolha',
        message = 'MENU',
        choices = ['Adicionar novo cadastro', 'Logar como ADM', 'Listar cadastros']
    )
]

respostas = inquirer.prompt(perguntas)
print(respostas['escolha'])
