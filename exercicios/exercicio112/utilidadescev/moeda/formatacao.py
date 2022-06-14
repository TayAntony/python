def formatacao(preço = 0, moeda= 'R$'):
    preço = float(preço)
    return f'{moeda} {preço:.2f}'.replace('.', ',')
