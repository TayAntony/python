print('Gerador de PA!')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{pt} → ', end='')
        pt += r
        cont += 1
    print('Pausa')
    mais = int(input('Quer ver mais quantos termos? '))
print(f'Progressão finalizada com {total} termos mostrados!')
