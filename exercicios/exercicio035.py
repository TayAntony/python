from cores import *
print('.-'*20)
print(f'{cores["azul"]}Analisador de triângulos{limpar} ', end='')
print('\U0001F53A')
print('.-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos {cores["verde"]}{fx["sublinhado"]}PODEM{limpar} formar um triângulo ', end='')
    print(' ✔️')
else:
    print(f'Os segmentos {cores["vermelho"]}{fx["sublinhado"]}NÃO PODEM{limpar} formar um triângulo ', end='')
    print('❌')
