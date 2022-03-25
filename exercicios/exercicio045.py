from random import randint
from time import sleep
print('Vamos jogar JOKENPÔ?')
print('''Suas opções:
{ 0 } PEDRA ✊
{ 1 } PAPEL 🖐
{ 2 } TESOURA ✌️''')
opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
resposta = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('*' * 30)
print(f'O computador escolheu {opcoes[computador]}')
print(f'O jogador escolheu {opcoes[resposta]}')
print('*' * 30)
if computador == 0: #jogou pedra
    if resposta == 0:
        print('EMPATE')
    elif resposta == 1:
        print('JOGADOR VENCEU')
    elif resposta == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada Inválida')

elif computador == 1: #jogou papel
    if resposta == 0:
        print('COMPUTADOR VENDEU')
    elif resposta == 1:
        print('EMPATE')
    elif resposta == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada Inválida')

elif computador == 2: #jogou tesoura
    if resposta == 0:
        print('JOGADOR VENCEU')
    elif resposta == 1:
        print('COMPUTADOR VENCEU')
    elif resposta == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')
