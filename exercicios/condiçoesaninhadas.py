from cores import *
comida = str(input('Qual sua comida preferida? '))
if comida == 'frango':
    print(f'Eu {cores["vermelho_claro"]}adoro{limpar} frango também 😋')
elif comida in 'pudim mousse maionese lanche pastel':
    print(f'Uhh eu {cores["azul"]}amo{limpar} isso também 🤩')
elif comida in 'polenta fígado':
    print(f'{cores["verde"]}Ecaa{limpar} que nojo 🤢')
else:
    print(f'É... isso parece ser {cores["ciano"]}bom{limpar} também 😃')