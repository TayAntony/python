from cores import *
print('.-'*20)
print(f'{cores["azul"]}{fx["sublinhado"]}Analisador de triângulos{limpar} ', end='')
print('\U0001F53A')
print('.-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo ', end='')
    if r1==r2==r3:
        print(f'{cores["verde"]}{fx["sublinhado"]}EQUILÁTERO{limpar} ', end='')
        print(' ✔️')
    elif r1==r2 or r2==r3 or r3==r1:
        print(f'{cores["verde"]}{fx["sublinhado"]}ISÓSCELES{limpar}', end='')
        print(' ✔️')
    elif r1!=r2 or r2!=r3 or r3!=r1:
        print(f'{cores["verde"]}{fx["sublinhado"]}ESCALENO{limpar}', end='')
        print(' ✔️')
else:
    print('Os segmentos NÃO podem formar um triângulo! ❌')
