velocidade = int(input('A qual velocidade o veículo estava? '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print(f'Infelizmente seu veículo excedeu a velocidade de 80km/h, você recebeu uma multa de R${multa:.2f}! ', end='')
    print('\U0001F4B8')
else:
    print('Obrigada por dirigir abaixo do limite de velocidade! Tenha um bom dia. ', end='')
    print('\U0001F44B')