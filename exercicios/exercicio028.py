from random import choice
from cores import *
print('-=-' *26)
print(f'{cores["azul"]}{fx["negrito"]}Estou pensando em um número de 0 a 5... Tente adivinhar:{limpar}')
print('-=-' *26)
tentativa = int(input('Digite sua tentativa: '))
numeros = [0,1,2,3,4,5]
escolha = choice(numeros)
if tentativa == escolha:
    print(f'{cores["verde"]}Meus parabéns, você acertou!{limpar} ', end='')
    print('\U0001F929')
else:
    print(f'{cores["vermelho"]}Que pena, você errou. Eu pensei no número {escolha}! Mais sorte na próxima{limpar} ', end='')
    print("\U0001F97A")
