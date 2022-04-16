print('='*40)
print('{: ^40}'.format('Materiais de Estudos Web'))
print('='*40)
listagem = ('Notebook',4500,
            'Mouse',30,
            'Segunda Tela',240,
            'Teclado',150,
            'Fone de Ouvido',145,
            'Cabos',200,
            'Celular',1300,
            'MousePad',15)
total = int(6580.00)
for pos in range (0,16,1):
    if pos%2==0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
print('='*40)
print('{: >40}'.format(f'Total de: R$ {total:.2f}'))
