lista = [[], []]
for v in range (1,8):
    valores = int(input(f'Digite o {v}º valor: '))
    if valores%2==0:
        lista[0].append(valores)
    else:
        lista[1].append(valores)
print('='*40)
lista[0].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
lista[1].sort()
print(f'Os valores ímpares digitados foram: {lista[1]}')
