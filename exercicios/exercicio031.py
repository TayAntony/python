pergunta = int(input('Qual a distância da viagem em km? '))
distancia1 = float(pergunta*0.50)
distancia2 = float(pergunta*0.45)
if pergunta<=200:
    print(f'A sua viagem de {pergunta}km custará R${distancia1:.2f}!')
else:
    print(f'A sua viagem de {pergunta}km custará R${distancia2:.2f}!')

print('-=-'*20)