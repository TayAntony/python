from random import choice
print('-=-' *26)
print('Estou pensando em um número de 0 a 5... Tente adivinhar:')
print('-=-' *26)
tentativa = int(input('Digite sua tentativa: '))
numeros = [0,1,2,3,4,5]
escolha = choice(numeros)
if tentativa == escolha:
    print('Meus parabéns, você acertou! ', end='')
    print('\U0001F929')
else:
    print(f'Que pena, você errou. Eu pensei no número {escolha}! Mais sorte na próxima ', end='')
    print("\U0001F97A")
