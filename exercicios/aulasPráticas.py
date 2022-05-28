from cores import *
import emoji
comida = str(input('Qual sua comida preferida? '))
if comida == 'frango':
    print(f'Eu {cores["vermelho_claro"]}adoro{limpar} frango também 😋')
elif comida in 'pudim mousse maionese lanche pastel':
    print(f'Uhh eu {cores["azul"]}amo{limpar} isso também 🤩')
elif comida in 'polenta fígado':
    print(f'{cores["verde"]}Ecaa{limpar} que nojo 🤢')
else:
    print(f'É... isso parece ser {cores["ciano"]}bom{limpar} também 😃')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}!')
if m>= 7.0:
     print('A sua média foi boa, parabéns! ',end="")
     print("\U0001F970")
else:
     print('A sua média foi ruim, estude mais! ',end="")
     print("\U0001F62C")
