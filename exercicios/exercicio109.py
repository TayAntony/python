from exercicio109 import moeda

valor = float(input('Digite o preço: R$').replace(',', '.'))
print(f'A metade de {moeda.format(valor)} é {moeda.metade(valor)}')
print(f'O dobro de {moeda.format(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando 20% de {moeda.format(valor)} temos {moeda.aumentar(valor, 20)}')
print(f'Reduzindo 25% de {moeda.format(valor)} temos {moeda.diminuir(valor, 25)}')
