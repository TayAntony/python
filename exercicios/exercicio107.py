from exercicio107 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10% de {valor} temos R${moeda.aumentar(valor, 10)}')
print(f'Reduzindo 13% de {valor} temos {moeda.diminuir(valor, 13)}')
