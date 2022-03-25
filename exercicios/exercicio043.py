from cores import *
print(f'{cores["azul"]}{fx["negrito"]}****Vamos descobrir seu Índice de Massa Corporal?****{limpar}')
peso = int(input('Digite seu peso: kg'))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
print(f'Seu IMC é de: {imc:.1f}')
if imc<18.5:
    print(f'{cores["ciano"]}Abaixo do peso! {limpar}')
elif imc >18.5 and imc <25:
    print(f'{cores["verde"]}Peso ideal! {limpar}')
elif imc >25 and imc <30:
    print(f'{cores["amarelo"]}Sobrepeso! {limpar}')
elif imc >30 and imc <40:
    print(f'{cores["vermelho"]}Obesidade! {limpar}')
else:
    print(f'{cores["preto"]}{bg["branco"]}Obesidade Mórbida! {limpar}')
