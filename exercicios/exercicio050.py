soma = 0
cont = 0
print('='*50)
for num in range(1, 7):
    num = int(input(f'Digite o {num}° valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} valores pares em que a soma é igual a {soma}.')
