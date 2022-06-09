from exercicio107_112 import moeda

valor = float(input('Digite o preço: R$'))
print(f'A metade de {valor} é {moeda.metade(valor):.2f}')
print(f'O dobro de {valor} é {moeda.dobro(valor):.2f}')
print(f'Aumentando 10% de {valor} temos {moeda.aumentar(valor, 10):.2f}')
print(f'Reduzindo 13% de {valor} temos {moeda.diminuir(valor, 13):.2f}')
