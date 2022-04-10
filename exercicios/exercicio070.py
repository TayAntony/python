print('-'*20)
print('{: ^20}'.format('Loja da Tay'))
print('-'*20)
total = mais_mil = menor = cont = 0
barato = ''
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    total += preco
    if preco > 1000:
        mais_mil += 1
    print('*'*30)
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DA COMPRA '))
print(f'O total da compra foi: R${total:.2f}')
print(f'{mais_mil} produto(os) custam mais de R$1000')
print(f'O produto mais barato foi {barato} que custou R${menor}')
