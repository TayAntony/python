cont = soma = media = n = p = 0
while p != 'N':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    p = input('Quer continuar? [S]/[N] ').upper().strip()[0]
media = soma/cont
print(f'Você digitou {cont} números. A média deles é {media}')
print(f'O maior número é {maior} e o menor é {menor}!')
 