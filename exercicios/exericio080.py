lista = []
maio = menor = 0
for v in range(0,5):
    valor = int(input('Digite um valor: '))
    if v == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-='*30)
print(f'Você digitou {lista}')
