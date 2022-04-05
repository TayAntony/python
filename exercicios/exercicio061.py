print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print(f'{pt} → ', end='')
    pt += r
    cont += 1
print('Acabou')
