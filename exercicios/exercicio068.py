from random import randint
from cores import *
from time import sleep
print(f'Vamos jogar {cores["azul"]}par{limpar} ou {cores["amarelo"]}ímpar{limpar}? ')
print('-='*15)
v = soma = 0
while True:
    jogador = int(input('Digite um valor: '))
    pi = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    while pi not in 'PI':
        pi = input('Par ou ímpar? [P/I] ').upper().strip()[0]
    pc = randint (0,10)
    soma = jogador+pc
    par = soma%2 == 0
    print(f'Você jogou {jogador} e o computador {pc}. O total foi {soma} que é ',end='')
    if par:
        print(f'{cores["azul"]}par{limpar}!')
    else:
        print(f'{cores["amarelo"]}ímpar{limpar}!')
    sleep(1)
    if pi == 'P':
        if par:
            print(f'{cores["verde"]}Você venceu{limpar}!')
            v += 1
        else:
            print(f'{cores["vermelho"]}Você perdeu{limpar}!')
            break
    elif pi == 'I':
        if not par:
            print(f'{cores["verde"]}Você venceu{limpar}!')
            v += 1
        else:
            print(f'{cores["vermelho"]}Você perdeu{limpar}!')
            break
    print('-='*15)
    print('Vamos jogar novamente...')
print(f'{fx["sublinhado"]}Game Over{limpar}! Você venceu {cores["verde"]}{v}{limpar} vezes!')
