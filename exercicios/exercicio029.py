from cores import *
velocidade = int(input('A qual velocidade o veículo estava? '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print(f'Infelizmente seu veículo excedeu a velocidade de 80km/h, você recebeu uma multa de {cores["vermelho"]}{fx["sublinhado"]}R${multa:.2f}{limpar}! ', end='')
    print('\U0001F4B8')
else:
    print(f'Obrigada por dirigir abaixo do limite de velocidade! {cores["verde"]}{fx["sublinhado"]}Tenha um bom dia.{limpar} ', end='')
    print('\U0001F44B')