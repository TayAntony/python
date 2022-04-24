expressao = input('Digite sua expressão: ')
pilha = 0
for cont in expressao:
    if cont == '(':
        pilha += 1
    if cont ==')':
        pilha -= 1
if pilha == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
