from cores import *
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'{cores["verde"]}', end=' ')
        tot += 1
    else:
        print(f'{cores["vermelho"]}', end=' ')
    print(f'{c}{limpar}', end=' ')
print('\n' f' O número {n} foi divisível {tot} vezes!')
if tot == 2:
    print(' E por isso ele É primo')
else:
    print(' E por isso ele NÃO é primo')
