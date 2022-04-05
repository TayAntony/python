''' Faça uma calculadora que a pessoa pode escolher entre 4 operações
básicas então colocar 2 numeros e o resultado e mostrado'''
5

print('=-=-=-=-=-= Calculadora do Gordo =-=-=-=-=-=')
print('''Escolha uma operação:
[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] DIVISÃO
[ 4 ] MULTIPLICAÇÃO''')
escolha = int(input('Sua opção: '))
n1 = int(input('Agora escolha o primeiro número: '))
n2 = int(input('E o segundo: '))
if escolha == 1:
    print(f'{n1+n2}')
elif escolha == 2:
    print(f'{n1-n2}')
elif escolha == 3:
    print(f'{n1/n2}')
elif escolha == 4:
    print(f'{n1*n2}')
else:
    print('COLOCA A PORRA DO NÚMERO CERTO DEMÔNIO')
#NOTA 8