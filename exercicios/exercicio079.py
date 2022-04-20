num = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor duplicado. Escolha outro...')
    continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if continuar in 'N':
        break
print('*-'*30)
num.sort()
print(f'Você digitou os valores {num}')
