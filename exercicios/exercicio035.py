print('.-'*20)
print('Analisador de triângulos ', end='')
print('\U0001F53A')
print('.-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 <r1 + r3 and r3< r1 + r2:
    print('Os segmentos PODEM formar um triângulo ', end='')
    print('✔️')
else:
    print('Os segmentos NÃO PODEM formar um triângulo ', end='')
    print('❌')
