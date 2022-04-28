print('------ BOLETIM ------')
alunos = []
ficha = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    ficha.append([nome, [n1, n2], media])
    continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if continuar in 'N':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>5}')
print('-'*40)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>5.1f}')
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        break
    if mostrar <= len(ficha) - 1:
        print(f'Notas de {ficha[mostrar][0]} são {ficha[mostrar][1]}')
print('<<< VOLTE SEMPRE >>>')
