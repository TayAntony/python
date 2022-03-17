frase = str(input('Digite uma frase: ')).upper().strip()
qntd = str(frase.count('A'))
pp = frase.find('A')+1
up = frase.rfind('A')+1
print(f'A letra A aparece {qntd} vezes na frase.')
print(f'A primeira letra A apareceu na posição {pp}')
print(f'A última letra A apareceu na posição {up}')