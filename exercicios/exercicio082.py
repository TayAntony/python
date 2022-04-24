lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    p = input('Quer continuar? [S/N]: ').upper().strip()
    if p in 'N':
        break
for i, v in enumerate(lista):
    if v%2==0:
        pares.append(v)
    else:
        impares.append(v)
print('*'*30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'Alista de ímpares é: {impares}')
print('=== FIM DO PROGRAMA ===')
