from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
pc = randint(0,10)
while not acertou:
    player = int(input('Digite seu palpite: '))
    palpites += 1
    if player == pc:
        acertou = True
    else:
        if player < pc:
            print('Mais... tente novamente!')
        elif player > pc:
            print('Menos... tente novamente')
print(f'Parabéns, você acertou com {palpites} tentativas!')
